#!/usr/bin/env python3
"""
Sync local markdown issues to GitHub Issues for Sabyrzhan01/fieldnote-atlas.

Usage:
    export GITHUB_TOKEN="ghp_your_personal_access_token"
    python scripts/sync_github_issues.py [--dry-run]
"""

import os
import sys
import glob
import re
import json
import urllib.request
import urllib.error
from pathlib import Path

REPO_OWNER = "Sabyrzhan01"
REPO_NAME = "fieldnote-atlas"
GITHUB_API = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}"

ROOT_DIR = Path(__file__).resolve().parents[1]

LABELS = [
    {
        "name": "e2e-test",
        "color": "0052cc",
        "description": "Playwright end-to-end tests for application features"
    },
    {
        "name": "devops",
        "color": "1d76db",
        "description": "Containerization, infrastructure, CI/CD, and deployment"
    },
    {
        "name": "docker",
        "color": "2496ed",
        "description": "Docker and container packaging"
    },
    {
        "name": "database",
        "color": "006b75",
        "description": "PostgreSQL and SQLite database migrations"
    },
    {
        "name": "aws",
        "color": "ff9900",
        "description": "Amazon Web Services CloudFormation deployment"
    },
    {
        "name": "gcp",
        "color": "4285f4",
        "description": "Google Cloud Platform Terraform deployment"
    },
    {
        "name": "ci-cd",
        "color": "2ea44f",
        "description": "Continuous Integration and Continuous Deployment"
    }
]

def make_request(url, method="GET", data=None, token=None):
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "fieldnote-atlas-sync-script"
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    body = json.dumps(data).encode("utf-8") if data else None
    req = urllib.request.Request(url, data=body, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        err_msg = e.read().decode("utf-8")
        raise RuntimeError(f"HTTP {e.code} for {method} {url}: {err_msg}")

def parse_issue_file(filepath: Path):
    content = filepath.read_text(encoding="utf-8")
    lines = content.strip().split("\n")
    title = lines[0].lstrip("#").strip()
    labels = []
    body_lines = []

    for line in lines[1:]:
        label_match = re.search(r"\*\*Labels:\*\*\s*(.*)", line)
        if label_match:
            raw_labels = label_match.group(1)
            labels = [l.strip("` ,'\"") for l in raw_labels.split(",") if l.strip("` ,'\"")]
        else:
            body_lines.append(line)

    body = "\n".join(body_lines).strip()
    return title, labels, body

def main():
    dry_run = "--dry-run" in sys.argv
    token = os.getenv("GITHUB_TOKEN")
    for i, arg in enumerate(sys.argv):
        if arg == "--token" and i + 1 < len(sys.argv):
            token = sys.argv[i + 1]
        elif arg.startswith("--token="):
            token = arg.split("=", 1)[1]

    if not token and not dry_run:
        print("[!] Warning: GITHUB_TOKEN environment variable not set.")
        print("    Running in --dry-run mode. Set GITHUB_TOKEN to actually create issues on GitHub.")
        print("    Example: export GITHUB_TOKEN=ghp_... && python scripts/sync_github_issues.py\n")
        dry_run = True

    issue_files = sorted(
        list(ROOT_DIR.glob("issues/e2e-tests/*.md")) +
        list(ROOT_DIR.glob("issues/devops/*.md"))
    )

    print(f"[*] Found {len(issue_files)} local issue markdown specifications.")

    existing_titles = set()
    if not dry_run:
        print("[*] Fetching existing issues from GitHub...")
        try:
            issues = make_request(f"{GITHUB_API}/issues?state=all&per_page=100", token=token)
            existing_titles = {i["title"].strip() for i in issues}
            print(f"[*] Found {len(existing_titles)} existing GitHub issues in repository.")
        except Exception as e:
            print(f"[!] Warning: Could not fetch issues: {e}")

        # Ensure labels exist
        print("[*] Ensuring required GitHub labels exist...")
        for lbl in LABELS:
            try:
                make_request(f"{GITHUB_API}/labels", method="POST", data=lbl, token=token)
                print(f"  [+] Created label: {lbl['name']}")
            except RuntimeError as e:
                if "already_exists" in str(e):
                    pass # Label already exists
                else:
                    print(f"  [-] Label {lbl['name']}: {e}")

    created_count = 0
    for f in issue_files:
        title, labels, body = parse_issue_file(f)
        print(f"\n--- Processing: {f.name} ---")
        print(f"  Title:  {title}")
        print(f"  Labels: {', '.join(labels)}")

        if title in existing_titles:
            print(f"  [SKIP] Issue already exists on GitHub with title '{title}'")
            continue

        if dry_run:
            print("  [DRY-RUN] Would create issue on GitHub.")
            created_count += 1
            continue

        try:
            payload = {
                "title": title,
                "body": body,
                "labels": labels
            }
            res = make_request(f"{GITHUB_API}/issues", method="POST", data=payload, token=token)
            print(f"  [CREATED] Issue #{res['number']}: {res['html_url']}")
            created_count += 1
        except Exception as e:
            print(f"  [ERROR] Failed to create issue: {e}")

    print(f"\n[DONE] Successfully processed {len(issue_files)} issues ({created_count} new).")

if __name__ == "__main__":
    main()
