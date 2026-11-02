import { test, expect } from '@playwright/test';

test.describe('Issue #62 — Interactive map markers & detail synchronization', () => {
  test.beforeEach(async ({ request }) => {
    await request.post('/api/test/reset');
  });

  test('selecting map pins updates active marker styling and detail reader content (#62)', async ({ page }) => {
    await page.goto('/');

    await expect(page.locator('.map-caption')).toContainText('ALMATY, KAZAKHSTAN');
    await expect(page.locator('button.pin')).toHaveCount(6);

    const pinTwo = page.locator("button.pin[title*='second bus']");
    await pinTwo.click();

    await expect(pinTwo).toHaveClass(/pin-active/);
    await expect(page.locator('.detail h2')).toContainText('We wait for the second bus');
    await expect(page.locator('.detail .note-place')).toContainText('Dostyk × Satpaev');

    await page.locator('#zoomIn').click();
    await expect(page.locator('.toast')).toContainText('Map zoom: 125%');

    await page.locator('#layers').click();
    await expect(page.locator('.toast')).toContainText('Map layer: Blueprint Night');
  });
});
