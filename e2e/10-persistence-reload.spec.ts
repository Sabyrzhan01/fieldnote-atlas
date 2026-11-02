import { test, expect } from '@playwright/test';

test.describe('Issue #63 — Database persistence after browser reload', () => {
  test.beforeEach(async ({ request }) => {
    await request.post('/api/test/reset');
  });

  test('persists newly created observations across full page reloads (#63)', async ({ page }) => {
    await page.goto('/');

    await page.locator('#add').click();
    await page.fill("input[name='title']", 'Persistent Kok Tobe Observation');
    await page.fill("textarea[name='body']", 'Verified PostgreSQL persistence across browser reload.');
    await page.fill("input[name='place']", 'Kok Tobe');
    await page.fill("input[name='tags']", 'persistence, postgres');
    await page.locator('#noteForm button.add').click();

    await expect(page.locator('button.pin')).toHaveCount(7);
    await expect(page.locator('.detail h2')).toContainText('Persistent Kok Tobe Observation');

    await page.reload();

    await expect(page.locator('button.pin')).toHaveCount(7);
    await expect(page.locator("button.pin[title='Persistent Kok Tobe Observation']")).toBeVisible();
  });
});
