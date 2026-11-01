import pytest
from playwright.sync_api import Page, expect

def test_map_pin_selection_updates_detail_panel(page: Page, base_url: str):
    """E2E Test: Interactive Map observation pins and detail reader panel selection."""
    page.goto(base_url)

    # Verify map panel components
    map_panel = page.locator(".map-panel")
    expect(map_panel).to_be_visible()
    expect(page.locator(".map-caption")).to_contain_text("ALMATY, KAZAKHSTAN")

    # Pins should be visible on map
    pins = page.locator("button.pin")
    expect(pins).to_have_count(6)

    # By default, observation 1 is selected
    active_pin = page.locator(".pin.pin-active")
    expect(active_pin).to_be_visible()
    expect(page.locator(".detail h2")).to_contain_text("A city measured in puddles")
    expect(page.locator(".detail .note-place")).to_contain_text("Abay Avenue")

    # Click observation pin for "We wait for the second bus"
    pin_two = page.locator("button.pin[title*='second bus']")
    pin_two.click()

    # Active pin updates to pin 2
    expect(pin_two).to_have_class("pin pin-active")
    expect(page.locator(".detail h2")).to_contain_text("“We wait for the second bus”")
    expect(page.locator(".detail .note-place")).to_contain_text("Dostyk × Satpaev")
    expect(page.locator(".detail .note-type")).to_contain_text("INTERVIEW")
