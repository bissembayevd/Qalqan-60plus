# Qalqan-60+ — a calm, zero-surveillance shield against phone fraud for people aged 60+

[![CI](../../actions/workflows/ci.yml/badge.svg)](../../actions/workflows/ci.yml)
Code: MIT · Content: CC BY-SA 4.0 · Data: ODC-By 1.0 · SDG 10.2 · SDG 16.4 / 16.a

*Qalqan* (қалқан) means “shield” in Kazakh. Qalqan-60+ is an open-source **Digital Public Good** concept that
interrupts phone, messenger and SMS-code scams at the moment of persuasion, and lets a trusted relative help —
**without** seeing the older person’s messages, balances, call logs or location.

> Student project of the course *Open Source* (DPG track), Kazakh-British Technical University,
> Almaty, 2026. This repository contains a working clickable prototype, an open dataset, governance documents,
> the group report and the pitch deck. It is a concept, not a production app.

## Contents

- [Problem and solution](#problem-and-solution)
- [Live prototype and design rationale](#live-prototype-and-design-rationale)
- [DPG Standard compliance (9 indicators)](#dpg-standard-compliance-9-indicators)
- [SDG mapping](#sdg-mapping)
- [Quick start](#quick-start)
- [Architecture](#architecture)
- [Repository structure](#repository-structure)
- [Contributing](#contributing)
- [Licences](#licences)
- [Team and AI disclosure](#team-and-ai-disclosure)

## Problem and solution

**Problem.** Scam scripts win by speed, not by technology: “this is the bank security service”, “act now”,
“tell no one”, “dictate the SMS code”, “move your money to a safe account”. In 2025 participants of the national
Anti-Fraud Forum counted 26.3 thousand internet-fraud cases, and the Prosecutor General’s Office reported about
12.2 bn KZT of damage from internet fraud. Kazakhstan has about 2.8 million people aged 60+ (almost 14 %). With age,
processing speed and working memory slow down, so deliberate thinking loses the race against a scripted caller.
Existing protections (call blocking, the Anti-Fraud Center, the Stop-credit self-ban) act on networks and
transactions — not on the minute when a person is persuaded to act with their own hands. “Parental control” apps
answer with surveillance. Sources and exact scopes of every figure are given in the report (`docs/`).

**Solution — the twist: ethical friction and delegated access without surveillance.**

1. **Zero-button trigger.** A pause starts by itself only when two signals coincide on the phone:
   ① a call from a number that is not in the contacts (numbers saved less than 24 hours ago count as unknown) and
   ② the banking app opens or an SMS code arrives. One signal alone does nothing. A manual “I am being rushed”
   button remains as a backup.
2. **Script-breaking pause.** A calm 15-minute overlay with a breathing cue mirrors the scammer’s exact phrases.
   It can be ended early only with a **family code word** (recall, not a reflex click) — and it warns that anyone
   who dictates the word is a scammer. Calls are never blocked; a wrong word never locks anyone out.
3. **Zero-app delegated access.** One ordinary SMS goes to a trusted relative, with a no-login link showing only a
   status snapshot and a “call Mum calmly” button. The status travels after `#` in the link, so the server never
   receives it.
4. **Accessibility, AI oversight and data control.** Kazakh, Russian and English; text sizes A / A+ / A++;
   WCAG 2.1 AA; an optional, offline AI phishing filter that is off by default and explains itself; one-button
   export of anonymised statistics and one-button deletion of all data.

## Live prototype and design rationale

Open [`src/index.html`](src/index.html) in any modern browser (double-click is enough; it works offline).
When GitHub Pages is enabled for this repository, the prototype is served at
`https://<team-account>.github.io/qalqan-60plus/src/`.

The page shows a 390 × 844 phone and a **live demo control panel** for presentations:

| Screen | What it demonstrates |
|---|---|
| 1 · Onboarding and consent | Plain-language guarantees; three separate consents, none pre-ticked; trusted person (gets a welcome SMS, can reply STOP); family code word stored only as a salted hash |
| 2 · Calm home shield | Status, the clear-box rule (① + ② together), language and text-size switches |
| 3 · Scam scenario | Unknown call + banking app → the pause starts with no button; a trusted contact calling → no pause |
| 4 · 15-minute pause | Timer and breathing cue, scammer-script mirror, call buttons, code-word exit, calm wrong-word message |
| 5 · Relative’s phone | Ordinary SMS and the no-login status page that lists what it can never show |
| 6 · Privacy, AI and open data | AI filter switch with “last decision explained”, consent withdrawal, JSON/CSV export, delete-all dialog |

Panel controls: pause length (15-second demo / real 15 minutes), jump to screens (keys **1–6**), four scenarios,
*Fill demo data* (code word **Barsik**), *Reset demo*, and a clear-box log of every decision.

**Why friction here is ethical.** Dark patterns add friction to what is good for the user (deleting an account)
and remove it from what is good for the business. Qalqan does the opposite: the pause is transparent, chosen in
advance, reversible with the user’s own word, capped at 15 minutes and aimed only at what the scammer wants.
We deliberately refused false urgency (no red flashing alarms), confirmshaming, nagging, sneaking and obstruction.

**Accessibility (WCAG 2.1 AA).** Body text contrast 14.5:1, buttons 7.5:1, non-text contrast ≥ 4.3:1; text sizes
18 / 21 / 24 px plus browser zoom; native controls with a visible focus ring; live regions for the timer and
verdicts; language of the phone area switches to `kk`, `ru` or `en`; no flashing and support for reduced motion.

## DPG Standard compliance (9 indicators)

| # | DPG indicator | Status | Evidence in this repository |
|---|---|---|---|
| 1 | Relevance to the SDGs | Met | [SDG mapping](#sdg-mapping); report Section 1.1 |
| 2 | Use of approved open licences | Met | [`LICENSE`](LICENSE) (MIT), [`LICENSE-CONTENT.md`](LICENSE-CONTENT.md) (CC BY-SA 4.0), [`LICENSE-DATA.md`](LICENSE-DATA.md) (ODC-By 1.0) |
| 3 | Clear ownership | Met; long-term steward planned | Copyright holders in `LICENSE`; stewardship plan in [`GOVERNANCE.md`](GOVERNANCE.md) |
| 4 | Platform independence | Met | Plain HTML, CSS and JavaScript; no build step, no proprietary dependencies, no external requests |
| 5 | Documentation | Met | This README, [`CONTRIBUTING.md`](CONTRIBUTING.md), [`PRIVACY.md`](PRIVACY.md), [`data/README.md`](data/README.md), report in `docs/` |
| 6 | Mechanism for extracting non-personal data and content | Met | JSON/CSV export on screen 6; [`data/scam_patterns_non_pii.json`](data/scam_patterns_non_pii.json) and `.csv` |
| 7 | Adherence to privacy and applicable laws | Met by design; legal review planned | [`PRIVACY.md`](PRIVACY.md): data map, GDPR and Kazakhstan Law No. 94-V |
| 8 | Adherence to standards and best practices | Met; screen-reader test planned | WCAG 2.1 AA audit (report 2.5); HTML validation and data checks in CI |
| 9 | Do no harm by design (privacy and security, inappropriate content, harassment) | Met; monitoring planned | No collection by architecture; no user-generated content; reviewed dataset; [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md); red lines in [`GOVERNANCE.md`](GOVERNANCE.md) |

## SDG mapping

| SDG | Target | How Qalqan-60+ contributes |
|---|---|---|
| **10 Reduced inequalities** (primary) | **10.2** Inclusion of all, irrespective of age or disability | Older people can keep using digital banking and public services safely and independently; three languages and three text sizes; relatives need only SMS |
| **16 Peace, justice and strong institutions** (secondary) | **16.4** Combat organised crime | Interrupts organised scam scripts at the moment of persuasion |
| | **16.a** Strengthen institutions to prevent crime | Open, non-personal scam-script taxonomy and anonymised statistics that anti-fraud institutions and NGOs can reuse |

## Quick start

```bash
# 1. Try it — no installation needed
open src/index.html            # or double-click the file

# 2. Run the same checks as CI
npm install                    # html-validate (development only)
npm run lint:html
python tools/validate.py       # dataset, PII scan, CSV, translation parity, offline guarantee
```

Usage at a defence: press **Fill demo data**, run **Unknown call + banking app opens**, tick a phrase in the script
mirror, type a wrong word, then **Barsik**; open **5 · Relative’s phone** and tap the link; finish with
**Trusted contact calls + banking app** to show that there is no false alarm.

Deterministic screenshot states for documents: `src/index.html?shot=p2&lang=kk&fs=2` (states `ob1 ob2 ob3 home sc0 sc1 sc2 p1 p2 p3 r1 r2 v1 v2 v3`).

## Architecture

```
 Senior's Android phone (everything on the device)              Relative's phone (no app)
 ┌─────────────────────────────────────────────────┐            ┌───────────────────────────┐
 │ OS signals, read only as yes/no:                │            │ Standard SMS              │
 │  • call from a number not in contacts (>24 h)   │   SMS      │  "unknown call + bank app"│
 │  • banking app in the foreground                │ ─────────► │  + link …/s#v1-cb-1402    │
 │  • new SMS contains a one-time code             │ (consent)  │ Browser reads the #part;  │
 │            │                    │               │            │ static host never sees it │
 │            ▼                    ▼               │            └───────────────────────────┘
 │  Two-signal rule (deterministic)   Local AI filter (optional, note only)
 │            │                                    │            Open data (only on "Export")
 │            ▼                                    │            ┌───────────────────────────┐
 │  Pause overlay: script mirror · call · code word│ ─────────► │ weekly counts + taxonomy   │
 │  Storage: settings · trusted person · code-word │  (user)    │ ODC-By, counts < 5 hidden  │
 │  hash · weekly counters (90 days)               │            └───────────────────────────┘
 │  No Internet permission in the core app         │
 └─────────────────────────────────────────────────┘
 Never collected: call audio · chats · contact list · balances · location · caller's number · tracking IDs
```

The prototype simulates the signals. A real Android build would use call-screening and usage-statistics
interfaces rather than the accessibility service where possible; iOS allows only the manual mode.

## Repository structure

```
qalqan-60plus/
├── index.html                      # redirect to the prototype (GitHub Pages)
├── src/index.html                  # single-file clickable prototype (HTML + CSS + JS, offline)
├── data/
│   ├── scam_patterns_non_pii.json  # 24 scam-script patterns, 12 categories, kk/ru/en (ODC-By 1.0)
│   ├── scam_patterns_non_pii.csv   # same data as CSV
│   └── README.md                   # data dictionary
├── docs/
│   ├── Qalqan-60_Group_Report.docx # group report (KBTU format)
│   ├── Qalqan-60_Pitch_Deck.pptx   # 12 slides with speaker notes
│   ├── PITCH_SCRIPT.md             # timed 5-speaker script, demo steps, Q&A preparation
│   ├── SUBMISSION_CHECKLIST.md     # KBTU formatting and submission checklist
│   └── figures/                    # diagrams and screenshots (CC BY-SA 4.0)
├── tools/validate.py, make_csv.py  # repository checks and CSV generator
├── .github/                        # CI workflow, Dependabot, issue and PR templates
├── LICENSE, LICENSE-CONTENT.md, LICENSE-DATA.md
└── CONTRIBUTING.md, CODE_OF_CONDUCT.md, PRIVACY.md, GOVERNANCE.md, SECURITY.md
```

## Contributing

Coders, designers, translators, researchers and older adults are all welcome. Start with an issue labelled
`good first issue` — for example proofreading one language, adding a paraphrased scam pattern, or testing the
prototype with a screen reader. Please read [`CONTRIBUTING.md`](CONTRIBUTING.md) (setup, translation guide,
red lines) and the [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md).

## Licences

| Part | Licence | Why |
|---|---|---|
| Code (`src/`, `tools/`, `.github/`) | [MIT](LICENSE) | Widest reuse by banks, NGOs and public bodies |
| Educational content (interface texts, script mirror, `docs/`) | [CC BY-SA 4.0](LICENSE-CONTENT.md) | Improved anti-fraud advice must stay open |
| Data (`data/`, exported statistics) | [ODC-By 1.0](LICENSE-DATA.md) | Reuse by researchers and journalists with attribution |

All three licences are on the list accepted by the Digital Public Goods Alliance.

## Team and AI disclosure

| Member | Role | Course components |
|---|---|---|
| Bekkaliyev Zharas | Project coordinator, SDG lead | 1, 2, 13 |
| Bissembayev Dostyk | UX researcher, audience lead | 3, 6 |
| Kadyr Sultan | UX/UI prototyper, behavioural lead | 7, 9 |
| Kadyrova Nazerke | Human rights, ethics and accessibility lead | 4, 5, 8 |
| Tuleyeva Aizhan | Data, AI, DPG Standard and critical analysis lead | 10, 11, 12, 14 |

Tutor: M. G. Gerassimov. 

**AI use (course Level C, AI-assisted).** The team used the generative AI assistant Claude (Anthropic) to draft
text, generate and debug the prototype code and diagrams, and check formatting. The concept, the design twist and
the response to the tutor’s critiques are the team’s own; every statistic was checked against its source; research
data are collected by the team and are never generated. See Appendix C of the report.
