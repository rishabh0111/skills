"""Convert a Markdown file into one PDF that reads well on any screen.

Usage:
    python make_pdf.py NOTES.md [--out-dir DIR] [--lang en] [--keep-html]

The page is A6, the standard pocket-book size in the ISO 1:sqrt(2) shape.
Viewers scale a page to the screen, so readability rests on the type's size
relative to the page: about 43 characters a line, which a 6-inch e-reader shows
near printed size, a phone near the size of web text, and a tablet larger.
Needs Python-Markdown (pip install markdown) and Chrome or Edge.
"""

import argparse
import html
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

try:
    import markdown
except ImportError:
    sys.exit("Python-Markdown is missing: run  python -m pip install markdown")

# One layout for every screen: A6, slim margins because devices add their own
# bezel, and body type giving about 43 characters a line.
LAYOUT = {
    "size": "105mm 148mm",  # A6; Chrome does not know the name "A6"
    "margin": "8mm 7mm 10mm 7mm",
    "body": "12pt",
}

CSS = """
@page {
  size: %(size)s;
  margin: %(margin)s;
  @bottom-center { content: counter(page); font: 8pt "Segoe UI", Arial, sans-serif; color: #000; }
}
@page :first { @bottom-center { content: none; } }

html { font-size: %(body)s; }
body {
  margin: 0; background: #fff; color: #000;
  font-family: Georgia, Cambria, "Times New Roman", serif;
  line-height: 1.45; text-align: left;
  hyphens: auto; -webkit-hyphens: auto;
  overflow-wrap: break-word; font-kerning: normal;
  orphans: 2; widows: 2;
}

h1, h2, h3, h4, .answers-title, nav.toc {
  font-family: "Segoe UI", Arial, sans-serif;
  hyphens: manual; -webkit-hyphens: manual;
}
h1, h2, h3, h4 { line-height: 1.2; break-after: avoid; text-wrap: balance; }
h1 { font-size: 1.9em; margin: 0 0 .35em; }
h1 + p { font-family: "Segoe UI", Arial, sans-serif; font-size: .8em; margin-bottom: 1.4em; }
h2 { font-size: 1.4em; margin: 0 0 .5em; break-before: page; }
h3 { font-size: 1.12em; margin: 1.3em 0 .35em; }
h4 { font-size: 1em; margin: 1em 0 .3em; }

p { margin: 0 0 .65em; }
ul, ol { margin: 0 0 .65em; padding-left: 1.35em; }
ol { padding-left: 2em; }
p:has(+ ol), p:has(+ ul), p:has(+ .mermaid), p:has(+ pre), p:has(+ table) { break-after: avoid; }
h2 + p { font-style: italic; }
li { margin: .2em 0; }
li, blockquote, pre, .mermaid, img, tr { break-inside: avoid; }
thead { display: table-header-group; }
strong { font-weight: 700; }
a { color: #000; }

blockquote { margin: .7em 0; padding-left: .8em; border-left: 2px solid #000; font-style: italic; }
code { font-family: Consolas, "Courier New", monospace; font-size: .9em; }
pre { white-space: pre-wrap; overflow-wrap: anywhere; font-size: .85em; }
img, svg { max-width: 100%%; height: auto; }
table { border-collapse: collapse; width: 100%%; font-size: .85em; margin: .4em 0 .9em; }
th, td { border: 1px solid #000; padding: .2em .35em; text-align: left; vertical-align: top; }

.mermaid { margin: .8em 0; text-align: center; }
.mermaid.unrendered { white-space: pre-wrap; text-align: left; font-family: Consolas, monospace; font-size: .8em; }

nav.toc { break-before: page; font-size: .88em; line-height: 1.3; }
nav.toc h2 { break-before: avoid; }
nav.toc ol { list-style: none; padding: 0; margin: 0; }
nav.toc li { margin: .3em 0; }
nav.toc li.l2 { font-weight: 700; margin-top: .8em; }
nav.toc li.l3 { padding-left: 1em; font-weight: 400; }
nav.toc a { text-decoration: none; }

.questions li, .answers li { margin: .45em 0; }
.answers { break-before: page; }
.answers-title { font-weight: 700; font-size: .95em; margin: 0 0 .5em; }
"""

