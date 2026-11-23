# Licence for open data: ODC-By 1.0

The open dataset in `data/` (`scam_patterns_non_pii.json`, `scam_patterns_non_pii.csv`) and the anonymised
statistics exported from the prototype are made available under the
**Open Data Commons Attribution License v1.0** (ODC-By 1.0):
https://opendatacommons.org/licenses/by/1-0/

Attribution: “Qalqan-60+ contributors, ODC-By 1.0”.

## No personal data

The dataset contains no personal data. Phrases are generic paraphrases of scam scripts described in public
awareness materials and media reports. It contains no names, phone numbers, card or account numbers, links,
locations or victim stories. `tools/validate.py` checks every phrase for phone numbers, e-mail addresses, links
and card numbers on every change.

Statistics exported from the prototype contain only weekly counts (ISO week, trigger type, outcome, AI filter
on or off, whether the trusted person was called). When contributions from many phones are pooled for
publication, counts below 5 are suppressed.
