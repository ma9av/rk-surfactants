import json
from pathlib import Path

d = Path(__file__).parent / "reviews"
d.mkdir(parents=True, exist_ok=True)

reviews = {
"art_director": {
  "expert": "art_director",
  "scores": {
    "hierarchy_composition": {
      "score": 7.8,
      "evidence": "desktop_fold squint: three staggered mosaic panes (tanks; yard with drums and a worker; RKSPL tanker) dominate the right. Headline Entrust your supply to Gundlav is second. Filled Request a quote is third. Hero is left-aligned on mist. Mosaic col2 is now the yard. Inner folds all open on the same tanker crop so page identity is only the h1 word.",
      "strengths": [
        "Hero is a left claim / right three-pane mosaic with straight staggered cuts.",
        "Primary Request a quote is filled; See specification is a text link.",
        "Quality page proof sequence (lab photo, then LABSA in a beaker) is specific."
      ],
      "issues": [
        {"severity": "major", "where": "homepage h2 Barrel-filled at Plot 79/80", "problem": "After the photo mosaic this band is display-size type plus three bullets and no photograph. Later caption Barrel filling at the plant sits on a truck-cab/yard frame, not filling.", "fix": "Put the yard-and-drums pane in this section as a 420px right column. Do not caption a parked truck as barrel filling."},
        {"severity": "major", "where": "inner .pagehead on Quality, Manufacturing, About, LABSA 90%, Contact", "problem": "Every inner fold uses the same RKSPL tanker crop under the same navy wash. First-screen hierarchy does not change by page.", "fix": "Keep the translucent navy recipe. Use the lab on Quality, tank farm on Manufacturing, plant-team on About, tanker on LABSA and Contact."},
        {"severity": "minor", "where": "homepage below-fold rows", "problem": "Four consecutive left-copy / right-media 50/50 splits after the mosaic.", "fix": "Flip Every batch is tested to photo-left / copy-right and make The plant a full-bleed image strip."},
        {"severity": "minor", "where": "contact_fold h2 Your requirement vs Contact details", "problem": "Two equal-weight navy h2s split the quote fold.", "fix": "Keep Your requirement at ~38px. Set Contact details to 18px/600 on a #f2f5f8 panel."},
        {"severity": "minor", "where": "header Request a quote vs hero Request a quote", "problem": "Action #013ea8 and link #0154a7 read as one blue.", "fix": "Keep #013ea8 on filled buttons only. Set nav and body links to #243038 with underline."}
      ]
    },
    "reference_fidelity": {
      "score": 7.5,
      "evidence": "No compare.png. Judged from refs/vico-footer.png vs footer_crop.png, and inner photo pageheads vs a flat navy slab. Footer takes the idea: navy void, original shed/tanks/tanker/drums, no cranes, no Vico green. Skyline is mid-navy on #011637 so on squint it is quieter than the reference. Inner pageheads show the tanker through a navy wash instead of a solid slab.",
      "strengths": [
        "Footer uses original tank, tanker and drum skyline on a dark band; navy not Vico green.",
        "Inner pageheads are photo-backed rather than a flat navy slab.",
        "Pages still use this plant's photos, tables and place names."
      ],
      "issues": [
        {"severity": "major", "where": "footer silhouette vs refs/vico-footer.png", "problem": "RK tanks/tanker/drums are a close navy on #011637, so the signature strip almost disappears on squint.", "fix": "Recolor the silhouette fill to about #4a6a88 with #012056 inner cuts. Vary shed vs tank vs drum heights by at least 40px. Do not add cranes or import Vico green."},
        {"severity": "minor", "where": "inner .pagehead overlay", "problem": "Overlay near 0.88 keeps the banners feeling like navy slabs with faint tanker texture.", "fix": "Use a left-to-right overlay rgba(1,22,55,0.82) at the title to rgba(1,32,86,0.58) over the tanker."},
        {"severity": "minor", "where": "inner pagehead photo asset", "problem": "One repeated tanker banner on every inner page.", "fix": "Swap in the lab on Quality, tank farm on Manufacturing, and plant team on About; keep the tanker on LABSA and Contact."}
      ]
    }
  }
},
"typographer": {
  "expert": "typographer",
  "scores": {
    "typography": {
      "score": 8.2,
      "evidence": "Archivo 700 stretch 112% for display and IBM Plex Sans 400/600 for body. Audit sizes 12.5/14.4/16/18/20/24/38.4/44px; body 16px/1.65; h1 44px tracking -0.025em; p max-width 62ch; long_line_count 0. Mobile h1 33.6px. Contact h2 is now Quote LABSA 90% from Gundlav. Scale leaks (8 sizes, h3 = lead) keep this below 9.",
      "strengths": [
        "Archivo 112% stretch vs IBM Plex Sans is a deliberate industrial pair.",
        "Body 16px/1.65, 62ch measure, h1 44px with tight tracking, tabular-nums on spec figures.",
        "Hero locked to two lines; plant/sales phones set as Archivo numerals with tracked labels."
      ],
      "issues": [
        {"severity": "major", "where": "table.spec th on index.html #spec and labsa-90.html", "problem": "50/50 columns wrap labels as (% by / weight) and values as alkyl / benzene.", "fix": "Set table.spec to table-layout:fixed with col 13.5rem 1fr. Put a br before each (% by weight) unit."},
        {"severity": "minor", "where": "h3, .hero .lead, .pagehead p, .reach h3, figcaption", "problem": "h3 is 18px, the same size as lead. Eight sizes vs the 5-7 step scale.", "fix": "Set h3 to 1.25rem (20px). Restyle .reach h3 to 0.78125rem uppercase. Set figcaption to .78125rem."},
        {"severity": "minor", "where": "manufacturing.html h2#rm", "problem": "Raw materials and product tanks leaves the widow tanks.", "fix": "Add text-wrap:balance on h1,h2 and a br after Raw materials."},
        {"severity": "minor", "where": "about.html table td legal name", "problem": "Private Limited wraps so Limited sits alone.", "fix": "Use Private&nbsp;Limited so the legal suffix stays together."}
      ]
    }
  }
},
"systems_designer": {
  "expert": "systems_designer",
  "scores": {
    "color": {
      "score": 8.0,
      "evidence": "Tokens match DESIGN.md. Audit contrast_fail_count 0, distinct_bg_colors 5, dominant hue 225, cta_hues [218,218], purple_primary false. --action #013ea8 vs --blue #0154a7 remain 22 G-steps apart, same hue.",
      "strengths": [
        "Seven named tokens with blue-tinted mist, not default grey.",
        "Zero contrast failures; on-dark contact inverts CTAs to paper on --deep.",
        "One radius, no shadows, no purple/gradient-text palette"
      ],
      "issues": [
        {"severity": "major", "where": ":root --action vs --blue", "problem": "--action #013ea8 and --blue #0154a7 both measure hue 218. Filled quote, outline header CTA, and See specification all read as the same blue.", "fix": "Set --action to #012056 for filled .btn / .bar a+a only; keep --blue #0154a7 for links."},
        {"severity": "minor", "where": "input, .status.err, footer, pagehead p", "problem": "Named 7-colour system leaks hex: input #5c6b78, error #a4260c, on-dark #c9d3e0.", "fix": "Add --field, --on-dark, --press, --danger to :root and replace those literals."},
        {"severity": "minor", "where": ".top on inner pageheads", "problem": "Glass is rgba(255,255,255,.78) blur(16px). Over tanker banners the bar still reads as solid paper.", "fix": "On pages with .pagehead, lower alpha to .62 so the tanker wash tints the bar."}
      ]
    },
    "spacing_rhythm": {
      "score": 8.0,
      "evidence": "Audit spacing_grid_adherence 100; spacing_distinct 9; distinct_radii 1; distinct_shadows 0. Scale 4/8/12/16/24/32/48/80. Off-scale: footer padding 6.5rem / skyline 7.5rem. quality_fold lab photo taller than copy.",
      "strengths": [
        "100% 4px-grid adherence with one 4px radius and no card shadows.",
        "Consistent s7/s8 section padding and 5/6 column gap.",
        "Mosaic 8px seams vs 48-80px section gaps; .place 24px band is a real rhythm change."
      ],
      "issues": [
        {"severity": "major", "where": "quality.html .cols In-house laboratory", "problem": "Lab photograph fills the left column; two short paragraphs leave a tall white void under the copy.", "fix": "Cap the photo at max-height 22rem object-fit cover, or move the batch-check table into the text column."},
        {"severity": "minor", "where": "contact.html h2#fm and .reach h2", "problem": "Your requirement and Contact details use the same 1.5-2.4rem clamp as marketing h2s.", "fix": "Add .formcard h2, .reach h2 {font-size:1.5rem;margin-bottom:var(--s5)}."},
        {"severity": "minor", "where": "index.html section#uses", "problem": "Left column is a single h2 with no supporting line; right column is three list rows.", "fix": "Set this section to padding-block var(--s6) at 1024px and put a one-line p under the h2."},
        {"severity": "minor", "where": "footer", "problem": "Footer padding 6.5rem and ::after height 7.5rem are off the 4-80 scale. Privacy sits on the skyline.", "fix": "Change footer to padding var(--s6) 0 var(--s8); footer::after height var(--s8)."}
      ]
    }
  }
},
"ux_lead": {
  "expert": "ux_lead",
  "scores": {
    "ux_clarity": {
      "score": 7.0,
      "evidence": "desktop_fold five-second test passes: LABSA 90%, Entrust your supply to Gundlav, 90 +/- 1 at Gundlav GIDC, Request a quote, tel +91 97277 02597. Cover-the-logo passes. Mosaic col2 is now yard-drums. Company profile PDF is a real link. Two prior majors remain: document CTAs still open a quote form that requires Quantity (MT); plant figcaption Barrel filling at the plant is a parked truck and drums.",
      "strengths": [
        "Fold states product, place, buyer, and next action in one viewport.",
        "Spec numbers, ISO 9001:2015, CIN, Plot 79/80, and named chairman sit next to the claims they support.",
        "Quote form has labels, required markers, error/sending/success copy, and a phone fallback."
      ],
      "issues": [
        {"severity": "major", "where": "index/quality/labsa document CTAs; contact.html #quantity[required]", "problem": "A buyer asking for TDS/SDS/CoA with no order is sent to the quote form. Quantity required (MT) blocks submit. PDF download is fixed; the document path is not.", "fix": "Point those CTAs to contact.html?need=docs. If need=docs, unrequire quantity, prefill the message, and set the submit label to Send document request."},
        {"severity": "major", "where": "index.html #plant second figure figcaption Barrel filling at the plant", "problem": "The photo is a Tata truck nose and stacked blue drums. Proof does not sit next to the packing claim.", "fix": "Change that figcaption to Tata tanker nose and blue drums in the Gundlav yard. Do not caption a parked truck as barrel filling."},
        {"severity": "minor", "where": "quality.html .pagehead", "problem": "Quality first viewport is the RKSPL tanker, the same banner as Contact/About/LABSA.", "fix": "Keep the translucent navy pagehead. Set the Quality banner image to lab-900.webp."}
      ]
    }
  }
},
"motion_designer": {
  "expert": "motion_designer",
  "scores": {
    "interaction_motion": {
      "score": 7.5,
      "evidence": "hover.png and focus.png were not captured (skip-link off-canvas). CSS has :focus-visible 3px, hover/active on named controls, 150ms transitions inside prefers-reduced-motion:no-preference, 650ms mosaic entrance, DNA sway gated. Audit: has_motion true, has_reduced_motion_rule true, overshoot_easing false, focus_invisible_count 0. Generic body anchors have no hover.",
      "strengths": [
        "3px :focus-visible ring on 25 controls; audit reports 0 invisible focus.",
        "Motion is opt-in: 150ms control feedback and one 650ms mosaic entrance.",
        "prefers-reduced-motion gating leaves panes at their settled state."
      ],
      "issues": [
        {"severity": "major", "where": "a (body copy, .reach, .consent, table.spec td)", "problem": "Named .btn/.link/.nav/.foot/.phones controls have hover; generic anchors do not.", "fix": "Add a:hover{color:var(--deep)} a:active{color:var(--void)} and include a in the transition list."},
        {"severity": "minor", "where": ".btn[disabled] vs .btn:hover", "problem": "Hover can still paint a busy submit deep navy. Button label stays Send quote request.", "fix": "Add .btn[disabled]:hover,.btn[disabled]:active with pointer-events none. Set submit text to Sending while aria-busy."},
        {"severity": "minor", "where": ".mcol .pane:last-child animation-delay", "problem": "Column delays are overridden by last-child delay, so all three panes enter at 150ms.", "fix": "Delete the last-child delay. Keep nth-child(2) at .12s and nth-child(3) at .24s."},
        {"severity": "minor", "where": "form.enquiry [aria-invalid]", "problem": "JS sets aria-invalid but CSS has no invalid border.", "fix": "Add input[aria-invalid=true],textarea[aria-invalid=true]{border-color:#a4260c}."},
        {"severity": "minor", "where": ".contact .btn:hover and :active", "problem": "Pressed equals hover on the navy-band primary.", "fix": "Set .contact .btn:active{background:#c9d3e0;color:var(--void)}."}
      ]
    }
  }
},
"a11y_qa": {
  "expert": "a11y_qa",
  "scores": {
    "a11y_responsive": {
      "score": 8.6,
      "evidence": "Audit: blockers=[], contrast_fail_count 0, focus_invisible_count 0 of 25, tap_targets_under_44 0, img_missing_alt 0, landmarks main/nav/footer true, horizontal_overflow false. Skip is off-canvas and returns on focus at 44px. Mosaic empty alts under role=img. Team alts describe the group not names. mobile_full is a one-column reflow; tablet_full is two-column. Remaining: JS-only mobile nav, unnamed spec tables, 12.5px footer type, form novalidate.",
      "strengths": [
        "Clean audit: 0 contrast fails, 0 invisible focus, 0 sub-44 targets, skip + one h1 + landmarks.",
        "Labeled quote form with aria-invalid and real tel/WhatsApp/PDF anchors.",
        "375px and tablet reflow; mosaic decorative imgs empty-alt; team photo unnamed as demanded."
      ],
      "issues": [
        {"severity": "minor", "where": ".nav ul below 1024px", "problem": "Nav list is display:none until JS toggles .nav.open.", "fix": "Add a noscript or :target rule so #navlist displays as a column below 1024px without main.js."},
        {"severity": "minor", "where": "table.spec", "problem": "Data tables use th scope=row but have no caption or aria-label.", "fix": "Add a visually-hidden caption on the spec, plant, and company-details tables."},
        {"severity": "minor", "where": "footer", "problem": "footer font-size .78125rem (12.5px) is below a 14px low-vision floor.", "fix": "Set footer to font-size 1rem; if CIN must stay quieter, use .875rem on that line only."},
        {"severity": "minor", "where": "form.enquiry on contact.html", "problem": "novalidate turns off native required when JS is off, and the form has no action URL.", "fix": "Remove novalidate; keep the JS preventDefault path; add a mailto or server action."}
      ]
    }
  }
},
"skeptic": {
  "expert": "skeptic",
  "scores": {
    "distinctiveness": {
      "score": 6.5,
      "evidence": "desktop_fold cover-the-logo passes: Entrust your supply to Gundlav, Plot 79/80, mosaic of this plant's tanks, yard, and lettered RKSPL VALSAD tanker. Then undone: every inner page stamps the same tanker crop; CSS hides mosaic col3 below 1024px and all but the grey tank below 768px; Barrel filling caption sits on a parked cab and drums; TDS/SDS still require Quantity (MT). slop_flags empty. Not an 8: a competitor could keep the chrome, swap the H1, and reuse the tanker banner.",
      "strengths": [
        "Homepage mosaic uses this plant's tanks, yard with drums/worker, and RKSPL VALSAD lettering.",
        "Named facts: Plot 79/80, CIN U24297DN2019PTC005589, Binay Chandra Jha, 75 MT/day, 90+/-1; plant team unnamed as demanded.",
        "Hard-ban list is clean: slop_flags [], no purple primary, no gradient headlines, no three-card row."
      ],
      "issues": [
        {"severity": "major", "where": ".pagehead on all inner pages", "problem": "Every inner banner is the same RKSPL tanker crop under the same navy wash.", "fix": "Keep the navy wash. Use lab-900 for Quality, tank-red for Manufacturing, plant-team for About, labsa-beaker for LABSA 90%, yard-drums for Contact."},
        {"severity": "major", "where": "index.html #plant second figure", "problem": "Caption reads Barrel filling at the plant; alt is Tata tanker nose and blue barrels. The photo is a parked cab and drums, not filling.", "fix": "Change the home figcaption to Blue barrels and tanker nose in the Gundlav yard."},
        {"severity": "major", "where": ".mosaic at max-width 1023px and 767px", "problem": "The signature collage is desktop-only. Tablet hides the lettered tanker; mobile leaves only the grey tank.", "fix": "At 768-1023px keep tank + tanker. At 375px stack two clipped panes (tank and tanker) instead of display:none."},
        {"severity": "major", "where": "document CTAs vs contact.html Quantity required (MT)", "problem": "Copy promises sheets with no order; CTAs open the quote form whose quantity field is required MT. PDF links are fine.", "fix": "Point document CTAs to contact.html?intent=docs and unrequire quantity on that path."},
        {"severity": "minor", "where": "index.html h2#plant, h2#qc", "problem": "Below the demanded hero, headings are category labels: The plant, Every batch is tested.", "fix": "Rename to Plot 79/80, Gundlav GIDC and Klett, titration and hot-air oven at Gundlav."}
      ]
    }
  }
}
}

for name, obj in reviews.items():
    path = d / f"{name}.json"
    path.write_text(json.dumps(obj, ensure_ascii=True, indent=2), encoding="utf-8")
    print("wrote", path.name)
