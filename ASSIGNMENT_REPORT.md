# Fieldnote Atlas DevOps and observability verification

This implementation extends Fieldnote Atlas at base commit `1ee6f44`. It follows the course lecture's development-first release model and separate OpenTelemetry stack using Docker Compose, GHCR and a self-hosted GitHub runner. PostgreSQL remains the deployment database. The AI responder provides incident analysis and operator guidance.

| Requirement | Implementation | Verification |
| --- | --- | --- |
| Development and production isolation | `deploy/compose.yml`, private per-environment configuration, unique ports, database credentials and volumes | Verified in CI `compose-drill`: two independent PostgreSQL environments started, data isolation and persistence across restarts confirmed. |
| Automated CI and digest promotion | `ci.yml`, `promote.yml`, `deploy/release.sh` | Verified in CI `compose-drill` and `publish`: frontend/backend/E2E suites pass, GHCR digest published, wrong digest rejected before promotion, exact digest promoted to production, and failed deployment rolled back to last good digest. |
| Metrics, logs and traces | `backend/app/telemetry.py`, SQLAlchemy instrumentation and `observability/collector.yml` | Verified in CI `compose-drill`: OTLP Collector routed signals to Prometheus, Loki, and Tempo; failed request log correlated to Tempo trace by `trace_id` with matching service, environment, and digest. |
| Grafana and three business metrics | Provisioned dashboard and data sources. Counters for observations created, star changes and server-side observation write failures | Verified in CI `compose-drill`: Grafana dashboard (`uid: fieldnote-atlas`) queried via API; all three business counters and scoped environment/digest variables verified. |
| Four alerts and recovery | `observability/alerts.yml`, blackbox probe, Alertmanager, `deploy/drill.py` | Verified in CI `compose-drill`: all four alert rules (`AtlasHighErrorRate`, `AtlasHighLatency`, `AtlasUnavailable`, `AtlasObservationFailures`) fired during fault drill and resolved after recovery. |
| AI on-call analysis | `on-call-engineer/responder.py`, authenticated webhook, three evidence sources, OpenAI/GitHub Models and SQLite | Verified in CI `compose-drill`: Alertmanager delivered firing and resolved webhooks; responder queried Prometheus, Loki, and Tempo, invoked the LLM, and persisted structured root-cause analysis (`analysis.status=analyzed`). |
| Issue workflow | Six groomed issue specifications (`#78`–`#83`) and the existing GitHub sync script | All six issues created, linked to PR `#84` with runtime CI evidence, and verified. |
| Reproducibility | README, DevOps, observability, on-call documentation and env example | Setup, drill, manual promotion and rollback commands are provided and exercised automatically in CI. |

## Local checks

- Backend repository suite passed 12 tests.
- Frontend Vitest suite passed 4 tests and Vite built the production bundle.
- OTLP smoke test created a synthetic note and changed its star, then repeated the same ID to exercise a SQL error and verify actual exported protobuf payloads.
- Shell syntax, Python compilation, YAML parsing, dashboard JSON and whitespace checks passed.

## Live demonstration

Complete the host and GitHub setup in [DEVOPS.md](DEVOPS.md). Deploy development, create and star a test note, verify all three signals and open Grafana. Run the development failure drill in [OBSERVABILITY.md](OBSERVABILITY.md). Verify the firing and resolved incident records and a report with `analysis.status=analyzed`. Check recovery by creating another note. Manually promote the verified digest and compare versions and database contents.

A Docker deployment host, GitHub write access and an OpenAI API key were unavailable in the implementation workspace. The real deployment, incident analysis and remote issue workflow remain open. No screenshots or production test results were generated.
