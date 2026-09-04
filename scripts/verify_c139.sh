#!/usr/bin/env bash
set -euo pipefail

repo="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo"

expected_base="3a107eb735bee8fc142f9b981e207aca506692ea"
expected_paths="reference/python/c139/README.md
reference/python/c139/SHA256SUMS
reference/python/c139/c139_immport_metadata_audit_manifest.v1.json
reference/python/c139/c139_immport_metadata_audit_report.v1.json
reference/python/src/vfh2_c139/__init__.py
reference/python/src/vfh2_c139/__main__.py
reference/python/src/vfh2_c139/cli.py
reference/python/src/vfh2_c139/core.py
reference/python/tests/test_c139_immport_metadata_audit.py
scripts/verify_c139.sh"
manifest="reference/python/c139/c139_immport_metadata_audit_manifest.v1.json"
report="reference/python/c139/c139_immport_metadata_audit_report.v1.json"
python_bin="${PYTHON_BIN:-python3}"
export PYTHONDONTWRITEBYTECODE=1

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
  local c139_commits c139_commit c139_parent actual_commit_paths

  current_head="$(git rev-parse HEAD)"
  actual_status="$(git status --porcelain=v1 --untracked-files=all)"

  if [[ "$current_head" == "$expected_base" && -n "$actual_status" ]]; then
    if [[ "$(git branch --show-current)" != "master" ]]; then
      echo "FAIL: the uncommitted C139 candidate must be on master" >&2
      exit 1
    fi
    if ! git diff --cached --quiet; then
      echo "FAIL: the C139 candidate must be entirely unstaged" >&2
      exit 1
    fi
    actual_paths="$(candidate_paths)"
    if [[ "$actual_paths" != "$expected_paths" ]]; then
      echo "FAIL: $phase candidate is not the exact ten-path C139 change" >&2
      printf '%s\n' "$actual_paths" >&2
      exit 1
    fi
    verification_mode="candidate"
    return
  fi

  if [[ -n "$actual_status" ]]; then
    echo "FAIL: $phase repository state is neither the exact C139 candidate nor clean" >&2
    printf '%s\n' "$actual_status" >&2
    exit 1
  fi

  c139_commits="$(git log --diff-filter=A --format='%H' -- \
    reference/python/src/vfh2_c139/core.py)"
  if [[ -z "$c139_commits" || "$c139_commits" == *$'\n'* ]]; then
    echo "FAIL: expected exactly one C139 source-introduction commit" >&2
    exit 1
  fi
  c139_commit="$c139_commits"
  if ! git merge-base --is-ancestor "$c139_commit" HEAD; then
    echo "FAIL: the C139 introduction commit is not an ancestor of HEAD" >&2
    exit 1
  fi
  c139_parent="$(git rev-parse "${c139_commit}^")"
  if [[ "$c139_parent" != "$expected_base" ]]; then
    echo "FAIL: C139 was not introduced directly after the exact C138 base" >&2
    exit 1
  fi
  actual_commit_paths="$(git diff-tree --no-commit-id --name-only -r \
    "$c139_commit" | LC_ALL=C sort)"
  if [[ "$actual_commit_paths" != "$expected_paths" ]]; then
    echo "FAIL: the committed C139 milestone is not the exact ten-path change" >&2
    printf '%s\n' "$actual_commit_paths" >&2
    exit 1
  fi
  if ! git diff --quiet "$c139_commit" HEAD -- $expected_paths; then
    echo "FAIL: frozen C139 v1 artifacts changed after their introduction" >&2
    exit 1
  fi
  actual_paths="$(git ls-files -- \
    reference/python/c139 reference/python/src/vfh2_c139 \
    reference/python/tests/test_c139_immport_metadata_audit.py \
    scripts/verify_c139.sh | LC_ALL=C sort)"
  if [[ "$actual_paths" != "$expected_paths" ]]; then
    echo "FAIL: frozen C139 v1 tracked inventory changed" >&2
    exit 1
  fi
  verification_mode="committed"
}

