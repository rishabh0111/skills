---
name: sk-reading-pdf
description: Converts a Markdown file, such as book notes, into one PDF that reads well on a phone, Kindle or other e-reader, tablet or computer. Use when the user asks for a PDF of a Markdown file or notes, or wants to read them on another device; the sk-book-notes skill hands its file here.
---

# Reading PDF

A PDF does not reflow: viewers scale each page to the screen. So readability rests on the type's size relative to the page, not its printed size. This skill makes one PDF on an A6 page, the standard pocket-book size in the ISO paper shape, with type that gives about 43 characters a line. A 6-inch e-reader shows it near printed size, a phone near the size of web text, and a tablet or computer larger.

## 1. Make the PDF

Run the converter on the Markdown file:

```
python "<this skill's folder>/make_pdf.py" "<file.md>"
```

It writes `<file>.pdf` next to the source. Add `--out-dir` to write elsewhere, and `--lang` with the text's language code when it is not English, so words hyphenate correctly.

It needs Python-Markdown (`python -m pip install markdown`) and Chrome or Edge; set `CHROME_PATH` if the browser is somewhere unusual. A Mermaid diagram is drawn from the internet at conversion time; offline, it prints as plain text.

What the converter handles, so the source needs no changes:

- **Type for screens**: a screen-made serif for reading, black on white for e-ink, ragged right with hyphenation, slim margins, generous line spacing.
- **Page flow**: each `##` section starts a new page, no heading or lead-in line is left at the foot of a page, and no list item, quote or diagram is split across pages.
- **Navigation**: a contents page whose entries are links, PDF bookmarks for the side panel, and page numbers.
- **Review prompts**: each run of `question :: answer` lines becomes a numbered list of questions, with the answers on the following page, so the reader recalls before turning.
- **Overflow**: code, tables and images wrap or scale to the page width.

Done when: the command prints the PDF's path, page size and page count.

## 2. Check the result

Open the first pages, a page with a list or diagram, and a review page, and look at them. The text fits the width, nothing is cut at the margins, lists are set as lists, and each block of answers starts on its own page. A fault here is a fault in `make_pdf.py`: fix it there, so every later file benefits, and run the converter again.

Done when: every opened page reads cleanly.

## 3. Hand over

Reply with the PDF's path. For a Kindle, send it as a PDF, so the page layout is kept.
