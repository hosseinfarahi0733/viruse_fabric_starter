#!/usr/bin/env bash
set -euo pipefail

repo="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo"

command -v lake >/dev/null || {
  echo "FAIL: lake is not on PATH (Lean 4.31.0 is required)" >&2
  exit 1
}

actual_lean="$(lake env lean --version)"
case "$actual_lean" in
  "Lean (version 4.31.0,"*) ;;
  *)
    echo "FAIL: expected Lean 4.31.0, got: $actual_lean" >&2
    exit 1
    ;;
esac

lake build
lake env lean verification/C133SemanticFixtures.lean
lake env lean verification/C133AxiomAudit.lean

PYTHONPATH=reference/python/src \
  python3 -m unittest discover -s reference/python/tests -v

bash scripts/audit_product_restricted_frontdoors.sh
git diff --check

python3 - <<'PY'
from pathlib import Path

paths = [
    Path("lean/VFH2/Product/ThreeTimeCausalSemanticRecovery.lean"),
    Path("verification/C133SemanticFixtures.lean"),
    Path("verification/C133AxiomAudit.lean"),
]
for path in paths:
    raw = path.read_bytes()
    if b"\r\n" in raw:
        raise SystemExit(f"FAIL: CRLF found in {path}")
    for number, line in enumerate(raw.splitlines(), 1):
        if line.rstrip() != line:
            raise SystemExit(f"FAIL: trailing whitespace {path}:{number}")
print("C133 whitespace and LF audit: PASS")
PY

if grep -En \
  '(^|[^[:alnum:]_])(sorry|admit|axiom|unsafe|native_decide)([^[:alnum:]_]|$)' \
  lean/VFH2/Product/ThreeTimeCausalSemanticRecovery.lean \
  verification/C133SemanticFixtures.lean; then
  echo "FAIL: forbidden declaration token found" >&2
  exit 1
fi

echo "C133 full verification: PASS"
