# Design direction

## Reference brief for v0 / Lovable / coding agent
Create a quiet, editorial urban fieldwork atlas. Imagine a beautifully typeset research journal opened beside a map: warm off-white paper, delicate rules, dusty terracotta pins, sage map patches, tiny cartographic labels, and restrained dark ink. The interface should have hierarchy and whitespace; avoid generic SaaS gradients, bright blue, oversized cards, rounded-everything, and dashboard KPI clutter. Collection titles use an elegant display serif; operational labels use a precise mono; body copy is human and readable. The map is the hero, with selected evidence in a narrow reading panel. Use hand-composed map geometry and clear markers if live map tiles are unavailable.

## Inspiration references
- Mapbox Studio's restrained cartographic label hierarchy and layered map composition.
- Are.na's calm visual research/archive browsing and modular evidence objects.
- Kinfolk / The New Yorker digital typography: confident editorial serif paired with restrained utility text.
- Fieldnotes Brand notebooks: tactile, durable, practical fieldwork character.

These are visual references only; do not copy brand assets or exact layouts.

## Tokens and behavior
- Canvas `#f6f5f1`, sidebar `#f0efe9`, paper `#fbfaf7`, ink `#2c302b`, muted `#898b82`, rule `#e7e5de`, accent `#cc6949`.
- Typography: DM Sans for controls/body, DM Mono for metadata, Playfair Display for collection and note titles.
- Pins use category color and a selected halo. Labels reveal on hover or selection.
- Give buttons hover/focus states, meaningful accessible labels, visible error feedback, and preserve content when a form validation error occurs.
- Responsive desktop target; make layout usable at 900px. Mobile layout remains a follow-up.