verification_mode=""
assert_repo_state "initial"
printf 'C139 repository mode: %s\n' "$verification_mode"

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

report_stdout="$(mktemp)"
report_output="$(mktemp)"
temporary_index="$(mktemp)"
trap 'rm -f "$report_stdout" "$report_output" "$temporary_index"' EXIT

PYTHONPATH=reference/python/src \
  "$python_bin" -m unittest discover \
    -s reference/python/tests \
    -p 'test_c139_immport_metadata_audit.py' -v

PYTHONPATH=reference/python/src \
  "$python_bin" -m unittest discover -s reference/python/tests -v

PYTHONPATH=reference/python/src \
  "$python_bin" -m vfh2_c139 --manifest "$manifest" >"$report_stdout"
PYTHONPATH=reference/python/src \
  "$python_bin" -m vfh2_c139 --manifest "$manifest" \
    --output "$report_output"
cmp "$report" "$report_stdout"
cmp "$report_stdout" "$report_output"
echo "C139 frozen manifest/report and CLI byte stability: PASS"

sha256sum -c reference/python/c139/SHA256SUMS

"$python_bin" - <<'PY'
from __future__ import annotations

import ast
import hashlib
import re
from pathlib import Path


paths = [
    Path("reference/python/c139/README.md"),
    Path("reference/python/c139/SHA256SUMS"),
    Path("reference/python/c139/c139_immport_metadata_audit_manifest.v1.json"),
    Path("reference/python/c139/c139_immport_metadata_audit_report.v1.json"),
    Path("reference/python/src/vfh2_c139/__init__.py"),
    Path("reference/python/src/vfh2_c139/__main__.py"),
    Path("reference/python/src/vfh2_c139/cli.py"),
    Path("reference/python/src/vfh2_c139/core.py"),
    Path("reference/python/tests/test_c139_immport_metadata_audit.py"),
    Path("scripts/verify_c139.sh"),
]
for path in paths:
    raw = path.read_bytes()
    if raw.startswith(b"\xef\xbb\xbf"):
        raise SystemExit(f"FAIL: UTF-8 BOM found in {path}")
    if b"\r" in raw:
        raise SystemExit(f"FAIL: CR character found in {path}")
    if not raw.endswith(b"\n"):
        raise SystemExit(f"FAIL: missing final newline in {path}")
    if len(raw) > 1_000_000:
        raise SystemExit(f"FAIL: unexpectedly large C139 artifact: {path}")
    for number, line in enumerate(raw.splitlines(), 1):
        if line.rstrip() != line:
            raise SystemExit(f"FAIL: trailing whitespace {path}:{number}")

bad_extensions = {
    ".csv", ".tsv", ".xlsx", ".parquet", ".h5", ".hdf5",
    ".rds", ".sav", ".pkl", ".pickle", ".npy", ".npz", ".fastq",
    ".bam", ".sam", ".cel",
}
if any(path.suffix.lower() in bad_extensions for path in paths):
    raise SystemExit("FAIL: raw-data-like extension in the C139 boundary")

