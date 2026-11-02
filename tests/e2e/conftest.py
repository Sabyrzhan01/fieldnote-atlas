"""Playwright end-to-end testing fixtures for Fieldnote Atlas."""
import os
import sys
import time
import socket
import tempfile
import subprocess
import urllib.request
from pathlib import Path
import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT))

def get_free_port():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('', 0))
        return s.getsockname()[1]

@pytest.fixture(scope="session")
def app_server():
    """Start the FastAPI app in a background subprocess for end-to-end testing."""
    port = get_free_port()
    host = "127.0.0.1"

    temp_dir = tempfile.TemporaryDirectory()
    test_db = Path(temp_dir.name) / "e2e_test_atlas.sqlite3"
    
    env = os.environ.copy()
    if not env.get("FIELDNOTE_DB_URL") and not env.get("DATABASE_URL"):
        env["FIELDNOTE_DB_URL"] = f"sqlite:///{test_db}"
    env["HOST"] = host
    env["PORT"] = str(port)
    env["ENABLE_TEST_RESET"] = "1"
    env["PYTHONUNBUFFERED"] = "1"

    python_bin = sys.executable
    server_proc = subprocess.Popen(
        [python_bin, "-m", "uvicorn", "backend.app.main:app", "--host", host, "--port", str(port)],
        cwd=str(PROJECT_ROOT),
        env=env,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    base_url = f"http://{host}:{port}"
    max_retries = 40
    started = False
    for _ in range(max_retries):
        try:
            with urllib.request.urlopen(f"{base_url}/api/health", timeout=1) as resp:
                if resp.status == 200:
                    started = True
                    break
        except Exception:
            time.sleep(0.15)

    if not started:
        stdout, stderr = server_proc.communicate(timeout=2)
        pytest.fail(f"Server failed to start at {base_url}.\nStdout: {stdout.decode()}\nStderr: {stderr.decode()}")

    yield base_url

    server_proc.terminate()
    try:
        server_proc.wait(timeout=3)
    except subprocess.TimeoutExpired:
        server_proc.kill()
    temp_dir.cleanup()

@pytest.fixture(scope="session")
def base_url(app_server):
    return app_server

@pytest.fixture(autouse=True)
def reset_custom_observations(base_url):
    """Ensure each E2E test starts and ends with only the 6 deterministic seed observations."""
    try:
        req = urllib.request.Request(f"{base_url}/api/test/reset", method="POST")
        urllib.request.urlopen(req, timeout=2)
    except Exception:
        pass
    yield

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {"width": 1280, "height": 800},
    }
