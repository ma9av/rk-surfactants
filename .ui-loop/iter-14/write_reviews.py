import json
from pathlib import Path

reviews = {
    "art_director.json": {
        "expert": "art_director",
        "scores": {
            "hierarchy_composition": {
                "score": 7.3,
                "evidence": "desktop_fold squint: one focal point -- white Archivo h1 on the yard-drums pagehead. Eye then splits to twin navy h2s (Your requirement | Contact details) at the same clamp size (~38px vs h1 44px). desktop_full: .wrap.cols.flip 6fr/5fr still reads 50/50; the form ends at Send quote request while two maps hold the row open, leaving a ~200px paper void before the footer reprints the same line at display size. Section order (quote banner -> form + named plant/office -> phones) is right. Prev: inner .cols 50/50 not fixed; inner h1 mad-lib not fixed (pagehead and footer h2 both Quote LABSA 90% from Gundlav). catalogue h2s, index h2#uses hanging the, about table clip: not visible. .btn:hover #000 waived (hover_submit.png).",
                "strengths": [
                    "Fold is one photo-backed claim, not a centred stack",
                    "Header Request a quote stays ghost; WhatsApp in the footer is outline",
                    "Footer skyline (tanks, tanker, drums) closes the page with a plant-shaped edge",
                ],
                "issues": [
                    {
                        "severity": "major",
                        "where": "contact .wrap.cols.flip",
                        "problem": "Leftover 50/50 not fixed: form and Contact details are equal-weight columns, so the page's job (the form) does not win; maps stretch the row and dump empty paper under Send quote request.",
                        "fix": "Do not use .cols on this section. Stack: form full width, then a full-width maps band. If two columns stay, set grid-template-columns: 1.8fr 1fr, keep only phones/PDF in the rail, and move both iframes below the grid.",
                    },
                    {
                        "severity": "major",
                        "where": "pagehead h1 and footer h2",
                        "problem": "Inner h1 mad-lib not fixed. Squint shows two climaxes of the same sentence Quote LABSA 90% from Gundlav -- pagehead and footer -- so size is flattened and colour does all the hierarchy.",
                        "fix": "Keep the pagehead as the claim. Change footer h2 to the plant numbers only (already in .phones) or Call Gundlav -- +91 97277 02597. Drop the duplicate Request a quote button on contact.html; leave WhatsApp as the footer action.",
                    },
                ],
            },
            "reference_fidelity": {
                "score": 7.5,
                "evidence": "No compare.png; scored vs DESIGN.md tokens. Navy/paper holds (--deep headings, --blue links, footer void + original tanks/tanker/drums skyline, not Vico green). Inner pagehead is translucent navy over yard photo as demanded. Square radius-0 matte CTAs; no header phone; disclaimer text only (disclaimer.png); maps in-page (factory_map.png, office_map.png -- Google Open in Maps chip is iframe chrome). Body still snaps to a generic manufacturer form|address split (prev major, not fixed). Header glass is rgba(255,255,255,.78) blur 16px vs token .86 / 14px. Inputs use --r 4px against square buttons.",
                "strengths": [
                    "Translucent navy pagehead and original plant skyline match the fidelity checklist",
                    "Contact demands executed: inline maps, no checkbox, no header phone, square matte buttons",
                    "Archivo + IBM Plex and scale 12.5/16/18/24/38.4/44 match the token table",
                ],
                "issues": [
                    {
                        "severity": "major",
                        "where": "contact .cols",
                        "problem": "Content beyond the pagehead still reads as a stock 50/50 manufacturer contact template instead of the 5/6 industrial devices in DESIGN.md.",
                        "fix": "Drop .cols on contact. Full-width form, then a place-map band (3px --blue left rule like .place) for Plot 79/80 and Silvassa, not a matching-height address column.",
                    },
                    {
                        "severity": "minor",
                        "where": "input, textarea",
                        "problem": "Fields use border-radius: var(--r) (4px) while every button is radius 0, so the control language splits between photo radius and square matte.",
                        "fix": "Set input, textarea, .place-map { border-radius: 0 } so form controls match the square matte buttons.",
                    },
                ],
            },
        },
    },
    "typographer.json": {
        "expert": "typographer",
        "scores": {
            "typography": {
                "score": 7.5,
                "evidence": "contact.html desktop_fold/desktop_full/desktop_s01-s02, form_end, tablet_full, mobile_full. Audit desktop families Archivo (212 chars) + IBM Plex Sans (1383); sizes 12.5/16/18/24/38.4/44; body 16px; 0 long lines; mobile h1 clamps to 33.6px with a clean two-line wrap. CSS: body 1rem/1.65 Plex; h1 clamp 2.1-2.75rem Archivo 700 stretch 112% tracking -0.025em lh 1.1; h2 clamp 1.5-2.4rem (38.4 vs 44 = ratio 1.15); pagehead lead 1.125rem/52ch. Footer h2 is the same 8 words as the page h1. .reach h3 forced to 1rem. Previous: inner Gundlav h1 formula still on this page (not fixed); catalogue h2s, index #uses, about table clip not on this page; .cols 50/50 is layout not type; .btn:hover wipe waived.",
                "strengths": [
                    "Archivo 112% stretch for wordmark/headings/footer phones vs IBM Plex Sans 400/600 for UI -- two faces, industrial roles, not Inter/Roboto.",
                    "Measured 6-step scale, body 16/1.65, heading lh 1.1, h1 tracking -0.025em, p max 62ch / pagehead 52ch, 0 long-line hits.",
                    "Footer plant/sales numbers at 1.5rem Archivo with 12.5px tracked PLANT / SALES kickers -- the type system doing its job.",
                ],
                "issues": [
                    {
                        "severity": "major",
                        "where": "h1.pagehead + footer h2#c",
                        "problem": "Page opens and closes on the identical display line Quote LABSA 90% from Gundlav. Desktop h1 is 44px, footer h2 is 38.4px (ratio 1.15), so the sitewide CTA title sits in the same optical band as the page title and also matches the two 38.4px section h2s (Your requirement / Contact details). Inner Gundlav formula from last round is still here.",
                        "fix": "Rewrite footer h2 to a quieter line (e.g. Call Gundlav for a LABSA 90% price) and set footer h2 to 1.5rem (24px, lh 1.1, tracking -0.015em) so the 24px Archivo phone numbers are the display climax. Cap .contact h2 at clamp(1.5rem, 2.4vw, 1.75rem) so section titles sit a full step under the 44px h1.",
                    },
                    {
                        "severity": "minor",
                        "where": ".reach h3, .reach a[href^=tel], .reach a[href*='wa.me']",
                        "problem": ".reach h3 is overridden to 1rem Archivo 700, the same size as .field label (1rem Plex 600). Tel/WhatsApp numbers in the directory stay 16px Plex while DESIGN and footer .phones set numbers in Archivo. Factory / Registered office therefore read at 16px in the column and 18px as footer h3.",
                        "fix": "Remove the .reach h3 {font-size:1rem} override so directory headings use the 1.125rem h3. Set .reach tel/WhatsApp links to font-family:var(--head); font-stretch:112%; font-weight:700; font-size:1.125rem; letter-spacing:-0.015em; line-height:1.2.",
                    },
                    {
                        "severity": "minor",
                        "where": ".pagehead p (desktop_fold)",
                        "problem": "Lead is 18px/52ch/1.65 and breaks after The team, leaving will reply to start line 2. Awkward rag on the only banner paragraph.",
                        "fix": "Insert a break after Gundlav. so line 2 starts The team will reply. You can also call or WhatsApp +91 97277 02597. Keep max-width:52ch.",
                    },
                    {
                        "severity": "minor",
                        "where": ".reach Email p",
                        "problem": "Two addresses are joined with a trailing space inside the first mailto and a space-comma-space. Sloppy list setting for the directory.",
                        "fix": "Stack each mailto on its own line: display:block on the three email links, delete the comma and the trailing space inside the first anchor.",
                    },
                ],
            }
        },
    },
    "systems_designer.json": {
        "expert": "systems_designer",
        "scores": {
            "color": {
                "score": 8.0,
                "evidence": "desktop_fold/desktop_s01: paper form, deep h2s, mist readonly Product, blue tel/mailto/PDF links, square deep submit. Pagehead is demanded navy wash over yard drums; footer is --deep with mist primary + ghost WhatsApp. Audit: 0/61 contrast fails, 3 bg colors, hue 225, text_color_count 7, no purple. hover_submit #000 wipe waived. .reach still paints six consecutive #0154a7 links, so chromatic accent is not the 10% act-here role; .btn fill is --deep not --action.",
                "strengths": [
                    "Blue-tinted neutrals (mist #f2f5f8, line #d3dbe3) match DESIGN.md; not default grey or indigo-on-white",
                    "Navy bands vs paper split is clear; mist on readonly Product vs white inputs encodes state",
                    "Contrast holds (0 fails); CTA hues 218/210 stay inside the navy family",
                ],
                "issues": [
                    {
                        "severity": "minor",
                        "where": ".reach a, .btn, contact.html sidebar",
                        "problem": "Accent blue is used on every phone, email, PDF and docs link, while the primary submit fills --deep (#012056) instead of --action (#013ea8). Act here is split and the sidebar reads as a blue list.",
                        "fix": "Keep .btn background as --action (or keep --deep but then set .reach a {color:var(--deep)} and plant tel/WhatsApp to var(--action) so only the two plant numbers carry the chromatic accent). Stack the three emails as separate block links.",
                    },
                    {
                        "severity": "minor",
                        "where": "input, textarea",
                        "problem": "Field chrome uses unnamed #5c6b78, outside the 7 named tokens (line is #d3dbe3, muted is #3e4c58).",
                        "fix": "Replace the input border with var(--muted). Do not introduce a fourth grey.",
                    },
                ],
            },
            "spacing_rhythm": {
                "score": 7.5,
                "evidence": "Audit: spacing_grid_adherence 100, spacing_distinct 10 (named scale has 8), distinct_radii 1, distinct_shadows 1. desktop_fold: ~80px section padding, ~48px column gap, 16px field stack, 4px label-to-input. .cols.flip is 6fr 5fr (no longer 1fr 1fr) but still reads even. desktop_full/desktop_s02: left column dies after the submit while .reach continues through two 16rem maps, leaving a large paper void. .docs is margin 0 0 16px; .reach h3 is 1.25rem (20px).",
                "strengths": [
                    "Form proximity ladder is readable: 4px label gap, 16px field gap, 48px column gap, 80px section padding",
                    "Your requirement / Contact details share a top edge; 0 radius on buttons, 4px on inputs, no card shadows",
                    "Borders only on inputs, maps, header and footer rules",
                ],
                "issues": [
                    {
                        "severity": "major",
                        "where": "section.contact .wrap.cols.flip; .place-map",
                        "problem": "Maps in the 5fr sidebar make .reach much taller than .formcard. desktop_full shows ~200-300px of empty paper under Send quote request. 6fr/5fr still looks like leftover 50/50, so the form is not the dominant column.",
                        "fix": "On min-width 1024px set .contact .cols.flip {grid-template-columns:minmax(0,7fr) minmax(22rem,4fr);gap:var(--s7)}. Move both .place-map blocks out of .reach into a full-width maps row under the two-col grid (Factory map | Office map, gap var(--s5), iframe height 16rem). Sidebar then stops at Factory address.",
                    },
                    {
                        "severity": "minor",
                        "where": "p.docs (contact form)",
                        "problem": "Inline margin:0 0 var(--s4) wipes .docs {margin-top:var(--s5)}. The TDS/SDS link sits 16px from the quantity row and 16px above Message -- the same rhythm as fields -- so a second action is not a separate group.",
                        "fix": "Remove the inline margin. Set .formcard .docs {margin:var(--s5) 0} (24px above and below) so it sits between the field grid and Message as its own band.",
                    },
                    {
                        "severity": "minor",
                        "where": ".reach h3",
                        "problem": "margin-top:1.25rem (20px) is on a 4px grid but not on the named 4/8/12/16/24 scale; audit reports 10 distinct spacing values vs 8 tokens.",
                        "fix": "Change .reach h3 to margin-top:var(--s5) (24px). Keep the two phone p's at 0 so intra-group gap stays smaller than the 24px between Phone, WhatsApp, Email.",
                    },
                ],
            },
        },
    },
}

out = Path(".ui-loop/iter-14/reviews")
for name, data in reviews.items():
    (out / name).write_text(json.dumps(data, ensure_ascii=True), encoding="ascii")
    json.loads((out / name).read_text())
    print(name, "ok")
