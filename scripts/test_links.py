import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECTS_DIR = os.path.join(ROOT, 'projects')
FILES = [os.path.join(PROJECTS_DIR, f) for f in os.listdir(PROJECTS_DIR) if f.endswith('.md')]
FILES.append(os.path.join(ROOT, 'index.md'))

IMG_MD_PATTERN = re.compile(r'!\[[^\]]*\]\(([^)]+)\)')
IMG_HTML_PATTERN = re.compile(r'<img [^>]*src="([^"]+)"')

missing = []

for path in FILES:
    with open(path, 'r', encoding='utf-8') as fh:
        content = fh.read()
    for regex in (IMG_MD_PATTERN, IMG_HTML_PATTERN):
        for match in regex.findall(content):
            if match.startswith('http'):  # skip remote links
                continue
            # Remove optional title string for Markdown images
            match = re.sub(r'\s+".*"$', '', match)
            # Normalize path relative to repo root
            abs_path = os.path.normpath(os.path.join(os.path.dirname(path), match))
            if not os.path.isabs(abs_path):
                abs_path = os.path.join(ROOT, os.path.relpath(abs_path, ROOT))
            if not os.path.exists(abs_path):
                missing.append((path, match))

if missing:
    print('Missing files:')
    for m in missing:
        print(f'{m[0]} -> {m[1]}')
    sys.exit(1)
print('All local media links valid.')
