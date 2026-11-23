# KBTU formatting and submission checklist — Qalqan-60+

Written for: the five team members preparing the Week 15 submission and defence.

## 1. Fill in before submitting (everything highlighted in yellow in the report)

- [ ] Title page and Appendix A: replace the five “N. Surname” with the team members’ names (same order as the roles).
- [ ] Title page: insert the KBTU logo from the template in Appendix 1 of the course instructions.
- [ ] Table 7 (Subsection 2.1): enter the real survey and interview results. Never estimate or invent numbers.
- [ ] Appendix B.1: add the team contact e-mail to the consent text.
- [ ] Appendix C: adjust the AI-use statement so that it describes exactly how your team used AI.
- [ ] Appendix D: paste the published prototype link (GitHub Pages) after step 6 below.
- [ ] Ask a native speaker aged 60+ to read the Kazakh and Russian texts of the prototype.
- [ ] Remove all yellow highlighting.

## 2. Final check in Microsoft Word

- [ ] Open the report. When Word asks to update fields, press **Yes** (this rebuilds the table of contents with exact page numbers). Otherwise: click the contents, press **F9**, choose *Update entire table*.
- [ ] Check that no table is split across two pages. If one is, either move it whole to the next page or write “Continuation of Table N” above the continued part, repeat the header and remove the bottom line of the first part.
- [ ] Check that no page or section starts or ends with a figure or table.
- [ ] *File → Export → PDF* and check the PDF page by page.

## 3. Formatting rules (clauses 9.1–9.44, as summarised in the course instructions)

| Rule | Status in the generated report |
|---|---|
| A4, one side, Times New Roman 14, single spacing | Set |
| Margins: left 30, top 20, right 15, bottom 20 mm | Set |
| Structural headings (Contents, Definitions and abbreviations, Introduction, Conclusion, References) not numbered | Set, centred |
| Sections numbered 1–4 with Arabic numerals, no full stop, paragraph indent; subsections 1.1, 1.2 … | Set |
| Every section starts on a new page; subsections separated by blank space | Set (page break before each section, 28 pt before subsection headings) |
| Page numbers bottom centre, no full stop; title page counted but not numbered | Set |
| Figures: caption centred below, “Figure N — Title”, no full stop, referred to in the text | Set (10 figures) |
| Tables: title above with indent, “Table N — Title”, referred to in the text, closed by lines | Set (17 tables, header row repeats, rows kept together) |
| No two figures or two tables in a row without text; a section never begins or ends with a figure or table | Set; check after the TOC update |
| Formula on its own line, number in round brackets at the right margin, symbols explained below | Set (formula 1) |
| Sources cited as [1] in order of first citation; numbered list of references | Set (27 sources, numbered automatically) |
| Appendices: “Appendix A” centred, title on the next line, each appendix referred to in the text, numbering continues | Set (Appendices A–D) |
| Length: suggested 20–25 pages | Main text (Introduction to Conclusion) is about 23 pages; with title page, contents, references and appendices about 34 pages |

## 4. The 14 required components

| # | Component | Report | Slide |
|---|---|---|---|
| 1 | SDG and problem (2+ credible sources) | 1.1, Table 1 | 2 |
| 2 | Goal and success, incl. harm-avoided indicator | Introduction, 1.2, Table 2, formula (1) | 3 |
| 3 | Target audience, 2 personas, edge user, context | 1.3, Tables 3–4 | 4 |
| 4 | Human rights mapping (UDHR) | 1.4, Table 5 | 6 |
| 5 | Ethical principles → design decisions | 1.5, Table 6, decision tree | 6 |
| 6 | Ethical research (survey, 3 interviews, consent, 3 findings) | 2.1–2.2, Tables 7–8, Appendix B | 5 |
| 7 | Design and prototype (sitemap, flow, 6 screens incl. onboarding and consent) | 2.3–2.4, Figures 1–7, Appendix D | 8 (live) |
| 8 | Accessibility and content (WCAG, microcopy, languages) | 2.5, Tables 9–10, Figure 8 | 7 |
| 9 | Behaviour and manipulation (nudge audit) | 2.6, Table 11 | 5, 6 |
| 10 | Personalisation and AI, AI-sanity check | 3.1, Tables 12–13 | 9 |
| 11 | Data protection (data map, GDPR, consent and deletion screens) | 3.2, Figure 9, Table 14 | 9 |
| 12 | DPG Standard self-check and licences | 3.3, Table 15 | 10 |
| 13 | Sustainability and governance | 3.4 | 10 |
| 14 | Risk pre-mortem | 4.1, Table 16 | 11 |

Table and figure numbers follow the generated report; check them again after any edit.

## 5. Submission

- [ ] Deadline: midnight before your Week 15 practice (for a Monday practice, Sunday 23:59).
- [ ] **One** student uploads the report (PDF or DOCX) and the deck (PPTX) for the whole team.
- [ ] File names, for example: `Qalqan-60_Group_Report.pdf`, `Qalqan-60_Pitch_Deck.pptx`.
- [ ] The report contains Appendix A (who did what) and the AI-use statement (Appendix C).

## 6. Repository (optional but strong evidence for DPG indicators 2, 5, 6 and 8)

- [ ] Create a public GitHub repository `qalqan-60plus` and push this folder.
- [ ] Work in five branches, one per member (for example `m1-sdg-report`, `m2-research`, `m3-prototype`, `m4-ethics-a11y`, `m5-data-dpg`), and merge them through pull requests reviewed by another member — the history then shows the fair split of work.
- [ ] *Settings → Pages*: deploy from the `main` branch, root folder; the prototype opens at `https://<account>.github.io/qalqan-60plus/src/`.
- [ ] *Settings → Code security*: enable Dependabot alerts and private vulnerability reporting.
- [ ] Check that the **CI** workflow is green; create labels `good first issue`, `translation`, `dataset`, `rfc`.
- [ ] Replace `<team-account>` in README.md, CONTRIBUTING.md and the report with your account name.

## 7. Defence (10 minutes + 5 minutes Q&A)

- [ ] Every member presents about 2 minutes (see `docs/PITCH_SCRIPT.md`); rehearse with a timer.
- [ ] Laptop: `src/index.html` open offline, **Fill demo data** pressed, demo timer on 15 seconds.
- [ ] Two questions ready for other teams: one on ethics or rights, one on design or data.
- [ ] Every member can answer questions on any part of the project, not only their own.
- [ ] Be on time: the course attendance rules apply to the defence.
