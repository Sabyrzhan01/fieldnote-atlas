import pytest
from playwright.sync_api import Page, expect

def test_clicking_tag_chip_filters_observations(page: Page, base_url: str):
    """E2E Test: Clicking a tag chip in the detail reader triggers tag filtering."""
    page.goto(base_url)

    # Observation 1 is selected by default and has tags: #rain, #movement, #informal paths
    tag_rain = page.locator(".detail .tags button[data-tag='rain']")
    tag_movement = page.locator(".detail .tags button[data-tag='movement']")
    expect(tag_rain).to_be_visible()
    expect(tag_movement).to_be_visible()

    # Regression for Issue #32: verify tag chips do not overlap horizontally
    rain_box = tag_rain.bounding_box()
    movement_box = tag_movement.bounding_box()
    assert rain_box is not None and movement_box is not None
    assert movement_box["x"] >= rain_box["x"] + rain_box["width"], (
        f"Tag chips overlap: #rain={rain_box}, #movement={movement_box}"
    )

    # Click the #rain tag chip
    tag_rain.click()

    # Search bar should now contain 'rain'
    expect(page.locator("#search")).to_have_value("rain")

    # Map pins should be filtered by 'rain' tag
    pins = page.locator("button.pin")
    expect(pins).to_have_count(1)
    expect(page.locator(".detail h2")).to_contain_text("A city measured in puddles")
