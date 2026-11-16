import L from 'leaflet';
import 'leaflet/dist/leaflet.css';

const cityCenter = [43.2383, 76.9455];
const cityZoom = 11;

export function hasLocation(note) {
  return Number.isFinite(note?.latitude) && Number.isFinite(note?.longitude);
}

export function createCityMap({ onSelect, onPlace }) {
  const container = document.createElement('div');
  container.className = 'city-map';
  container.setAttribute('aria-label', 'Street map of Almaty');
  let map;
  let pins;

  function mount(slot, notes, selected) {
    slot.append(container);
    if (!map) {
      map = L.map(container, { scrollWheelZoom: false }).setView(cityCenter, cityZoom);
      const tiles = L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
      }).addTo(map);
      const status = document.createElement('p');
      status.className = 'city-map-status';
      status.setAttribute('role', 'status');
      container.append(status);
      let tileLoaded = false;
      tiles.on('loading', () => { tileLoaded = false; });
      tiles.on('tileload', () => { tileLoaded = true; status.textContent = ''; });
      tiles.on('load', () => {
        status.textContent = tileLoaded ? '' : 'Street tiles are unavailable. Try the sketch map.';
      });
      L.control.scale({ imperial: false }).addTo(map);
      pins = L.layerGroup().addTo(map);
      map.on('click', ({ latlng }) => onPlace({
        latitude: Number(latlng.lat.toFixed(6)),
        longitude: Number(latlng.wrap().lng.toFixed(6)),
      }));
    }
    map.invalidateSize({ pan: false });
    pins.clearLayers();
    for (const note of notes.filter(hasLocation)) {
      const label = document.createElement('span');
      label.textContent = note.title;
      const dot = L.divIcon({
        className: note.id === selected ? 'city-pin city-pin-selected' : 'city-pin',
        iconSize: [20, 20],
      });
      L.marker([note.latitude, note.longitude], { icon: dot, title: note.title, bubblingMouseEvents: false })
        .bindTooltip(label)
        .on('click', () => onSelect(note.id))
        .addTo(pins);
    }
  }

  return {
    mount,
    center: () => map?.setView(cityCenter, cityZoom),
    focus: note => map?.setView([note.latitude, note.longitude], 16),
  };
}