banned_imports = {
    "aiohttp", "boto3", "ftplib", "http", "httpx", "joblib", "numpy",
    "os", "pandas", "paramiko", "pickle", "requests", "scipy", "sklearn",
    "socket", "sqlite3", "subprocess", "tensorflow", "torch", "urllib",
}
for path in (
    Path("reference/python/src/vfh2_c139/core.py"),
    Path("reference/python/src/vfh2_c139/cli.py"),
):
    tree = ast.parse(path.read_text(encoding="utf-8"))
    imports = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imports.update(alias.name.split(".")[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            imports.add(node.module.split(".")[0])
    found = sorted(imports & banned_imports)
    if found:
        raise SystemExit(f"FAIL: forbidden C139 source imports in {path}: {found}")

init_tree = ast.parse(
    Path("reference/python/src/vfh2_c139/__init__.py").read_text("utf-8")
)
all_assignment = next(
    node for node in init_tree.body
    if isinstance(node, ast.Assign)
    and any(isinstance(target, ast.Name) and target.id == "__all__"
            for target in node.targets)
)
actual_api = set(ast.literal_eval(all_assignment.value))
expected_api = {
    "ALGORITHM", "BASE_COMMIT", "MANIFEST_SCHEMA", "REPORT_SCHEMA",
    "audit_manifest", "canonical_json_bytes", "load_manifest_bytes",
    "validate_manifest",
}
if actual_api != expected_api:
    raise SystemExit(
        "FAIL: C139 public API mismatch: " + repr(sorted(actual_api))
    )

checksum_lines = Path("reference/python/c139/SHA256SUMS").read_text(
    encoding="ascii"
).splitlines()
checksum_paths = [line.split("  ", 1)[1] for line in checksum_lines]
expected_checksum_paths = sorted(str(path).replace("\\", "/") for path in paths if path.name != "SHA256SUMS")
if checksum_paths != expected_checksum_paths:
    raise SystemExit("FAIL: C139 checksum inventory is not exact and sorted")
for line in checksum_lines:
    digest, relative = line.split("  ", 1)
    actual = hashlib.sha256(Path(relative).read_bytes()).hexdigest()
    if digest != actual:
        raise SystemExit(f"FAIL: checksum mismatch for {relative}")

credential_patterns = [
    re.compile(b"authorization" + rb"\s*[:=]\s*" + b"bearer", re.I),
    re.compile(b"bearer" + rb"\s+[A-Za-z0-9._~+/=-]+", re.I),
    re.compile(b"aws" + rb"[_-]access[_-]key[_-]id", re.I),
    re.compile(
        b"begin" + rb"\s+(?:rsa\s+|ec\s+|openssh\s+)?" + b"private key",
        re.I,
    ),
    re.compile(
        rb"(?:api[_-]?key|credential|password|secret|signature|token|"
        rb"x-amz-[a-z0-9-]+)\s*[:=]",
        re.I,
    ),
    re.compile(b"AKIA" + rb"[0-9A-Z]{16}"),
    re.compile(rb"(?:ghp_|github_pat_|sk-(?:proj-)?)" + rb"[A-Za-z0-9_-]{12,}"),
    re.compile(b"eyJ" + rb"[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{8,}\."
               rb"[A-Za-z0-9_-]{8,}"),
    re.compile(rb"[A-Za-z0-9_-]{160,}={0,2}"),
]
credential_probes = [
    b"Authorization" + b":" + b" Bearer" + b" " + b"x",
    b"Bearer" + b" " + b"x",
    b"credential" + b"=" + b"x",
    b"signature" + b"=" + b"x",
    b"x-amz-" + b"security-token" + b"=" + b"x",
    b"AK" + b"IA" + b"A" * 16,
    b"sk" + b"-proj-" + b"A" * 20,
    b"ey" + b"J" + b"A" * 10 + b"." + b"B" * 10 + b"." + b"C" * 10,
    b"A_" * 80,
]
for probe in credential_probes:
    if not any(pattern.search(probe) for pattern in credential_patterns):
        raise SystemExit("FAIL: credential scanner regression")
for path in paths:
    raw = path.read_bytes()
    for pattern in credential_patterns:
        if pattern.search(raw):
            raise SystemExit(f"FAIL: credential-like material found in {path}")

print("C139 scope, encoding, import, credential, API, and checksum audit: PASS")
PY

lake build
lake env lean lean/VFH2/Product.lean
bash scripts/audit_product_restricted_frontdoors.sh
git diff --check

cp "$(git rev-parse --git-path index)" "$temporary_index"
GIT_INDEX_FILE="$temporary_index" git add -- $expected_paths
GIT_INDEX_FILE="$temporary_index" git diff --cached --check
echo "C139 exact ten-path diff check: PASS"

initial_mode="$verification_mode"
assert_repo_state "final"
if [[ "$verification_mode" != "$initial_mode" ]]; then
  echo "FAIL: C139 repository mode changed during verification" >&2
  exit 1
fi

echo "C139 full verification: PASS ($verification_mode mode)"
