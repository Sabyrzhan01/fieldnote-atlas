import pytest
from playwright.sync_api import Page, expect

def test_search_observations_by_title_body_and_tags(page: Page, base_url: str):
    """E2E Test: Real-time search across observation title, body, and tags."""
    page.goto(base_url)

    search_input = page.locator("#search")
    expect(search_input).to_be_visible()

    # Search by keyword in title
    search_input.fill("puddles")
    pins = page.locator("button.pin")
    expect(pins).to_have_count(1)
    expect(page.locator(".map-count")).to_contain_text("1 observations mapped")
    expect(page.locator(".detail h2")).to_contain_text("A city measured in puddles")

    # Search by tag
    search_input.fill("transit")
    expect(pins).to_have_count(1)
    expect(page.locator(".detail h2")).to_contain_text("“We wait for the second bus”")

    # Search by body text
    search_input.fill("asphalt")
    expect(pins).to_have_count(1)
    expect(page.locator(".detail h2")).to_contain_text("The blue repair patch")

    # Non-matching search query
    search_input.fill("nonexistent-query-xyz")
    expect(pins).to_have_count(0)
    expect(page.locator(".empty-detail")).to_be_visible()

    # Clearing search restores full collection
    search_input.fill("")
    expect(page.locator("button.pin")).to_have_count(6)
