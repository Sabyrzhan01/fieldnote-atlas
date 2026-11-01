# DevOps: PaaS Deployment Configurations (Render, Railway, Vercel)

**Labels:** `devops`, `deployment`

## Goal
Deploy the application with Docker Compose configurations to Render, Railway, and Vercel.

## Description
Provide declarative configurations and step-by-step guides for deploying Fieldnote Atlas to modern PaaS platforms:
- **Render**: `render.yaml` Blueprint definition running the web Docker service linked to a managed PostgreSQL database.
- **Railway**: `railway.json` configuration for Docker Compose deployment with PostgreSQL plugin.
- **Vercel**: `vercel.json` configuration for container/serverless deployment and reverse proxying.
- Comprehensive deployment walkthroughs in `deploy/`.

## Deliverables
- `render.yaml`
- `railway.json`
- `vercel.json`
- `docs/deployment/render.md`, `docs/deployment/railway.md`, `docs/deployment/vercel.md`

## Acceptance Criteria
- [x] `render.yaml` syntax valid for Render Blueprints.
- [x] Railway config ready for one-click repository deploy.
- [x] Vercel routing configured.
- [x] Detailed guides written with screenshots and environment variable instructions.
