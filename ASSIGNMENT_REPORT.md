# Fieldnote Atlas DevOps and observability verification

This implementation extends Fieldnote Atlas at base commit `1ee6f44`. It follows the course lecture's development-first release model and separate OpenTelemetry stack using Docker Compose, GHCR and a self-hosted GitHub runner. PostgreSQL remains the deployment database. The AI responder provides incident analysis and operator guidance.

| Requirement | Implementation | Verification |
| --- | --- | --- |
| Development and production isolation | `deploy/compose.yml`, private per-environment configuration, unique ports, database credentials and volumes | Compose YAML parsed. Running two PostgreSQL environments and checking data isolation is pending. |
| Automated CI and digest promotion | `ci.yml`, `promote.yml`, `deploy/release.sh` | Existing local frontend and backend tests passed. Workflow YAML and release shell syntax checked. GHCR publish, hosted CI, real rollback and production dispatch are pending. |
| Metrics, logs and traces | `backend/app/telemetry.py`, SQLAlchemy instrumentation and `observability/collector.yml` | Local HTTP smoke test exercised real FastAPI requests and decoded three OTLP protobuf streams using a local receiver. Confirmed HTTP and SQL spans, a trace-correlated error log and application metric names. Collector and storage ingestion are pending. |
| Grafana and three business metrics | Provisioned dashboard and data sources. Counters for observations created, star changes and server-side observation write failures | Dashboard JSON parsed with eight panels. The local OTLP smoke test observed all three counters. Grafana rendering and data-source queries are pending. |
| Four alerts and recovery | `observability/alerts.yml`, blackbox probe, Alertmanager, `deploy/drill.py` | Configuration syntax checked. The local application returned a real 500 during a controlled request. The full Prometheus drill, alert delivery and recovery are pending. |
| AI on-call analysis | `on-call-engineer/responder.py`, authenticated webhook, three evidence sources, OpenAI and SQLite | Local webhook smoke checked unauthorized rejection, repeated delivery deduplication and database persistence with mocked evidence and no LLM key. Live evidence queries and OpenAI analysis are pending. |
| Issue workflow | Six groomed issue specifications and the existing GitHub sync script | Dry run found six issues. Remote issue creation, PR links and independent QA are pending. |
| Reproducibility | README, DevOps, observability, on-call documentation and env example | Setup, drill, manual promotion and rollback commands are provided. |

## Local checks

- Backend repository suite passed 12 tests.
- Frontend Vitest suite passed 4 tests and Vite built the production bundle.
- OTLP smoke test created a synthetic note and changed its star, then repeated the same ID to exercise a SQL error and verify actual exported protobuf payloads.
- Shell syntax, Python compilation, YAML parsing, dashboard JSON and whitespace checks passed.

## Live demonstration

Complete the host and GitHub setup in [DEVOPS.md](DEVOPS.md). Deploy development, create and star a test note, verify all three signals and open Grafana. Run the development failure drill in [OBSERVABILITY.md](OBSERVABILITY.md). Verify the firing and resolved incident records and a report with `analysis.status=analyzed`. Check recovery by creating another note. Manually promote the verified digest and compare versions and database contents.

A Docker deployment host, GitHub write access and an OpenAI API key were unavailable in the implementation workspace. The real deployment, incident analysis and remote issue workflow remain open. No screenshots or production test results were generated.
