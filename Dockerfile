# Single container for Fieldnote Atlas: Connected Static Frontend + FastAPI Backend
FROM python:3.11-slim

# Prevent Python from buffering stdout/stderr and writing .pyc files
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=8091 \
    HOST=0.0.0.0

WORKDIR /app

# Install system dependencies (curl for healthchecks)
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install Python backend dependencies
COPY backend/requirements.txt ./backend/requirements.txt
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r backend/requirements.txt

# Copy Backend application
COPY backend/ ./backend/
COPY server.py ./
COPY openapi.yaml ./

# Copy Static Frontend assets (served by FastAPI static mount at '/')
COPY index.html ./
COPY app.js ./
COPY style.css ./
COPY services.js ./
COPY docs/ ./docs/

# Create non-privileged user for security
RUN groupadd -r appuser && useradd -r -g appuser -d /app -s /sbin/nologin appuser && \
    chown -R appuser:appuser /app

USER appuser

EXPOSE 8091

# Container healthcheck
HEALTHCHECK --interval=15s --timeout=5s --start-period=10s --retries=3 \
    CMD curl -f http://127.0.0.1:${PORT}/api/health || exit 1

# Launch FastAPI server (respects $PORT and $HOST)
CMD ["python3", "server.py"]
