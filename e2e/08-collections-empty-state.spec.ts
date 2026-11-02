import { test, expect } from '@playwright/test';

test.describe('Issue #61 — Collections switching & empty collection state', () => {
  test.beforeEach(async ({ request }) => {
    await request.post('/api/test/reset');
  });

  test('switches between collections and renders empty-detail state when collection has 0 notes (#61)', async ({ page }) => {
    await page.goto('/');

    await expect(page.locator('.hero h1')).toContainText('The city after rain');
    await expect(page.locator('button.pin')).toHaveCount(6);

    const secondCollection = page.locator("[data-col='1']");
    await secondCollection.click();

    await expect(secondCollection).toHaveClass(/selected/);
    await expect(page.locator('.hero h1')).toContainText('Quiet infrastructures');
    await expect(page.locator('button.pin')).toHaveCount(0);
    await expect(page.locator('.empty-detail')).toBeVisible();
    await expect(page.locator('.empty-detail')).toContainText('No observation selected');
  });
});
