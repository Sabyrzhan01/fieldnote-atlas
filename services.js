/** Shared service contract for the mock and integrated API workflows. */
export function createMockService({ storage = globalThis.localStorage, seedObservations = [], collections = [], key = 'fieldnote-atlas-v1' } = {}) {
  const read = () => {
    try { return JSON.parse(storage.getItem(key)) || structuredClone(seedObservations); }
    catch { return structuredClone(seedObservations); }
  };
  const write = (observations) => storage.setItem(key, JSON.stringify(observations));
  const atlas = (observations) => ({
    collections: collections.map((collection) => ({
      ...collection,
      observationCount: observations.filter((item) => (item.collection_id || 'c1') === collection.id).length,
    })),
    observations,
  });
  return {
    async getAtlas() { return atlas(read()); },
    async createObservation(input) {
      const current = read();
      const item = { ...input, id: input.id || crypto.randomUUID(), collection_id: input.collection_id || 'c1' };
      write([item, ...current]);
      return atlas([item, ...current]);
    },
    async toggleStar(id) {
      const current = read().map((item) => item.id === id ? { ...item, starred: !item.starred } : item);
      write(current);
      return atlas(current);
    },
    async deleteObservation(id) {
      const current = read().filter((item) => item.id !== id);
      write(current);
      return atlas(current);
    },
  };
}

export function createApiService(fetchImpl = globalThis.fetch, base = '/api') {
  async function request(path, options) {
    const response = await fetchImpl(`${base}${path}`, options);
    if (!response.ok) throw new Error(`API request failed (${response.status})`);
    return response.json();
  }
  return {
    getAtlas: () => request('/atlas'),
    createObservation: (item) => request('/observations', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(item) }),
    toggleStar: (id) => request(`/observations/${encodeURIComponent(id)}/star`, { method: 'POST' }),
    deleteObservation: (id) => request(`/observations/${encodeURIComponent(id)}`, { method: 'DELETE' }),
  };
}
