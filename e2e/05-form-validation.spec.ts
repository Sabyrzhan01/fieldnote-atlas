import { test, expect } from '@playwright/test';

test.describe('Issue #58 — Form validation & API schema validation', () => {
  test.beforeEach(async ({ request }) => {
    await request.post('/api/test/reset');
  });

  test('enforces required form fields in UI and rejects invalid payloads with 422 (#58)', async ({ page, request }) => {
    await page.goto('/');

    await page.locator('#add').click();
    const modal = page.locator('#noteForm');
    await expect(modal).toBeVisible();

    await expect(modal.locator("input[name='title']")).toHaveAttribute('required', '');
    await expect(modal.locator("textarea[name='body']")).toHaveAttribute('required', '');

    await page.locator('#cancel').click();
    await expect(modal).toHaveCount(0);

    const invalidResp = await request.post('/api/observations', {
      data: {
        collection_id: 'c1',
        title: '   ',
        body: 'Valid body',
        kind: 'InvalidKind',
        place: 'Abay',
        region: 'Almaty',
        date: 'Today',
        color: '#d87551',
        tags: [],
        source: 'Walk',
        starred: false,
        x: 150,
        y: -10,
      },
    });
    expect(invalidResp.status()).toBe(422);
  });
});
