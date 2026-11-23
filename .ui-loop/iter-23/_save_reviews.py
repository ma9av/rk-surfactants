import json
from pathlib import Path

out = Path(__file__).parent / "reviews"
out.mkdir(exist_ok=True)
reviews = {
    "art_director": {
        "expert": "art_director",
        "scores": {
            "hierarchy_composition": {
                "score": 7.6,
                "evidence": "desktop_fold.png: one chromatic mass T-01/T-02/T-03. Pagehead is a quiet navy label. Two majors: equal app tiles; #about and #intro share heading+lede+traits+photo skeleton.",
                "strengths": ["Fold has a single chromatic focal: the labelled tanks."],
                "issues": [
                    {
                        "severity": "major",
                        "where": "#about + #intro",
                        "problem": "Two consecutive splits share the same skeleton.",
                        "fix": "Leave #about as demanded. Rebuild #intro without ul.traits.",
                    }
                ],
            },
            "reference_fidelity": {
                "score": 8.2,
                "evidence": "Intro split copy left, tanks right, chevron list. Tinted tiles and staggered process intact. RK navy/mist/paper.",
                "strengths": ["Intro split with T-01 tanks is the reference layout move."],
                "issues": [
                    {
                        "severity": "minor",
                        "where": ".apps",
                        "problem": "Three tiles sit half-empty.",
                        "fix": "Span detergent full width.",
                    }
                ],
            },
        },
    },
    "typographer": {
        "expert": "typographer",
        "scores": {
            "typography": {
                "score": 7.8,
                "evidence": "Archivo vs IBM Plex. Body 16px/1.65. Fold h2 wraps so 90% sits alone.",
                "strengths": ["Two-family industrial system, 0 long lines."],
                "issues": [
                    {
                        "severity": "minor",
                        "where": "h2#about",
                        "problem": "Line two is only 90%.",
                        "fix": "br after Introduction to so line two is LABSA 90%.",
                    }
                ],
            }
        },
    },
    "systems_designer": {
        "expert": "systems_designer",
        "scores": {
            "color": {
                "score": 8.0,
                "evidence": "Intro on mist. Audit 0 contrast fails of 117. Paper/mist/deep bands.",
                "strengths": ["Intro sits on mist beside the tank photo."],
                "issues": [
                    {
                        "severity": "minor",
                        "where": ".apps Agriculture",
                        "problem": "8% mix barely reads as a card.",
                        "fix": "Do not go below 12% blue into mist.",
                    }
                ],
            },
            "spacing_rhythm": {
                "score": 7.5,
                "evidence": "99.1% grid. Intro copy shorter than 4:3 photo, mist void under traits.",
                "strengths": ["80px section padding on the 4px scale."],
                "issues": [
                    {
                        "severity": "major",
                        "where": "section#about .cols--media",
                        "problem": "Photo taller than the text stack.",
                        "fix": "This figure 16/10 max-height 18rem.",
                    }
                ],
            },
        },
    },
    "ux_lead": {
        "expert": "ux_lead",
        "scores": {
            "ux_clarity": {
                "score": 7.4,
                "evidence": "Fold names LABSA 90% and Request a quote. Intro copy kept. Buyer line sits below the fold.",
                "strengths": ["Quote chrome-only. Intro wording not cut."],
                "issues": [
                    {
                        "severity": "major",
                        "where": ".pagehead p",
                        "problem": "Plot 79/80 with no city; buyer sentence below the fold.",
                        "fix": "Keep intro verbatim. Lead: Gundlav, Valsad, Gujarat.",
                    }
                ],
            }
        },
    },
    "motion_designer": {
        "expert": "motion_designer",
        "scores": {
            "interaction_motion": {
                "score": 8.2,
                "evidence": "Translucent RTL wash on tank-labsa. Overlay 700ms. Reduced-motion gated. Two consecutive .ph share the same wipe.",
                "strengths": ["Translucent RTL default on the new tanks photo."],
                "issues": [
                    {
                        "severity": "minor",
                        "where": "#about .ph + #intro .ph",
                        "problem": "Two landscape stills use the same RTL wipe.",
                        "fix": "Give dispatch storage a floor wipe.",
                    }
                ],
            }
        },
    },
    "a11y_qa": {
        "expert": "a11y_qa",
        "scores": {
            "a11y_responsive": {
                "score": 8.4,
                "evidence": "Audit 0 blockers, 0 contrast, 0 overflow, 21/21 focus. Intro reflows copy then photo below 1024.",
                "strengths": ["Intro split reflows. Photo has specific alt."],
                "issues": [
                    {
                        "severity": "minor",
                        "where": "ol.flow .flow-n",
                        "problem": "Step badges aria-hidden.",
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
                "score": 6.4,
                "evidence": "Fold is SKU plus demanded blog intro. Two matching chevron lists. Mid-page plant facts are real. Intro copy not listed as delete.",
                "strengths": ["Acid-not-salt. 75 MT/day. 700-800 MT."],
                "issues": [
                    {
                        "severity": "major",
                        "where": "#about ul.traits and #intro ul.traits",
                        "problem": "Same chevron grid for marketing traits and plant facts.",
                        "fix": "Keep six intro strings. Restyle #about .traits without chevrons.",
                    },
                    {
                        "severity": "major",
                        "where": ".apps Textile Agriculture Leather",
                        "problem": "Encyclopedia openings.",
                        "fix": "Lead with plant constraints.",
                    },
                    {
                        "severity": "major",
                        "where": "pagehead h1",
                        "problem": "Category SKU, no Gundlav, Valsad, Gujarat.",
                        "fix": "Keep LABSA 90%. Name the place in the lead.",
                    },
                ],
            }
        },
    },
}
for name, data in reviews.items():
    p = out / f"{name}.json"
    p.write_text(json.dumps(data, ensure_ascii=True, indent=2), encoding="utf-8")
    print("wrote", p.name)
