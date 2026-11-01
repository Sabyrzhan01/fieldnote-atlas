# DevOps: GitHub Actions CI/CD Pipeline (Unit, E2E Tests & Auto-Deploy)

**Labels:** `devops`, `ci-cd`, `github-actions`

## Goal
Implement a complete GitHub Actions CI/CD pipeline running all unit, integration, and Playwright E2E tests, and auto-deploying on every commit to main.

## Description
Create `.github/workflows/ci-cd.yml`:
1. **Lint and Static Checks**: `compileall`, OpenAPI validation, Docker compose validation.
2. **Backend Unit & Integration Tests**: Spins up PostgreSQL service container in GitHub Actions and runs all repository and migration tests against both SQLite and PostgreSQL.
3. **Frontend Unit Tests**: Runs Node.js test suite for `services.js`.
4. **Playwright End-to-End Tests**: Boots the application stack and runs the 11 Playwright E2E tests across all features, uploading HTML reports and artifacts on failure.
5. **Continuous Deployment (CD)**: Automatically triggers re-deployment to Render, Railway, AWS, or GCP upon merge to `main`.

## Deliverables
- `.github/workflows/ci-cd.yml`

## Acceptance Criteria
- [x] Workflow triggers on push and pull requests to `main`.
- [x] Includes dedicated PostgreSQL service container for integration checks.
- [x] Playwright E2E suite runs in headless CI container.
- [x] Deployment step triggers on main branch push.
