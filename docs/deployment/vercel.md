# Deploying Fieldnote Atlas to Vercel

Vercel excels at hosting edge static frontends and routing backend API calls via `vercel.json` rewrites to containerized backend services (such as Render or Railway).

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
