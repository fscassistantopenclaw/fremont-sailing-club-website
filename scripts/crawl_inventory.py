#!/usr/bin/env python3
import collections
import json
import re
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from html.parser import HTMLParser
from pathlib import Path
from typing import Optional

BASE_URL = "https://www.fremontsailingclub.org/"
SITEMAP_URL = urllib.parse.urljoin(BASE_URL, "sitemap.xml")
OUTPUT_DIR = Path("migration/inventory")
USER_AGENT = "Mozilla/5.0 (compatible; FSCMigrationInventory/1.0; +https://github.com/fscassistantopenclaw/fremont-sailing-club-website)"
ASSET_EXTENSIONS = {
    ".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg", ".ico",
    ".pdf", ".doc", ".docx", ".xls", ".xlsx", ".csv", ".txt",
    ".mp4", ".mov", ".mp3", ".wav", ".zip", ".css", ".js", ".xml"
}
HTML_EXTENSIONS = {"", ".html", ".htm"}


def fetch_text(url: str) -> str:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=30) as response:
        charset = response.headers.get_content_charset() or "utf-8"
        return response.read().decode(charset, errors="replace")


def normalize_url(url: str, base_url: str) -> Optional[str]:
    if not url:
        return None
    url = url.strip()
    if not url or url.startswith(("mailto:", "tel:", "javascript:", "#")):
        return None
    absolute = urllib.parse.urljoin(base_url, url)
    parsed = urllib.parse.urlparse(absolute)
    if parsed.scheme not in {"http", "https"}:
        return None
    normalized = parsed._replace(fragment="")
    return urllib.parse.urlunparse(normalized)


def path_ext(url: str) -> str:
    return Path(urllib.parse.urlparse(url).path).suffix.lower()


def is_internal(url: str) -> bool:
    return urllib.parse.urlparse(url).netloc == urllib.parse.urlparse(BASE_URL).netloc


def is_html_page(url: str) -> bool:
    parsed = urllib.parse.urlparse(url)
    if not is_internal(url):
        return False
    if parsed.query:
        return False
    ext = path_ext(url)
    return ext in HTML_EXTENSIONS


def classify_page(url: str) -> str:
    slug = Path(urllib.parse.urlparse(url).path).name or "index.html"
    slug = slug.lower()
    if slug in {"", "index.html"}:
        return "home"
    if re.fullmatch(r"\d{4}\.html", slug):
        return "year-archive"
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}\.html", slug):
        return "dated-post"
    if re.fullmatch(r"\d{4}-\d{2}\.html", slug):
        return "monthly-post"
    if "gallery" in slug or "slideshow" in slug or slug == "photos.html":
        return "gallery"
    if "calendar" in slug:
        return "calendar"
    if any(token in slug for token in ["series-day", "overall", "results", "instructions"]):
        return "racing"
    if slug in {"membership.html", "fleets.html", "contacts.html", "windjammer-newsletter.html", "commodores-comments.html"}:
        return "core-info"
    if slug in {"lido.html", "el-toro.html"}:
        return "fleet-page"
    return "general"


@dataclass
class PageData:
    url: str
    title: str = ""
    h1: str = ""
    anchors: list = field(default_factory=list)
    images: set = field(default_factory=set)
    stylesheets: set = field(default_factory=set)
    scripts: set = field(default_factory=set)
    iframes: set = field(default_factory=set)
    forms: list = field(default_factory=list)
    assets: set = field(default_factory=set)
    external_links: set = field(default_factory=set)
    text_samples: list = field(default_factory=list)
    page_type: str = "general"


