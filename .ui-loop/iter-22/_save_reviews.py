import json
from pathlib import Path

out = Path(__file__).parent / "reviews"
out.mkdir(exist_ok=True)

reviews = {
    "art_director": {
        "expert": "art_director",
        "scores": {
            "hierarchy_composition": {
                "score": 7.5,
                "evidence": "desktop_fold.png squint: two competing masses, not one. White Archivo h1 LABSA 90% on a short navy pagehead and the large storage-tank photograph in the intro split. Hierarchy otherwise uses size+weight+colour together. Process zipper changes rhythm after the four-up.",
                "strengths": ["Intro split is a composed industrial spread.", "Process zipper changes rhythm after the four-up."],
                "issues": [
                    {
                        "severity": "major",
                        "where": "desktop_fold.png / .pagehead + intro figure.ph",
                        "problem": "Fold squint fails the one-focal test. Two similar industrial stills stacked.",
                        "fix": "Point .pagehead--beaker at the sample-tube still. Leave storage-tanks only on the intro figure.",
                    },
                    {
                        "severity": "major",
                        "where": ".apps 4-up",
                        "problem": "Four equal tiles flatten the 700-800 MT detergent story.",
                        "fix": "Make the first article grid-column span 2. Keep four tiles.",
                    },
                ],
            },
            "reference_fidelity": {
                "score": 8.0,
                "evidence": "Shree Shyam layout signatures vs desktop_full: intro split, tinted tiles, staggered process. RK navy/mist/paper held. Inner pagehead is a plant photo under a translucent navy wash.",
                "strengths": ["Three Shree Shyam layout moves in RK navy/mist/paper."],
                "issues": [
                    {
                        "severity": "minor",
                        "where": ".chem-row and .apps",
                        "problem": "Large unused mist around the molecule; three under-filled tiles.",
                        "fix": "Tighten chem-row padding. Span detergent 2 columns.",
                    }
                ],
            },
        },
    },
    "typographer": {
        "expert": "typographer",
        "scores": {
            "typography": {
                "score": 8.0,
                "evidence": "Archivo 700 stretch 112% vs IBM Plex Sans. Body 16px/1.65; h1 44px tracking -0.025em. Detergent plants is one line. Leather 5.5-6.5 still drops to its own line after free-acid.",
                "strengths": ["Archivo vs IBM Plex with distinct roles.", "Body 16px/1.65, 0 long lines."],
                "issues": [
                    {
                        "severity": "minor",
                        "where": ".apps article:nth-child(4) p",
                        "problem": "nowrap keeps 5.5-6.5 intact but the token still drops a line.",
                        "fix": "Wrap 'Same free-acid 5.5-6.5' in nowrap.",
                    },
                    {
                        "severity": "minor",
                        "where": ".pagehead p",
                        "problem": "Lead wraps so Plot 79/80 sits alone on line two.",
                        "fix": "nowrap the place phrase.",
                    },
                ],
            }
        },
    },
    "systems_designer": {
        "expert": "systems_designer",
        "scores": {
            "color": {
                "score": 8.2,
                "evidence": "paper/mist/deep split. Audit 0 contrast fails. Pagehead overlay is translucent. .apps mixes still read as one dusty panel.",
                "strengths": ["0 contrast fails", "Blue as signature chrome"],
                "issues": [
                    {
                        "severity": "minor",
                        "where": ".apps article fills",
                        "problem": "22/14/8/16 color-mix still reads as one pale slab.",
                        "fix": "Steepen mixes to 34/20/8/26.",
                    }
                ],
            },
            "spacing_rhythm": {
                "score": 8.3,
                "evidence": "Audit spacing_grid_adherence 99% desktop. Pack section padding s7/s8. Process stagger even +32px.",
                "strengths": ["99% 4px grid", "One 4px photo radius; square buttons"],
                "issues": [
                    {
                        "severity": "minor",
                        "where": ".apps at 1024",
                        "problem": "Grid stretch leaves empty fill under short copy.",
                        "fix": "align-items: start on .apps.",
                    }
                ],
            },
        },
    },
    "ux_lead": {
        "expert": "ux_lead",
        "scores": {
            "ux_clarity": {
                "score": 7.5,
                "evidence": "Fold states LABSA 90%, 90 +/- 1, Request a quote. Quote chrome-only. Hero subhead still Plot 79/80 not Gundlav, Valsad, Gujarat. Textile/Agriculture/Leather still open with category-use sentences.",
                "strengths": ["Fold states product, buyer, next step.", "Quote confined to header, footer, mobile bar."],
                "issues": [
                    {
                        "severity": "major",
                        "where": ".pagehead p",
                        "problem": "Subhead says made at Plot 79/80. City and state not in the fold.",
                        "fix": "Lead with Gundlav, Valsad, Gujarat. Plot only in the footer.",
                    },
                    {
                        "severity": "minor",
                        "where": ".apps Textile Agriculture Leather",
                        "problem": "Open with category-use lines; plant constraints buried.",
                        "fix": "Lead with plant-specific sentence then the use.",
                    },
                ],
            }
        },
    },
    "motion_designer": {
        "expert": "motion_designer",
        "scores": {
            "interaction_motion": {
                "score": 8.0,
                "evidence": "Settled photos show no leftover curtain. CSS: translucent color-mix wash not opaque --deep. Directions: RTL default, tall rise/drop, product clip, portrait iris, grid floor, pack-shot slant. Reduced-motion skips overlay. audit has_motion true, overshoot_easing false.",
                "strengths": [
                    "Translucent washes with picture-specific directions instead of one opaque LTR curtain.",
                    "Reduced-motion skip is double-gated.",
                ],
                "issues": [
                    {
                        "severity": "minor",
                        "where": "html.motion .ph::before",
                        "problem": "Overlay 0.95s and image 1.4s over the 500-800ms entrance cap.",
                        "fix": "Overlay 700ms; image transform 650ms.",
                    },
                    {
                        "severity": "minor",
                        "where": ".ph--product.is-in::before",
                        "problem": "inset(100% 0 0 0) peels from the top. Fill-from-bottom was the intent.",
                        "fix": "inset(0 0 100% 0) so the wash recedes upward.",
                    },
                    {
                        "severity": "minor",
                        "where": ".ph::before easing",
                        "problem": "cubic-bezier(.7,0,.2,1) is ease-in weighted.",
                        "fix": "Use var(--ease).",
                    },
                    {
                        "severity": "minor",
                        "where": ".photos even stills",
                        "problem": "Even grid stills collapse axis-aligned; slant exists only on pack-shot.",
                        "fix": "Give even grid stills the pack-shot polygon.",
                    },
                ],
            }
        },
    },
    "a11y_qa": {
        "expert": "a11y_qa",
        "scores": {
            "a11y_responsive": {
                "score": 8.7,
                "evidence": "Audit 0 blockers; 0 contrast fails; 0 taps under 44; no 375 overflow; 21/21 focus. Photo wash gated by html.motion and prefers-reduced-motion.",
                "strengths": ["Audit clean", "Layout reflows desktop to mobile"],
                "issues": [
                    {
                        "severity": "minor",
                        "where": "ol.flow .flow-n",
                        "problem": "Visible 01-04 badges are aria-hidden.",
                        "fix": "Remove aria-hidden from .flow-n.",
                    }
                ],
            }
        },
    },
    "skeptic": {
        "expert": "skeptic",
        "scores": {
            "distinctiveness": {
                "score": 6.6,
                "evidence": "Fold h1 is the SKU LABSA 90%. Scroll has 75 MT/day, RKSPL VALSAD, 700-800 MT, acid-not-salt. Catalog headings are user demands. Textile/Agriculture/Leather still encyclopedia openings.",
                "strengths": ["Acid-not-salt with sample tube", "Detergent tile names 700-800 MT"],
                "issues": [
                    {
                        "severity": "major",
                        "where": "pagehead h1 and lead",
                        "problem": "Headline is a category SKU. Gundlav, Valsad, Gujarat not in the hero.",
                        "fix": "Lead: 90 +/- 1 from Gundlav, Valsad, Gujarat.",
                    },
                    {
                        "severity": "major",
                        "where": ".apps Textile Agriculture Leather",
                        "problem": "Openings are generic use-cases.",
                        "fix": "Lead with plant constraints.",
                    },
                    {
                        "severity": "major",
                        "where": "intro spec flow FAQ",
                        "problem": "Same plant numbers restated.",
                        "fix": "Keep packing in spec; FAQ tanker only.",
                    },
                ],
            }
        },
    },
}

for name, data in reviews.items():
    path = out / f"{name}.json"
    path.write_text(json.dumps(data, ensure_ascii=True, indent=2), encoding="utf-8")
    print("wrote", path.name)
