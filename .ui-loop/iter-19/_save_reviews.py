import json
from pathlib import Path

out = Path(__file__).parent / "reviews"
out.mkdir(parents=True, exist_ok=True)

reviews = {
    "art_director": {
        "expert": "art_director",
        "scores": {
            "hierarchy_composition": {
                "score": 8.4,
                "evidence": "Squint on desktop_fold.png: one dominant mass, navy pagehead and white h1. Quote only in header and footer. Pack padding 80px from 1024. Process 2-col stagger, bars do not overlap.",
                "strengths": [
                    "Navy pagehead h1 is the single squint focal point",
                    "Section order is a buyer argument",
                    "Paper/mist bands plus 80px pack padding read as designed breaks"
                ],
                "issues": [
                    {
                        "severity": "minor",
                        "where": ".apps article",
                        "problem": "Detergent tile is 5 lines; the other three are 2, so stretch leaves empty tint.",
                        "fix": "Shorten Detergent to two lines so all four tiles fill evenly."
                    }
                ]
            },
            "reference_fidelity": {
                "score": 8.5,
                "evidence": "Intro photo-left plus chevron list; four RK-tint tiles; numbered process with stagger. Quote in chrome only.",
                "strengths": [
                    "Intro split matches photo-left plus chevron list",
                    "Four app tiles and 01-04 process keep the reference signature",
                    "RK navy pagehead and footer silhouette stay"
                ],
                "issues": [
                    {
                        "severity": "minor",
                        "where": ".apps article fills",
                        "problem": "Four tints collapse to one pale bar at squint.",
                        "fix": "Step fills 16%, 10%, 6%, 12% of --blue on --mist."
                    }
                ]
            }
        }
    },
    "typographer": {
        "expert": "typographer",
        "scores": {
            "typography": {
                "score": 7.8,
                "evidence": "Archivo vs IBM Plex, body 16px, 0 long lines. Four-up apps wrap Detergent to 5-6 ragged lines. 9 computed sizes.",
                "strengths": [
                    "Archivo headings vs IBM Plex Sans body",
                    "Body 16px/1.65, 0 long lines",
                    "h1 tracking tight; mobile h1 two lines"
                ],
                "issues": [
                    {
                        "severity": "major",
                        "where": ".apps at 1024px",
                        "problem": "Four columns leave about 25ch; Detergent wraps to 5-6 lines.",
                        "fix": "Keep 4 columns. Shorten Detergent body to two lines with state abbreviations."
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
                "evidence": "Paper/mist/deep. 0/102 contrast fails. Ghost overlay gone.",
                "strengths": [
                    "Paper/mist/deep split; 0 contrast fails",
                    "Process and spec use navy tints",
                    "Blue reserved for links and table rule"
                ],
                "issues": [
                    {
                        "severity": "minor",
                        "where": ".apps article fills",
                        "problem": "Four tints read as one pale slab.",
                        "fix": "Step color-mix of --blue on --mist 18/12/8/4%."
                    }
                ]
            },
            "spacing_rhythm": {
                "score": 8.5,
                "evidence": "99% 4px grid. Pack s7/s8 as designed breaks. Process stagger. Intro photo taller than traits.",
                "strengths": [
                    "99% 4px grid; 48/80px pack padding as band breaks",
                    "Process stagger with non-overlapping bars",
                    "Chem pair heights match; ghost gone"
                ],
                "issues": [
                    {
                        "severity": "minor",
                        "where": "intro .cols--top",
                        "problem": "Photo taller than copy, paper rag under traits.",
                        "fix": "Push .traits to margin-top:auto in a flex copy column."
                    }
                ]
            }
        }
    },
    "ux_lead": {
        "expert": "ux_lead",
        "scores": {
            "ux_clarity": {
                "score": 8.0,
                "evidence": "Fold names product, 90 +/- 1, Gundlav, quote. Quote only in header, footer, mobile bar. Remaining MT/barrel repeats across traits, spec, apps, FAQ.",
                "strengths": [
                    "Fold names product, 90 +/- 1, Gundlav, Request a quote",
                    "Quote CTA is header, footer, and mobile bar only",
                    "Detergent tile names 700-800 MT and six states"
                ],
                "issues": [
                    {
                        "severity": "major",
                        "where": "traits / spec / apps / FAQ packing",
                        "problem": "Metric tonnes / barrel / no consumer stated five times.",
                        "fix": "Keep packing only in the spec table. Drop Industrial MT trait. Merge FAQ 1 and 3. Cut FAQ documents duplicate."
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
                "evidence": "Ghost nav quote fills on hover; 3px focus. Tokens 150/200/650ms. Dual reduced-motion gate.",
                "strengths": [
                    "Square ghost CTA vs filled hover vs 3px focus",
                    "Duration tokens 150/200/650ms ease-out",
                    "Dual reduced-motion gate"
                ],
                "issues": [
                    {
                        "severity": "minor",
                        "where": ".faq details",
                        "problem": "FAQ snaps open; plus/minus is a content swap.",
                        "fix": "Rotate + 45deg on open over 200ms."
                    }
                ]
            }
        }
    },
    "a11y_qa": {
        "expert": "a11y_qa",
        "scores": {
            "a11y_responsive": {
                "score": 8.5,
                "evidence": "0 blockers, 0/102 contrast, 0 invisible focus, 1 h1, 375 reflow. 1 tap under 44px.",
                "strengths": [
                    "Skip, labelled nav, one h1, native FAQ details",
                    "0 contrast fails, 21/21 focus visible",
                    "375 and tablet reflow"
                ],
                "issues": [
                    {
                        "severity": "minor",
                        "where": "footer .foot nav a",
                        "problem": "About is under 44px wide.",
                        "fix": "min-width 44px and padding 0 12px on footer links."
                    }
                ]
            }
        }
    },
    "skeptic": {
        "expert": "skeptic",
        "scores": {
            "distinctiveness": {
                "score": 7.2,
                "evidence": "Cover-the-logo passes on Plot 79/80, tanker, 75 MT, six states. Fails on catalog H2s As dispatched, Where it is specified, How it is made. Intro still a chemistry definition.",
                "strengths": [
                    "Plant-locked proof: Plot 79/80, RKSPL tanker, 75 MT, 700-800 MT to named states",
                    "Acid-not-salt sits on a plant sample tube",
                    "FAQ asks desk questions, not encyclopedia"
                ],
                "issues": [
                    {
                        "severity": "major",
                        "where": "#intro h2 and intro p",
                        "problem": "As dispatched is empty; lede is a chemistry definition.",
                        "fix": "Retitle to Barrel-filled at Plot 79/80. One dispatch fact the table does not carry."
                    },
                    {
                        "severity": "major",
                        "where": "h2#use and h2#how",
                        "problem": "Catalog Mad Libs. Gundlav stripped from process title.",
                        "fix": "Rename use to Cake plants in six states. Rename how to Four vessels at Plot 79/80."
                    },
                    {
                        "severity": "major",
                        "where": "intro vs spec vs #st",
                        "problem": "Light brown / neutralize restated.",
                        "fix": "Cut intro to one Plot 79/80 sentence. Neutralize only under acid-not-salt."
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
