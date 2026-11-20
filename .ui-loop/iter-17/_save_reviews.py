import json
from pathlib import Path

out = Path(__file__).parent / "reviews"
out.mkdir(parents=True, exist_ok=True)

reviews = {
    "art_director": {
        "expert": "art_director",
        "scores": {
            "hierarchy_composition": {
                "score": 7.6,
                "evidence": "Squint on desktop_fold.png: one focal point, the navy pagehead and white h1 LABSA 90% from Gundlav; eye goes next to the tank photo, then to LABSA 90% as we dispatch it. Hierarchy uses size, navy/white contrast, and a tracked kicker. Spec pairs a filled Request a quote with a quieter PDF text link. Pack padding-block is 24px and adjacent .alt bands collapse. Remaining hole: #how is the only centered stack, and .flow is align-items:start so 03 sits as a short island beside 04. Previous overlapping blue lines, cramped FAQ/apps type, .apps-lead indent, hanging Appearance widow, and LABSA 90%from missing space are fixed.",
                "strengths": [
                    "Navy pagehead h1 is the single squint focal point on desktop_fold.png",
                    "Section order is a chemical-buyer argument, not a SaaS template",
                    "Spec pairs a filled Request a quote with a quieter PDF text link"
                ],
                "issues": [
                    {
                        "severity": "major",
                        "where": ".band--center #how",
                        "problem": "How it is made at Gundlav is the only centered heading-plus-lead on a left-aligned page, so desktop_s03.png reads as a mist void between the app row and the process cards.",
                        "fix": "Remove .band--center from the how section. Left-align #how like #use and #faq, keep .band max-width at 42rem, keep pack section padding-block at 24px."
                    },
                    {
                        "severity": "major",
                        "where": ".flow at min-width 768px",
                        "problem": "align-items:start plus short copy in 02 and 03 leaves ragged holes beside taller neighbors.",
                        "fix": "Set .flow {align-items:stretch} so row partners share height. Do not restore large margin-top stagger (user asked to avoid empty space)."
                    },
                    {
                        "severity": "minor",
                        "where": "h1 then #intro",
                        "problem": "Two display lines both open with LABSA 90%.",
                        "fix": "Keep the pagehead h1. Change #intro to As we dispatch it so the second title does not repeat LABSA 90%."
                    }
                ]
            },
            "reference_fidelity": {
                "score": 7.7,
                "evidence": "No compare.png. Intro is photo left, kicker, heading, body, 2-col chevron list. Apps are four equal tiles in RK tints, not competitor purple/green. Process has 01-04 badges with odd/even 4px bars but a flat 2x2. Spec table, sample tube, structure, Gundlav pagehead, square matte buttons, no header phone kept.",
                "strengths": [
                    "Intro is photo-left plus a 2-col chevron list",
                    "Four equal app tiles use RK navy tints, not competitor purple or green",
                    "Process cards keep numbered badges and odd/even 4px side bars"
                ],
                "issues": [
                    {
                        "severity": "major",
                        "where": ".flow li:nth-child(even)",
                        "problem": "Reference asked for staggered numbered process cards. Current 2x2 has tops aligned. Large stagger was dropped to clear empty gaps (user demand: avoid empty space).",
                        "fix": "At min-width 768px use a modest transform:translateY(1.25rem) on even items plus matching padding-bottom, not a large margin-top gap."
                    },
                    {
                        "severity": "minor",
                        "where": ".band--center",
                        "problem": "The how block is a centered default.",
                        "fix": "Left-align the how band to match #use and the intro copy column."
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
                "evidence": "Pagehead h1 now reads LABSA 90% from Gundlav as one line; h2 We sell the acid, not the salt replaced Appearance as dispatched; FAQ summaries 1.125rem/1.35; Archivo 628 vs IBM Plex Sans 4813; body 16px; 0 long lines. Anchor 10.0 does not bind.",
                "strengths": [
                    "Archivo 112% stretch on headings versus IBM Plex Sans on body",
                    "Heading/body split is consistent: body 16px/1.65, heads 1.1",
                    "Prior bugs gone: h1 space, Appearance widow, cramped FAQ/apps titles"
                ],
                "issues": [
                    {
                        "severity": "minor",
                        "where": ".apps article:first-child h3",
                        "problem": "Detergent manufacturing wraps to a second line while the other three h3s stay one line.",
                        "fix": "Shorten the first title to Detergent plants so all four h3s stay one line at four-column width."
                    },
                    {
                        "severity": "minor",
                        "where": ".band--center p",
                        "problem": "Centered process dek ends on a short last line.",
                        "fix": "Left-align the how band (also an empty-space fix)."
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
                "evidence": "Paper/mist/deep bands. Audit 0/111 contrast fails. Four RK-blue app tints. Square navy CTAs. Wordmark uses --brand #2f256c.",
                "strengths": [
                    "Paper/mist/deep bands match DESIGN 60/30 split",
                    "Zero contrast failures on 111 checks",
                    "App tiles stay RK navy tints, not competitor purple"
                ],
                "issues": [
                    {
                        "severity": "minor",
                        "where": ".apps article:nth-child(4)",
                        "problem": "Leather tile fill is raw #e8eef6, outside the named set.",
                        "fix": "Replace #e8eef6 with color-mix(in srgb, var(--blue) 8%, var(--mist))."
                    }
                ]
            },
            "spacing_rhythm": {
                "score": 8.0,
                "evidence": "Audit 99.1% 4px grid. .pack section padding is s5 (24px). Prior overlapping bars, 11rem min-height, and stagger margin-top are gone. .flow is 2x2 with align-items:start; card 03 shorter than 04.",
                "strengths": [
                    "99.1% spacing grid adherence on a 4px scale",
                    "s5 pack padding without 11rem empty card holes",
                    "Process left/right 4px bars do not overlap"
                ],
                "issues": [
                    {
                        "severity": "major",
                        "where": ".flow at min-width 768px",
                        "problem": "align-items:start leaves 03 shorter than 04; row bottoms and the 4px end bars do not line up.",
                        "fix": "Set .flow { align-items: stretch; } and do not add min-height."
                    },
                    {
                        "severity": "minor",
                        "where": ".apps article, .flow li",
                        "problem": "Content tiles use 4px radius. DESIGN limits 4px to photographs.",
                        "fix": "Set border-radius: 0 on .apps article and .flow li."
                    },
                    {
                        "severity": "minor",
                        "where": ".chem .fig img",
                        "problem": "Schematic is max-width 22rem, leaving a paper hole beside it.",
                        "fix": "Set .chem .fig img { max-width: none; width: 100%; }."
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
                "evidence": "Five-second test passes: h1 LABSA 90% from Gundlav, 90 +/- 1%, detergent buyers, Request a quote. FAQ answers real objections. Encyclopedia h2 gone. Traits still clone the spec table.",
                "strengths": [
                    "Fold names product, plant, 90 +/- 1, detergent buyers, and quote",
                    "FAQ answers real objections and offers Request documents with no order",
                    "Quote CTA sits on the applications band; process cites 300 MT / 200 MT"
                ],
                "issues": [
                    {
                        "severity": "major",
                        "where": "ul.traits",
                        "problem": "The six arrows restate Active matter, Klett, and metric tonnes from the spec table, while Used in detergents / Industrial applications / Wets and emulsifies are generic.",
                        "fix": "Keep ul.traits. Replace items with dispatch facts the table does not list: Barrel-filled at Plot 79/80; Buyers neutralize on their line; Same CoA for textile agro leather; No consumer pack; Own RKSPL VALSAD tanker; 75 MT per day."
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
                "evidence": "hover.png fills navbar Request a quote solid navy; focus.png adds 3px outline. Tokens 150/200/650ms ease-out. Dual gate reduced-motion plus html.motion. Square matte wipe is a user demand.",
                "strengths": [
                    "Square ghost CTA rest vs filled hover and 3px focus",
                    "Duration tokens 150/200/650ms ease-out; no bounce",
                    "Dual gate: reduced-motion media plus html.motion"
                ],
                "issues": [
                    {
                        "severity": "minor",
                        "where": ".faq details / summary::after",
                        "problem": "Native details snap height; plus/minus is a content swap with no rotation.",
                        "fix": "Animate summary::after with transform:rotate(45deg) instead of swapping + and en-dash."
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
                "evidence": "Audit: 0 blockers, 0/111 contrast fails, 0/19 invisible focus, 1 h1, no 375 overflow, 1 tap under 44. Header phone omitted per demand.",
                "strengths": [
                    "Skip, labelled nav, one h1, native FAQ details at 48px",
                    "0 contrast fails and visible 3px focus on 19 controls",
                    "375 and tablet reflow; 56px Call/Quote bar"
                ],
                "issues": [
                    {
                        "severity": "minor",
                        "where": "ul.traits and ol.flow",
                        "problem": "list-style:none can drop list semantics in WebKit.",
                        "fix": "Add role=list on ul.traits and ol.flow (keep aria-hidden on .flow-n)."
                    }
                ]
            }
        }
    },
    "skeptic": {
        "expert": "skeptic",
        "scores": {
            "distinctiveness": {
                "score": 7.0,
                "evidence": "Cover-the-logo passes on Gundlav, CoA numbers, 700-800 MT, 75 MT/day, acid-not-salt. Fails on three trait slogans, glossary FAQ, and interchangeable industry cards.",
                "strengths": [
                    "Acid-not-salt heading with the plant sample tube",
                    "Detergent card names 700-800 MT and six states",
                    "Process lede has 75 MT/day, 2275 MT/month, RKSPL VALSAD tanker"
                ],
                "issues": [
                    {
                        "severity": "major",
                        "where": "ul.traits right column",
                        "problem": "Used in detergents, Industrial applications, and Wets and emulsifies are interchangeable slogans.",
                        "fix": "Keep all six chevrons. Replace those three with: 98% H2SO4 feed, barrel-filled at Plot 79/80, waste acid sold to fertilizer plants."
                    },
                    {
                        "severity": "major",
                        "where": ".faq first details",
                        "problem": "What does LABSA stand for? is encyclopedia copy.",
                        "fix": "Drop the acronym question. Ask a desk question: minimum MT, CoA with the lot, or drum vs tanker."
                    },
                    {
                        "severity": "major",
                        "where": ".apps article:nth-child(2), (3), (4)",
                        "problem": "Textile, Agriculture, and Leather only repeat not a separate grade.",
                        "fix": "Keep four tiles. Give each mill type one plant constraint: textile same 20-25 Klett lots; agro MT-only no 50 kg pack; leather free-acid 5.5-6.5."
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
