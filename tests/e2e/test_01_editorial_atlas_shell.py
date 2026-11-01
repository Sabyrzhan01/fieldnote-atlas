import pytest
from playwright.sync_api import Page, expect

def test_editorial_atlas_shell_renders_header_sidebar_and_collections(page: Page, base_url: str):
    """E2E Test: Editorial Atlas Shell rendering, branding, sidebar, and collections."""
    page.goto(base_url)

    # 1. Check Brandmark and Title
    brand = page.locator(".brand")
    expect(brand).to_contain_text("FIELDNOTE")
    expect(brand).to_contain_text("ATLAS / STUDIO")

    # 2. Check Workspace Selector
    workspace = page.locator(".workspace")
    expect(workspace).to_contain_text("Sabyr’s workspace")
    expect(workspace).to_contain_text("Personal studio")

    # 3. Check Collections in Library
    collections = page.locator(".library button.collection")
    expect(collections).to_have_count(3)
    
    # First collection should be selected by default
    first_col = collections.first
    expect(first_col).to_have_class("collection selected")
    expect(first_col).to_contain_text("The city after rain")

    # 4. Check Topbar Breadcrumb and Status
    breadcrumbs = page.locator(".breadcrumbs")
    expect(breadcrumbs).to_contain_text("The city after rain")
    expect(page.locator(".breadcrumbs .pill")).to_contain_text("PRIVATE")

    # 5. Check Hero Section
    expect(page.locator(".hero h1")).to_contain_text("The city after rain")
    expect(page.locator(".hero-side .hero-number").first).to_contain_text("OBSERVATIONS")

    # 6. Switch to second collection
    second_col = page.locator("[data-col='1']")
    second_col.click()
    expect(second_col).to_have_class("collection selected")
    expect(page.locator(".hero h1")).to_contain_text("Quiet infrastructures")
