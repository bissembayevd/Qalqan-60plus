# Contributing to Qalqan-60+

Thank you for helping older people stay safe from phone fraud without losing their privacy or dignity.
You do not need to be a programmer: **designers, translators, researchers, social workers and older adults
themselves** are just as welcome as coders.

By taking part you agree to follow our [Code of Conduct](CODE_OF_CONDUCT.md).

## Ways to contribute

| You are… | You can… |
|---|---|
| A **coder** | fix bugs, improve accessibility, build the Android proof of concept, extend the checks in `tools/validate.py` |
| A **designer** | improve the six screens, test contrast and text sizes, design the printable stop card |
| A **translator** | review Kazakh and Russian texts, add a Latin-script Kazakh locale, simplify wording |
| A **researcher** | improve the survey and interview guides, run usability tests with people aged 60+ |
| Anyone | report a new scam script (paraphrased, without personal data), suggest clearer wording |

## Good first issues

Look for issues labelled [`good first issue`](../../labels/good%20first%20issue). Typical starters:

1. **Proofread one language.** Read every Kazakh or Russian text in the `i18n` block of `src/index.html` and suggest simpler words.
2. **Add a scam pattern.** Paraphrase one script you have heard about into `data/scam_patterns_non_pii.json` in all three languages.
3. **Check one WCAG criterion.** Test the prototype with the keyboard only, or with NVDA/TalkBack, and report what is unclear.
4. **Improve the stop card.** Turn the script-mirror questions into a printable A6 card (PDF or SVG, CC BY-SA 4.0).
5. **Write a test.** Add one more check to `tools/validate.py` (for example, that every category is used by at least one pattern).

## Getting started

The prototype has **no build step**. Open `src/index.html` in any modern browser; it works offline.

```bash
git clone https://github.com/<team-account>/qalqan-60plus.git
cd qalqan-60plus
# run the same checks as CI
npm install            # installs html-validate (development only)
npm run lint:html      # HTML validation
python tools/validate.py   # dataset, PII, CSV, translation parity, offline checks
```

If you change the dataset, regenerate the CSV and the copy embedded in the prototype:

```bash
python tools/make_csv.py
# then paste the JSON into the <script id="dataset"> block of src/index.html (CI checks they are identical)
```

## Rules that protect users (please read)

These are design red lines. Pull requests that break them will not be merged — see [GOVERNANCE.md](GOVERNANCE.md).

- **No surveillance.** Do not add call recording, chat or message reading (except the optional on-device SMS
  filter), contact-list upload, location, analytics, trackers or remote control by relatives.
- **No network calls from the core.** The prototype keeps `Content-Security-Policy: default-src 'none'`.
  The planned Android app must not request the Internet permission.
- **No dark patterns.** No false urgency, red flashing alarms, confirmshaming, nagging, hidden SMS or
  obstruction of deletion or consent withdrawal.
- **Calls are never blocked** and a wrong code word never locks anyone out.
- **Every text exists in Kazakh, Russian and English.** CI fails if a key is missing in one language.

## Translation guide

- Texts live in the `i18n` JSON block of `src/index.html`, one object per language (`kk`, `ru`, `en`).
- Keep the same key in all three languages. Placeholders such as `{name}` or `{time}` must stay unchanged.
- Write for a tired, frightened person: short sentences, everyday words, the second person, an action rather
  than an alarm, no blame. Say “SMS code”, not “OTP”.
- Kazakh uses Cyrillic today. A Latin-script locale (`kk-Latn`) can be added as a fourth object; add it to
  `LANGS` in `tools/validate.py` as well.

## Adding a scam pattern

1. Paraphrase. Never copy a message word for word if it contains names, numbers or links.
2. Add an entry with the next `QP-nnn` id, an existing `category`, `channel`, `asks_for`, `red_flags`
   and the `phrase` in `kk`, `ru` and `en`.
3. In the pull request, describe the public source (police warning, bank notice, news article) — not in the data.
4. Two maintainers review every change to the dataset.

## Pull requests

- One topic per pull request; describe *why* the change helps older users.
- Run the checks above before you push. CI must be green.
- Screenshots are welcome for visual changes (use the `?shot=` states of the prototype).
- By contributing you agree that code is licensed under MIT, content under CC BY-SA 4.0 and data under ODC-By 1.0.
