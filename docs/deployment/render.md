# Deploying Fieldnote Atlas to Render (Blueprint Alternative to Docker Compose)

> **Platform Distinction Note:** Render does **not** execute `docker-compose.yml` directly in production. Instead, per [Render's Docker documentation](https://render.com/docs/docker), multi-service setups on Render use a declarative **Render Blueprint (`render.yaml`)** that provisions the `Dockerfile` web service and a separate managed Render PostgreSQL database (`fieldnote-atlas-db`), injecting `DATABASE_URL` automatically. For direct `docker-compose.yml` import, see the [Railway deployment guide](railway.md) or the [AWS CloudFormation](../../aws/README.md) / [GCP Terraform](../../terraform/README.md) VM guides.

---

## Architecture on Render
- **Web Service:** Built directly from root `Dockerfile`.
- **Database:** Managed Render PostgreSQL instance (`fieldnote-atlas-db`), connected through internal database URL injected automatically as `DATABASE_URL`.
- **Static Assets:** Bundled into the image and served by FastAPI.

---

## Step-by-Step Instructions

1. **Push your code to GitHub:**
   Ensure `render.yaml` and `Dockerfile` are pushed to your repository `https://github.com/Sabyrzhan01/fieldnote-atlas`.

2. **Connect to Render:**
   - Go to [dashboard.render.com](https://dashboard.render.com/).
   - Click **New +** → Select **Blueprint**.
   - Connect your GitHub account and choose the `fieldnote-atlas` repository.

3. **Deploy the Blueprint:**
   - Render automatically detects `render.yaml`.
   - It will show two resources to create:
     1. Web Service: `fieldnote-atlas` (Docker, Free Plan)
     2. PostgreSQL: `fieldnote-atlas-db` (Free Plan)
   - Click **Apply**.

4. **Verify Deployment:**
   - Once build completes, Render will assign a public URL (e.g. `https://fieldnote-atlas.onrender.com`).
   - Visit the URL to open Fieldnote Atlas.
   - Check health endpoint: `https://fieldnote-atlas.onrender.com/api/health`.

---

## Environment Variables Configured
| Variable | Value | Source |
|---|---|---|
| `PORT` | `8091` | Configured in `render.yaml` |
| `HOST` | `0.0.0.0` | Configured in `render.yaml` |
| `DATABASE_URL` | Injected dynamically | From `fieldnote-atlas-db` connection string |
