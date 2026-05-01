#!/usr/bin/env bash
# fetch_docs.sh — download the JMP 19 JSL reference PDFs, extract them into
# searchable per-section markdown under references/, then delete the PDFs.
#
# This is the canonical way to (re)build the offline reference set. The PDFs
# are large and not directly grep-able by an LLM; the markdown derivatives are.
#
# Optional second step: also mirror the online JMP Scripting Index
# (https://jsl.jmp.com/) into references/scripting-index/ as runnable-example
# markdown. This is a separate script (`fetch_scripting_index.sh`) that you
# can invoke from here with `--with-index`.
#
# Requires: curl OR wget; pdftotext (poppler-utils); python3.
# Optional: pandoc (only if you also want the online Scripting Index mirror).
#
# Usage:
#   bash scripts/fetch_docs.sh                # PDFs -> markdown, then drop PDFs
#   bash scripts/fetch_docs.sh --keep-pdfs    # also keep the original PDFs
#   bash scripts/fetch_docs.sh --with-index   # also fetch the online index

set -euo pipefail

SKILL_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
REF_DIR="${SKILL_ROOT}/references"
SCRATCH="$(mktemp -d -t jsl-fetch-XXXXX)"

KEEP_PDFS=0
WITH_INDEX=0
for arg in "$@"; do
    case "${arg}" in
        --keep-pdfs)  KEEP_PDFS=1 ;;
        --with-index) WITH_INDEX=1 ;;
        *) echo "unknown option: ${arg}" >&2; exit 2 ;;
    esac
done

trap 'rm -rf "${SCRATCH}"' EXIT
mkdir -p "${REF_DIR}"

SYNTAX_URL="https://www.jmp.com/content/dam/jmp/documents/en/support/jmp19/jsl-syntax-reference.pdf"
GUIDE_URL="https://www.jmp.com/content/dam/jmp/documents/en/support/jmp19/scripting-guide.pdf"
SYNTAX_PDF="${SCRATCH}/jsl-syntax-reference.pdf"
GUIDE_PDF="${SCRATCH}/scripting-guide.pdf"

download() {
    local url="$1"
    local out="$2"
    echo "  [get]  ${url}"
    if command -v curl >/dev/null 2>&1; then
        curl -fL --progress-bar -o "${out}" "${url}"
    elif command -v wget >/dev/null 2>&1; then
        wget -q --show-progress -O "${out}" "${url}"
    else
        echo "ERROR: neither curl nor wget is installed." >&2
        exit 1
    fi
}

echo "Step 1: download PDFs into ${SCRATCH}"
download "${SYNTAX_URL}" "${SYNTAX_PDF}"
download "${GUIDE_URL}"  "${GUIDE_PDF}"

if ! command -v pdftotext >/dev/null 2>&1; then
    echo "ERROR: pdftotext is required (install poppler-utils)." >&2
    exit 1
fi
if ! command -v python3 >/dev/null 2>&1; then
    echo "ERROR: python3 is required." >&2
    exit 1
fi

echo
echo "Step 2: extract PDFs and slice into per-section markdown"
python3 "${SKILL_ROOT}/scripts/build_references.py" \
    "${SYNTAX_PDF}" "${GUIDE_PDF}" --out "${REF_DIR}"

echo
if [[ "${KEEP_PDFS}" == "1" ]]; then
    cp "${SYNTAX_PDF}" "${REF_DIR}/jsl-syntax-reference.pdf"
    cp "${GUIDE_PDF}"  "${REF_DIR}/scripting-guide.pdf"
    echo "Step 3: kept original PDFs in ${REF_DIR}/ (per --keep-pdfs)"
else
    echo "Step 3: dropping original PDFs (markdown is the canonical reference now)"
fi

if [[ "${WITH_INDEX}" == "1" ]]; then
    echo
    echo "Step 4: mirror the online JMP Scripting Index"
    bash "${SKILL_ROOT}/scripts/fetch_scripting_index.sh"
fi

echo
echo "Done. References live under ${REF_DIR}"
ls -lh "${REF_DIR}"
