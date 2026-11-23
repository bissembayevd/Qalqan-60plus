# Qalqan-60+ — pitch script (10 minutes, 5 speakers)

Written for: the five team members who present the pitch at the Week 15 defence.

Deck: `docs/Qalqan-60_Pitch_Deck.pptx` (the same text is in the speaker notes of every slide). Speaking rate is about 135 words per minute. Replace `[name]` with your own name.

## Timing

| Order | Speaker | Slides | Time |
|---|---|---|---|
| 1 | Speaker 1 — coordinator, SDG lead | 1, 2, 3, 12 | 0:20 + 0:50 + 0:35 + 0:25 = 2:10 |
| 2 | Speaker 2 — UX research, audience | 4, 5 | 1:00 + 1:00 = 2:00 |
| 3 | Speaker 4 — rights, ethics, accessibility | 6, 7 | 1:00 + 0:55 = 1:55 |
| 4 | Speaker 3 — prototype, behaviour (live demo) | 8 | 2:00 |
| 5 | Speaker 5 — data, AI, DPG, risks | 9, 10, 11 | 0:40 + 0:40 + 0:35 = 1:55 |

**Total: 10:00.** Rehearse with a timer at least twice; hand over with one sentence (“Now [name] shows …”).

## Slide-by-slide script

### Slide 1 — Qalqan-60+  (SPEAKER 1 · 0:20)

Good morning. We are team Qalqan-60+. “Qalqan” means “shield” in Kazakh. Our Digital Public Good protects people over sixty from phone and SMS-code fraud without spying on them. I am [name], the coordinator. After me, my colleagues present the users and research, rights and ethics, the live prototype, and data and governance.

### Slide 2 — Phone fraud wins by speed, not by technology  (SPEAKER 1 · 0:50)

Why does this matter? Participants of the national Anti-Fraud Forum counted 26.3 thousand internet-fraud cases in 2025. The Prosecutor General’s Office reports about 12.2 billion tenge of damage from internet fraud last year, and the police intercepted 85 million scam calls. At the same time Kazakhstan has 2.8 million people aged sixty and over. Scammers do not hack phones — they hack time: “act now”, “tell no one”, “dictate the code”. Research shows that with age deliberate thinking slows down, while the script stays fast. So this is an inclusion problem — SDG 10.2 — and an organised-crime problem — SDG 16.4 and 16.a. One honest note: official sources count fraud in different categories, so in our report every number carries its exact scope.

### Slide 3 — Goal: interrupt the script, not the person  (SPEAKER 1 · 0:35)

Our goal in one sentence: reduce successful phone and SMS-code fraud against people sixty-plus with an automatic, calm, script-breaking pause and a family call-back channel that never exposes their private life. We measure three things. First, harm avoided: at least ninety percent of pauses end with no money sent and no code disclosed. Second, the harm we might cause ourselves: false alarms below fifteen percent. Third, inclusion: eighty percent of older users finish onboarding without help.

### Slide 4 — Designed for the edge user first  (SPEAKER 2 · 1:00)

Thank you. We designed for three people. Gulnara is sixty-seven, a retired teacher in Shymkent. She pays her bills in a banking app, and her biggest fear is not the scammer — it is that her children will take her card away. Her son Daniyar works in Astana. He wants to help, but he will not install another tracking app, and he does not want to read his mother’s messages. And Valentina, seventy-nine, is our edge user: she lives alone, has a cataract and may only have a basic phone. If our design needed a modern smartphone or a relative nearby, it would exclude her. So we added extra-large text, a manual button, a paper stop card, and the option to name a neighbour or an NGO volunteer as the trusted person. The moment we design for is short, stressful and private.

### Slide 5 — Research changed the design: version 1 → version 2  (SPEAKER 2 · 1:00)

Our research has three parts: an expert review with our tutor, an anonymous survey of at least twenty-four people, and three interviews — an older adult, an adult child and a professional. Everyone gives informed consent; we ask no names, banks or amounts, and the data are deleted after the course. The expert review changed our design three times. Version one had a panic button — but people under stress freeze and never press it, so now the shield starts by itself when two signals coincide. Version one asked “are you sure?” — but scammers tell victims in advance to click through such pop-ups, so now the pause mirrors the scammer’s exact words and can be ended early only with a family code word. And relatives refused another app, so now they receive an ordinary SMS.

### Slide 6 — Rights and principles built into the interface  (SPEAKER 4 · 1:00)

I am [name], responsible for rights, ethics and accessibility. We mapped every feature to the Universal Declaration of Human Rights. Article 12, privacy: the shield reads only yes-or-no signals on the phone — never calls, chats, balances or location. Article 17, property: we protect savings, but we never block a call or the banking app, so a real emergency is never stopped. Article 2: three languages and three text sizes, so nobody is excluded. And our principles became decisions, not slogans. Autonomy: every consent is off until you turn it on, and you can end the pause yourself. Transparency: the home screen shows the exact rule, and you see the exact SMS your family receives. Safety: calm colours instead of red alarms, and no lock-out after a wrong word.

### Slide 7 — Everything stays on the phone, in three languages  (SPEAKER 4 · 0:55)

Here is the architecture. Everything about the older person stays on the phone: two signals are read as yes or no, a deterministic rule starts the pause, and the settings are stored locally — the code word only as a salted hash. The relative gets one standard SMS; the status travels after the hash sign in the link, so our server never receives it. At the bottom you see what we never collect — by architecture, not by promise. For accessibility we followed WCAG 2.1 AA: body text contrast is 14.5 to 1, three text sizes, keyboard and screen-reader roles, and full parity in Kazakh, Russian and English, which an automated check enforces.

