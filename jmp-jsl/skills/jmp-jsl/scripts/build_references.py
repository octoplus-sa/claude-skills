#!/usr/bin/env python3
"""Slice the JMP JSL Syntax Reference and Scripting Guide into per-section
markdown files and build a function index.

Usage:
    build_references.py <syntax.pdf> <guide.pdf> [--out <references-dir>]

Inputs may be either .pdf (pdftotext is invoked automatically) or .txt files
already produced by `pdftotext` *without* -layout (so pages are split by \\f).

Default output dir: ~/.claude/skills/jsl/references/

This script is idempotent — re-running it overwrites the per-section files
under the output directory.
"""
import argparse, os, re, subprocess, sys, tempfile
from pathlib import Path

# ─── Section page maps (from the JMP 19 published TOCs) ─────────────────────

# Chapter 2 — Function categories. We let the heading-finder locate these
# because they all sit on their own page with a clean section heading.
SYN_FUNCTION_SECTIONS = [
    "Assignment Functions", "Character Functions", "Character Pattern Functions",
    "Comment Functions", "Comparison Functions", "Conditional and Logical Functions",
    "Constant Functions", "Date and Time Functions", "Discrete Probability Functions",
    "Display Functions", "Expression Functions", "File Functions", "Financial Functions",
    "Graphics Functions", "HTTP Functions", "List Functions",
    "MATLAB Integration Functions", "Matrix Functions", "Numeric Functions",
    "Optimization Functions", "Probability Functions", "Programming Functions",
    "Python Integration Functions", "R Integration Functions", "JMPEX R Functions",
    "Random Functions", "Row Functions", "Row State Functions", "SQL Functions",
    "Statistical Functions", "Transcendental Functions", "Trigonometric Functions",
    "Utility Functions",
]

# Chapter 3 — Message sections. Hardcoded page numbers from the TOC because
# multiple sections share starting pages and headings vary.
SYN_MESSAGES_PAGED = [
    ("Alpha Shape Messages",                376),
    ("Associative Array Messages",          376),
    ("Class Messages",                      377),
    ("Data Connector Messages",             379),
    ("Data Table Messages",                 381),
    ("Data Feed Messages",                  422),
    ("Display Box Messages",                425),
    ("Dynamic Link Library (DLL) Messages", 465),
    ("Image Messages",                      467),
    ("Interactive HTML Messages",           470),
    ("JMP Application Messages",            472),
    ("MATLAB Messages",                     475),
    ("Namespace Messages",                  478),
    ("Data Historian Import Messages",      480),
    ("Python Integration Messages",         485),
    ("R Integration Messages",              490),
    ("Schedule Messages",                   493),
    ("Sockets Messages",                    494),
    ("SQL Messages",                        497),
    ("Messages for Other Objects",          501),
]

# Scripting Guide chapters — hardcoded page list from the Guide TOC.
GUIDE_CHAPTERS_PAGED = [
    ("Introduction to Writing JSL Scripts", "introduction",          39),
    ("Get Started",                          "get-started",          51),
    ("Scripting Tools",                      "scripting-tools",      61),
    ("JSL Building Blocks",                  "building-blocks",      99),
    ("Types of Data",                        "types-of-data",       145),
    ("Data Structures",                      "data-structures",     193),
    ("Programming Methods",                  "programming-methods", 255),
    ("Data Tables",                          "data-tables",         325),
    ("Scripting Platforms",                  "scripting-platforms", 475),
    ("Display Trees",                        "display-trees",       521),
    ("Scripting Graphs",                     "scripting-graphs",    635),
    ("Three-Dimensional Scenes",             "scenes-3d",           725),
    ("Extending JMP",                        "extending-jmp",       769),
    ("Python",                               "python",              833),
    ("Creating Projects",                    "creating-projects",   855),
    ("Creating Applications",                "creating-applications", 867),
    ("Common Tasks",                         "common-tasks",        917),
    ("Compatibility Notes",                  "compatibility-notes", 931),
    ("Efficient Scripts",                    "efficient-scripts",   933),
    ("References",                           "references",          939),
    ("Scripting Guide Glossary",             "glossary",            941),
]