# Each diagram is rendered under its own id: headless printing freezes the clock,
# so mermaid's time-based ids would collide and draw every diagram into the first.
MERMAID = """
<script type="module">
  import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10.9.1/dist/mermaid.esm.min.mjs';
  mermaid.initialize({
    startOnLoad: false, theme: 'base', securityLevel: 'strict',
    flowchart: { htmlLabels: false, useMaxWidth: true, nodeSpacing: 22, rankSpacing: 28, padding: 14 },
    themeVariables: {
      primaryColor: '#ffffff', primaryBorderColor: '#000000', primaryTextColor: '#000000',
      lineColor: '#000000', fontFamily: 'Segoe UI, Arial, sans-serif', fontSize: '15px'
    }
  });
  const blocks = [...document.querySelectorAll('div.mermaid')];
  for (let i = 0; i < blocks.length; i++) {
    try {
      const { svg } = await mermaid.render('diagram-' + i, blocks[i].textContent);
      blocks[i].innerHTML = svg;
    } catch (e) {
      blocks[i].classList.add('unrendered');
    }
  }
</script>
"""

QA_LINE = re.compile(r"^\s*(?:[-*]\s+)?(.+?)\s+::\s+(.+?)\s*$")
FENCE = re.compile(r"^\s*(```|~~~)\s*([\w-]*)")
HEADING = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
BLOCK_START = re.compile(r"^(\d+[.)]\s|[-*+]\s|\|)")


def inline(text):
    """Render one line of Markdown without the surrounding paragraph."""
    out = markdown.markdown(text)
    return re.sub(r"^<p>(.*)</p>$", r"\1", out, flags=re.S)


def qa_block(pairs, group):
    qs = "".join(f"<li>{inline(q)}</li>" for q, _ in pairs)
    ans = "".join(f"<li>{inline(a)}</li>" for _, a in pairs)
    title = f"Answers: {html.escape(group)}" if group else "Answers"
    return (
        f'<div class="qa"><ol class="questions">{qs}</ol>'
        f'<section class="answers"><p class="answers-title">{title}</p><ol>{ans}</ol></section></div>'
    )


def preprocess(text):
    """Turn mermaid fences into diagram blocks and question :: answer lines into
    a question list followed, on a new page, by its answers."""
    out, pairs, group = [], [], ""
    lines = text.splitlines()
    i = 0

    def flush():
        if pairs:
            out.extend(["", qa_block(pairs, group), ""])
            pairs.clear()

    while i < len(lines):
        line = lines[i]
        fence = FENCE.match(line)
        if fence:
            flush()
            marker, lang = fence.group(1), fence.group(2).lower()
            body, i = [], i + 1
            while i < len(lines) and not lines[i].strip().startswith(marker):
                body.append(lines[i])
                i += 1
            i += 1
            if lang == "mermaid":
                out.extend(["", f'<div class="mermaid">{html.escape(chr(10).join(body))}</div>', ""])
            else:
                out.extend([f"{marker}{lang}", *body, marker])
            continue
        qa = QA_LINE.match(line)
        if qa:
            pairs.append((qa.group(1), qa.group(2)))
            i += 1
            continue
        if pairs and not line.strip():
            i += 1
            continue
        flush()
        heading = HEADING.match(line)
        if heading:
            group = heading.group(2)
        # A list or table written straight after a paragraph line needs a blank
        # line before it, or Markdown folds it into the paragraph.
        if BLOCK_START.match(line) and out and out[-1].strip() and not BLOCK_START.match(out[-1]) \
                and not out[-1].startswith((" ", "\t")):
            out.append("")
        # Notes are written one line per paragraph, so an unindented line after a
        # list item starts a new paragraph rather than continuing the item.
        elif line.strip() and not line.startswith((" ", "\t")) and not BLOCK_START.match(line) \
                and not HEADING.match(line) and out and BLOCK_START.match(out[-1]):
            out.append("")
        out.append(line)
        i += 1
    flush()
    return "\n".join(out)


