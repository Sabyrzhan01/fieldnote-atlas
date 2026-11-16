FROM python:3.12-slim
WORKDIR /app
RUN pip install --no-cache-dir fastapi==0.115.14 uvicorn==0.34.3 httpx==0.28.1 && \
    useradd --uid 10001 responder && mkdir /incidents && chown responder /incidents
COPY responder.py .
USER responder
CMD ["uvicorn", "responder:app", "--host", "0.0.0.0", "--port", "8080", "--limit-concurrency", "12"]
