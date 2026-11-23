# Privacy notice

Qalqan-60+ is designed so that it **cannot** watch the people it protects. This notice describes the clickable
prototype in this repository and the planned Android application. It follows the GDPR (Regulation (EU) 2016/679)
and the Law of the Republic of Kazakhstan No. 94-V “On Personal Data and Their Protection”.

## What the prototype does

The prototype (`src/index.html`) runs entirely in your browser. Its Content-Security-Policy (`default-src 'none'`)
forbids any network request: no server receives anything. All calls, banks and SMS in it are simulated.
Settings are kept in the browser’s `localStorage` until you press **Delete all my data**.

## Data map (planned application)

| Data | Why | Where | How long | Who can see it |
|---|---|---|---|---|
| Consents, language, text size | Respect your choices | Your phone | Until you delete them | You |
| Trusted person’s name and number | Call button and the alert SMS | Your phone | Until you delete them or they reply STOP | You; the mobile operator when an SMS is sent |
| Family code word | End a pause early | Your phone, as a salted hash | Until you change it | Nobody (it cannot be read back) |
| Signals: call from a number not in contacts, banking app open, SMS with a code | Decide whether to start a pause | Phone memory, as yes/no | Discarded immediately | Nobody |
| Text of a new SMS (only if the AI filter is on) | Add a gentle note | Phone memory | Discarded immediately | Nobody |
| Alert SMS (event type and start time after `#` in the link) | Ask your trusted person to call | Mobile network, their phone | As long as they keep the SMS | Your trusted person; the operator |
| Weekly pause counters | Measure whether Qalqan helps | Your phone | 90 days | You; shared only if you export them |

**Never collected:** call audio, message or chat content, the contact list, bank balances or payments, location,
the caller’s number, advertising or tracking identifiers.

## Your rights

- **Consent and withdrawal** (GDPR Art. 6–7; Law No. 94-V): every function is off until you switch it on, and you
  can switch it off in *Privacy and data* at any time.
- **Erasure** (Art. 17): *Delete all my data* removes everything from the phone in one step. We hold no copy.
- **Portability** (Art. 20): *Export* gives you anonymised statistics as JSON or CSV.
- **Privacy by design and by default** (Art. 25): the architecture has no server and the core requests no
  Internet permission; personal data stay on the device in Kazakhstan.

## Your trusted person

Their number is personal data of another person. Qalqan sends them one welcome SMS so they know and can reply STOP.

## Status page

The link in the alert SMS opens a static page. The status is written after `#` in the link and is never sent to the
web server. The hosting provider may log the visit (IP address, time) under its own policy.

## Contact

Questions and requests: the maintainers listed in [GOVERNANCE.md](GOVERNANCE.md).
