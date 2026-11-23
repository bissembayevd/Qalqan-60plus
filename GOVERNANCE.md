# Governance

## Ownership and stewardship

Qalqan-60+ is created by a five-person student team of the course *Ethical Digital Design* (DPG track) at
Kazakh-British Technical University, Almaty, 2026. Copyright is held by the Qalqan-60+ contributors (see `LICENSE`).

| Phase | Steward | What changes |
|---|---|---|
| 2026 | Student team | Concept, prototype, research, open dataset |
| 2027 | University open-source laboratory with a faculty adviser | Android proof of concept, usability tests |
| Later | An NGO working with older people | Pilot, stop-card distribution, long-term maintenance |

## Maintainers

| Maintainer | Area |
|---|---|
| Member 1 (N. Surname) | Coordination, SDG alignment, releases |
| Member 2 (N. Surname) | Research and user testing |
| Member 3 (N. Surname) | Prototype and design |
| Member 4 (N. Surname) | Ethics, rights, accessibility, translations |
| Member 5 (N. Surname) | Data, AI, privacy, DPG compliance |

Private contact for conduct and privacy reports: the team e-mail address (to be published by the maintainers)
or GitHub’s private vulnerability reporting.

## How decisions are made

- Ordinary changes: one maintainer review and green CI.
- Changes to the scam dataset, the trigger rule or any text shown during a pause: **two** maintainer reviews.
- Changes that touch the red lines below: a public proposal (issue labelled `rfc`) open for at least 14 days,
  then a decision by all maintainers, recorded in the issue.

## Red lines

The following will not be added, whoever asks or pays for it:

1. recording or analysing calls, reading chats or messengers, uploading contacts;
2. location tracking, analytics, advertising or tracking identifiers;
3. any server that receives personal data, or the Internet permission in the core Android app;
4. remote control by relatives (approving payments, blocking apps, reading data);
5. dark patterns: false urgency, confirmshaming, nagging, obstruction, hidden messages.

## Sponsors and partners

Sponsors (for example banks) and partners (for example the NPCK Anti-Fraud Center) may fund work or share
public scam patterns. They receive **no user data and no veto** over code, content or the red lines.
Sponsorship is listed publicly in the README.

## Exit plan

If the project ends: a final release is published and the repository is archived read-only; the application keeps
working because it needs no server; data stay on users’ phones and can still be deleted; anyone can host the static
status page; and the open licences allow an NGO, a university or a bank to continue the work.
