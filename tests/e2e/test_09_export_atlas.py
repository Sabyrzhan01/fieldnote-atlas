import json
import pytest
from playwright.sync_api import Page, expect

def test_export_atlas_downloads_json_archive(page: Page, base_url: str):
    """E2E Test: Export button initiates download of fieldnote-atlas.json archive."""
    page.goto(base_url)

    export_btn = page.locator("#export")
    expect(export_btn).to_be_visible()

    # Listen for download event
    with page.expect_download() as download_info:
        export_btn.click()

    download = download_info.value
    assert download.suggested_filename == "fieldnote-atlas.json"

    # Verify downloaded file content
    download_path = download.path()
    with open(download_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    assert isinstance(data, list)
    assert len(data) >= 6
    # Verify required keys in exported items
    first_item = data[0]
    for key in ["id", "title", "body", "place", "tags"]:
        assert key in first_item
