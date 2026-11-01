# Deploying Fieldnote Atlas to Vercel (Non-Compose Edge/Serverless Caveat)

> **Platform Distinction Note:** As documented in [Vercel's Docker Compose guidance](https://vercel.com/i/can-you-run-docker-compose-on-vercel), **Vercel cannot run `docker-compose.yml` or host stateful long-running Docker/PostgreSQL containers**. Vercel is a serverless/edge platform that requires its own service configuration (`vercel.json`) and an external database/backend. Therefore, `vercel.json` is provided here only as an optional edge frontend + `/api/*` rewrite proxy to a containerized backend hosted on Railway, Render, AWS, or GCP. For true Docker Compose deployment, use **Railway** ([guide](railway.md)) or the **AWS/GCP VM** stacks.

---

## Architecture on Vercel
- **Frontend:** Static files (`index.html`, `app.js`, `style.css`, `services.js`) deployed to Vercel's global CDN edge.
- **Backend API:** FastAPI application hosted on Render / Railway / Cloud Run.
- **Routing:** `vercel.json` rewrites all `/api/*` traffic transparently to the backend URL, completely eliminating CORS friction.

---

## Step-by-Step Instructions

1. **Deploy Backend to Render or Railway First:**
   - Deploy the container stack to Render or Railway (see Render or Railway guide).
   - Copy the live backend URL (e.g. `https://fieldnote-atlas.onrender.com`).

2. **Configure `vercel.json`:**
   In `vercel.json`, ensure destination matches your live backend URL:
   ```json
   {
     "rewrites": [
       {
         "source": "/api/:match*",
         "destination": "https://fieldnote-atlas.onrender.com/api/:match*"
       },
       {
         "source": "/(.*)",
         "destination": "/$1"
       }
     ]
   }
   ```

3. **Deploy with Vercel CLI or Dashboard:**
   - From the repository root:
     ```bash
     npx vercel
     ```
   - Or in the Vercel Dashboard, import `Sabyrzhan01/fieldnote-atlas` and click **Deploy**.
