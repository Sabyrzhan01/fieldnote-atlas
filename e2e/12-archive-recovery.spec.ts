import { readFile } from 'node:fs/promises';
import { test, expect } from '@playwright/test';

test('confirms deletion, restores across a reload, and expires the undo window', async ({ page, request }) => {
  await request.post('/api/test/reset');
  const missing = await request.delete('/api/observations/missing-id-for-undo-check');
  expect(missing.status()).toBe(404);
  await page.goto('/');
  await expect(page.locator('button.pin')).toHaveCount(6);
  await page.locator('#options').click();
  await page.getByRole('button', { name: 'Delete observation' }).click();
  await expect(page.getByRole('dialog')).toContainText('A city measured in puddles');
  await page.getByRole('button', { name: 'Cancel', exact: true }).click();
  await expect(page.locator('button.pin')).toHaveCount(6);

  async function removeSelected() {
    await page.locator('#options').click();
    await page.getByRole('button', { name: 'Delete observation' }).click();
    await page.getByRole('button', { name: 'Confirm delete' }).click();
    await expect(page.locator('button.pin')).toHaveCount(5);
  }

  await removeSelected();
  await page.reload();
  await page.getByRole('button', { name: 'Undo', exact: true }).click();
  await expect(page.locator('button.pin')).toHaveCount(6);
  await page.reload();
  await expect(page.locator('button.pin')).toHaveCount(6);

  await page.clock.install();
  await removeSelected();
  await expect(page.getByRole('button', { name: 'Undo', exact: true })).toBeVisible();
  await page.clock.fastForward(31_000);
  await expect(page.getByRole('button', { name: 'Undo', exact: true })).toHaveCount(0);
  await page.reload();
  await expect(page.locator('button.pin')).toHaveCount(5);
});

test('browses, searches, creates and exports a filtered collection at 390px', async ({ page }) => {
  await page.setViewportSize({ width: 390, height: 844 });
  await page.goto('/?mock=1');
  await page.getByRole('button', { name: /Quiet infrastructures/ }).click();
  await page.locator('#add').click();
  await page.getByLabel('Title', { exact: true }).fill('Алматы — Café & «арық»');
  await page.getByLabel('Observation', { exact: true }).fill('Тестовая заметка');
  await page.getByLabel('Place', { exact: true }).fill('Алматы');
  await page.getByLabel('Tags', { exact: true }).fill('Алматы, café');
  await page.getByRole('button', { name: /Add to atlas/ }).click();
  const search = page.getByRole('textbox', { name: 'Search observations' });
  await search.focus();
  await expect(search).toBeFocused();
  await search.fill('café Алматы');
  await expect(page.getByRole('heading', { name: 'Алматы — Café & «арық»' })).toBeVisible();
  const downloadPromise = page.waitForEvent('download');
  await page.locator('#export').click();
  const download = await downloadPromise;
  const filename = await download.path();
  expect(filename).toBeTruthy();
  const notes = JSON.parse(await readFile(filename!, 'utf8'));
  expect(notes).toHaveLength(1);
  expect(notes[0]).toMatchObject({
    collection_id: 'c2', title: 'Алматы — Café & «арық»', tags: ['Алматы', 'café'],
  });
});
