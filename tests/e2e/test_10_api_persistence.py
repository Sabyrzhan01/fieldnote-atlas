import pytest
import httpx
from playwright.sync_api import Page, expect

def test_full_api_and_ui_persistence_lifecycle(page: Page, base_url: str):
    """E2E Test: Full API lifecycle - verify UI changes hit backend and persist."""
    # 1. Check API health endpoint
    health_resp = httpx.get(f"{base_url}/api/health")
    assert health_resp.status_code == 200
    assert health_resp.json() == {"status": "ok"}

    # 2. Open frontend
    page.goto(base_url)

    # 3. Create observation via UI
    page.locator("#add").click()
    page.fill("input[name='title']", "PostgreSQL Persistence Note")
    page.fill("textarea[name='body']", "Verifying database integrity across client and server boundaries.")
    page.fill("input[name='place']", "Panfilov Promenade")
    page.fill("input[name='tags']", "db, postgres, test")
    page.locator("#noteForm button.add").click()

    expect(page.locator(".toast")).to_contain_text("Observation added to your atlas")
    expect(page.locator(".detail h2")).to_contain_text("PostgreSQL Persistence Note")

    # 4. Verify directly via backend REST API
    api_atlas = httpx.get(f"{base_url}/api/atlas").json()
    obs_list = api_atlas["observations"]
    created_obs = next((o for o in obs_list if o["title"] == "PostgreSQL Persistence Note"), None)
    assert created_obs is not None
    assert created_obs["place"] == "Panfilov Promenade"
    assert "postgres" in created_obs["tags"]

    # 5. Delete observation via REST API
    delete_resp = httpx.delete(f"{base_url}/api/observations/{created_obs['id']}")
    assert delete_resp.status_code == 200

    # 6. Reload UI and ensure deleted observation is gone
    page.reload()
    expect(page.locator(f"button.pin[data-pin='{created_obs['id']}']")).to_have_count(0)
