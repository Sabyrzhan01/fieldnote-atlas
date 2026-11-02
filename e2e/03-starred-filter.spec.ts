import { test, expect } from '@playwright/test';

test.describe('Issue #56 — Starred and Interviews filter cycling', () => {
  test.beforeEach(async ({ request }) => {
    await request.post('/api/test/reset');
  });

  test('cycles through All notes, Starred, and Interviews filters (#56)', async ({ page }) => {
    await page.goto('/');

    const filterBtn = page.locator('#filter');
    await expect(filterBtn).toContainText('All notes');
    await expect(page.locator('button.pin')).toHaveCount(6);

    await filterBtn.click();
    await expect(filterBtn).toContainText('Starred');
    await expect(page.locator('button.pin')).toHaveCount(2);

    await filterBtn.click();
    await expect(filterBtn).toContainText('Interviews');
    await expect(page.locator('button.pin')).toHaveCount(2);
    await expect(page.locator('.detail .note-type')).toContainText('INTERVIEW');

    await filterBtn.click();
    await expect(filterBtn).toContainText('All notes');
    await expect(page.locator('button.pin')).toHaveCount(6);
  });
});
