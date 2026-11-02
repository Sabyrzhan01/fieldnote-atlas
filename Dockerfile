# Stage 1: Build the Frontend SPA with Vite
FROM node:20-alpine AS frontend-build
WORKDIR /frontend
COPY frontend/package.json ./
RUN npm install
COPY frontend/ ./
RUN npm run build

# Stage 2: Production Python Runtime serving FastAPI API + Built Frontend SPA
FROM python:3.11-slim
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app/backend:/app \
    PORT=8000

WORKDIR /app

# Install curl for healthcheck and libpq for psycopg
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    libpq5 \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY backend/requirements.txt ./backend/requirements.txt
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r backend/requirements.txt

# Copy backend application, Alembic migrations, seed/migration scripts, and OpenAPI spec
COPY alembic.ini ./alembic.ini
COPY backend/ ./backend/
COPY scripts/ ./scripts/
COPY openapi.yaml ./openapi.yaml

# Copy built frontend static assets from Stage 1
COPY --from=frontend-build /frontend/dist ./frontend/dist

# Run as a non-root user
RUN useradd --create-home --shell /bin/bash appuser && \
    chown -R appuser:appuser /app
USER appuser

EXPOSE 8000

HEALTHCHECK --interval=15s --timeout=5s --start-period=10s --retries=3 \
    CMD sh -c "curl -fsS http://127.0.0.1:${PORT:-8000}/api/health || exit 1"

# Run Alembic migrations + seed when DATABASE_URL is configured, then launch FastAPI on $PORT
CMD ["sh", "-c", "if [ -n \"$DATABASE_URL\" ]; then alembic upgrade head && python -m scripts.seed_db; fi && exec uvicorn backend.app.main:app --host 0.0.0.0 --port ${PORT:-8000}"]
