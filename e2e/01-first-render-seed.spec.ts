import { test, expect } from '@playwright/test';

test.describe('Issue #54 — First render & seeded data', () => {
  test.beforeEach(async ({ request }) => {
    await request.post('/api/test/reset');
  });

  test('renders editorial shell, 3 collections, and 6 seeded Almaty observations (#54)', async ({ page }) => {
    await page.goto('/');

    await expect(page.locator('.brand')).toContainText('FIELDNOTE');
    await expect(page.locator('.brand')).toContainText('ATLAS / STUDIO');
    await expect(page.locator('.workspace')).toContainText('Sabyr’s workspace');

    const collections = page.locator('.library button.collection');
    await expect(collections).toHaveCount(3);
    await expect(collections.first()).toHaveClass(/selected/);
    await expect(collections.first()).toContainText('The city after rain');

    await expect(page.locator('.hero h1')).toContainText('The city after rain');
    await expect(page.locator('button.pin')).toHaveCount(6);
    await expect(page.locator('.detail h2')).toContainText('A city measured in puddles');
  });
});