class InventoryParser(HTMLParser):
    def __init__(self, page_url: str):
        super().__init__(convert_charrefs=True)
        self.page_url = page_url
        self.data = PageData(url=page_url, page_type=classify_page(page_url))
        self._in_title = False
        self._in_h1 = False
        self._current_anchor = None
        self._ignore_text_depth = 0

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag in {"script", "style", "noscript"}:
            self._ignore_text_depth += 1
        if tag == "title":
            self._in_title = True
        elif tag == "h1":
            self._in_h1 = True
        elif tag == "a":
            href = normalize_url(attrs.get("href", ""), self.page_url)
            self._current_anchor = {"href": href, "text": ""}
        elif tag == "img":
            src = normalize_url(attrs.get("src", ""), self.page_url)
            if src:
                self.data.images.add(src)
                self.data.assets.add(src)
            for candidate in attrs.get("srcset", "").split(","):
                part = candidate.strip().split(" ")[0]
                srcset_url = normalize_url(part, self.page_url)
                if srcset_url:
                    self.data.images.add(srcset_url)
                    self.data.assets.add(srcset_url)
        elif tag == "link":
            href = normalize_url(attrs.get("href", ""), self.page_url)
            if href:
                rel = attrs.get("rel", "")
                if "stylesheet" in rel:
                    self.data.stylesheets.add(href)
                self.data.assets.add(href)
        elif tag == "script":
            src = normalize_url(attrs.get("src", ""), self.page_url)
            if src:
                self.data.scripts.add(src)
                self.data.assets.add(src)
        elif tag == "iframe":
            src = normalize_url(attrs.get("src", ""), self.page_url)
            if src:
                self.data.iframes.add(src)
        elif tag == "form":
            action = normalize_url(attrs.get("action", self.page_url), self.page_url)
            self.data.forms.append({
                "action": action,
                "method": (attrs.get("method") or "get").lower(),
            })
        elif tag in {"source", "video", "audio"}:
            src = normalize_url(attrs.get("src", ""), self.page_url)
            if src:
                self.data.assets.add(src)

    def handle_endtag(self, tag):
        if tag in {"script", "style", "noscript"} and self._ignore_text_depth:
            self._ignore_text_depth -= 1
        if tag == "title":
            self._in_title = False
        elif tag == "h1":
            self._in_h1 = False
        elif tag == "a" and self._current_anchor:
            text = re.sub(r"\s+", " ", self._current_anchor["text"]).strip()
            href = self._current_anchor["href"]
            if href:
                self.data.anchors.append({"href": href, "text": text})
                if not is_internal(href):
                    self.data.external_links.add(href)
                elif path_ext(href) in ASSET_EXTENSIONS and not is_html_page(href):
                    self.data.assets.add(href)
            self._current_anchor = None

    def handle_data(self, data):
        if self._ignore_text_depth:
            return
        if self._in_title:
            self.data.title += data
        if self._in_h1:
            self.data.h1 += data
        if self._current_anchor is not None:
            self._current_anchor["text"] += data
        stripped = re.sub(r"\s+", " ", data).strip()
        if stripped and len(stripped) > 30 and len(self.data.text_samples) < 5:
            self.data.text_samples.append(stripped)


def parse_page(url: str, html: str) -> PageData:
    parser = InventoryParser(url)
    parser.feed(html)
    data = parser.data
    data.title = re.sub(r"\s+", " ", data.title).strip()
    data.h1 = re.sub(r"\s+", " ", data.h1).strip()
    return data


