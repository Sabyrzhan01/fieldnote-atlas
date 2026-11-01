# Deploying Fieldnote Atlas to Railway (Recommended Docker Compose Target)

Among Railway, Render, and Vercel, **Railway is the primary platform that supports importing a `docker-compose.yml` file directly** into its canvas to provision both the containerized FastAPI web service and the `postgres:16-alpine` service together (see [Railway Docker & Compose documentation](https://docs.railway.com/builds/dockerfiles)).

---

## Why Railway Fits the Docker Compose Requirement
- **Native Compose Import:** Railway allows dragging and dropping or importing `docker-compose.yml` directly into a project canvas, automatically creating linked services (`web` and `db`) and persistent volumes (`pgdata`).
- **Single-Dockerfile Support:** Alternatively, Railway can build the `Dockerfile` via `railway.json` and link to a Railway PostgreSQL service.
- **Port Handling:** Railway injects `$PORT` dynamically (`server.py` reads `PORT` with fallback to `8091`).

---

## Step-by-Step Instructions (Option A: Direct `docker-compose.yml` Import)

1. **Log in to Railway:**
   - Go to [railway.app](https://railway.app/) and sign in with your GitHub account.

2. **Import `docker-compose.yml`:**
   - Click **New Project** → **Empty Project** (or press `⌘K` / `Ctrl+K` on the canvas and select **Import Docker Compose**).
   - Upload or paste the repository's `docker-compose.yml` file, or connect the `Sabyrzhan01/fieldnote-atlas` GitHub repository so `web` builds directly from the repo root.
   - Railway creates both the `web` service and the `db` (`postgres:16-alpine`) service along with the `pgdata` volume.

3. **Generate Public Domain:**
   - Click the `web` service card → **Settings** → **Networking** → **Generate Domain** (target port `8091`).
   - Your stack is live at `https://<generated-domain>.up.railway.app` and automatically redeploys on commits to `main` when linked to the GitHub repo!

---

## Step-by-Step Instructions (Option B: GitHub Repo + Managed Railway PostgreSQL)

1. **Log in to Railway:**
   - Go to [railway.app](https://railway.app/) and authenticate with your GitHub account.

2. **Create New Project:**
   - Click **New Project** → Select **Deploy from GitHub repo**.
   - Select `Sabyrzhan01/fieldnote-atlas`.

3. **Add PostgreSQL Database:**
   - In your Railway project canvas, click **Create** (or `+`) → Select **Database** → **Add PostgreSQL**.
   - Railway spins up a PostgreSQL container and exposes `DATABASE_URL`.

4. **Connect Web Service to Database:**
   - Click on your `fieldnote-atlas` web service card.
   - Go to **Variables** → Click **Add Reference** → Select `DATABASE_URL` from the PostgreSQL service.
   - Railway will trigger an automatic redeploy.

5. **Generate Public Domain:**
   - Under the web service settings, go to **Networking** → Click **Generate Domain**.
   - Your site is now live at `https://<generated-domain>.up.railway.app`!
