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
  - remove the number from the header, and give the buttons , matte finish , and I dont want rounded edges in the button , and want it animated and look good
  - dont remove the translucent banner like you did, as it doesnt look good , just make the change in the navbar, remove number and make the button changes
  - contact.html: remove the checkbox, just keep the disclaimer, and instead of open in maps, show the map in the webpage

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
Header glass: rgba(255,255,255,.86) with 14px blur. Pagehead overlay (one for every page): 105deg rgba(1,22,55,.9) → rgba(1,32,86,.74) → rgba(1,32,86,.46) plus a bottom fade, over the page photo at saturate(.72); per page only `--ph` / `--ph-pos` change.

### Photography
- Files are colour-graded once by `.ui-loop/grade_photos.py` (gentle white balance, exposure to a common luma, S-curve, saturation ×0.84, navy shadows / warm highlights). Ungraded originals live in `.ui-loop/img-originals/`; re-run the script after adding a photo.
- Every content photo is `<figure class="ph">`: 4px radius, navy bottom gradient + 1px inset line, caption with a 14px blue tick. `.ph--tall` = 4:5. No feathered/blended variants (user demand: every photo gets the same framed treatment).
- Photos: process-tanks (plant hall vessels), labsa-sample-tube, tanker-rkspl, tank-labsa, tank-red, lab, plant-team.

### Type
- Display face + role: Archivo (variable, slight stretch 112%) for wordmark, h1–h3, phone numbers
- Body face + role: IBM Plex Sans 400/600 for UI, body, tables
- Scale ratio and sizes (5 to 7 steps, body >= 16px): 12.5 / 16 / 18 / 24 / 38.4 / 44 (kicker 0.78rem, body 1rem, lead 1.125rem, h3 1.125rem, h2 clamp 1.5–2.4rem, h1 clamp 2.1–2.75rem)
- Line-height: body 1.65, headings 1.1
- Max line length: 62ch body; hero h1 two lines via `<br>` after “supply”

### Space and shape
- Spacing scale (4px base): 4 / 8 / 12 / 16 / 24 / 32 / 48 / 80
- Radii (max 3 values): 0 on buttons and the menu control (user demand: no rounded edges); 4px on photographs; 0 on the hero carousel frame (diagonal 2rem bottom cut)
- Shadows (max 3 elevations, or none): none (industrial, flat)
- Borders: 1px --line for tables, header, fact strip; used to encode structure only

### Motion
- Duration tokens: --t-feedback 150ms, --t-ui 200ms, --t-enter 650ms, --t-scroll 500ms
- Easing (ease-out family, no bounce): cubic-bezier(.2,.7,.2,1)
- Signature entrance (one orchestrated moment): hero carousel settles 650ms; slides change by a slanted clip-path wipe (900ms) with a 7s Ken Burns settle and the caption rising after 450ms. Inner pageheads: title and lead settle 550ms.
- Scroll (informational, not fade-up on every block): 2px read-progress on the sticky header; .place left rule draws; spec rows take a 3px blue inset when in view; uses ticks scale in; header densifies after 8px scroll.
- Photo reveal: a navy curtain wipes off each `.ph` (900ms) while the image settles from 1.12 to 1 (1.4s); pagehead photos do a 16s Ken Burns settle.
- Hover / micro: every text link shifts to --deep; plant photos scale to 1.04 and the tint lifts; nav underline; spec row mist; square matte buttons wipe fill from the left in 200ms (no gloss, no radius); inputs border to --blue.
- Header bar: no plant phone (user demand). Quote is the only navbar action. Number stays in the footer and the mobile Call bar. Inner-page translucent photo banners stay (user demand: do not remove them).
- UI changes 200ms: mobile menu fade/slide; form aria-invalid #a4260c; submit label becomes “Sending…” while aria-busy; disabled buttons ignore hover.
- All of the above lives behind prefers-reduced-motion: no-preference (and html.motion). Reduced-motion renders the settled end state. User demand: scroll, hover, micro and major motion across pages.

## Layout concept
- Archetype: industrial manufacturer — left-aligned claim, plant photography on the right, spec tables, place-named contact.
- Signature move: hero carousel (WAI-ARIA pattern) telling Make → Store → Test → Ship in four plant photos, diagonal-cut frame on an offset blue tint, step-labelled progress bar that autoplays at 6s, pauses on hover / keyboard focus / pause button, never autoplays under reduced motion, swipe on touch; quiet benzene/helix field in the gutters (not overlapping); inner pages use a photo-backed navy pagehead; footer sits on a plant skyline silhouette (tanks, tanker, drums).
- Deliberate asymmetry: hero 5/6 columns; carousel frame offset block breaks the column edge.
- Section order and why it serves the argument: claim → plant facts (ISO, storage, place) → barrel proof with yard photograph → spec numbers → plant proof (tanker, acid tank) → lab/ISO → named leadership + unnamed plant team → call/quote. Inner pages each use a different plant photo under the navy pagehead (sample tube, acid tank, lab, plant team, process tanks), each with a 1.5rem diagonal bottom edge matching the hero.

## Content rules
- Headline claim (specific, real number or outcome): “LABSA 90%, direct from the maker.” with kicker “Surfactant manufacturer · Gujarat”. Do not lead with Gundlav in headings (user demand); keep it to the factory address. Support with 90 ± 1 active matter, ISO 9001:2015, 75 MT/day (~2,275 MT/month), 300 MT raw / 200 MT finished storage, own RKSPL VALSAD tanker, chairman’s 25 years in detergents and LABSA plants, incorporated 16 November 2019.
- Real product/people/imagery to show: own tanks, RKSPL tanker, barrel yard, LABSA in a beaker, unnamed plant team, in-house lab, named directors, Plot 79/80 Gundlav, Silvassa registered office, company profile PDF.
- Banned phrases: leading manufacturer, world-class, cutting-edge, transform your, unmatched quality, synergy, lorem, generic mission-speak without a plant fact. Do not invent packing kg. Do not name the seven workers.

## Fidelity checklist (only if a reference exists)
- [x] Palette stays navy/paper; Vico green is not imported
- [x] Footer silhouette along the bottom of a dark band (original tanks/tanker/drums, not Vico cranes)
- [x] Inner pageheads use a plant photo under a translucent navy wash
- [x] New content still uses this plant's language (Gundlav, LABSA 90%, Plot 79/80)
