#!/usr/bin/env bash
set -euo pipefail

repo="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo"

expected_base="d475d8a2efb732d53467fbc3c1ca40dc881f66d2"
expected_candidate_status=" M lean/VFH2/Product.lean
?? lean/VFH2/Product/ThreeTimeInterventionalConstraintCausality.lean
?? scripts/verify_c134.sh
?? verification/C134AxiomAudit.lean
?? verification/C134SemanticFixtures.lean"
expected_commit_paths="lean/VFH2/Product.lean
lean/VFH2/Product/ThreeTimeInterventionalConstraintCausality.lean
scripts/verify_c134.sh
verification/C134AxiomAudit.lean
verification/C134SemanticFixtures.lean"

command -v git >/dev/null || {
  echo "FAIL: git is not on PATH" >&2
  exit 1
}
command -v lake >/dev/null || {
  echo "FAIL: lake is not on PATH (Lean 4.31.0 is required)" >&2
  exit 1
}
command -v python3 >/dev/null || {
  echo "FAIL: python3 is not on PATH" >&2
  exit 1
}

assert_repo_state() {
  local phase="$1"
  local actual_status current_head c134_commits c134_commit c134_parent
  local actual_commit_paths

  actual_status="$(git status --porcelain=v1 --untracked-files=all)"
  current_head="$(git rev-parse HEAD)"

  if [[ "$current_head" == "$expected_base" &&
        "$actual_status" == "$expected_candidate_status" ]]; then
    if [[ "$(git branch --show-current)" != "master" ]]; then
      echo "FAIL: the uncommitted C134 candidate must be on master" >&2
      exit 1
    fi
    verification_mode="candidate"
    return
  fi

  if [[ -n "$actual_status" ]]; then
    echo "FAIL: $phase repository state is neither the exact uncommitted C134 candidate nor clean" >&2
    printf '%s\n' "$actual_status" >&2
    exit 1
  fi

  c134_commits="$(git log --diff-filter=A --format='%H' -- \
    lean/VFH2/Product/ThreeTimeInterventionalConstraintCausality.lean)"
  if [[ -z "$c134_commits" || "$c134_commits" == *$'\n'* ]]; then
    echo "FAIL: expected exactly one C134 source-introduction commit" >&2
    exit 1
  fi
  c134_commit="$c134_commits"
  if ! git merge-base --is-ancestor "$c134_commit" HEAD; then
    echo "FAIL: the C134 introduction commit is not an ancestor of HEAD" >&2
    exit 1
  fi
  c134_parent="$(git rev-parse "${c134_commit}^")"
  if [[ "$c134_parent" != "$expected_base" ]]; then
    echo "FAIL: C134 was not introduced directly after the exact C133 base" >&2
    exit 1
  fi
  actual_commit_paths="$(git diff-tree --no-commit-id --name-only -r \
    "$c134_commit" | LC_ALL=C sort)"
  if [[ "$actual_commit_paths" != "$expected_commit_paths" ]]; then
    echo "FAIL: the committed C134 milestone is not the exact five-path change" >&2
    printf '%s\n' "$actual_commit_paths" >&2
    exit 1
  fi
  verification_mode="committed"
}

verification_mode=""
assert_repo_state "initial"
printf 'C134 repository mode: %s\n' "$verification_mode"

actual_lean="$(lake env lean --version)"
case "$actual_lean" in
  "Lean (version 4.31.0,"*) ;;
  *)
    echo "FAIL: expected Lean 4.31.0, got: $actual_lean" >&2
    exit 1
    ;;
esac
printf '%s\n' "$actual_lean"

# A cold clone has no C133 oleans.  Build only the imported dependency closure
# before the direct C134 compile, then install the C134 olean for its fixtures.
lake build VFH2.Product.ThreeTimeCausalSemanticRecovery
lake env lean lean/VFH2/Product/ThreeTimeInterventionalConstraintCausality.lean
lake build VFH2.Product.ThreeTimeInterventionalConstraintCausality
lake env lean verification/C134SemanticFixtures.lean

