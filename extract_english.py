#!/usr/bin/env python3
"""Extract all unique untranslated English lines from the translated docs."""
import os, re

dirs = [
    'D:/tiktok/tiktok-docs/zh/API_Reference/Products',
    'D:/tiktok/tiktok-docs/zh/API_Reference/Products_Global_Products',
    'D:/tiktok/tiktok-docs/zh/API_Reference/Products_Compliance',
]

chinese_pattern = re.compile(r'[\u4e00-\u9fff]')

results = {}  # filepath -> [(line_num, line_text)]

for d in dirs:
    for f in sorted(os.listdir(d)):
        if not f.endswith('.md'):
            continue
        filepath = os.path.join(d, f)
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
                # Skip URLs
                if stripped.startswith('http://') or stripped.startswith('https://'):
                    continue
                # Skip lines that are just locale codes or enum values
                if re.match(r'^[*\s]*`?[a-z]{2}[-_][A-Z]{2}`?\s*\|?$', stripped):
                    continue
                # This line has significant English content
                if f not in results:
                    results[f] = []
                results[f].append((i, stripped))

# Print unique lines sorted by frequency
all_lines = []
line_counts = {}
for f, lines in results.items():
    for num, text in lines:
        all_lines.append((f, num, text))
        # Normalize for counting
        normalized = text.strip('| ').strip()
        line_counts[normalized] = line_counts.get(normalized, 0) + 1

# Print lines that appear in multiple files (high value targets)
print("=== HIGH FREQUENCY LINES (appear in 3+ files) ===")
high_freq = [(text, count) for text, count in line_counts.items() if count >= 3 and len(text) > 10]
high_freq.sort(key=lambda x: -x[1])
for text, count in high_freq[:100]:
    print(f"  [{count}x] {text[:200]}")

print(f"\n=== TOTAL UNIQUE ENGLISH LINES: {len(line_counts)} ===")
print(f"=== TOTAL FILES WITH ISSUES: {len(results)} ===")

# Print all lines per file
print("\n=== ALL UNTRANSLATED LINES BY FILE ===")
for f in sorted(results.keys()):
    lines = results[f]
    print(f"\n--- {f} ({len(lines)} lines) ---")
    for num, text in lines:
        print(f"  L{num}: {text[:250]}")
