import test from 'node:test';
import assert from 'node:assert/strict';
import { createMockService, createApiService } from '../../services.js';

class MemoryStorage {
  values = new Map();
  getItem(key) { return this.values.get(key) ?? null; }
  setItem(key, value) { this.values.set(key, value); }
}
const seed = [
  { id: 'one', collection_id: 'c1', title: 'Rain path', body: 'Shortcuts', starred: false, tags: ['rain'] },
  { id: 'two', collection_id: 'c2', title: 'Night pipe', body: 'Low hum', starred: true, tags: ['sound'] },
];
const collections = [{ id: 'c1', title: 'Rain' }, { id: 'c2', title: 'Infrastructure' }];

test('mock service creates in selected collection and calculates scoped counts', async () => {
  const storage = new MemoryStorage();
  const service = createMockService({ storage, seedObservations: seed, collections });
  const result = await service.createObservation({ id: 'three', collection_id: 'c2', title: 'Valve', body: 'Clicks at dusk', starred: false, tags: [] });
  assert.equal(result.observations[0].id, 'three');
  assert.deepEqual(result.collections.map((c) => c.observationCount), [1, 2]);
  const reloaded = await createMockService({ storage, seedObservations: seed, collections }).getAtlas();
  assert.equal(reloaded.observations.length, 3);
});

test('mock service toggles star and deletes only the requested note', async () => {
  const service = createMockService({ storage: new MemoryStorage(), seedObservations: seed, collections });
  const starred = await service.toggleStar('one');
  assert.equal(starred.observations.find((x) => x.id === 'one').starred, true);
  const deleted = await service.deleteObservation('one');
  assert.deepEqual(deleted.observations.map((x) => x.id), ['two']);
  assert.deepEqual(deleted.collections.map((c) => c.observationCount), [0, 1]);
});

test('API service uses the documented HTTP routes and JSON body', async () => {
  const calls = [];
  const service = createApiService(async (path, options = {}) => {
    calls.push([path, options]);
    return { ok: true, json: async () => ({ observations: [] }) };
  });
  await service.getAtlas();
  await service.createObservation({ title: 'Test' });
  await service.toggleStar('a b');
  await service.deleteObservation('a b');
  assert.deepEqual(calls.map((x) => x[0]), ['/api/atlas', '/api/observations', '/api/observations/a%20b/star', '/api/observations/a%20b']);
  assert.equal(JSON.parse(calls[1][1].body).title, 'Test');
});

test('API service surfaces a useful error for rejected requests', async () => {
  const service = createApiService(async () => ({ ok: false, status: 422 }));
  await assert.rejects(service.getAtlas(), /422/);
});
