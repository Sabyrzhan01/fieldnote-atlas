import { test, expect } from '@playwright/test';

test.describe('Issue #55 — Real-time search across title, body, and tags', () => {
  test.beforeEach(async ({ request }) => {
    await request.post('/api/test/reset');
  });

  test('filters map pins and detail reader by title, tag, and body query (#55)', async ({ page }) => {
    await page.goto('/');

    const search = page.locator('#search');
    await expect(search).toBeVisible();

    await search.fill('puddles');
    await expect(page.locator('button.pin')).toHaveCount(1);
    await expect(page.locator('.detail h2')).toContainText('A city measured in puddles');

    await search.fill('transit');
    await expect(page.locator('button.pin')).toHaveCount(1);
    await expect(page.locator('.detail h2')).toContainText('We wait for the second bus');

    await search.fill('asphalt');
    await expect(page.locator('button.pin')).toHaveCount(1);
    await expect(page.locator('.detail h2')).toContainText('The blue repair patch');

    await search.fill('nonexistent-xyz-query');
    await expect(page.locator('button.pin')).toHaveCount(0);
    await expect(page.locator('.empty-detail')).toBeVisible();

    await search.fill('');
    await expect(page.locator('button.pin')).toHaveCount(6);
  });
});
