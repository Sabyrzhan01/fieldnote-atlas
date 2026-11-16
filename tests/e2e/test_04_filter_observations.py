from playwright.sync_api import Page, expect

def test_filter_observations_all_starred_and_interviews(page: Page, base_url: str):
    """E2E Test: Select All notes, Starred, and Interviews."""
    page.goto(base_url)

    note_filter = page.locator("#filter")
    expect(note_filter).to_have_value("All notes")
    expect(page.locator("button.pin")).to_have_count(6)

    # 1. Select 'Starred' filter
    note_filter.select_option("Starred")
    expect(note_filter).to_have_value("Starred")

    # In seeded data, notes 1 and 3 are starred in default collection
    starred_pins = page.locator("button.pin")
    expect(starred_pins).to_have_count(2)
    # The active detail should show a starred note
    expect(page.locator("#star")).to_have_attribute("aria-label", "Unstar observation")

    # 2. Select 'Interviews' filter
    note_filter.select_option("Interviews")
    expect(note_filter).to_have_value("Interviews")

    # Notes 2 and 6 are interviews
    interview_pins = page.locator("button.pin")
    expect(interview_pins).to_have_count(2)
    expect(page.locator(".detail .note-type")).to_contain_text("INTERVIEW")

    # 3. Select 'All notes'
    note_filter.select_option("All notes")
    expect(note_filter).to_have_value("All notes")
    expect(page.locator("button.pin")).to_have_count(6)
