import json
from pathlib import Path

out = Path(__file__).parent / "reviews"
out.mkdir(parents=True, exist_ok=True)

reviews = {
    "art_director": {
        "expert": "art_director",
        "scores": {
            "hierarchy_composition": {
                "score": 8.0,
                "evidence": "Squint: navy pagehead h1. Quote chrome-only. Plant facts restored. Detergent tile taller than the other three.",
                "strengths": [
                    "Navy pagehead h1 is the single squint focal point",
                    "Buyer section order",
                    "Photo-left intro and staggered process"
                ],
                "issues": [
                    {
                        "severity": "major",
                        "where": ".apps article:first-child",
                        "problem": "Detergent manufacturing wraps to two title lines and a long body vs shorter tiles.",
                        "fix": "Rename h3 to Detergent plants. Keep the 700-800 MT and six-state facts."
                    }
                ]
            },
            "reference_fidelity": {
                "score": 8.2,
                "evidence": "Intro photo-left plus chevrons; four tiles; staggered 01-04; spec, tube, structure, banners, square buttons. Quote chrome-only.",
                "strengths": [
                    "Intro split matches photo-left plus chevron list",
                    "Four tiles and 01-04 stagger",
                    "RK pagehead, tube, structure, spec kept"
                ],
                "issues": [
                    {
                        "severity": "minor",
                        "where": ".apps fills",
                        "problem": "Four tints still read as one pale bar.",
                        "fix": "Steepen mixes to 32/20/10/4 percent blue on mist."
                    }
                ]
            }
        }
    },
    "typographer": {
        "expert": "typographer",
        "scores": {
            "typography": {
                "score": 7.5,
                "evidence": "Archivo vs Plex, 16px body, kickers gone. Detergent h3 two lines; body ragged in 4-col.",
                "strengths": [
                    "Archivo heads vs IBM Plex Sans body",
                    "Body 16px/1.65, 0 long lines",
                    "Kickers removed"
                ],
                "issues": [
                    {
                        "severity": "major",
                        "where": ".apps 4-col",
                        "problem": "Detergent manufacturing wraps; Leather splits 5.5-6.5.",
                        "fix": "Rename h3 to Detergent plants. Wrap 5.5-6.5 in nowrap. Keep the facts."
                    }
                ]
            }
        }
    },
    "systems_designer": {
        "expert": "systems_designer",
        "scores": {
            "color": {
                "score": 8.3,
                "evidence": "Paper/mist/deep. 0/104 contrast fails.",
                "strengths": [
                    "Paper/mist/deep split with 0 contrast fails",
                    "Blue as a rare signature",
                    "Square CTAs stay navy"
                ],
                "issues": [
                    {
                        "severity": "minor",
                        "where": ".apps fills",
                        "problem": "Tiles still one pale slab.",
                        "fix": "Steepen color-mix 32/20/10/4."
                    }
                ]
            },
            "spacing_rhythm": {
                "score": 8.2,
                "evidence": "99% 4px grid. 48/80px pack padding as demanded.",
                "strengths": [
                    "48/80px pack section padding",
                    "Process stagger with non-overlapping bars",
                    "One 4px photo radius"
                ],
                "issues": [
                    {
                        "severity": "minor",
                        "where": ".apps at 1024",
                        "problem": "Detergent tile taller than the others.",
                        "fix": "Keep facts; shorten the h3 so the row height matches better."
                    }
                ]
            }
        }
    },
    "ux_lead": {
        "expert": "ux_lead",
        "scores": {
            "ux_clarity": {
                "score": 8.2,
                "evidence": "Fold names grade, 90 +/- 1, plant, quote. Spec, 75 MT, 700-800 MT, process, FAQ restored. Quote chrome-only. Kickers gone.",
                "strengths": [
                    "Fold names the grade, spec, plant, and next action",
                    "Spec, 75 MT/day, 700-800 MT, process, and FAQ are back",
                    "Request a quote is header, footer, and mobile bar only"
                ],
                "issues": [
                    {
                        "severity": "minor",
                        "where": "FAQ 1 and 3",
                        "problem": "Both repeat barrel vs tanker.",
                        "fix": "Keep dispatch path in FAQ 1. FAQ 3 storage only."
                    }
                ]
            }
        }
    },
    "motion_designer": {
        "expert": "motion_designer",
        "scores": {
            "interaction_motion": {
                "score": 8.2,
                "evidence": "Ghost quote fills on hover; 3px focus. Tokens 150/200/650ms. Dual reduced-motion.",
                "strengths": [
                    "Ghost square quote vs filled hover vs 3px focus",
                    "150/200/650ms ease-out",
                    "Dual reduced-motion gate"
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
                "score": 8.6,
                "evidence": "0 blockers, 0 contrast fails, 0 taps under 44, 375 reflow.",
                "strengths": [
                    "0 contrast fails, 21/21 focus, 0 taps under 44px",
                    "Skip, one h1, native FAQ",
                    "Reflow not shrink"
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
                "score": 6.8,
                "evidence": "Plant facts pass cover-the-logo. Catalog H2s Specification/Applications/How it is made are a user demand (restore necessary section titles, not cute subheads). Four tiles and chrome quote not penalised.",
                "strengths": [
                    "Plot 79/80, 75 MT a day, RKSPL tanker, ISO 9001:2015",
                    "Acid-not-salt on a plant sample tube",
                    "Detergent tile names 700-800 MT and six states"
                ],
                "issues": [
                    {
                        "severity": "major",
                        "where": "spec Packing / flow 04 / FAQ",
                        "problem": "Barrel-filled restated in process and FAQ.",
                        "fix": "Keep packing in the spec row. Process 04 lab checks and 200 MT tanks. FAQ 1 unit and tanker."
                    },
                    {
                        "severity": "major",
                        "where": ".apps Textile Agriculture Leather",
                        "problem": "Openings are generic use-cases.",
                        "fix": "Keep four tiles. Keep plant constraints (same CoA, no 50 kg, free-acid lot)."
                    },
                    {
                        "severity": "minor",
                        "where": "#intro p",
                        "problem": "Intro restates appearance already in the spec table.",
                        "fix": "Keep the Plot 79/80 sulphonation sentence; table keeps appearance."
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
