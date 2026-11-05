# DESIGN.md  (single source of truth for this project's look)

Fill from the brief and from measured references. Reviewers score against this file.

## Brief
- Subject / product: Radha Krishna Surfactants Pvt. Ltd. (RK Surfactants) — LABSA 90% manufactured at Plot 79/80, Gundlav GIDC, Valsad, Gujarat 396035.
- Audience: Procurement and technical buyers at detergent, soap and cleaning-product plants in India who need a named LABSA 90% source with a spec, a plant, and a phone number.
- The page's one job (single primary action): Request a quote (or call +91 97277 02597).
- Format: web page (multi-page company site)
- User demands that override defaults (verbatim):
  - review as a LABSA 90% producer; walk the site; add/delete for customer experience
  - keep DNA-like structure sparse (not overlapping) and collage gaps as straight angled lines at staggered positions
  - hero headline “Entrust your supply to Gundlav.” — simple, professional, not generic
  - sync four new plant photos (yard/drums, RKSPL tanker, LABSA beaker, plant team)
  - provide a link to the company profile PDF
  - add new facts from the company profile
  - footer factory silhouette like the Vico Forge reference (original art, not copied)
  - inner-page banners little translucent with a plant photo behind them
  - do not name the seven workers in the team photograph

## References (one line each: file, what to take from it)
- Vico Forge footer: dark band with a factory silhouette along the bottom. Take the idea only; do not copy logo, copy, crane artwork or colours.
- Quality pagehead (before): solid navy slab. Replace with a photo-backed translucent navy banner, as on industrial template sites.

## Tokens
### Colour (name, hex, role). 5 to 7 total. Accent <= 10% of visual weight.
| name | hex | role |
|---|---|---|
| paper | #ffffff | background (about 60%) |
| mist | #f2f5f8 | surface / secondary bands (about 30%), blue-tinted grey |
| ink | #243038 | body text |
| muted | #3e4c58 | secondary text (must hold 4.5:1 on paper) |
| blue | #0154a7 | headings, links, signature chemistry lines |
| deep | #012056 | dark bands, header emphasis |
| action | #013ea8 | primary buttons only |

Line: #d3dbe3. Footer void: #011637.
Header glass: rgba(255,255,255,.86) with 14px blur. Pagehead overlay: rgba(1,22,55,.88) to rgba(1,32,86,.74) over tanker photo.

### Type
- Display face + role: Archivo (variable, slight stretch 112%) for wordmark, h1–h3, phone numbers
- Body face + role: IBM Plex Sans 400/600 for UI, body, tables
- Scale ratio and sizes (5 to 7 steps, body >= 16px): 12.5 / 16 / 18 / 24 / 38.4 / 44 (kicker 0.78rem, body 1rem, lead 1.125rem, h3 1.125rem, h2 clamp 1.5–2.4rem, h1 clamp 2.1–2.75rem)
- Line-height: body 1.65, headings 1.1
- Max line length: 62ch body; hero h1 two lines via `<br>` after “supply”

### Space and shape
- Spacing scale (4px base): 4 / 8 / 12 / 16 / 24 / 32 / 48 / 80
- Radii (max 3 values): 4px default; 0 on mosaic panes
- Shadows (max 3 elevations, or none): none (industrial, flat)
- Borders: 1px --line for tables, header, fact strip; used to encode structure only

### Motion
- Duration tokens (feedback 100-150ms, UI 150-250ms, entrance 500-800ms): feedback 150ms, UI 200ms, mosaic entrance 650ms
- Easing (ease-out family, no bounce): cubic-bezier(.2,.7,.2,1)
- The one signature moment: staggered mosaic panes settle in; chemistry field may sway slowly if motion is allowed

## Layout concept
- Archetype: industrial manufacturer — left-aligned claim, plant photography on the right, spec tables, place-named contact.
- Signature move: three-column plant mosaic with straight, staggered diagonal cuts; quiet benzene/helix field in the gutters (not overlapping); inner pages use a photo-backed navy pagehead; footer sits on a plant skyline silhouette (tanks, tanker, drums).
- Deliberate asymmetry: hero 5/6 columns; mosaic cuts at three different heights so the white seam is not one chevron.
- Section order and why it serves the argument: claim → plant facts (ISO, storage, place) → what buyers use it for → spec numbers → plant proof (tanker, barrels) → lab/ISO → named leadership + unnamed plant team → call/quote. Inner pages: product, plant, lab, people, quote form.

## Content rules
- Headline claim (specific, real number or outcome): “Entrust your supply to Gundlav.” with kicker LABSA 90%. Support with Gundlav GIDC, Valsad, 90 ± 1 active matter, ISO 9001:2015, 75 MT/day (~2,275 MT/month), 450 MT raw / 250 MT finished storage, own RKSPL VALSAD tanker, chairman’s 25 years in detergents and LABSA plants, incorporated 16 November 2019.
- Real product/people/imagery to show: own tanks, RKSPL tanker, barrel yard, LABSA in a beaker, unnamed plant team, in-house lab, named directors, Plot 79/80 Gundlav, Silvassa registered office, company profile PDF.
- Banned phrases: leading manufacturer, world-class, cutting-edge, transform your, unmatched quality, synergy, lorem, generic mission-speak without a plant fact. Do not invent packing kg. Do not name the seven workers.

## Fidelity checklist (only if a reference exists)
- [x] Palette stays navy/paper; Vico green is not imported
- [x] Footer silhouette along the bottom of a dark band (original tanks/tanker/drums, not Vico cranes)
- [x] Inner pageheads use a plant photo under a translucent navy wash
- [x] New content still uses this plant's language (Gundlav, LABSA 90%, Plot 79/80)
