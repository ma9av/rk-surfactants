# UI review loop report

Target: 9.0  |  Profile: web

| Iter | Final | Blockers | Decision |
|---|---|---|---|
| 1 | 6.6 | 1 | CONTINUE |
| 2 | 7.1 | 0 | CONTINUE |
| 3 | 7.5 | 0 | CONTINUE |
| 4 | 7.6 | 0 | CONTINUE |
| 5 | 7.8 | 0 | STOP_MAX_ITER |
| 6 | 7.7 | 0 | STOP_MAX_ITER |
| 7 | 7.5 | 0 | STOP_PLATEAU |
| 8 | 7.5 | 0 | STOP_PLATEAU |
| 9 | 7.8 | 0 | STOP_PLATEAU |
| 10 | 7.6 | 0 | STOP_PLATEAU |
| 11 | 7.5 | 0 | STOP_MAX_ITER |
| 12 | 7.5 | 0 | STOP_MAX_ITER |
| 13 | 7.3 | 0 | STOP_MAX_ITER |
| 14 | 7.5 | 0 | STOP_MAX_ITER |
| 15 | 7.8 | 0 | STOP_PLATEAU |
| 16 | 7.8 | 0 | STOP_MAX_ITER |
| 17 | 7.9 | 0 | STOP_PLATEAU |
| 18 | 8.1 | 0 | PASS |
| 19 | 8.1 | 0 | STOP_PLATEAU |
| 20 | 8.1 | 0 | STOP_PLATEAU |
| 21 | 7.9 | 0 | STOP_PLATEAU |
| 22 | 7.8 | 0 | STOP_PLATEAU |

## Final dimension scores

| Dimension | Score | Note |
|---|---|---|
| hierarchy_composition | 7.5 |  |
| typography | 8.0 |  |
| color | 8.2 |  |
| spacing_rhythm | 8.3 |  |
| distinctiveness | 6.6 |  |
| ux_clarity | 7.5 |  |
| reference_fidelity | 8.0 |  |
| interaction_motion | 8.0 |  |
| a11y_responsive | 8.7 |  |

## Still open

- **hierarchy_composition** desktop_fold.png / .pagehead + intro figure.ph: Fold squint fails the one-focal test. Two similar industrial stills stacked. (fix: Point .pagehead--beaker at the sample-tube still. Leave storage-tanks only on the intro figure.)
- **hierarchy_composition** .apps 4-up: Four equal tiles flatten the 700-800 MT detergent story. (fix: Make the first article grid-column span 2. Keep four tiles.)
- **distinctiveness** pagehead h1 and lead: Headline is a category SKU. Gundlav, Valsad, Gujarat not in the hero. (fix: Lead: 90 +/- 1 from Gundlav, Valsad, Gujarat.)
- **distinctiveness** .apps Textile Agriculture Leather: Openings are generic use-cases. (fix: Lead with plant constraints.)
- **distinctiveness** intro spec flow FAQ: Same plant numbers restated. (fix: Keep packing in spec; FAQ tanker only.)
- **ux_clarity** .pagehead p: Subhead says made at Plot 79/80. City and state not in the fold. (fix: Lead with Gundlav, Valsad, Gujarat. Plot only in the footer.)

## Waived at the user's request

- header_phone_removed: user demand: remove the number from the header (stays in footer and mobile Call bar)
- square_matte_buttons: user demand: matte finish, no rounded edges, animated
- keep_translucent_banners: user demand: do not remove inner-page photo banners; navbar-only change
- contact_disclaimer_no_checkbox: user demand: remove the checkbox, keep the disclaimer as text
- contact_inline_maps: user demand: instead of Open in Maps links, show the map in the webpage
- labsa_copy_from_reference: user demand: use shreeshyamgroup.co/Home/Labsa as a content reference; rewrite in RK voice, keep our styling and existing page elements. Do not copy their visual system.
- labsa_ref_layout: user demand: use pasted reference images for layout (tinted cards, process steps, intro split) with our theme colors; fix overlapping blue lines and FAQ/apps text
- labsa_lean_copy: user demand: remove unnecessary text and repeated Request a quote, not the good information; remove unnecessary subheadings; retrieve necessary plant facts; keep designed section breaks
- photo_reveal_translucent_varied: user demand: different image animations, not all left-to-right; translucent overlay instead of opaque