### Slide 8 — Live demo: zero button → pause → code word → relative  (SPEAKER 3 · 2:00 (LIVE — open src/index.html before the talk; press “Fill demo data”))

Now the live prototype. It is one HTML file that works offline. This is the calm home screen. [Click ҚАЗ, then A++, then back to ENG and A.] First, a scam scenario. [Click “Unknown call + banking app opens”.] A stranger says he is from bank security and asks Gulnara to open her banking app and tell no one. She opens it — and she presses nothing: two signals coincide and the pause starts by itself. [Pause screen.] Calm colours, a countdown and a breathing cue. Below is the script mirror. [Tick “Tell me the SMS code”.] The verdict is plain: this is exactly how scammers talk — hang up. The biggest button calls her daughter. Now imagine the scammer says “type this word to close the window”. [Type “wrong”, press End pause.] No lock-out and no shame — the pause simply continues. Only our family word works. [Type “Barsik”, press End pause.] Pause ended. Now her daughter’s phone. [Click “5 · Relative’s phone”.] An ordinary SMS, no app. [Tap the link.] She sees only the status, a “call Mum calmly” button and the list of what she can never see. Finally, false alarms. [Click “Trusted contact calls + banking app”.] A known caller — Qalqan stays quiet.

BACKUP if the laptop fails: walk through the four screenshots on this slide.

### Slide 9 — Data protection and clear-box AI  (SPEAKER 5 · 0:40)

I am [name], data and AI. Our data map has nine items; the sensitive ones never leave the phone or are discarded at once. The AI phishing filter is optional and off by default: it reads only the text of a new SMS in memory, never blocks anything, and explains which phrase it marked — that is our clear-box answer to the Week 14 AI-sanity check. Users can withdraw any consent, export anonymous statistics or delete everything with one button — GDPR articles 7, 17, 20 and 25 — and we meet Kazakhstan’s personal data law because nothing leaves the device.

### Slide 10 — DPG Standard: all nine indicators addressed  (SPEAKER 5 · 0:40)

Against the nine DPG indicators: SDG relevance, open licences — MIT for code, CC BY-SA for content, ODC-By for data — clear ownership, platform independence, documentation, non-personal data export, privacy, standards and do-no-harm are all met at concept stage; a legal review, a screen-reader test, monitoring and a long-term steward are planned. Running costs are close to zero: one 140-kilobyte file, no servers, no trackers. The project moves from our team to a university open-source lab and then to an NGO, and if it ends, it keeps working offline and anyone can fork it.

### Slide 11 — Pre-mortem: how Qalqan-60+ itself could cause harm  (SPEAKER 5 · 0:35)

Finally, our pre-mortem: three ways Qalqan itself could cause harm. One: exclusion and false alarms — so calls are never blocked, known contacts never trigger, and there is a manual mode and a paper card. Two: family coercion — relatives get no control and no data, and the code word is never transmitted. Three: mission creep — someone adds telemetry “for better protection”; our core app has no Internet permission and no server, so that would need a public decision.

### Slide 12 — Slow the script, keep the dignity  (SPEAKER 1 · 0:25)

To conclude: friction can be ethical when it is transparent, reversible and on the user’s side, and “without surveillance” must be built into the architecture. Our next step is testing with older adults. Two questions for you: would you accept a pause that you cannot skip without a family word? And what is the minimum a relative should see to help? Thank you.

## Live demo checklist (Speaker 3)

1. Before the talk: open `src/index.html` in Chrome or Edge on the presentation laptop (no Internet needed), press F11 for full screen, then **Fill demo data**. Pause length stays on **Demo: 15 seconds**.
2. Keys **1–6** jump between screens if a click goes wrong; **Reset demo** clears everything.
3. Code word for the demo: **Barsik** (any case).
4. Backup: if the laptop fails, present slide 8 (four screenshots) with the same words.

## Questions we ask other teams (prepare two)

- **Ethics or rights:** “Which group of users is most likely to be excluded by your design, and what did you change because of them?”
- **Design or data:** “Which personal data does your DPG collect that it does not strictly need, and how long do you keep it?”

## Questions we expect, with short answers

| Question | Answer (who) |
|---|---|
| Isn’t a pause you cannot skip paternalistic? | The person chooses it in advance, sets the code word, can end it with that word, and it ends by itself after 15 minutes; relatives get no control. (Speaker 4) |
| What if a real emergency needs a payment? | Calls are never blocked, known contacts never trigger, the code word ends the pause, and 112/102 are always available. (Speaker 4) |
| Can a scammer just say “save my number first”? | Numbers saved less than 24 hours ago still count as unknown. (Speaker 3) |
| How does Android know the banking app is open without spying? | The planned app reads only yes/no signals through call-screening and usage-statistics interfaces, on the device, with no Internet permission. It never reads screen content. (Speaker 5) |
| Does the AI read my messages? | Only if you switch the optional filter on; it checks a new SMS in memory, never stores or sends it, never blocks, and explains what it marked. (Speaker 5) |
| Why should a relative trust a link? | It is an ordinary SMS from the senior’s own number; the link has no login and shows only a status snapshot. (Speaker 2) |
| Your statistics disagree (86.1 % growth vs. a 13 % fall)? | Different categories and periods; we cite each number with its exact scope in the report, Table 1. (Speaker 1) |
| What about iPhone and push-button phones? | iOS allows only the manual mode; for basic phones we offer a printable stop card and an SMS-only path. This is our main residual risk. (Speaker 5) |
| Where is your survey data? | Collected with consent and summarised in Table 7 of the report; we never fill in estimates. (Speaker 2) |
| Who maintains it after the course? | Team → university open-source lab → NGO; running cost is near zero; it keeps working offline if the project ends. (Speaker 1) |
