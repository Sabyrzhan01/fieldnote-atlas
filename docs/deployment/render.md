# Deploying Fieldnote Atlas to Render (Blueprint Alternative to Docker Compose)

> **Platform Distinction Note:** Render does **not** execute `docker-compose.yml` directly in production. Instead, per [Render's Docker documentation](https://render.com/docs/docker), multi-service setups on Render use a declarative **Render Blueprint (`render.yaml`)** that provisions the multi-stage `Dockerfile` web service and a managed Render PostgreSQL database (`fieldnote-atlas-db`), injecting `DATABASE_URL` automatically. For direct `docker-compose.yml` import, see the [Railway deployment guide](railway.md) or the [AWS / GCP IaC guide](../../infra/README.md).

---

## Architecture on Render
- **Web Service (`fieldnote-atlas`):** Built from root multi-stage `Dockerfile` (Stage 1 builds `frontend/dist` with Vite; Stage 2 runs `alembic upgrade head && python -m scripts.seed_db` and serves FastAPI + `StaticFiles` on port `8000`).
- **Database (`fieldnote-atlas-db`):** Managed Render Free PostgreSQL instance connected via `DATABASE_URL` (`postgres://` connection strings are automatically normalized to `postgresql+psycopg://`).
- **Healthcheck:** Configured on `GET /api/health` (`healthCheckPath: /api/health`).

---

## Step-by-Step Instructions

1. **Connect to Render:**
   - Go to [dashboard.render.com](https://dashboard.render.com/).
   - Click **New +** → Select **Blueprint**.
   - Connect your GitHub account and choose `Sabyrzhan01/fieldnote-atlas`.

2. **Deploy the Blueprint (`render.yaml`):**
   - Render detects `render.yaml` and provisions:
     1. Web Service: `fieldnote-atlas` (`runtime: docker`, `plan: free`, `PORT=8000`, `healthCheckPath: /api/health`)
     2. PostgreSQL: `fieldnote-atlas-db` (`plan: free`, `databaseName: fieldnote_atlas`)
   - Click **Apply**.

3. **Verify Full-Stack Deployment:**
   - Open your assigned `https://<your-render-service>.onrender.com` URL.
   - Verify `GET /api/health` returns `{"status":"ok"}`.
   - Verify `GET /api/atlas` returns the 3 collections and 6 seeded Almaty observations from PostgreSQL.
   - Optional: Copy the Render Deploy Hook URL from **Settings → Deploy Hook** and add it as `RENDER_DEPLOY_HOOK_URL` in GitHub Repository Secrets so `.github/workflows/cd.yml` triggers a redeploy after every green `CI` run on `main`.

---

## Environment Variables Configured
| Variable | Value | Source |
|---|---|---|
| `PORT` | `8000` | Configured in `render.yaml` |
| `DATABASE_URL` | Injected dynamically | From `fieldnote-atlas-db` `connectionString` |