# ─── Helpers ─────────────────────────────────────────────────────────────────

def pdf_to_text(pdf_path):
    """Run pdftotext (without -layout) and return path to the .txt file."""
    out = Path(tempfile.mkdtemp(prefix='jsl-extract-')) / (pdf_path.stem + '.txt')
    subprocess.run(['pdftotext', str(pdf_path), str(out)], check=True,
                   stderr=subprocess.DEVNULL)
    return out

def resolve_input(p):
    p = Path(p)
    if p.suffix.lower() == '.pdf':
        print(f"[extract] {p.name}")
        return pdf_to_text(p)
    return p

def load_pages(path):
    return open(path).read().split('\f')

def slug(s):
    s = re.sub(r'[^a-zA-Z0-9 ]', '', s).lower().strip()
    return re.sub(r'\s+', '-', s)

def find_first_page(pages, title, start_from=0):
    pat = re.compile(r'^\s*' + re.escape(title) + r'\s*$', re.IGNORECASE)
    for i in range(start_from, len(pages)):
        lines = [l for l in pages[i].splitlines() if l.strip()][:6]
        for ln in lines:
            if pat.match(ln) or ln.strip().lower() == title.lower():
                return i
    return -1

def find_starts(pages, headings, search_from):
    starts, cursor = [], search_from
    for h in headings:
        idx = find_first_page(pages, h, cursor)
        if idx == -1:
            alt = h.replace(' Functions', '').replace(' Messages', '')
            idx = find_first_page(pages, alt, cursor)
        if idx == -1:
            print(f"  WARN: could not find '{h}' from page {cursor}", file=sys.stderr)
            starts.append(None)
        else:
            starts.append(idx)
            cursor = idx
    return starts

_TOC_LINE = re.compile(r'^.+\.\s\.\s\.\s\.\s.*\d+\s*$')   # "Foo Bar  . . . . . . 123"
_NEXT_CHAPTER = re.compile(r'^\s*(JSL Messages|JSL Functions, Operators, and Messages|Summary of Messages|Summary of Commands)\s*$')

