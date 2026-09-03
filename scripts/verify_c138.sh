#!/usr/bin/env bash
set -euo pipefail

repo="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo"

expected_base="ade9914375f022a73b3a1e8abb0fc36d56b7fa8f"
expected_paths=".github/workflows/validate-proof-artifacts.yml
reference/python/fixtures/c138_interventional_conformance_report.json
reference/python/src/vfh2_c138/__init__.py
reference/python/src/vfh2_c138/__main__.py
reference/python/src/vfh2_c138/cli.py
reference/python/src/vfh2_c138/core.py
reference/python/tests/test_c138_interventional_conformance.py
scripts/verify_c138.sh
verification/C138AxiomAudit.lean
verification/C138SemanticFixtures.lean"
python_bin="${PYTHON_BIN:-python3}"

command -v git >/dev/null || {
  echo "FAIL: git is not on PATH" >&2
  exit 1
}
command -v lake >/dev/null || {
  echo "FAIL: lake is not on PATH (Lean 4.31.0 is required)" >&2
  exit 1
}
command -v "$python_bin" >/dev/null || {
  echo "FAIL: $python_bin is not on PATH (Python 3.12 is required)" >&2
  exit 1
}

candidate_paths() {
  {
    git diff --name-only
    git ls-files --others --exclude-standard
  } | sed '/^$/d' | LC_ALL=C sort
}

assert_repo_state() {
  local phase="$1"
  local current_head actual_status actual_paths
  local c138_commits c138_commit c138_parent actual_commit_paths

  current_head="$(git rev-parse HEAD)"
  actual_status="$(git status --porcelain=v1 --untracked-files=all)"

  if [[ "$current_head" == "$expected_base" && -n "$actual_status" ]]; then
    if [[ "$(git branch --show-current)" != "master" ]]; then
      echo "FAIL: the uncommitted C138 candidate must be on master" >&2
      exit 1
    fi
    if ! git diff --cached --quiet; then
      echo "FAIL: the C138 candidate must be entirely unstaged" >&2
      exit 1
    fi
    actual_paths="$(candidate_paths)"
    if [[ "$actual_paths" != "$expected_paths" ]]; then
      echo "FAIL: $phase candidate is not the exact ten-path C138 change" >&2
      printf '%s\n' "$actual_paths" >&2
      exit 1
    fi
    verification_mode="candidate"
    return
  fi

  if [[ -n "$actual_status" ]]; then
    echo "FAIL: $phase repository state is neither the exact C138 candidate nor clean" >&2
    printf '%s\n' "$actual_status" >&2
    exit 1
  fi

  c138_commits="$(git log --diff-filter=A --format='%H' -- \
    reference/python/src/vfh2_c138/core.py)"
  if [[ -z "$c138_commits" || "$c138_commits" == *$'\n'* ]]; then
    echo "FAIL: expected exactly one C138 source-introduction commit" >&2
    exit 1
  fi
  c138_commit="$c138_commits"
  if ! git merge-base --is-ancestor "$c138_commit" HEAD; then
    echo "FAIL: the C138 introduction commit is not an ancestor of HEAD" >&2
    exit 1
  fi
  c138_parent="$(git rev-parse "${c138_commit}^")"
  if [[ "$c138_parent" != "$expected_base" ]]; then
    echo "FAIL: C138 was not introduced directly after the exact C137 base" >&2
    exit 1
  fi
  actual_commit_paths="$(git diff-tree --no-commit-id --name-only -r \
    "$c138_commit" | LC_ALL=C sort)"
  if [[ "$actual_commit_paths" != "$expected_paths" ]]; then
    echo "FAIL: the committed C138 milestone is not the exact ten-path change" >&2
    printf '%s\n' "$actual_commit_paths" >&2
    exit 1
  fi
  verification_mode="committed"
}

verification_mode=""
assert_repo_state "initial"
printf 'C138 repository mode: %s\n' "$verification_mode"

actual_lean="$(lake -R env lean --version)"
case "$actual_lean" in
  "Lean (version 4.31.0,"*) ;;
  *)
    echo "FAIL: expected Lean 4.31.0, got: $actual_lean" >&2
    exit 1
    ;;
esac
printf '%s\n' "$actual_lean"

actual_python="$($python_bin -c \
  'import sys; print(".".join(map(str, sys.version_info[:3])))')"
case "$actual_python" in
  3.12.*) ;;
  *)
    echo "FAIL: expected Python 3.12.x, got: $actual_python" >&2
    exit 1
    ;;
esac
printf 'Python %s\n' "$actual_python"

lake build VFH2.Product.ThreeTimeObservationalNonidentifiability
lake env lean lean/VFH2/Product/ThreeTimeObservationalNonidentifiability.lean
lake env lean verification/C138SemanticFixtures.lean

axiom_log="$(mktemp)"
report_one="$(mktemp)"
report_two="$(mktemp)"
trap 'rm -f "$axiom_log" "$report_one" "$report_two"' EXIT

lake env lean verification/C138AxiomAudit.lean 2>&1 | tee "$axiom_log"
"$python_bin" - "$axiom_log" <<'PY'
from pathlib import Path
import re
import sys