axiom_log="$(mktemp)"
trap 'rm -f "$axiom_log"' EXIT
lake env lean verification/C134AxiomAudit.lean 2>&1 | tee "$axiom_log"
python3 - "$axiom_log" <<'PY'
from pathlib import Path
import re
import sys

expected = {
    "VFH2.ThreeTime.booleanParitySCM_evenParity_characterizesFutureLaw",
    "VFH2.ThreeTime.booleanParitySCM_executableParity_characterizesFutureLaw",
    "VFH2.ThreeTime.booleanParitySCM_presentCausalContrastAt_iff_present_ne",
    "VFH2.ThreeTime.booleanParitySCM_presentHasCausalEffectOnFuture",
}
text = Path(sys.argv[1]).read_text(encoding="utf-8")
seen = set(re.findall(
    r"^'([^']+)' does not depend on any axioms$", text, re.MULTILINE
))
dependent = re.findall(
    r"^'([^']+)' depends on axioms: \[([^]]*)\]$", text, re.MULTILINE
)
if dependent:
    details = "; ".join(f"{name}: [{axioms}]" for name, axioms in dependent)
    raise SystemExit(f"FAIL: C134 axiom dependency found: {details}")
missing = expected - seen
if missing:
    raise SystemExit(
        "FAIL: missing axiom-audit declarations: " + ", ".join(sorted(missing))
    )
print("C134 axiom audit judgment: PASS (all public theorems axiom-free)")
PY

lake build
lake env lean lean/VFH2/Product.lean
bash scripts/verify_c133.sh
bash scripts/audit_product_restricted_frontdoors.sh
git diff --check

python3 - <<'PY'
from pathlib import Path
import re

paths = [
    Path("lean/VFH2/Product.lean"),
    Path("lean/VFH2/Product/ThreeTimeInterventionalConstraintCausality.lean"),
    Path("verification/C134SemanticFixtures.lean"),
    Path("verification/C134AxiomAudit.lean"),
    Path("scripts/verify_c134.sh"),
]
for path in paths:
    raw = path.read_bytes()
    if b"\r\n" in raw:
        raise SystemExit(f"FAIL: CRLF found in {path}")
    for number, line in enumerate(raw.splitlines(), 1):
        if line.rstrip() != line:
            raise SystemExit(f"FAIL: trailing whitespace {path}:{number}")

source = Path(
    "lean/VFH2/Product/ThreeTimeInterventionalConstraintCausality.lean"
).read_text(encoding="utf-8")
declarations = [
    ("def", "PresentCausalContrastAt"),
    ("def", "PresentHasCausalEffectOnFuture"),
    ("def", "ConstraintCharacterizesFutureLaw"),
    ("theorem", "booleanParitySCM_evenParity_characterizesFutureLaw"),
    ("theorem", "booleanParitySCM_executableParity_characterizesFutureLaw"),
    ("theorem", "booleanParitySCM_presentCausalContrastAt_iff_present_ne"),
    ("theorem", "booleanParitySCM_presentHasCausalEffectOnFuture"),
]
for kind, name in declarations:
    count = len(re.findall(
        rf"^{kind}\s+{re.escape(name)}\b", source, re.MULTILINE
    ))
    if count != 1:
        raise SystemExit(f"FAIL: expected one {kind} declaration {name}, got {count}")
print("C134 LF, whitespace, and declaration inventory audit: PASS")
PY

if grep -En \
  '(^|[^[:alnum:]_])(sorry|admit|axiom|unsafe|native_decide)([^[:alnum:]_]|$)' \
  lean/VFH2/Product/ThreeTimeInterventionalConstraintCausality.lean \
  verification/C134SemanticFixtures.lean; then
  echo "FAIL: forbidden declaration token found" >&2
  exit 1
fi

initial_mode="$verification_mode"
assert_repo_state "final"
if [[ "$verification_mode" != "$initial_mode" ]]; then
  echo "FAIL: C134 repository mode changed during verification" >&2
  exit 1
fi

echo "C134 full verification: PASS ($verification_mode mode)"
