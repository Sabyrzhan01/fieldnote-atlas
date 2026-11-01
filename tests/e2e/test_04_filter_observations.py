import pytest
from playwright.sync_api import Page, expect

def test_filter_observations_all_starred_and_interviews(page: Page, base_url: str):
    """E2E Test: Filter cycling through All notes, Starred, and Interviews."""
    page.goto(base_url)

    filter_btn = page.locator("#filter")
    expect(filter_btn).to_contain_text("All notes")
    expect(page.locator("button.pin")).to_have_count(6)

    # 1. Cycle to 'Starred' filter
    filter_btn.click()
    expect(filter_btn).to_contain_text("Starred")
    
    # In seeded data, notes 1 and 3 are starred in default collection
    starred_pins = page.locator("button.pin")
    expect(starred_pins).to_have_count(2)
    # The active detail should show a starred note
    expect(page.locator("#star")).to_have_attribute("aria-label", "Unstar observation")

    # 2. Cycle to 'Interviews' filter
    filter_btn.click()
    expect(filter_btn).to_contain_text("Interviews")
    
    # Notes 2 and 6 are interviews
    interview_pins = page.locator("button.pin")
    expect(interview_pins).to_have_count(2)
    expect(page.locator(".detail .note-type")).to_contain_text("INTERVIEW")

    # 3. Cycle back to 'All notes'
    filter_btn.click()
    expect(filter_btn).to_contain_text("All notes")
    expect(page.locator("button.pin")).to_have_count(6)
