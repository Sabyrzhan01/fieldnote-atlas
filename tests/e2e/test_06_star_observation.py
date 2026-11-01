import pytest
from playwright.sync_api import Page, expect

def test_toggle_star_observation_and_toast(page: Page, base_url: str):
    """E2E Test: Star and unstar observation with toast feedback and persistence."""
    page.goto(base_url)

    # Select observation "We wait for the second bus" (unstarred initially)
    pin_two = page.locator("button.pin[title*='second bus']")
    pin_two.click()

    star_btn = page.locator("#star")
    expect(star_btn).to_have_attribute("aria-label", "Star observation")
    expect(star_btn).to_contain_text("♡")

    # Click star
    star_btn.click()

    # Should update to filled heart and show toast
    expect(star_btn).to_have_attribute("aria-label", "Unstar observation")
    expect(star_btn).to_contain_text("♥")
    expect(page.locator(".toast")).to_contain_text("Added to starred observations")

    # Reload page to verify persistence
    page.reload()
    pin_two = page.locator("button.pin[title*='second bus']")
    pin_two.click()
    expect(page.locator("#star")).to_have_attribute("aria-label", "Unstar observation")

    # Toggle off
    page.locator("#star").click()
    expect(page.locator("#star")).to_have_attribute("aria-label", "Star observation")
    expect(page.locator(".toast")).to_contain_text("Removed from starred observations")
