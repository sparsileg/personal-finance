#!/bin/bash
# Preview one document: ./render.sh NAME SCRIPT
# Builds out/NAME.docx, converts it to PDF, prints the page count, and makes
# page-preview montages (out/NAME-m*.png). Needs LibreOffice, poppler-utils
# and ImageMagick. LibreOffice lacks the Aptos font, so check final pages in Word.
set -e
cd "$(dirname "$0")"
PY=${PYTHON:-python3}
mkdir -p out
"$PY" "$2" "out/$1.docx"
cd out && rm -f "$1".pdf "$1"-pg*.png "$1"-m*.png
soffice --headless --convert-to 'pdf:writer_pdf_Export:{"IsSkipEmptyPages":{"type":"boolean","value":"false"}}' "$1.docx" >/dev/null 2>&1
pdftoppm -r 60 -png "$1.pdf" "$1-pg"
n=$(ls "$1"-pg*.png | wc -l); echo "$1: $n pages"
ls "$1"-pg*.png | split -l 6 - "$1-grp-"
i=1; for g in "$1"-grp-*; do montage $(cat $g) -tile 3x2 -geometry +4+4 "$1-m$i.png"; rm $g; i=$((i+1)); done
