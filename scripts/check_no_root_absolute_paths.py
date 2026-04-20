#!/usr/bin/env python3
from html.parser import HTMLParser
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
HTML_FILES = sorted(ROOT.glob("*.html"))

class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.issues = []

    def handle_starttag(self, tag, attrs):
        for name, value in attrs:
            if name not in {"href", "src"} or not value:
                continue
            if value.startswith(("http://", "https://", "mailto:", "tel:", "#", "//")):
                continue
            if value.startswith("/"):
                self.issues.append((tag, name, value))

issues = []
for html_file in HTML_FILES:
    parser = LinkParser()
    parser.feed(html_file.read_text())
    for tag, attr, value in parser.issues:
        issues.append((html_file.name, tag, attr, value))

if issues:
    print("Found root-absolute local paths that may break on GitHub Pages project subpaths:")
    for filename, tag, attr, value in issues:
        print(f"- {filename}: <{tag} {attr}=\"{value}\">")
    sys.exit(1)

print(f"OK: checked {len(HTML_FILES)} generated HTML files, no root-absolute local href/src values found.")
