import pytest
from playwright.sync_api import Page, expect

def test_connected_observation_link_navigation(page: Page, base_url: str):
    """E2E Test: Connected evidence navigation between linked observations."""
    page.goto(base_url)

    # Observation 1 has a connection link to "We wait for the second bus"
    connection_btn = page.locator("#connected")
    expect(connection_btn).to_be_visible()
    expect(connection_btn).to_contain_text("“We wait for the second bus”")

    # Click connection link
    connection_btn.click()

    # Active detail should update to observation "We wait for the second bus"
    expect(page.locator(".detail h2")).to_contain_text("“We wait for the second bus”")
    expect(page.locator(".pin.pin-active")).to_have_attribute("title", "“We wait for the second bus”")
