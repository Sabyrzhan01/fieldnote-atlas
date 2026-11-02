# Deploying Fieldnote Atlas to Railway (Recommended Docker Compose Target)

Among Railway, Render, and Vercel, **Railway is the primary platform that supports importing a `docker-compose.yml` file directly** into its canvas to provision both the containerized FastAPI + Vite SPA service (`app`) and the `postgres:16-alpine` service (`db`) together (see [Railway Docker & Compose documentation](https://docs.railway.com/builds/dockerfiles)).

---

## Why Railway Fits the Docker Compose Requirement
- **Native Compose Import:** Railway allows dragging and dropping or importing `docker-compose.yml` directly into a project canvas, automatically creating linked services (`app` and `db`) and persistent volumes (`pgdata`).
- **Single-Dockerfile Support:** Alternatively, Railway builds the multi-stage `Dockerfile` via `railway.json` (which runs `alembic upgrade head && python -m scripts.seed_db` before starting Uvicorn) and links to a Railway PostgreSQL service via `DATABASE_URL`.
- **Port Handling:** Railway injects `$PORT` dynamically (`Dockerfile` and `railway.json` bind `--port ${PORT:-8000}`).

---

## Step-by-Step Instructions (Option A: Direct `docker-compose.yml` Import)

1. **Log in to Railway:**
   - Go to [railway.app](https://railway.app/) and sign in with your GitHub account.

2. **Import `docker-compose.yml`:**
   - Click **New Project** → **Empty Project** (or press `⌘K` / `Ctrl+K` on the canvas and select **Import Docker Compose**).
   - Upload or paste the repository's `docker-compose.yml` file, or connect the `Sabyrzhan01/fieldnote-atlas` GitHub repository so `app` builds directly from the repo root.
   - Railway creates both the `app` service and the `db` (`postgres:16-alpine`) service along with the `pgdata` volume.

3. **Generate Public Domain & Verify:**
   - Click the `app` service card → **Settings** → **Networking** → **Generate Domain** (target port `8000`).
   - Verify healthcheck at `https://<your-railway-domain>.up.railway.app/api/health` (`{"status":"ok"}`) and API data at `/api/atlas`.

---

## Step-by-Step Instructions (Option B: GitHub Repo + Managed Railway PostgreSQL)

1. **Create New Project:**
   - On [railway.app](https://railway.app/), click **New Project** → **Deploy from GitHub repo** → Select `Sabyrzhan01/fieldnote-atlas`.
2. **Add PostgreSQL Database:**
   - In your Railway project canvas, click **+ Create** → **Database** → **Add PostgreSQL**.
3. **Connect `DATABASE_URL`:**
   - Click the `fieldnote-atlas` web service card → **Variables** → **Add Reference** → select `DATABASE_URL` from the PostgreSQL service (`backend/app/repository.py` automatically normalizes `postgres://` or `postgresql://` to `postgresql+psycopg://`).
4. **Generate Domain & Auto-Redeploy:**
   - Under **Settings** → **Networking**, click **Generate Domain** (port `8000`).
   - Railway automatically redeploys on every push to `main`, or via `RAILWAY_WEBHOOK_URL` in `.github/workflows/cd.yml`.
