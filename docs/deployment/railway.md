# Deploying Fieldnote Atlas to Railway with Docker Compose

Railway natively runs multi-service container stacks and Dockerfiles with automatic managed PostgreSQL provisioning.

---

## Architecture on Railway
- **Web Service:** Built from `Dockerfile` defined in `railway.json`.
- **Database:** Railway Postgres Plugin providing persistent cloud PostgreSQL.
- **Port Handling:** Railway sets `$PORT` dynamically; our application listens on `$PORT` seamlessly.

---

## Step-by-Step Instructions

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
