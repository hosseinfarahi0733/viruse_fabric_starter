#!/usr/bin/env bash
set -Eeuo pipefail

REPO="${1:-.}"
if ! cd "$REPO"; then
  echo "ERROR: cannot enter repository root: $REPO" >&2
  exit 2
fi

PRODUCT_DIR="lean/VFH2/Product"
PRODUCT_AGGREGATE="lean/VFH2/Product.lean"
PREFERRED_FILE="$PRODUCT_DIR/ProductRestrictedParamsPreferredFrontDoor.lean"
FAILURES=0
OPERATIONAL_FAILURES=0
LEAN_FILES=()

fail() {
  printf 'ERROR: %s\n' "$*" >&2
  FAILURES=$((FAILURES + 1))
}

fail_operational() {
  printf 'ERROR: %s\n' "$*" >&2
  OPERATIONAL_FAILURES=$((OPERATIONAL_FAILURES + 1))
}

count_fixed() {
  local token="$1"
  local path="$2"
  local output rc

  if output="$(grep -aFo -- "$token" "$path")"; then
    printf '%s\n' "$output" | wc -l | tr -d '[:space:]'
    return 0
  else
    rc=$?
    if [ "$rc" -eq 1 ]; then
      printf '0\n'
      return 0
    fi
    return "$rc"
  fi
}

# Every token below is an intentionally frozen compatibility or construction
# boundary. A new occurrence requires an explicit architecture review and a
# deliberate baseline update; it must not silently enter downstream code.
check_token_baseline() {
  local token="$1"
  shift
  local -a specs=("$@")
  local -a matches=()
  local path spec allowed_path expected actual allowed rc

  for path in "${LEAN_FILES[@]}"; do
    if grep -aFq -- "$token" "$path"; then
      matches+=("$path")
    else
      rc=$?
      if [ "$rc" -ne 1 ]; then
        fail_operational "cannot scan $path for '$token' (grep exit $rc)"
      fi
    fi
  done

  for path in "${matches[@]}"; do
    allowed=0
    for spec in "${specs[@]}"; do
      allowed_path="${spec%%=*}"
      if [ "$path" = "$allowed_path" ]; then
        allowed=1
        break
      fi
    done
    if [ "$allowed" -ne 1 ]; then
      fail "forbidden downstream use of '$token' in $path"
    fi
  done

  for spec in "${specs[@]}"; do
    allowed_path="${spec%%=*}"
    expected="${spec##*=}"
    if [ ! -f "$allowed_path" ]; then
      fail_operational "missing baseline source $allowed_path for '$token'"
      continue
    fi
    if ! actual="$(count_fixed "$token" "$allowed_path")"; then
      fail_operational "cannot count '$token' in $allowed_path"
      continue
    fi
    if [ "$actual" != "$expected" ]; then
      fail "baseline drift for '$token' in $allowed_path: expected $expected, found $actual"
    fi
  done
}

expect_exact_line_count() {
  local path="$1"
  local regex="$2"
  local expected="$3"
  local label="$4"
  local actual rc

  if [ ! -f "$path" ]; then
    fail_operational "missing $label source: $path"
    return
  fi
  if actual="$(grep -aEc -- "$regex" "$path")"; then
    :
  else
    rc=$?
    if [ "$rc" -ne 1 ]; then
      fail_operational "cannot check $label in $path (grep exit $rc)"
      return
    fi
  fi
  actual="$(printf '%s' "$actual" | tr -d '[:space:]')"
  if [ "$actual" != "$expected" ]; then
    fail "$label: expected $expected matching line(s), found $actual"
  fi
}

if [ ! -d "$PRODUCT_DIR" ] || [ ! -f "$PRODUCT_AGGREGATE" ]; then
  echo "ERROR: run this guard from the VF-H2 repository root (or pass it as argument 1)" >&2
  exit 2
fi

shopt -s globstar nullglob dotglob
for path in lean/**; do
  if [ -L "$path" ]; then
    fail "symbolic links are not allowed under the Lean source root: $path"
  elif [ -d "$path" ] && { [ ! -r "$path" ] || [ ! -x "$path" ]; }; then
    fail_operational "Lean source directory is not readable/searchable: $path"
  fi
done
for path in lean/**/*.lean; do
  if [ -L "$path" ]; then
    fail "symbolic Lean source is not allowed: $path"
  elif [ ! -f "$path" ] || [ ! -r "$path" ]; then
    fail_operational "Lean source is not a readable regular file: $path"
  else
    LEAN_FILES+=("$path")
  fi
