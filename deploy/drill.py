#!/usr/bin/env python3
"""Run a controlled failure drill against the development deployment only."""
import json
import os
import subprocess
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from uuid import uuid4

state = Path(os.getenv("ATLAS_DEPLOY_HOME", Path.home() / ".config/fieldnote-atlas")) / "development"
image = (state / "current").read_text().strip()
port = os.getenv("ATLAS_DEV_PORT", "8000")
url = f"http://127.0.0.1:{int(port)}"
release_env = dict(os.environ, APP_ENV="development", APP_IMAGE=image, APP_VERSION=image.split("@")[1])
compose = ["docker", "compose", "-p", "atlas-development", "--env-file",
           str(state / "host.env"), "-f", "deploy/compose.yml"]


def run(*args):
    subprocess.run([*compose, *args], env=release_env, check=True)


def get(address):
    with urllib.request.urlopen(address, timeout=5) as response:
        return json.load(response)


def firing():
    rules = get("http://127.0.0.1:9090/api/v1/alerts")["data"]["alerts"]
    return {alert["labels"]["alertname"] for alert in rules
            if alert["labels"].get("deployment_environment_name") == "development"
            and alert["state"] == "firing"}


def write():
    payload = dict(id=uuid4().hex, title="Development drill", body="Test only",
                   kind="Field note", place="Lab", region="Lab", date="2026-01-01",
                   color="blue", source="Synthetic")
    request = urllib.request.Request(url + "/api/observations", json.dumps(payload).encode(),
                                     {"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(request, timeout=5):
            raise RuntimeError("Expected the development fault to reject the write")
    except urllib.error.HTTPError as error:
        if error.code != 503:
            raise


def wait_for(predicate, seconds):
    deadline = time.monotonic() + seconds
    while time.monotonic() < deadline:
        if predicate():
            return
        time.sleep(2)
    raise RuntimeError("Timed out waiting for the expected alert or recovery")


if __name__ == "__main__":
    assert get(url + "/api/version") == {
        "environment": "development", "version": release_env["APP_VERSION"]
    }
    get(url + "/api/health")
    run("exec", "-T", "app", "touch", "/tmp/atlas-fault")
    expected = {"AtlasHighErrorRate", "AtlasHighLatency", "AtlasObservationFailures"}
    try:
        with ThreadPoolExecutor(max_workers=4) as pool:
            deadline = time.monotonic() + 100
            while time.monotonic() < deadline and not expected <= firing():
                list(pool.map(lambda _: write(), range(4)))
        assert expected <= firing(), firing()
        print("Write failures, error rate and latency alerts firing", flush=True)
    finally:
        run("exec", "-T", "app", "rm", "-f", "/tmp/atlas-fault")
    try:
        run("stop", "app")
        wait_for(lambda: "AtlasUnavailable" in firing(), 80)
        print("Availability alert firing", flush=True)
    finally:
        run("up", "-d", "--wait", "--wait-timeout", "150")
    get(url + "/api/health")
    wait_for(lambda: not (expected | {"AtlasUnavailable"}) & firing(), 180)
    print("Development recovered and all drill alerts cleared", flush=True)
