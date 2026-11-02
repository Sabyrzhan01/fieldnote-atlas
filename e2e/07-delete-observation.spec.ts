import { test, expect } from '@playwright/test';

test.describe('Issue #60 — Delete observation', () => {
  test.beforeEach(async ({ request }) => {
    await request.post('/api/test/reset');
  });

  test('deletes selected observation via options modal and updates map pins (#60)', async ({ page }) => {
    await page.goto('/');

    await expect(page.locator('button.pin')).toHaveCount(6);
    await expect(page.locator('.detail h2')).toContainText('A city measured in puddles');

    await page.locator('#options').click();
    const deleteBtn = page.locator('#deleteNote');
    await expect(deleteBtn).toBeVisible();
    await deleteBtn.click();

    await expect(page.locator('.toast')).toContainText('Observation deleted');
    await expect(page.locator('button.pin')).toHaveCount(5);
    await expect(page.locator('.detail h2')).not.toContainText('A city measured in puddles');
  });
});
