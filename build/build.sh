#!/bin/bash
# Build all 15 session documents into build/out/.
#   ./build.sh            build only
#   ./build.sh --install  build, then copy them over the .docx files in the repo root
# Needs Python 3 with python-docx (pip install python-docx). Set PYTHON to use another interpreter.
set -e
cd "$(dirname "$0")"
PY=${PYTHON:-python3}
mkdir -p out
TOPICS=("" "Understanding Your Money Story" "Creating a Budget" "Breaking the Debt Cycle"
        "Financial Safety Net" "Building Wealth")
for n in 1 2 3 4 5; do
  "$PY" "s$n.py" "out/$n - ${TOPICS[$n]}.docx"
  "$PY" "f$n.py" "out/$n - Facilitator Notes.docx"
  "$PY" "t$n.py" "out/$n - Take-Home Worksheets.docx"
done
echo "Built $(ls out/[1-5]\ -\ *.docx | wc -l) documents in build/out/"
if [ "$1" = "--install" ]; then
  cp out/[1-5]\ -\ *.docx ..
  echo "Copied them to the repo root."
fi
