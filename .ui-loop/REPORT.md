# UI review loop report

Target: 8.0  |  Profile: web

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

## Final dimension scores

| Dimension | Score | Note |
|---|---|---|
| hierarchy_composition | 8.0 |  |
| typography | 8.3 |  |
| color | 8.0 |  |
| spacing_rhythm | 8.0 |  |
| distinctiveness | 7.5 |  |
| ux_clarity | 8.5 |  |
| reference_fidelity | 8.2 |  |
| interaction_motion | 8.0 |  |
| a11y_responsive | 8.7 |  |

## Still open

- **hierarchy_composition** .chem .fig and .chem::after: Full-width SVG plus a 7% ghost leave a pale field under the strokes. (fix: Cap .chem .fig img at max-width 28rem. Set .chem::after {content:none}.)
- **distinctiveness** .faq details biodegradable feedstock: Still encyclopedia copy. (fix: Replace with Do you send a CoA and SDS before the first order?)
- **distinctiveness** #intro h2: As we dispatch it is an empty heading; lede still opens with a definition. (fix: Retitle to Barrel-filled at Plot 79/80 and start at At Plot 79/80 we sulphonate...)
- **distinctiveness** .faq cosmetics and personal use: Two FAQ rows answer the same no consumer pack. (fix: Keep one personal-size question; replace the other with What is on the CoA.)
- **spacing_rhythm** section.chem .cols--top / .ph--product: Beaker is shorter than heading plus full-width schematic, leaving a mist hole under the photo. (fix: Cap the schematic at 28rem and stretch the photo column, or drop the ghost.)
- **color** .chem::after vs .chem .fig img: Ghost structure sits on the solid schematic as overlapping blue lines. (fix: Set .pack .chem::after{content:none}.)

## Waived at the user's request

- header_phone_removed: user demand: remove the number from the header (stays in footer and mobile Call bar)
- square_matte_buttons: user demand: matte finish, no rounded edges, animated
- keep_translucent_banners: user demand: do not remove inner-page photo banners; navbar-only change
- contact_disclaimer_no_checkbox: user demand: remove the checkbox, keep the disclaimer as text
- contact_inline_maps: user demand: instead of Open in Maps links, show the map in the webpage
- labsa_copy_from_reference: user demand: use shreeshyamgroup.co/Home/Labsa as a content reference; rewrite in RK voice, keep our styling and existing page elements. Do not copy their visual system.
- labsa_ref_layout: user demand: use pasted reference images for layout (tinted cards, process steps, intro split) with our theme colors; fix overlapping blue lines and FAQ/apps text; avoid empty space
