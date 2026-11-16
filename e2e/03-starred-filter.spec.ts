import { test, expect } from '@playwright/test';

test.describe('Issue #56 — Starred and Interviews filters', () => {
  test.beforeEach(async ({ request }) => {
    await request.post('/api/test/reset');
  });

  test('selects All notes, Starred, and Interviews filters (#56)', async ({ page }) => {
    await page.goto('/');

    const filter = page.locator('#filter');
    await expect(filter).toHaveValue('All notes');
    await expect(page.locator('button.pin')).toHaveCount(6);

    await filter.selectOption('Starred');
    await expect(filter).toHaveValue('Starred');
    await expect(page.locator('button.pin')).toHaveCount(2);

    await filter.selectOption('Interviews');
    await expect(filter).toHaveValue('Interviews');
    await expect(page.locator('button.pin')).toHaveCount(2);
    await expect(page.locator('.detail .note-type')).toContainText('INTERVIEW');

    await filter.selectOption('All notes');
    await expect(filter).toHaveValue('All notes');
    await expect(page.locator('button.pin')).toHaveCount(6);
  });
});
