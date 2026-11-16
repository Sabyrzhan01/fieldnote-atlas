"""Verify Grafana's provisioned selectors and execute the scoped panel queries."""
import base64
import json
import os
from pathlib import Path
import sys
import time
from urllib.parse import urlencode
from urllib.request import Request, urlopen


def query(expression):
    endpoint = "http://127.0.0.1:3000/api/datasources/proxy/uid/prometheus/api/v1/query"
    token = base64.b64encode(f"admin:{os.environ['GRAFANA_PASSWORD']}".encode()).decode()
    request = Request(f"{endpoint}?{urlencode({'query': expression})}",
                      headers={"Authorization": f"Basic {token}"})
    with urlopen(request, timeout=10) as response:
        return json.load(response)["data"]["result"]


if __name__ == "__main__":
    dashboard = json.loads(Path(sys.argv[1]).read_text())["dashboard"]
    assert len(dashboard["panels"]) == 8
    selectors = {variable["name"] for variable in dashboard["templating"]["list"]}
    assert {"environment", "version"} <= selectors
    for _ in range(3):
        with urlopen("http://127.0.0.1:8000/api/atlas", timeout=5) as response:
            assert response.status == 200
        time.sleep(10)
    checked = 0
    for panel in dashboard["panels"]:
        for target in panel["targets"]:
            expression = target["expr"]
            if "$version" not in expression:
                continue
            assert "$environment" in expression, panel["title"]
            scoped = expression.replace("$environment", "development").replace("$version", sys.argv[2])
            assert query(scoped), panel["title"]
            assert not query(scoped.replace(sys.argv[2], "nonexistent-digest")), panel["title"]
            assert not query(scoped.replace("development", "nonexistent-environment")), panel["title"]
            checked += 1
    assert checked == 6, checked
    print("Verified six request and application queries filter by environment and digest through Grafana")
