export const undoWindowMs = 30_000;

export function recoverableDeletion(storage, key, now = Date.now()) {
  try {
    const record = JSON.parse(storage.getItem(key));
    if (record?.observation?.id && record.expiresAt > now) return record;
    storage.removeItem(key);
  } catch {
    return null;
  }
  return null;
}

export function exportObservations(observations) {
  return JSON.stringify(observations, null, 2);
}