def trim_trailing_toc(body: str) -> str:
    """Drop a trailing 'Contents'/next-chapter TOC bleed if present."""
    lines = body.splitlines()
    # Walk backwards from the end. If we find a 'Contents' header followed mostly
    # by TOC-style dot-leader lines, cut the body at the start of that block.
    cut_at = None
    for i, ln in enumerate(lines):
        s = ln.strip()
        if s == 'Contents' or _NEXT_CHAPTER.match(ln):
            # Look ahead: are most of the next 10 non-empty lines TOC-pattern?
            tail = [l for l in lines[i+1:i+30] if l.strip()]
            if tail and sum(1 for l in tail if _TOC_LINE.match(l)) >= max(3, len(tail)//2):
                cut_at = i
                break
    if cut_at is not None:
        # Walk back over preceding "JSL Messages" / "Summary of ..." marker lines too
        while cut_at > 0 and (
            lines[cut_at-1].strip() in {'JSL Messages', 'JSL Functions, Operators, and Messages'}
            or _NEXT_CHAPTER.match(lines[cut_at-1])
        ):
            cut_at -= 1
        lines = lines[:cut_at]
    return '\n'.join(lines).rstrip()

# Heuristics for spotting a function/message entry header. We treat as an entry:
#   - lines that begin a JSL function call: `FunctionName(...)` or `FunctionName()`
#   - message-form lines: `obj << Message Name(...)` or `obj << Message Name`
# We then build a per-file index showing each entry's line number in the rendered .md.
_ENTRY_FUNC = re.compile(r'^([A-Z][A-Za-z0-9 ]{0,40}?)\s*\(')
_ENTRY_MSG  = re.compile(r'^[a-z][a-zA-Z0-9_]*\s*<<\s*([A-Z][A-Za-z0-9 ]{0,60}?)(?:\s*\(|\s*$)')

def build_file_index(body: str) -> str:
    """Return a markdown bulleted list of every entry name in this body, with the
    line number it appears at *within the rendered file* (1-based, after the
    fixed front-matter prefix)."""
    seen = {}
    for i, ln in enumerate(body.splitlines(), start=1):
        s = ln.strip()
        if not s:
            continue
        m = _ENTRY_FUNC.match(s)
        if m:
            name = m.group(1).strip()
            words = name.split()
            if len(name) > 40 or len(words) > 6:
                continue
            if any(w[0].islower() for w in words):
                continue
            if len(words) == 1 and name.isupper() and len(name) > 6:
                continue
            if name in {'A', 'An', 'The', 'For', 'If', 'Note', 'Tip', 'Use', 'Returns',
                        'Required', 'Optional', 'See', 'Example', 'Examples',
                        'Description', 'When', 'This', 'These', 'In', 'On', 'By',
                        'With', 'Using', 'Without', 'Where', 'Here', 'Then', 'Else',
                        'Both', 'Each', 'Either', 'Some', 'All', 'Any', 'Most',
                        'Not', 'Such', 'Only', 'Just', 'Contents'}:
                continue
            seen.setdefault(name + '()', i)
            continue
        m = _ENTRY_MSG.match(s)
        if m:
            name = '<< ' + m.group(1).strip()
            seen.setdefault(name, i)
    if not seen:
        return ''
    lines = ['## Index (line numbers in this file)', '']
    for name in sorted(seen):
        lines.append(f"- `{name}` — L{seen[name]}")
    lines.append('')
    return '\n'.join(lines)

def write_section(out_path, heading, pages, page_range, source_label):
    body = '\n\n'.join(pages[page_range[0]:page_range[1]])
    body = re.sub(r'^\s*(JSL Syntax Reference|Scripting Guide)\s*$', '', body, flags=re.M)
    body = re.sub(r'^\s*Chapter \d+\s*$', '', body, flags=re.M)
    body = re.sub(r'^\s*\d{1,4}\s+(Chapter|JSL Syntax Reference|Scripting Guide|Contents|JSL Functions, Operators, and Messages|JSL Messages)\s*$', '', body, flags=re.M)
    body = re.sub(r'\n{3,}', '\n\n', body).strip()
    body = trim_trailing_toc(body)

    # Compose the file: front matter, body, then we go back and prepend an index
    # whose line numbers match the *rendered* body. We do this in two passes:
    # first compute the body's start line, then compute index from body, then write.
    front = f"# {heading}\n\nSource: {source_label} (PDF pages {page_range[0]+1}-{page_range[1]}).\n\n"
    raw_index = build_file_index(body)
    if raw_index:
        # Normalize index to the canonical form we'll actually write — splitlines+join
        # drops any trailing newline, so the count we compute here matches the file.
        index_lines = raw_index.splitlines()
        # Compute the line number where body L1 will land in the final file.
        # File layout: [front lines] + [index_lines] + ["---", ""] + body…
        # body L1 file_line = (front lines) + (index_lines count) + 2 + 1
        front_line_count = front.count('\n')   # front ends with '\n', so count==num of lines
        body_l1_file_line = front_line_count + len(index_lines) + 2 + 1
        shift = body_l1_file_line - 1   # so body L_N maps to file L (N + shift)
        shifted = []
        for ln in index_lines:
            m = re.match(r'^(- `[^`]+` — L)(\d+)$', ln)
            shifted.append(f"{m.group(1)}{int(m.group(2)) + shift}" if m else ln)
        out_path.write_text(front + '\n'.join(shifted) + '\n---\n\n' + body + '\n')
    else:
        out_path.write_text(front + '---\n\n' + body + '\n')

# ─── Main pipeline ───────────────────────────────────────────────────────────

def run(syntax_txt, guide_txt, out_dir):
    syn_out = out_dir / 'syntax'
    guide_out = out_dir / 'guide'
    syn_out.mkdir(parents=True, exist_ok=True)
    guide_out.mkdir(parents=True, exist_ok=True)

    # ─── Syntax reference: function sections ─────────────────────────────
    syn_pages = load_pages(syntax_txt)
    print("[syntax] locating function sections...")
    syn_func_starts = find_starts(syn_pages, SYN_FUNCTION_SECTIONS, 20)
    sql_appendix = find_first_page(syn_pages, "SQL Functions Available for JMP Queries", 450)
    if sql_appendix == -1:
        sql_appendix = len(syn_pages) - 5

    syn_msg_starts = [p - 1 for _, p in SYN_MESSAGES_PAGED]
    SYN_MESSAGES = [t for t, _ in SYN_MESSAGES_PAGED]

    # Build (heading, start, end) ranges for function sections
    func_ranges = []
    n = len(SYN_FUNCTION_SECTIONS)
    for i, (h, s) in enumerate(zip(SYN_FUNCTION_SECTIONS, syn_func_starts)):
        if s is None:
            continue
        e = syn_msg_starts[0] if syn_msg_starts else sql_appendix
        for j in range(i+1, n):
            if syn_func_starts[j] is not None:
                e = syn_func_starts[j]
                break
        func_ranges.append((h, s, e))

    # Message ranges
    msg_ranges = []
    for i, (h, s) in enumerate(zip(SYN_MESSAGES, syn_msg_starts)):
        e = sql_appendix
        for j in range(i+1, len(SYN_MESSAGES)):
            if syn_msg_starts[j] > s:
                e = syn_msg_starts[j]
                break
        # If two consecutive sections share a start page (e.g. Alpha Shape and
        # Associative Array on p.376), give the first a 1-page slice and let
        # the second cover from there.
        if e <= s:
            e = s + 1
        msg_ranges.append((h, s, e))

    # Write syntax-reference sections
    syn_index_rows = []
    print("[syntax] writing function sections...")
    for h, s, e in func_ranges:
        f = syn_out / f"{slug(h)}.md"
        write_section(f, h, syn_pages, (s, e), "JMP 19 JSL Syntax Reference")
        syn_index_rows.append((h, s+1, e, 'function'))

    print("[syntax] writing message sections...")
    for h, s, e in msg_ranges:
        f = syn_out / f"messages-{slug(h)}.md"
        write_section(f, h, syn_pages, (s, e), "JMP 19 JSL Syntax Reference")
        syn_index_rows.append((h, s+1, e, 'message'))

    # ─── Scripting Guide chapters ────────────────────────────────────────
    guide_pages = load_pages(guide_txt)
    print("[guide] slicing chapters...")
    guide_index_rows = []
    n = len(GUIDE_CHAPTERS_PAGED)
    for i, (title, slug_id, page_start) in enumerate(GUIDE_CHAPTERS_PAGED):
        s = page_start - 1
        e = GUIDE_CHAPTERS_PAGED[i+1][2] - 1 if i + 1 < n else len(guide_pages)
        f = guide_out / f"{slug_id}.md"
        write_section(f, title, guide_pages, (s, e), "JMP 19 Scripting Guide")
        guide_index_rows.append((title, slug_id, s+1, e))

    # ─── Function index ──────────────────────────────────────────────────
    print("[index] extracting function names from syntax reference...")
    func_names = {}
    fname_pat = re.compile(r'^([A-Z][A-Za-z0-9 ]{0,40}?)\s*\(')
    for h, s, e in func_ranges:
        for pi in range(s, e):
            for ln in syn_pages[pi].splitlines():
                ln = ln.strip()
                m = fname_pat.match(ln)
                if not m:
                    continue
                name = m.group(1).strip()
                words = name.split()
                if len(name) > 40 or len(words) > 6:
                    continue
                if any(w[0].islower() for w in words):
                    continue  # sentence fragment, not a function name
                if len(words) == 1 and name.isupper() and len(name) > 6:
                    continue
                if name in {'A', 'An', 'The', 'For', 'If', 'Note', 'Tip', 'Use', 'Returns',
                            'Required', 'Optional', 'See', 'Example', 'Examples',
                            'Description', 'When', 'This', 'These', 'In', 'On', 'By',
                            'With', 'Using', 'Without', 'Where', 'Here', 'Then', 'Else',
                            'Both', 'Each', 'Either', 'Some', 'All', 'Any', 'Most',
                            'Not', 'Such', 'Only', 'Just'}:
                    continue
                if name not in func_names:
                    func_names[name] = (h, pi+1)

    print(f"[index] collected {len(func_names)} function entries")

    by_section = {}
    for name, (sec, page) in sorted(func_names.items()):
        by_section.setdefault(sec, []).append((name, page))

    with open(out_dir / 'function-index.md', 'w') as f:
        f.write("# JSL Function Index\n\n")
        f.write("Flat alphabetical index of JSL functions extracted from the JMP 19 JSL "
                "Syntax Reference. Each entry shows the category and PDF page where the "
                "function is documented. For full signatures + descriptions, open the "
                "matching `syntax/<category>.md` file.\n\n")
        f.write("**How to use this file:** grep here first for any function name. If "
                "found, jump to the per-category file for full docs. If not found, the "
                "function may be a message (see `syntax/messages-*.md`) or may not exist "
                "— treat \"not found here\" as a strong red flag against using it.\n\n---\n\n")
        for sec in sorted(by_section):
            f.write(f"## {sec}\n\nFile: `syntax/{slug(sec)}.md`\n\n")
            for name, page in sorted(by_section[sec]):
                f.write(f"- `{name}()` — p.{page}\n")
            f.write("\n")

    # ─── Master index ────────────────────────────────────────────────────
    with open(out_dir / 'index.md', 'w') as f:
        f.write("# JSL References — Index\n\n"
                "Per-section markdown extracted from the JMP 19 JSL Syntax Reference and "
                "Scripting Guide. These are greppable, cheap to load, and replace the "
                "original PDFs as the primary lookup path.\n\n")
        f.write("## Quick lookup\n\n")
        f.write("- **Looking up a function name?** → grep `references/function-index.md` first.\n")
        f.write("- **Looking up a message (e.g., `<< Get Items`)?** → see `references/syntax/messages-*.md`.\n")
        f.write("- **How does X work conceptually (scoping, namespaces, display boxes)?** → see `references/guide/<topic>.md`.\n")
        f.write("- **Want runnable examples?** → online Scripting Index at `https://jsl.jmp.com/`, or the offline mirror under `references/scripting-index/` if it has been built.\n\n---\n\n")
        f.write("## Syntax Reference — Function categories\n\n")
        for h, s, e, kind in syn_index_rows:
            if kind == 'function':
                f.write(f"- [{h}](syntax/{slug(h)}.md) — pp.{s}-{e}\n")
        f.write("\n## Syntax Reference — Object / display-box messages\n\n")
        for h, s, e, kind in syn_index_rows:
            if kind == 'message':
                f.write(f"- [{h}](syntax/messages-{slug(h)}.md) — pp.{s}-{e}\n")
        f.write("\n## Scripting Guide — Conceptual chapters\n\n")
        for title, slug_id, s, e in guide_index_rows:
            f.write(f"- [{title}](guide/{slug_id}.md) — pp.{s}-{e}\n")
        f.write("\n## Function index\n\n")
        f.write("- [function-index.md](function-index.md) — flat list of all JSL functions, alphabetical by category\n")
        f.write("\n---\n\n"
                "Generated from `jsl-syntax-reference.pdf` and `scripting-guide.pdf` via "
                "`scripts/fetch_docs.sh` + `scripts/build_references.py`. The source PDFs "
                "are not kept in this skill — they are downloaded, extracted, and deleted "
                "by `fetch_docs.sh`. To re-extract, just rerun `fetch_docs.sh`.\n")

    print()
    print("[done]")
    print(f"  syntax sections: {sum(1 for _,_,_,k in syn_index_rows if k=='function')} function "
          f"+ {sum(1 for _,_,_,k in syn_index_rows if k=='message')} message")
    print(f"  guide chapters:  {len(guide_index_rows)}")
    print(f"  function index:  {len(func_names)} entries")

def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('syntax', help='Path to jsl-syntax-reference (.pdf or .txt)')
    ap.add_argument('guide',  help='Path to scripting-guide (.pdf or .txt)')
    ap.add_argument('--out', default=str(Path.home() / '.claude' / 'skills' / 'jsl' / 'references'),
                    help='Output references directory')
    args = ap.parse_args()
    return run(resolve_input(args.syntax), resolve_input(args.guide), Path(args.out))

if __name__ == '__main__':
    main()