def parse_sitemap() -> list[str]:
    xml_text = fetch_text(SITEMAP_URL)
    root = ET.fromstring(xml_text)
    namespace = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    urls = [node.text.strip() for node in root.findall("sm:url/sm:loc", namespace) if node.text]
    urls = sorted(set(urls))
    if urllib.parse.urljoin(BASE_URL, "index.html") not in urls:
        urls.insert(0, urllib.parse.urljoin(BASE_URL, "index.html"))
    return urls


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    page_urls = parse_sitemap()
    pages = []
    common_links = collections.Counter()
    link_presence = collections.defaultdict(set)
    asset_counter = collections.Counter()
    external_domains = collections.Counter()
    risky_pages = []

    for idx, url in enumerate(page_urls, start=1):
        try:
            html = fetch_text(url)
            page = parse_page(url, html)
            pages.append(page)
            for anchor in page.anchors:
                if anchor["href"] and is_internal(anchor["href"]) and is_html_page(anchor["href"]):
                    key = (anchor["text"], anchor["href"])
                    common_links[key] += 1
                    link_presence[key].add(page.url)
            for asset in sorted(page.assets | page.images | page.stylesheets | page.scripts):
                asset_counter[asset] += 1
            for external in page.external_links | page.iframes | page.scripts:
                if not is_internal(external):
                    external_domains[urllib.parse.urlparse(external).netloc] += 1
            if page.forms or page.iframes or any(not is_internal(s) for s in page.scripts) or any(not is_internal(a) for a in page.assets):
                risky_pages.append(page)
            if idx % 25 == 0:
                time.sleep(0.5)
        except Exception as exc:
            pages.append(PageData(url=url, title=f"ERROR: {exc}", page_type=classify_page(url)))

    homepage = next((p for p in pages if p.url.endswith("index.html") or p.url == BASE_URL), None)
    homepage_links = []
    if homepage:
        seen = set()
        for anchor in homepage.anchors:
            href = anchor["href"]
            text = anchor["text"]
            if not href or not text or not is_internal(href) or not is_html_page(href):
                continue
            key = (text, href)
            if key in seen:
                continue
            seen.add(key)
            homepage_links.append({
                "text": text,
                "url": href,
                "present_on_pages": len(link_presence.get(key, set()))
            })

    likely_nav = [
        item for item in homepage_links
        if item["present_on_pages"] >= max(8, int(len(pages) * 0.2))
    ]

    page_type_counts = collections.Counter(page.page_type for page in pages)
    asset_types = collections.Counter(path_ext(url) or "(no-ext)" for url in asset_counter)

    payload = {
        "base_url": BASE_URL,
        "page_count": len(pages),
        "asset_count": len(asset_counter),
        "pages": [
            {
                "url": page.url,
                "slug": Path(urllib.parse.urlparse(page.url).path).name or "index.html",
                "title": page.title,
                "h1": page.h1,
                "page_type": page.page_type,
                "internal_link_count": len({a['href'] for a in page.anchors if a['href'] and is_internal(a['href'])}),
                "external_link_count": len(page.external_links),
                "image_count": len(page.images),
                "script_count": len(page.scripts),
                "iframe_count": len(page.iframes),
                "form_count": len(page.forms),
            }
            for page in pages
        ],
        "page_type_counts": dict(page_type_counts),
        "assets": [
            {
                "url": asset,
                "type": path_ext(asset) or "(no-ext)",
                "referenced_by_pages": count,
                "domain": urllib.parse.urlparse(asset).netloc,
            }
            for asset, count in sorted(asset_counter.items(), key=lambda item: (-item[1], item[0]))
        ],
        "asset_type_counts": dict(asset_types),
        "likely_navigation": likely_nav,
        "homepage_common_links": homepage_links,
        "external_dependencies": [
            {"domain": domain, "references": count}
            for domain, count in external_domains.most_common()
        ],
        "risky_pages": [
            {
                "url": page.url,
                "forms": page.forms,
                "iframes": sorted(page.iframes),
                "external_links": sorted(page.external_links)[:10],
                "external_scripts": sorted([s for s in page.scripts if not is_internal(s)]),
            }
            for page in risky_pages
        ],
    }

    (OUTPUT_DIR / "site-inventory.json").write_text(json.dumps(payload, indent=2), encoding="utf-8")

    lines = []
    lines.append(f"# Fremont Sailing Club site inventory\n")
    lines.append(f"- Base URL: {BASE_URL}")
    lines.append(f"- Pages in sitemap: {len(pages)}")
    lines.append(f"- Unique referenced assets: {len(asset_counter)}")
    lines.append("")
    lines.append("## Page types")
    for page_type, count in sorted(page_type_counts.items(), key=lambda item: (-item[1], item[0])):
        lines.append(f"- {page_type}: {count}")
    lines.append("")
    lines.append("## Likely global navigation (derived from homepage links reused across many pages)")
    for item in likely_nav:
        lines.append(f"- {item['text']} -> {item['url']} (seen on {item['present_on_pages']} pages)")
    lines.append("")
    lines.append("## Top asset types")
    for ext, count in sorted(asset_types.items(), key=lambda item: (-item[1], item[0]))[:12]:
        lines.append(f"- {ext}: {count}")
    lines.append("")
    lines.append("## Top external dependencies")
    for item in payload["external_dependencies"][:20]:
        lines.append(f"- {item['domain']}: {item['references']} references")
    lines.append("")
    lines.append("## Sample pages")
    for page in payload["pages"][:25]:
        label = page['h1'] or page['title'] or page['slug']
        lines.append(f"- {page['slug']} [{page['page_type']}] - {label}")
    lines.append("")
    lines.append("## Risky pages with forms, embeds, or external scripts")
    for item in payload["risky_pages"][:50]:
        flags = []
        if item["forms"]:
            flags.append(f"forms={len(item['forms'])}")
        if item["iframes"]:
            flags.append(f"iframes={len(item['iframes'])}")
        if item["external_scripts"]:
            flags.append(f"external_scripts={len(item['external_scripts'])}")
        lines.append(f"- {item['url']} ({', '.join(flags)})")
    (OUTPUT_DIR / "site-inventory-summary.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
