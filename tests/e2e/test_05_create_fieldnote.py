import pytest
from playwright.sync_api import Page, expect

def test_create_fieldnote_via_modal(page: Page, base_url: str):
    """E2E Test: Create observation modal flow, cancellation, form validation, and instant atlas update."""
    page.goto(base_url)

    # Initial count
    initial_pins = page.locator("button.pin").count()

    # 1. Verify modal open and cancellation does not modify atlas
    page.locator("#add").click()
    expect(page.locator("#noteForm")).to_be_visible()
    page.locator("#cancel").click()
    expect(page.locator("#noteForm")).to_have_count(0)
    expect(page.locator("button.pin")).to_have_count(initial_pins)

    # 2. Re-open Modal to create a new fieldnote
    add_btn = page.locator("#add")
    add_btn.click()

    modal = page.locator("#noteForm")
    expect(modal).to_be_visible()
    expect(modal.locator("h2")).to_contain_text("What did you notice?")

    # 3. Fill form fields
    page.fill("input[name='title']", "Zhibek Zholy Metro Mosaic")
    page.fill("textarea[name='body']", "Glazed ceramic murals depict silk road travelers under warm underground lights.")
    page.fill("input[name='place']", "Zhibek Zholy Station")
    page.fill("input[name='tags']", "metro, mosaic, silkroad")

    # 4. Submit form
    modal.locator("button.add").click()

    # 5. Verify modal closes and toast appears
    expect(page.locator("#noteForm")).to_have_count(0)
    toast = page.locator(".toast")
    expect(toast).to_contain_text("Observation added to your atlas")

    # 6. Verify pin count increased
    expect(page.locator("button.pin")).to_have_count(initial_pins + 1)

    # 7. Verify newly created observation is active in detail reader
    expect(page.locator(".detail h2")).to_contain_text("Zhibek Zholy Metro Mosaic")
    expect(page.locator(".detail .note-place")).to_contain_text("Zhibek Zholy Station")
    expect(page.locator(".detail .tags")).to_contain_text("#metro")
    expect(page.locator(".detail .tags")).to_contain_text("#mosaic")
