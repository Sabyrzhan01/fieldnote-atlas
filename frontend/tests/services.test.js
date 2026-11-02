import { describe, it, expect } from 'vitest';
import { createMockService, createApiService } from '../services.js';

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

describe('Fieldnote Atlas Frontend Services', () => {
  it('mock service creates in selected collection and calculates scoped counts', async () => {
    const storage = new MemoryStorage();
    const service = createMockService({ storage, seedObservations: seed, collections });
    const result = await service.createObservation({
      id: 'three',
      collection_id: 'c2',
      title: 'Valve',
      body: 'Clicks at dusk',
      starred: false,
      tags: [],
    });
    expect(result.observations[0].id).toBe('three');
    expect(result.collections.map((c) => c.observationCount)).toEqual([1, 2]);
    const reloaded = await createMockService({ storage, seedObservations: seed, collections }).getAtlas();
    expect(reloaded.observations.length).toBe(3);
  });

  it('mock service toggles star and deletes only the requested note', async () => {
    const service = createMockService({ storage: new MemoryStorage(), seedObservations: seed, collections });
    const starred = await service.toggleStar('one');
    expect(starred.observations.find((x) => x.id === 'one').starred).toBe(true);
    const updated = await service.updateObservation('one', { title: 'Updated rain path' });
    expect(updated.observations.find((x) => x.id === 'one').title).toBe('Updated rain path');
    const deleted = await service.deleteObservation('one');
    expect(deleted.observations.map((x) => x.id)).toEqual(['two']);
    expect(deleted.collections.map((c) => c.observationCount)).toEqual([0, 1]);
  });

  it('API service uses the documented HTTP routes and JSON body', async () => {
    const calls = [];
    const service = createApiService(async (path, options = {}) => {
      calls.push([path, options]);
      return { ok: true, json: async () => ({ observations: [] }) };
    });
    await service.getAtlas();
    await service.createObservation({ title: 'Test' });
    await service.toggleStar('a b');
    await service.deleteObservation('a b');
    expect(calls.map((x) => x[0])).toEqual([
      '/api/atlas',
      '/api/observations',
      '/api/observations/a%20b/star',
      '/api/observations/a%20b',
    ]);
    expect(JSON.parse(calls[1][1].body).title).toBe('Test');
  });

  it('API service surfaces a useful error for rejected requests', async () => {
    const service = createApiService(async () => ({ ok: false, status: 422 }));
    await expect(service.getAtlas()).rejects.toThrow(/422/);
  });
});
