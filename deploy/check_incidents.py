"""Verify delivery and trace correlation from inside the Compose on-call service."""
import json
import sqlite3
import sys
import time
from contextlib import closing

import httpx

ALERTS = {"AtlasHighErrorRate", "AtlasHighLatency", "AtlasObservationFailures", "AtlasUnavailable"}


def development_reports():
    with closing(sqlite3.connect("file:/incidents/reports.db?mode=ro", uri=True)) as db:
        reports = [json.loads(row[0]) for row in db.execute("SELECT report FROM incidents")]
    return [r for r in reports if r["alert"]["labels"].get("deployment_environment_name") == "development"]


def find_failed_request(client, reports, version):
    trace_ids = dict.fromkeys(
        entry["trace_id"]
        for report in reports
        if isinstance(report["evidence"].get("logs"), list)
        for entry in report["evidence"]["logs"]
        if entry.get("trace_id")
    )
    for trace_id in trace_ids:
        response = client.get(f"http://tempo:3200/api/traces/{trace_id}")
        if response.status_code == 404:
            continue
        response.raise_for_status()
        trace = response.json()
        for batch in trace.get("batches", trace.get("resourceSpans", [])):
            attributes = {item["key"]: item["value"].get("stringValue")
                          for item in batch.get("resource", {}).get("attributes", [])}
            if not (attributes.get("service.name") == "fieldnote-atlas"
                    and attributes.get("deployment.environment.name") == "development"
                    and attributes.get("service.version") == version):
                continue
            spans = (span for scope in batch.get("scopeSpans", []) for span in scope["spans"])
            if any(span["name"] == "POST /api/observations" and
                   span.get("status", {}).get("code") in (2, "STATUS_CODE_ERROR") for span in spans):
                return trace_id
    raise AssertionError("No Loki error log matched a failed Tempo request with the expected resource labels")


if __name__ == "__main__":
    expected = {(name, status) for name in ALERTS for status in ("firing", "resolved")}
    deadline = time.monotonic() + 90
    while True:
        reports = development_reports()
        delivered = {(r["alert"]["labels"]["alertname"], r["alert"]["status"]) for r in reports}
        if expected <= delivered:
            break
        if time.monotonic() >= deadline:
            raise AssertionError(f"Missing webhook deliveries: {sorted(expected - delivered)}")
        time.sleep(3)
    for name, status in sorted(expected):
        print(f"Verified persisted development webhook: {name} {status}")
    firing_reports = [r for r in reports if r["alert"]["status"] == "firing"]
    assert firing_reports, "Expected firing incident reports"
    for r in firing_reports:
        assert "metrics" in r["evidence"] and "logs" in r["evidence"] and "traces" in r["evidence"], "Missing three signal evidence in firing report"
        assert r.get("analysis", {}).get("status") in {"analyzed", "missing_api_key", "analysis_failed"}, f"Unexpected analysis status: {r.get('analysis')}"
    analyzed = [r for r in firing_reports if r.get("analysis", {}).get("status") == "analyzed"]
    if analyzed:
        sample_analysis = analyzed[0]["analysis"]
        assert sample_analysis.get("most_likely_root_cause") and sample_analysis.get("troubleshooting_steps"), "Missing structured AI analysis fields"
        print(f"Verified AI responder analyzed {len(analyzed)} firing incidents (cause: {sample_analysis['most_likely_root_cause'][:80]}...)")
    else:
        print(f"Verified firing incident reports collected 3-signal evidence (analysis status: {firing_reports[0].get('analysis', {}).get('status')})")
    with httpx.Client(timeout=5) as client:
        trace_id = find_failed_request(client, reports, sys.argv[1])
    print(f"Correlated a Loki failure log with Tempo trace {trace_id} and verified service, environment and digest")
