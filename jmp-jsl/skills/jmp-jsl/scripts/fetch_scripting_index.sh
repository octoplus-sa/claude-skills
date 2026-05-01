#!/usr/bin/env bash
# fetch_scripting_index.sh — mirror the JMP online Scripting Index
# (https://jsl.jmp.com/) into the skill's references/ directory as
# searchable markdown. Each function/box/message gets its own .md file
# with runnable example snippets.
#
# Requires: curl, pandoc
# Usage:    bash scripts/fetch_scripting_index.sh

set -euo pipefail

SKILL_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT_DIR="${SKILL_ROOT}/references/scripting-index"
TMP_DIR="$(mktemp -d -t jsl-scrindex-XXXXX)"
BASE="https://jsl.jmp.com"

trap 'rm -rf "${TMP_DIR}"' EXIT

mkdir -p "${OUT_DIR}"
echo "Mirroring ${BASE} into ${OUT_DIR}"
echo "(temp scratch: ${TMP_DIR})"

# 1. Pull the home page to extract the full nav of .html links.
echo "[fetch] home page"
curl -fsS -A "Mozilla/5.0" "${BASE}/" -o "${TMP_DIR}/index.html"

# 2. Extract every internal .html link (these are nav targets).
grep -oE 'href="[^"]+\.html[^"]*"' "${TMP_DIR}/index.html" \
  | sed -E 's/href="//; s/"$//; s/#.*$//' \
  | grep -v '^http' \
  | sort -u > "${TMP_DIR}/pages.txt"

TOTAL=$(wc -l < "${TMP_DIR}/pages.txt")
echo "[fetch] ${TOTAL} pages discovered"

# 3. Fetch each page in parallel (8 at a time).
mkdir -p "${TMP_DIR}/html"
fetch_page() {
    local rel="$1"
    local enc_rel
    # The hrefs are already URL-encoded (e.g., "All%20Categories/...").
    enc_rel="${rel}"
    local local_path="${TMP_DIR}/html/${rel}"
    mkdir -p "$(dirname "${local_path}")"
    curl -fsS -A "Mozilla/5.0" "${BASE}/${enc_rel}" -o "${local_path}" || true
}
export -f fetch_page
export BASE TMP_DIR

xargs -a "${TMP_DIR}/pages.txt" -I{} -P 8 bash -c 'fetch_page "$@"' _ {}
echo "[fetch] HTML downloaded"

# 4. Convert each HTML file to markdown via pandoc.
#    We extract just the main content section (#main-content, .wy-nav-content)
#    and feed it to pandoc with --from html --to gfm.
echo "[convert] pandoc HTML -> markdown"
CONVERTED=0
FAILED=0
while read -r rel; do
    [ -z "${rel}" ] && continue
    # Skip the JSL home page — it's just a welcome banner with one nav link,
    # and we want the slot for our generated flat lookup (also "index.md").
    [ "${rel}" = "index.html" ] && continue
    src="${TMP_DIR}/html/${rel}"
    [ -f "${src}" ] || { FAILED=$((FAILED+1)); continue; }

    # MkDocs renders content inside <div role="main"> ... </div>.
    # Use python to slice out that subtree, then pandoc it.
    extracted="$(python3 -c '
import sys, re
html = open(sys.argv[1]).read()
m = re.search(r"<div[^>]+role=\"main\"[^>]*>(.*?)</div>\s*</section>", html, re.S)
if not m:
    m = re.search(r"<div[^>]+itemprop=\"articleBody\"[^>]*>(.*?)</div>", html, re.S)
print(m.group(1) if m else html)
' "${src}")"

    # Decode URL-encoded path segments for the output file path.
    decoded_rel="$(printf '%b' "${rel//%/\\x}")"
    out_md="${OUT_DIR}/${decoded_rel%.html}.md"
    mkdir -p "$(dirname "${out_md}")"

    # Pandoc: HTML -> GitHub-flavored markdown, no wrapping.
    {
        # Title from the URL stem
        stem="$(basename "${decoded_rel%.html}")"
        printf "# %s\n\n*Source: [%s](%s/%s)*\n\n---\n\n" \
            "${stem}" "${BASE}/${rel}" "${BASE}" "${rel}"
        printf '%s' "${extracted}" \
            | pandoc --from html --to gfm-raw_html --wrap=none 2>/dev/null \
            || printf '%s' "${extracted}"
    } > "${out_md}"
    CONVERTED=$((CONVERTED+1))
done < "${TMP_DIR}/pages.txt"

echo "[convert] ${CONVERTED} converted, ${FAILED} failed"

# 5. Build a flat alphabetical index of every page.
INDEX="${OUT_DIR}/index.md"
{
    echo "# JMP Scripting Index — offline mirror"
    echo
    echo "Markdown mirror of <https://jsl.jmp.com/>."
    echo "Each entry below is a JSL function, display box, message, or category overview"
    echo "with the official runnable example. Greppable; cheap to load."
    echo
    echo "**Lookup tip:** if you're searching for a specific function or message,"
    echo "grep this file for the name, then open the linked file."
    echo
    echo "---"
    echo
    find "${OUT_DIR}" -type f -name '*.md' -not -name 'index.md' \
        | sed "s|^${OUT_DIR}/||" \
        | sort \
        | awk -F/ '{
            cat=""; for(i=1;i<NF;i++) cat = cat (i>1?" / ":"") $i;
            stem=$NF; sub(/\.md$/, "", stem);
            printf "- [`%s`](%s) — %s\n", stem, $0 "::" stem, cat
        }' \
        | sed 's|::[^)]*||'
} > "${INDEX}"

echo "[done] ${OUT_DIR}"
echo "       index: ${INDEX}"
du -sh "${OUT_DIR}"
