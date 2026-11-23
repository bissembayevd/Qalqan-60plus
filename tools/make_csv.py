#!/usr/bin/env python3
"""Regenerate data/scam_patterns_non_pii.csv from the JSON dataset: python tools/make_csv.py"""
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
data = json.loads((ROOT / 'data' / 'scam_patterns_non_pii.json').read_text(encoding='utf-8'))
cats = {c['id']: c for c in data['categories']}
with (ROOT / 'data' / 'scam_patterns_non_pii.csv').open('w', encoding='utf-8-sig', newline='') as fh:
    w = csv.writer(fh)
    w.writerow(['id', 'category', 'category_en', 'channel', 'asks_for', 'red_flags', 'phrase_kk', 'phrase_ru', 'phrase_en', 'safe_response_en'])
    for p in data['patterns']:
        c = cats[p['category']]
        w.writerow([p['id'], p['category'], c['name']['en'], '|'.join(p['channel']), '|'.join(p['asks_for']), '|'.join(p['red_flags']),
                    p['phrase']['kk'], p['phrase']['ru'], p['phrase']['en'], c['safe_response']['en']])
print('written', len(data['patterns']), 'rows')
