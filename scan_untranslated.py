#!/usr/bin/env python3
"""Scan translated files for remaining untranslated English content."""
import os, re

dirs = [
    'D:/tiktok/tiktok-docs/zh/API_Reference/Products',
    'D:/tiktok/tiktok-docs/zh/API_Reference/Products_Global_Products',
    'D:/tiktok/tiktok-docs/zh/API_Reference/Products_Compliance',
]

chinese_pattern = re.compile(r'[\u4e00-\u9fff]')

# English function words that indicate untranslated content
ENG_WORDS = set("""
the is are was were have has had will would could should must shall can may
might this that these those your they their them which where when what how why
about from with without into upon after before between through during towards
among along already also always never often sometimes usually just only even
still yet not but and else either neither both each every any all most more
less least much many few several some such rather quite too very being been
does doing done going make makes made making take takes taken took give gives
given gave come comes coming saw know knows known think thinks thought find
finds found look looks looked want wants used using call calls called try tries
tried ask asks asked work works worked working become becomes became leave
leaves left begin begins began show shows showed keep keeps kept let lets run
runs running write writes wrote set sets turn turns turned move moves moved pay
pays paid send sends sent build builds built hold holds held bring brings
brought happen happens appeared appear includes included provide provides
provided require requires required represent represents referred refer refers
ensure ensures ensured help helps helped allow allows allowed enable enables
enabled describe describes described determine determines determined indicate
indicates indicated specify specifies specified define defines defined create
creates created retrieve retrieves retrieved delete deletes deleted update
updates updated edit edits edited submit submits submitted upload uploads
uploaded check checks checked search searches searched list lists listed get
gets got activate activates activated deactivate deactivates publish publishes
published replicate replicates replicated optimize optimizes optimized diagnose
diagnoses diagnosed recommend recommends recommended filter filters filtered
sort sorts sorted compare compares compared convert converts converted assign
assigns assigned apply applies applied remove removes removed add adds added
replace replaces replaced change changes changed pass passes passed fail fails
failed failing reach reached graduate graduated subject limited available
important particularly especially however therefore furthermore moreover
nevertheless nonetheless otherwise instead meanwhile accordingly consequently
hence thus whereas although though since because unless until whether wherever
whenever provided assuming given considering regarding concerning follows
following followed above below hereby herein hereinafter thereby thereof thereto
means meaning mean seller sellers shop shops product products api apis tiktok
parameter parameters value values error errors code codes message messages
response request requests attribute attributes category categories brand brands
image images file files video videos certification certifications size chart
charts weight height width length dimensions package packages dimension
description descriptions information title titles name names type types status
statuses level levels country countries region regions market markets currency
currencies precision decimal place places number numbers date dates time times
timestamp format formats extension local globally global locally example
examples note notes warning warnings detail details specific generally general
standard standards built custom defined undefined required optional mandatory
supported unsupported applicable only mainly primarily primarily second third
first fourth fifth sixth seventh eighth ninth tenth
""".split())

untranslated_lines = []
total_files = 0
files_with_issues = 0

for d in dirs:
    for f in sorted(os.listdir(d)):
        if not f.endswith('.md'):
            continue
        total_files += 1
        filepath = os.path.join(d, f)
        has_issue = False
        with open(filepath, 'r', encoding='utf-8') as fh:
            in_code = False
            for i, line in enumerate(fh, 1):
                stripped = line.strip()
                if stripped.startswith('```'):
                    in_code = not in_code
                    continue
                if in_code:
                    continue
                if not stripped:
                    continue
                # Skip lines that are mostly Chinese
                chinese_chars = len(chinese_pattern.findall(stripped))
                total_chars = len(stripped)
                if total_chars > 0 and chinese_chars / total_chars > 0.25:
                    continue
                # Skip pure markdown table separators
                if stripped.startswith('|') and '---' in stripped:
                    continue
                # Skip HTML/img/svg
                if stripped.startswith('<img') or stripped.startswith('data:image'):
                    continue
                if 'from="flow-chart"' in stripped or 'payload=' in stripped:
                    continue
                # Skip URLs and links
                if stripped.startswith('http://') or stripped.startswith('https://'):
                    continue
                # Count English words
                words = re.findall(r'[a-zA-Z]+', stripped)
                eng_count = sum(1 for w in words if w.lower() in ENG_WORDS)
                if eng_count >= 3 and len(words) >= 3:
                    untranslated_lines.append((f, i, stripped[:150]))
                    has_issue = True
        if has_issue:
            files_with_issues += 1

print(f'Total files: {total_files}')
print(f'Files with untranslated content: {files_with_issues}')
print(f'Total untranslated lines: {len(untranslated_lines)}')
print()
for f, i, line in untranslated_lines:
    print(f'{f}:{i}: {line}')
