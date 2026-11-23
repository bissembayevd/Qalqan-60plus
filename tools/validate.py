#!/usr/bin/env python3
"""Repository checks for Qalqan-60+ (run locally or in CI): python tools/validate.py

1. data/scam_patterns_non_pii.json is valid and complete (ids, categories, kk/ru/en phrases, red-flag codes).
2. The open data contains no personal data patterns (phone numbers, e-mails, links, card numbers).
3. data/scam_patterns_non_pii.csv matches the JSON file.
4. Every interface text in src/index.html exists in Kazakh, Russian and English (translation parity).
5. The dataset embedded in src/index.html is identical to the JSON file.
6. The prototype makes no external requests (no http(s) URLs in src, script, link or img attributes).
"""
import csv
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / 'data' / 'scam_patterns_non_pii.json'
CSV = ROOT / 'data' / 'scam_patterns_non_pii.csv'
HTML = ROOT / 'src' / 'index.html'
LANGS = ('kk', 'ru', 'en')
errors = []


def fail(msg):
    errors.append(msg)


# 1. dataset structure
data = json.loads(DATA.read_text(encoding='utf-8'))
for key in ('name', 'version', 'license', 'categories', 'patterns', 'red_flag_codes'):
    if key not in data:
        fail(f'dataset: missing top-level key "{key}"')
if data.get('license') != 'ODC-By-1.0':
    fail('dataset: licence must be ODC-By-1.0')
cats = {c['id'] for c in data.get('categories', [])}
for c in data.get('categories', []):
    for field in ('name', 'safe_response'):
        for lang in LANGS:
            if not c.get(field, {}).get(lang, '').strip():
                fail(f'category {c["id"]}: missing {field}.{lang}')
ids = set()
flags = set(data.get('red_flag_codes', {}))
for p in data.get('patterns', []):
    pid = p.get('id', '?')
    if not re.fullmatch(r'QP-\d{3}', pid):
        fail(f'pattern {pid}: id must look like QP-001')
    if pid in ids:
        fail(f'pattern {pid}: duplicate id')
    ids.add(pid)
    if p.get('category') not in cats:
        fail(f'pattern {pid}: unknown category {p.get("category")}')
    for lang in LANGS:
        if not p.get('phrase', {}).get(lang, '').strip():
            fail(f'pattern {pid}: missing phrase.{lang}')
    for f in p.get('red_flags', []):
        if f not in flags:
            fail(f'pattern {pid}: unknown red flag {f}')
    if not p.get('channel') or not p.get('asks_for'):
        fail(f'pattern {pid}: channel and asks_for are required')

# 2. no personal data in open data
PII = {
    'phone number': re.compile(r'(?:\+?\d[\s\-()]*){10,}'),
    'e-mail': re.compile(r'[\w.+-]+@[\w-]+\.[\w.]+'),
    'link': re.compile(r'(?:https?://|www\.)\S+', re.I),
    'card number': re.compile(r'\b(?:\d[ -]?){13,19}\b'),
}
for p in data.get('patterns', []):
    for lang, text in p.get('phrase', {}).items():
        for what, rx in PII.items():
            if rx.search(text):
                fail(f'pattern {p["id"]}.{lang}: looks like it contains a {what}')

# 3. CSV mirrors JSON
if CSV.exists():
    with CSV.open(encoding='utf-8-sig', newline='') as fh:
        rows = list(csv.DictReader(fh))
    if [r['id'] for r in rows] != [p['id'] for p in data['patterns']]:
        fail('CSV ids differ from JSON ids; regenerate the CSV')
    for r, p in zip(rows, data['patterns']):
        for lang in LANGS:
            if r.get('phrase_' + lang) != p['phrase'][lang]:
                fail(f'CSV {r["id"]}: phrase_{lang} differs from JSON')
else:
    fail('data/scam_patterns_non_pii.csv is missing')

# 4-5. prototype checks
html = HTML.read_text(encoding='utf-8')


def json_block(block_id):
    m = re.search(r'<script type="application/json" id="' + block_id + r'">(.*?)</script>', html, re.S)
    if not m:
        fail(f'src/index.html: JSON block #{block_id} not found')
        return None
    return json.loads(m.group(1))


i18n = json_block('i18n')
if i18n:
    keys = {lang: set(i18n.get(lang, {})) for lang in LANGS}
    all_keys = set().union(*keys.values())
    for lang in LANGS:
        missing = sorted(all_keys - keys[lang])
        if missing:
            fail(f'translation parity: {lang} is missing {len(missing)} key(s): {", ".join(missing[:10])}')
        empty = [k for k, v in i18n.get(lang, {}).items() if not str(v).strip()]
        if empty:
            fail(f'translation: empty {lang} text(s): {", ".join(empty[:10])}')
    used = set(re.findall(r'data-i18n(?:-ph|-aria)?="([\w]+)"', html)) | set(re.findall(r"\bt\('([\w]+)'\s*[,)]", html))
    unknown = sorted(k for k in used if k not in keys['en'])
    if unknown:
        fail(f'interface uses unknown text keys: {", ".join(unknown)}')

embedded = json_block('dataset')
if embedded is not None and embedded != data:
    fail('the dataset embedded in src/index.html differs from data/scam_patterns_non_pii.json')

# 6. no external requests from the prototype
ext = re.findall(r'<(?:script|link|img|iframe)[^>]+(?:src|href)="https?://', html, re.I)
if ext:
    fail('src/index.html loads external resources; the prototype must work offline')
if "default-src 'none'" not in html:
    fail('src/index.html must keep the Content-Security-Policy default-src \'none\'')

if errors:
    print('FAILED:')
    for e in errors:
        print('  -', e)
    sys.exit(1)
print(f'OK: {len(data["patterns"])} patterns, {len(cats)} categories, '
      f'{len(i18n["en"]) if i18n else 0} interface texts in {len(LANGS)} languages, no PII, no external requests.')
