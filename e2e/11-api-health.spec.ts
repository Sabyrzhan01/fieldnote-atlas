import { test, expect } from '@playwright/test';

test.describe('Issue #64 — GET /api/health & REST contract verification', () => {
  test.beforeEach(async ({ request }) => {
    await request.post('/api/test/reset');
  });

  test('GET /api/health returns 200 ok and /api/atlas returns collections and observations (#64)', async ({ request }) => {
    const healthResp = await request.get('/api/health');
    expect(healthResp.status()).toBe(200);
    const healthJson = await healthResp.json();
    expect(healthJson).toEqual({ status: 'ok' });

    const atlasResp = await request.get('/api/atlas');
    expect(atlasResp.status()).toBe(200);
    const atlasJson = await atlasResp.json();
    expect(atlasJson.collections.length).toBeGreaterThanOrEqual(3);
    expect(atlasJson.observations.length).toBe(6);
  });
});
