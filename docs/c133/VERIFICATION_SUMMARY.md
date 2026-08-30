# C133 verification summary

Date: 2026-08-30

Base commit: `83e1432f171e790bdc53323702e01568d56edbd2`

Lean toolchain: `leanprover/lean4:v4.31.0`

## Final result

```text
FULL_LAKE_BUILD=PASS (220 jobs)
DIRECT_SEMANTIC_FIXTURES=PASS
AXIOM_AUDIT=PASS
PYTHON_REFERENCE_TESTS=PASS (9 tests)
EXHAUSTIVE_BOOLEAN_RELATIONS=PASS (256 relations)
PRODUCT_FRONTDOOR_HYGIENE=PASS
FORBIDDEN_DECLARATION_SCAN=PASS
WHITESPACE_AND_LF_AUDIT=PASS
GIT_DIFF_CHECK=PASS
```

## Axiom report

- `downstreamIntervention_preserves_past`: no axioms.
- `candidatePast_antitone_of_evidenceRefines`: no axioms.
- `exists_strict_recontextualization_without_pastChange`: standard `propext`.
- defect/factorization theorem: standard `propext`.
- executable parity non-chain theorem: standard `propext`, `Quot.sound`.

No custom axiom, `sorry`, `admit`, `unsafe` declaration or `native_decide` is
used by the new formal surface.

## Reproduction

From the repository root with Lean 4.31.0 on `PATH`:

```bash
bash scripts/verify_c133.sh
```

The script performs the full build, direct fixture compile, axiom print,
independent Python test suite, legacy front-door guard and hygiene scans.
