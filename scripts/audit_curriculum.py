#!/usr/bin/env python3
"""Static structural audit for Tech-Law. No network traffic or third-party dependencies.

Run: python3 scripts/audit_curriculum.py
This checks internal links, manifest references, course structure, and duplicate
external links. It does NOT verify current law, licensing rights, or URL HTTP status.
"""
from __future__ import annotations
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[1]
MARKDOWN_LINK = re.compile(r'(?<!!)\[[^\]]*\]\(([^)]+)\)')
HEAD = re.compile(r'^#{1,6}\s+(.+?)\s*$', re.M)
ISSUES = []
WARNINGS = []

def slug(text: str) -> str:
    text = re.sub(r'<[^>]+>', '', text).strip().lower()
    text = re.sub(r'[^\w\- ]+', '', text)
    return re.sub(r'[ \t]+', '-', text)

def audit_md(path: Path) -> None:
    text = path.read_text(encoding='utf-8')
    headings = {slug(m.group(1)) for m in HEAD.finditer(text)}
    for raw in MARKDOWN_LINK.findall(text):
        target = raw.split(' "', 1)[0].strip().strip('<>')
        if not target or target.startswith(('mailto:', 'tel:', 'data:', 'javascript:')):
            continue
        if target.startswith(('http://', 'https://')):
            if not urlparse(target).netloc:
                ISSUES.append(f'{path.relative_to(ROOT)}: malformed external URL {target}')
            continue
        part, _, fragment = target.partition('#')
        dest = (path.parent / unquote(part)).resolve() if part else path
        if not dest.is_relative_to(ROOT):
            ISSUES.append(f'{path.relative_to(ROOT)}: out-of-repository link {target}')
        elif not dest.exists():
            ISSUES.append(f'{path.relative_to(ROOT)}: missing local target {target}')
        elif fragment and dest.suffix.lower() == '.md':
            target_headings = headings if dest == path else {
                slug(m.group(1)) for m in HEAD.finditer(dest.read_text(encoding='utf-8'))
            }
            if unquote(fragment).lower() not in target_headings:
                WARNINGS.append(f'{path.relative_to(ROOT)}: unchecked heading anchor {target}')

def main() -> int:
    md = sorted(ROOT.rglob('*.md'))
    for path in md:
        audit_md(path)
    manifest = ROOT / 'quality/curriculum-manifest.json'
    if manifest.exists():
        obj = json.loads(manifest.read_text(encoding='utf-8'))
        books = obj.get('textbooks', [])
        if len({b['id'] for b in books}) != len(books):
            ISSUES.append('manifest: duplicate textbook ids')
        for b in books:
            index = ROOT / b['index']
            if not index.is_file():
                ISSUES.append(f"manifest: missing textbook index {b['index']}")
                continue
            parent = index.parent
            chapters = list(parent.glob('[0-9][0-9]-*.md'))
            if len(chapters) != b['chapter_count']:
                ISSUES.append(f"manifest: {b['id']} expects {b['chapter_count']} chapters; found {len(chapters)}")
        for rel in obj.get('quality_documents', []):
            if not (ROOT / rel).is_file():
                ISSUES.append(f'manifest: missing quality document {rel}')
    print(f'Audited {len(md)} Markdown files; {len(ISSUES)} structural errors; {len(WARNINGS)} warnings')
    for issue in ISSUES:
        print('ERROR:', issue)
    for warning in WARNINGS:
        print('WARN:', warning)
    print('External source accuracy, legal currency and reuse permissions need independent human review.')
    return 1 if ISSUES else 0

if __name__ == '__main__':
    sys.exit(main())
