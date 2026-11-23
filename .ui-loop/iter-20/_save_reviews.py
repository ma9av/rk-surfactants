import json
from pathlib import Path

out = Path(__file__).parent / "reviews"
out.mkdir(parents=True, exist_ok=True)

reviews = {
    "art_director": {
        "expert": "art_director",
        "scores": {
            "hierarchy_composition": {
                "score": 8.3,
                "evidence": "Squint: navy pagehead h1. Quote in chrome only. Intro hole gone. 80px pack padding.",
                "strengths": [
                    "Navy pagehead h1 is the single squint focal point",
                    "Section order is a buyer argument",
                    "Paper/mist bands with 80px pack padding"
                ],
                "issues": [
                    {
                        "severity": "minor",
                        "where": ".apps article:first-child",
                        "problem": "Detergent still wraps to four body lines.",
                        "fix": "Two lines: 700-800 MT cake and powder in Gujarat, MH, CG, MP, TN, Kerala."
                    }
                ]
            },
            "reference_fidelity": {
                "score": 8.5,
                "evidence": "Intro photo-left plus chevrons; four tiles; staggered 01-04. Quote not in spec/apps/FAQ.",
                "strengths": [
                    "Intro split matches photo-left plus chevron list",
                    "Four app tiles and 01-04 stagger",
                    "RK navy pagehead, square buttons, tube, structure, spec stay"
                ],
                "issues": [
                    {
                        "severity": "minor",
                        "where": ".apps fills",
                        "problem": "Four tints still collapse to one pale bar.",
                        "fix": "Steepen fills to 22/14/8/16 percent blue on mist."
                    }
                ]
            }
        }
    },
    "typographer": {
        "expert": "typographer",
        "scores": {
            "typography": {
                "score": 8.0,
                "evidence": "Archivo vs Plex, body 16px, 0 long lines. Detergent 4 lines not 2.",
                "strengths": [
                    "Archivo display vs IBM Plex Sans body",
                    "Body 16px at 1.65, 0 long lines",
                    "Mobile h1 two lines"
                ],
                "issues": [
                    {
                        "severity": "major",
                        "where": ".apps 4-col",
                        "problem": "Detergent still 4 ragged lines with Kerala widow.",
                        "fix": "Two lines: 700-800 MT cake and powder. Then GJ, MH, CG, MP, TN, KL."
                    }
                ]
            }
        }
    },
    "systems_designer": {
        "expert": "systems_designer",
        "scores": {
            "color": {
                "score": 8.5,
                "evidence": "Paper/mist/deep. 0/96 contrast fails.",
                "strengths": [
                    "Paper/mist/deep bands; 0 contrast fails",
                    "Blue reserved for links and rules",
                    "Flat navy CTAs"
                ],
                "issues": [
                    {
                        "severity": "minor",
                        "where": ".apps fills",
                        "problem": "Tiles still read as one pale slab.",
                        "fix": "Steepen color-mix 28/18/10/6 percent."
                    }
                ]
            },
            "spacing_rhythm": {
                "score": 8.3,
                "evidence": "98.9% 4px grid. 48/80px pack padding as designed breaks. Photo taller than copy.",
                "strengths": [
                    "98.9% 4px grid; 48/80px pack padding",
                    "Process stagger with non-overlapping bars",
                    "One 4px radius"
                ],
                "issues": [
                    {
                        "severity": "minor",
                        "where": ".apps at 1024",
                        "problem": "Detergent tile taller than the other three.",
                        "fix": "Shorten Detergent copy so heights match."
                    }
                ]
            }
        }
    },
    "ux_lead": {
        "expert": "ux_lead",
        "scores": {
            "ux_clarity": {
                "score": 7.5,
                "evidence": "Fold clear. Quote chrome only. Packing still five times including intro h2.",
                "strengths": [
                    "Fold names product, 90 +/- 1, Gundlav, quote",
                    "Quote is header, footer, mobile bar only",
                    "Acid-not-salt plus 700-800 MT"
                ],
                "issues": [
                    {
                        "severity": "major",
                        "where": "intro h2 / spec Packing / flow 04 / FAQ",
                        "problem": "Barrel/MT still stated five times. Intro h2 is Barrel-filled next to a tank photo.",
                        "fix": "Rename intro h2 to the 75 MT/day claim. Keep packing only in the spec table. Delete FAQ."
                    }
                ]
            }
        }
    },
    "motion_designer": {
        "expert": "motion_designer",
        "scores": {
            "interaction_motion": {
                "score": 7.8,
                "evidence": "Ghost quote fills on hover; 3px focus. Tokens 150/200/650ms. Dual reduced-motion.",
                "strengths": [
                    "Ghost square quote vs filled hover vs 3px focus",
                    "150/200/650ms ease-out",
                    "Reduced-motion dual gate"
                ],
                "issues": [
                    {
                        "severity": "minor",
                        "where": ".faq details",
                        "problem": "FAQ snaps open.",
                        "fix": "Rotate plus 45deg on open."
                    }
                ]
            }
        }
    },
    "a11y_qa": {
        "expert": "a11y_qa",
        "scores": {
            "a11y_responsive": {
                "score": 8.7,
                "evidence": "0 blockers, 0 contrast fails, 0 taps under 44px after footer min-width.",
                "strengths": [
                    "0 contrast fails, 23/23 visible focus, 0 taps under 44px",
                    "Skip, one h1, native FAQ",
                    "375 and tablet reflow"
                ],
                "issues": [
                    {
                        "severity": "minor",
                        "where": "div.bar",
                        "problem": "Call bar is outside a landmark.",
                        "fix": "Wrap in nav aria-label Get a quote."
                    }
                ]
            }
        }
    },
    "skeptic": {
        "expert": "skeptic",
        "scores": {
            "distinctiveness": {
                "score": 7.4,
                "evidence": "Catalog H2s gone. Plant numbers hold. Specification leftover; packing restated; three app tiles restate spec. Four tiles are a user demand, not to be deleted.",
                "strengths": [
                    "Headings Barrel-filled at Plot 79/80, Cake plants in six states, Four vessels at Plot 79/80",
                    "75 MT/day, RKSPL tanker, 700-800 MT to six states",
                    "Acid-not-salt on a plant sample tube"
                ],
                "issues": [
                    {
                        "severity": "major",
                        "where": "h2#sp Specification",
                        "problem": "Leftover catalog datasheet label.",
                        "fix": "Retitle to 90 +/- 1 as dispatched."
                    },
                    {
                        "severity": "major",
                        "where": "intro h2 vs packing repeats",
                        "problem": "Barrel-filled written four times.",
                        "fix": "Keep packing only in the spec row. Rename intro h2 to 75 MT a day at Gundlav."
                    },
                    {
                        "severity": "major",
                        "where": ".apps Textile Agriculture Leather",
                        "problem": "Three tiles only restate CoA numbers. Four tiles are a user demand so keep them but give each a plant constraint not already in the table.",
                        "fix": "Keep four tiles. Textile: dye baths when a mill switches a tanker from cake work. Agriculture: no 50 kg bags, quote drum size. Leather: hide dye at the same free-acid lot as cake."
                    }
                ]
            }
        }
    }
}

for name, obj in reviews.items():
    path = out / f"{name}.json"
    path.write_text(json.dumps(obj, ensure_ascii=True, indent=2), encoding="utf-8")
    print("wrote", path.name)
