import { test, expect } from '@playwright/test';

test.describe('Issue #57 — Create new observation entry modal', () => {
  test.beforeEach(async ({ request }) => {
    await request.post('/api/test/reset');
  });

  test('creates a new observation via modal and updates map pins and detail reader (#57)', async ({ page }) => {
    await page.goto('/');

    await expect(page.locator('button.pin')).toHaveCount(6);
    await page.locator('#add').click();

    const modal = page.locator('#noteForm');
    await expect(modal).toBeVisible();

    await page.fill("input[name='title']", 'Zhibek Zholy Metro Mosaic');
    await page.fill("textarea[name='body']", 'Glazed ceramic murals under warm underground lights.');
    await page.fill("input[name='place']", 'Zhibek Zholy Station');
    await page.fill("input[name='tags']", 'metro, mosaic');

    await modal.locator('button.add').click();

    await expect(modal).toHaveCount(0);
    await expect(page.locator('button.pin')).toHaveCount(7);
    await expect(page.locator('.detail h2')).toContainText('Zhibek Zholy Metro Mosaic');
    await expect(page.locator('.detail .note-place')).toContainText('Zhibek Zholy Station');
  });
});