expected = {
    "VFH2.ThreeTime.constraintCharacterizesFutureLaw_presentCausalContrastAt_iff",
    "VFH2.ThreeTime.constraintCharacterizesFutureLaw_presentHasCausalEffectOnFuture_iff",
    "VFH2.ThreeTime.pastDrivenBooleanSCM_nonChain_without_presentCausalEffect",
    "VFH2.ThreeTime.presentDrivenBooleanSCM_chain_with_presentCausalEffect",
    "VFH2.ThreeTime.pastDriven_presentDriven_same_completeObservations_different_presentCausality",
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
    raise SystemExit(f"FAIL: C138 axiom dependency found: {details}")
missing = expected - seen
unexpected = seen - expected
if missing or unexpected:
    raise SystemExit(
        "FAIL: C138 axiom inventory mismatch; missing="
        + repr(sorted(missing))
        + ", unexpected="
        + repr(sorted(unexpected))
    )
print("C138 axiom audit judgment: PASS (all mirrored theorems axiom-free)")
PY

PYTHONPATH=reference/python/src \
  "$python_bin" -m unittest discover \
    -s reference/python/tests \
    -p 'test_c138_interventional_conformance.py' -v

PYTHONPATH=reference/python/src \
  "$python_bin" -m unittest discover -s reference/python/tests -v

PYTHONPATH=reference/python/src \
  "$python_bin" -m vfh2_c138 >"$report_one"
PYTHONPATH=reference/python/src \
  "$python_bin" -m vfh2_c138 --output "$report_two"
cmp reference/python/fixtures/c138_interventional_conformance_report.json \
  "$report_one"
cmp "$report_one" "$report_two"
echo "C138 frozen JSON and CLI byte-stability audit: PASS"

bash scripts/verify_c133.sh
lake build
lake env lean lean/VFH2/Product.lean
bash scripts/audit_product_restricted_frontdoors.sh
git diff --check

"$python_bin" - <<'PY'
from pathlib import Path
import ast

paths = [
    Path(".github/workflows/validate-proof-artifacts.yml"),
    Path("reference/python/fixtures/c138_interventional_conformance_report.json"),
    Path("reference/python/src/vfh2_c138/__init__.py"),
    Path("reference/python/src/vfh2_c138/__main__.py"),
    Path("reference/python/src/vfh2_c138/cli.py"),
    Path("reference/python/src/vfh2_c138/core.py"),
    Path("reference/python/tests/test_c138_interventional_conformance.py"),
    Path("scripts/verify_c138.sh"),
    Path("verification/C138AxiomAudit.lean"),
    Path("verification/C138SemanticFixtures.lean"),
]
for path in paths:
    raw = path.read_bytes()
    if raw.startswith(b"\xef\xbb\xbf"):
        raise SystemExit(f"FAIL: UTF-8 BOM found in {path}")
    if b"\r" in raw:
        raise SystemExit(f"FAIL: CR character found in {path}")
    if not raw.endswith(b"\n"):
        raise SystemExit(f"FAIL: missing final newline in {path}")
    for number, line in enumerate(raw.splitlines(), 1):
        if line.rstrip() != line:
            raise SystemExit(f"FAIL: trailing whitespace {path}:{number}")

init_tree = ast.parse(
    Path("reference/python/src/vfh2_c138/__init__.py").read_text("utf-8")
)
all_assignment = next(
    node for node in init_tree.body
    if isinstance(node, ast.Assign)
    and any(isinstance(target, ast.Name) and target.id == "__all__"
            for target in node.targets)
)
actual_api = set(ast.literal_eval(all_assignment.value))
expected_api = {
    "BOOLEAN_DOMAIN",
    "PAST_COPY_SCM",
    "PRESENT_COPY_SCM",
    "SCHEMA",
    "BooleanTriTemporalSCM",
    "State",
    "constraint_characterizes_future_law",
    "constraint_contrast_witness_exists",
    "do_present",
    "full_interventional_conformance_report",
    "law_graph",
    "observationally_equivalent",
    "present_causal_contrast_at",
    "present_has_causal_effect_on_future",
    "realize",
}
if actual_api != expected_api:
    raise SystemExit(
        "FAIL: C138 public API mismatch; actual=" + repr(sorted(actual_api))
    )
core = Path("reference/python/src/vfh2_c138/core.py").read_text("utf-8")
if "vfh2_c133" in core:
    raise SystemExit("FAIL: C138 core must not import or wrap C133")
print("C138 LF, whitespace, and public API audit: PASS")
PY

if grep -En \
  '(^|[^[:alnum:]_])(sorry|admit|axiom|unsafe|native_decide)([^[:alnum:]_]|$)' \
  verification/C138SemanticFixtures.lean; then
  echo "FAIL: forbidden Lean declaration token found" >&2
  exit 1
fi

initial_mode="$verification_mode"
assert_repo_state "final"
if [[ "$verification_mode" != "$initial_mode" ]]; then
  echo "FAIL: C138 repository mode changed during verification" >&2
  exit 1
fi

echo "C138 full verification: PASS ($verification_mode mode)"
