# AI on-call responder

Alertmanager delivers firing and resolved events to the internal `oncall:8080/alerts` endpoint. A shared bearer secret authenticates the endpoint. The responder matches Fieldnote Atlas and the environment, captures Prometheus query results, recent Loki error events and Tempo error-trace summaries, and calls OpenAI with the evidence. The report retains the alert name, service, severity, environment, evidence, likely cause, confidence and proposed next checks. The responder has no shell, deployment or write-access integrations. Its only application write is the incident database. Human operators handle remediation.

Set `OPENAI_API_KEY` in the monitoring env file and optionally choose an account-enabled `OPENAI_MODEL`. The webhook persists reports in a dedicated volume. Missing credentials and API failures are recorded with their explicit analysis status. Resolved notifications are stored without invoking the model. The same fingerprint, start time, environment and status produce one database record.

Read reports on the host:

```bash
docker compose -p atlas-monitoring \
  --env-file "$HOME/.config/fieldnote-atlas/monitoring.env" \
  -f observability/compose.yml exec -T oncall python -c \
  'import sqlite3; db=sqlite3.connect("file:/incidents/reports.db?mode=ro", uri=True); print("\n".join(row[0] for row in db.execute("SELECT report FROM incidents ORDER BY rowid")))'
```

An end-to-end LLM check requires a firing event and a report with `analysis.status=analyzed`. Review the evidence and remove sensitive content before publishing an incident report to GitHub. Automatic GitHub incident creation is optional and is not configured.