def build_html(md_text, layout, lang):
    md = markdown.Markdown(extensions=["fenced_code", "tables", "sane_lists", "toc"])
    body = md.convert(preprocess(md_text))

    title_match = re.search(r"<h1[^>]*>(.*?)</h1>", body, re.S)
    title = re.sub(r"<[^>]+>", "", title_match.group(1)).strip() if title_match else "Notes"

    entries = re.findall(r'<h([23]) id="([^"]+)">(.*?)</h\1>', body, re.S)
    if len(entries) > 2:
        items = "".join(
            f'<li class="l{lvl}"><a href="#{hid}">{re.sub(r"<[^>]+>", "", txt)}</a></li>'
            for lvl, hid, txt in entries
        )
        toc = f'<nav class="toc"><h2>Contents</h2><ol>{items}</ol></nav>'
        first_h2 = body.find("<h2")
        body = body[:first_h2] + toc + body[first_h2:] if first_h2 >= 0 else body + toc

    mermaid = MERMAID if 'class="mermaid"' in body else ""
    return (
        f'<!doctype html><html lang="{lang}"><head><meta charset="utf-8">'
        f"<title>{html.escape(title)}</title><style>{CSS % layout}</style></head>"
        f"<body>{body}{mermaid}</body></html>"
    )


def find_browser():
    env = os.environ.get("CHROME_PATH")
    if env and Path(env).exists():
        return env
    candidates = [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
    ]
    for name in ["google-chrome", "google-chrome-stable", "chromium", "chromium-browser", "microsoft-edge"]:
        found = shutil.which(name)
        if found:
            candidates.append(found)
    for c in candidates:
        if Path(c).exists():
            return c
    sys.exit("No Chrome or Edge found; set CHROME_PATH to a Chromium-based browser.")


def print_pdf(browser, html_path, pdf_path, profile_dir):
    cmd = [
        browser, "--headless=new", "--disable-gpu", "--no-first-run", "--no-default-browser-check",
        f"--user-data-dir={profile_dir}", "--no-pdf-header-footer", "--generate-pdf-document-outline",
        "--export-tagged-pdf", "--virtual-time-budget=20000", "--run-all-compositor-stages-before-draw",
        f"--print-to-pdf={pdf_path}", html_path.as_uri(),
    ]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=180)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("source")
    ap.add_argument("--out-dir")
    ap.add_argument("--lang", default="en", help="language code, used for hyphenation")
    ap.add_argument("--keep-html", action="store_true")
    args = ap.parse_args()

    src = Path(args.source).resolve()
    out_dir = Path(args.out_dir).resolve() if args.out_dir else src.parent
    out_dir.mkdir(parents=True, exist_ok=True)
    md_text = src.read_text(encoding="utf-8")
    browser = find_browser()

    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        html_path = tmp / "notes.html"
        html_path.write_text(build_html(md_text, LAYOUT, args.lang), encoding="utf-8")
        pdf_path = out_dir / f"{src.stem}.pdf"
        print_pdf(browser, html_path, pdf_path, tmp / "chrome")
        if not pdf_path.exists() or pdf_path.stat().st_size == 0:
            sys.exit("Printing failed")
        pages = len(re.findall(rb"/Type\s*/Page[^s]", pdf_path.read_bytes()))
        if args.keep_html:
            shutil.copy(html_path, out_dir / f"{src.stem}.html")
        print(f"{pdf_path}  [{LAYOUT['size']}, {pages} pages]")


if __name__ == "__main__":
    main()
