# Open dataset: scam-script taxonomy (non-PII)

`scam_patterns_non_pii.json` (and the same data in `scam_patterns_non_pii.csv`) describes typical social-engineering
scripts used against people in Kazakhstan, in **Kazakh, Russian and English**. It feeds the scammer-script mirror and
the optional local AI filter of Qalqan-60+, and it can be reused by NGOs, banks, researchers and journalists.

- Licence: **ODC-By 1.0** — attribution “Qalqan-60+ contributors”.
- Personal data: **none**. Phrases are paraphrased from public awareness materials and media reports; no names,
  numbers, links, locations or victim stories. `tools/validate.py` scans every phrase on each change.

## Structure

| Field | Type | Meaning |
|---|---|---|
| `categories[].id` | string | Threat type, e.g. `fake_bank_security`, `safe_account`, `code_request` |
| `categories[].name.{kk,ru,en}` | string | Short name of the threat type |
| `categories[].safe_response.{kk,ru,en}` | string | Plain-language advice for an older adult |
| `patterns[].id` | string | Stable id `QP-001` … |
| `patterns[].category` | string | Refers to `categories[].id` |
| `patterns[].channel` | list | `phone_call`, `messenger_call`, `messenger_voice`, `messenger_video`, `messenger_message`, `sms` |
| `patterns[].asks_for` | list | What the scammer wants: `sms_code`, `egov_code`, `transfer`, `card_details`, `install_app`, `new_loan`, … |
| `patterns[].red_flags` | list | Psychological levers, codes in `red_flag_codes` (`secrecy`, `act_now`, `code`, `transfer`, `authority`, `fear`, `reward`, `install_app`) |
| `patterns[].phrase.{kk,ru,en}` | string | Typical sentence of the script |

The CSV has one row per pattern: `id, category, category_en, channel, asks_for, red_flags, phrase_kk, phrase_ru,
phrase_en, safe_response_en` (lists joined with `|`, UTF-8 with BOM for spreadsheet programs).

## Categories (12)

Fake bank security service · fake police, prosecutor or National Bank · transfer to a “safe account” · request for an
SMS or eGov code · relative in trouble · cloned voice or video · “a loan is being taken in your name” · remote-access
app · fake compensation or pension bonus · phishing SMS or link · fake utility or mobile operator · too-good-to-be-true
investment.

## Exported statistics

The prototype’s *Export* button produces a separate file with weekly counts only:
`week, trigger, outcome, ai_filter, called_trusted_person, count` plus the taxonomy ids. When pooled from many phones,
counts below 5 are suppressed before publication.

## Changing the data

Run `python tools/make_csv.py` after editing the JSON, copy the JSON into the `<script id="dataset">` block of
`src/index.html`, and run `python tools/validate.py`. Two maintainers review every change.