done

# Raw not-all-active compatibility boundary.
check_token_baseline \
  'exists_inactive_of_not_all_active' \
  "$PRODUCT_DIR/ProductRestrictedParamsActiveCoverage.lean=3" \
  "$PRODUCT_DIR/ProductRestrictedParamsActiveNoncoverageCertificate.lean=1"
check_token_baseline \
  'InactiveIndexCertificate.of_not_all_active' \
  "$PRODUCT_DIR/ProductRestrictedParamsActiveCoverage.lean=1"
check_token_baseline \
  'ActiveNoncoverageCertificate.of_not_all_active' \
  "$PRODUCT_DIR/ProductRestrictedParamsActiveNoncoverageCertificate.lean=1" \
  "$PRODUCT_DIR/ProductRestrictedParamsActiveCustomEnumKernel.lean=1" \
  "$PRODUCT_DIR/ProductRestrictedParamsActiveLengthLowerBound.lean=1"
check_token_baseline \
  'restrictedParams_notAllActive_fixedProductState_to_currentBestMainTheorem' \
  "$PRODUCT_DIR/ProductRestrictedParamsActiveCoverage.lean=1" \
  "$PREFERRED_FILE=1"
check_token_baseline \
  'currentBestMainTheorem_of_notAllActive' \
  "$PREFERRED_FILE=2"

# Direct erase-construction boundary. Downstream construction-level callers
# must enter through ProductRestrictedParamsPreferredFrontDoor instead.
check_token_baseline \
  'activeWithoutProductIndex' \
  "$PRODUCT_DIR/ProductRestrictedParamsActiveEraseConstruction.lean=13"
check_token_baseline \
  'paramsWithInactiveProductIndex' \
  "$PRODUCT_DIR/ProductRestrictedParamsActiveEraseConstruction.lean=25" \
  "$PREFERRED_FILE=4"
check_token_baseline \
  'activeLengthLtTypedWidthSource_of_paramsWithInactiveProductIndex' \
  "$PRODUCT_DIR/ProductRestrictedParamsActiveEraseConstruction.lean=3" \
  "$PREFERRED_FILE=1"
check_token_baseline \
  'activeNoncoverageCertificate_of_paramsWithInactiveProductIndex' \
  "$PRODUCT_DIR/ProductRestrictedParamsActiveEraseConstruction.lean=3" \
  "$PREFERRED_FILE=1"
check_token_baseline \
  'restrictedParams_paramsWithInactiveProductIndex_fixedProductState_to_currentBestMainTheorem' \
  "$PRODUCT_DIR/ProductRestrictedParamsActiveEraseConstruction.lean=2" \
  "$PREFERRED_FILE=1"

# Positive preferred-API invariants.
expect_exact_line_count \
  "$PRODUCT_AGGREGATE" \
  '^import VFH2[.]Product[.]ProductRestrictedParamsPreferredFrontDoor$' \
  1 \
  'aggregate preferred-front-door import'
expect_exact_line_count \
  "$PREFERRED_FILE" \
  '^noncomputable def currentBestMainTheorem$' \
  1 \
  'preferred currentBestMainTheorem declaration'
expect_exact_line_count \
  "$PREFERRED_FILE" \
  '^namespace Compatibility$' \
  1 \
  'explicit compatibility namespace'

if [ "$OPERATIONAL_FAILURES" -ne 0 ]; then
  printf 'C35C product front-door hygiene guard: ERROR (%s operational failure(s))\n' \
    "$OPERATIONAL_FAILURES" >&2
  exit 2
fi

if [ "$FAILURES" -ne 0 ]; then
  printf 'C35C product front-door hygiene guard: FAIL (%s violation(s))\n' "$FAILURES" >&2
  printf '%s\n' \
    'Use ProductRestrictedParamsPreferredFrontDoor.currentBestMainTheorem for erase construction.' \
    'Use the structural-source or certificate adapters only for genuine compatibility callers.' >&2
  exit 1
fi

echo 'C35C product front-door hygiene guard: PASS'
echo 'Preferred erase-construction API is present; raw routes remain baseline-locked compatibility declarations.'
