"""Opt-in OTLP telemetry. Attribute values are bounded and exclude user data."""
import logging
import os
from time import perf_counter

from opentelemetry.exporter.otlp.proto.http._log_exporter import OTLPLogExporter
from opentelemetry.exporter.otlp.proto.http.metric_exporter import OTLPMetricExporter
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.instrumentation.sqlalchemy import SQLAlchemyInstrumentor
from opentelemetry.sdk._logs import LoggerProvider, LoggingHandler
from opentelemetry.sdk._logs.export import BatchLogRecordProcessor
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader
from opentelemetry.sdk.metrics.view import ExplicitBucketHistogramAggregation, View
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor

ENVIRONMENT = os.getenv("APP_ENV", "local")
VERSION = os.getenv("APP_VERSION", "local")
logger = logging.getLogger("fieldnote.telemetry")

OPERATIONS = {
    ("POST", "/api/observations"): "create",
    ("POST", "/api/observations/{observation_id}/star"): "star",
    ("PUT", "/api/observations/{observation_id}"): "update",
    ("DELETE", "/api/observations/{observation_id}"): "delete",
}


def configure(app, engine):
    endpoint = os.getenv("OTEL_EXPORTER_OTLP_ENDPOINT", "").rstrip("/")
    if not endpoint:
        return
    resource = Resource.create({
        "service.name": "fieldnote-atlas",
        "deployment.environment.name": ENVIRONMENT,
        "service.version": VERSION,
    })
    traces = TracerProvider(resource=resource)
    traces.add_span_processor(BatchSpanProcessor(OTLPSpanExporter(endpoint + "/v1/traces")))
    logs = LoggerProvider(resource=resource)
    logs.add_log_record_processor(BatchLogRecordProcessor(OTLPLogExporter(endpoint + "/v1/logs")))
    logger.addHandler(LoggingHandler(logger_provider=logs))
    logger.setLevel(logging.INFO)
    provider = MeterProvider(resource=resource, metric_readers=[
        PeriodicExportingMetricReader(OTLPMetricExporter(endpoint + "/v1/metrics"), 5000),
    ], views=[View(
        instrument_name="atlas_http_duration",
        aggregation=ExplicitBucketHistogramAggregation(
            [0.01, 0.025, 0.05, 0.1, 0.25, 0.5, 0.75, 1, 1.5, 2.5, 5, 10]
        ),
    )])
    meter = provider.get_meter(__name__)
    requests = meter.create_counter("atlas_http_requests")
    duration = meter.create_histogram("atlas_http_duration", unit="s")
    created = meter.create_counter("atlas_observations_created")
    starred = meter.create_counter("atlas_observation_star_changes")
    failures = meter.create_counter("atlas_observation_failures")

    for status_class in ("2xx", "5xx"):
        requests.add(0, {"route": "/api/observations", "status_class": status_class})
    for operation in set(OPERATIONS.values()):
        failures.add(0, {"operation": operation})
    created.add(0)
    starred.add(0)

    @app.middleware("http")
    async def observe(request, call_next):
        started = perf_counter()
        status = 500
        try:
            response = await call_next(request)
            status = response.status_code
            return response
        finally:
            route = getattr(request.scope.get("route"), "path", "unmatched")
            operation = OPERATIONS.get((request.method, route))
            labels = {"route": route, "status_class": f"{status // 100}xx"}
            if route != "/api/health":
                requests.add(1, labels)
                duration.record(perf_counter() - started, labels)
                logger.log(logging.ERROR if status >= 500 else logging.INFO,
                           "HTTP request completed",
                           extra={**labels, "business_operation": operation or "none"})
            if operation and status >= 500:
                failures.add(1, {"operation": operation})
            elif status < 300 and operation == "create":
                created.add(1)
            elif status < 300 and operation == "star":
                starred.add(1)

    if engine is not None:
        SQLAlchemyInstrumentor().instrument(engine=engine, tracer_provider=traces)
    FastAPIInstrumentor.instrument_app(app, tracer_provider=traces, meter_provider=provider,
                                      excluded_urls="/api/health")
