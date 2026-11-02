import { test, expect } from '@playwright/test';

test.describe('Issue #59 — Star and unstar observation', () => {
  test.beforeEach(async ({ request }) => {
    await request.post('/api/test/reset');
  });

  test('toggles observation starred state and shows toast notification (#59)', async ({ page }) => {
    await page.goto('/');

    const pinTwo = page.locator("button.pin[title*='second bus']");
    await pinTwo.click();

    const starBtn = page.locator('#star');
    await expect(starBtn).toHaveAttribute('aria-label', 'Star observation');

    await starBtn.click();
    await expect(starBtn).toHaveAttribute('aria-label', 'Unstar observation');
    await expect(page.locator('.toast')).toContainText('Added to starred observations');

    await starBtn.click();
    await expect(starBtn).toHaveAttribute('aria-label', 'Star observation');
    await expect(page.locator('.toast')).toContainText('Removed from starred observations');
  });
});
