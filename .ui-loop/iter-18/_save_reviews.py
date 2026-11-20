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
                "evidence": "Squint on desktop_fold.png: one focal point, navy pagehead and white h1 LABSA 90% from Gundlav. How is left-aligned; flow stretch equal height; overlapping bars, cramped FAQ, missing h1 space fixed. Remaining stall is .chem pale field under the full-width SVG plus ghost ::after.",
                "strengths": [
                    "Navy pagehead h1 is the single squint focal point",
                    "Section order is a chemical-buyer argument",
                    "How and FAQ are left-aligned; process cards stretch"
                ],
                "issues": [
                    {
                        "severity": "major",
                        "where": ".chem .fig and .chem::after",
                        "problem": "Full-width SVG plus a 7% ghost leave a pale field under the strokes.",
                        "fix": "Cap .chem .fig img at max-width 28rem. Set .chem::after {content:none}."
                    }
                ]
            },
            "reference_fidelity": {
                "score": 8.2,
                "evidence": "Intro is photo left plus 2-col chevron list. Four RK-tint app tiles. Process 01-04 with odd/even 4px bars, no overlap. Flat 2x2 waived so empty space stays tight.",
                "strengths": [
                    "Intro is photo-left plus a 2-col chevron list",
                    "Four equal app tiles use RK navy tints",
                    "Process cards keep numbered badges and side bars"
                ],
                "issues": [
                    {
                        "severity": "minor",
                        "where": ".chem::after",
                        "problem": "A 7% duplicate of structure.svg is decorative wallpaper the reference does not use.",
                        "fix": "Remove .chem::after. Keep the real .fig diagram only."
                    }
                ]
            }
        }
    },
    "typographer": {
        "expert": "typographer",
        "scores": {
            "typography": {
                "score": 8.3,
                "evidence": "h1 is one line with a space. Appearance value one line. FAQ readable. Detergent plants one line. Body 16px. Anchor 8.5.",
                "strengths": [
                    "Archivo headings versus IBM Plex Sans body",
                    "Body 16px/1.65, 0 long lines",
                    "Prior h1 space, Appearance widow, cramped FAQ, title wrap gone"
                ],
                "issues": [
                    {
                        "severity": "minor",
                        "where": "#intro p",
                        "problem": "90 +/- wraps onto 1%.",
                        "fix": "Wrap 90 +/- 1% in span.nowrap."
                    }
                ]
            }
        }
    },
    "systems_designer": {
        "expert": "systems_designer",
        "scores": {
            "color": {
                "score": 8.0,
                "evidence": "Paper/mist/deep. 0/110 contrast fails. Four RK tints. Ghost structure overlaps the schematic.",
                "strengths": [
                    "Paper/mist/deep split; 0 contrast fails",
                    "App tiles stay RK navy tints",
                    "Square navy CTAs; no purple gradient"
                ],
                "issues": [
                    {
                        "severity": "major",
                        "where": ".chem::after vs .chem .fig img",
                        "problem": "Ghost structure sits on the solid schematic as overlapping blue lines.",
                        "fix": "Set .pack .chem::after{content:none}."
                    }
                ]
            },
            "spacing_rhythm": {
                "score": 8.0,
                "evidence": "99.1% 4px grid. Pack padding 24px. Prior min-height, indent, flow holes, centered how void gone. Remaining hole under the 16rem beaker vs taller right column.",
                "strengths": [
                    "99.1% spacing grid; pack 24px without 11rem holes",
                    "Process 2x2 stretch; bars do not overlap",
                    "How intro is left-aligned"
                ],
                "issues": [
                    {
                        "severity": "major",
                        "where": "section.chem .cols--top / .ph--product",
                        "problem": "Beaker is shorter than heading plus full-width schematic, leaving a mist hole under the photo.",
                        "fix": "Cap the schematic at 28rem and stretch the photo column, or drop the ghost."
                    }
                ]
            }
        }
    },
    "ux_lead": {
        "expert": "ux_lead",
        "scores": {
            "ux_clarity": {
                "score": 8.5,
                "evidence": "Fold names LABSA 90% from Gundlav, 90 +/- 1, quote. Traits are dispatch facts. Encyclopedia h2 gone.",
                "strengths": [
                    "Fold names product, plant, 90 +/- 1, and the quote",
                    "Traits are dispatch facts the spec table does not list",
                    "FAQ plus Request documents with no order required"
                ],
                "issues": [
                    {
                        "severity": "minor",
                        "where": ".faq details 2 and 6",
                        "problem": "Two FAQs both answer no consumer sizes.",
                        "fix": "Merge into one summary about consumer or personal sizes."
                    }
                ]
            }
        }
    },
    "motion_designer": {
        "expert": "motion_designer",
        "scores": {
            "interaction_motion": {
                "score": 8.0,
                "evidence": "Square ghost nav CTA fills on hover; 3px focus. Tokens 150/200/650ms. Dual reduced-motion gate.",
                "strengths": [
                    "Square ghost CTA rest, filled hover, 3px focus",
                    "Duration tokens 150/200/650ms ease-out",
                    "Dual gate: no-preference plus html.motion"
                ],
                "issues": [
                    {
                        "severity": "minor",
                        "where": ".faq details / summary::after",
                        "problem": "Opening snaps height; plus/minus is a content swap.",
                        "fix": "Rotate summary::after 45deg on open over 200ms."
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
                "evidence": "0 blockers, 0/110 contrast, 0 invisible focus, 1 h1, role=list on traits and flow, 375 reflow. Header phone omitted per demand.",
                "strengths": [
                    "Skip, labelled nav, one h1, native FAQ details",
                    "0 contrast fails and 3px focus on 19 controls",
                    "375 and tablet reflow; role=list on traits and flow"
                ],
                "issues": [
                    {
                        "severity": "minor",
                        "where": "footer nav a About",
                        "problem": "One tap target under 44px wide.",
                        "fix": "Set .foot nav a min-width 44px."
                    }
                ]
            }
        }
    },
    "skeptic": {
        "expert": "skeptic",
        "scores": {
            "distinctiveness": {
                "score": 7.5,
                "evidence": "Trait slogans rewritten with Plot 79/80 facts. Industry cards carry Klett and free-acid numbers. Fails on empty dispatch heading, Wikipedia lede, leftover glossary FAQ.",
                "strengths": [
                    "Trait list names barrel fill, 98% sulphuric feed, RKSPL tanker, 75 MT a day",
                    "Detergent tile names 700-800 MT and six states",
                    "Acid-not-salt sits on a real plant sample tube"
                ],
                "issues": [
                    {
                        "severity": "major",
                        "where": ".faq details biodegradable feedstock",
                        "problem": "Still encyclopedia copy.",
                        "fix": "Replace with Do you send a CoA and SDS before the first order?"
                    },
                    {
                        "severity": "major",
                        "where": "#intro h2",
                        "problem": "As we dispatch it is an empty heading; lede still opens with a definition.",
                        "fix": "Retitle to Barrel-filled at Plot 79/80 and start at At Plot 79/80 we sulphonate..."
                    },
                    {
                        "severity": "major",
                        "where": ".faq cosmetics and personal use",
                        "problem": "Two FAQ rows answer the same no consumer pack.",
                        "fix": "Keep one personal-size question; replace the other with What is on the CoA."
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
