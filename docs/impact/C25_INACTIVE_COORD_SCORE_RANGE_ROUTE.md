# C25 Impact Report: Inactive Coordinate Score Range Route

## Summary

C25 introduces a concrete coordinate-based score candidate:

```lean
inactiveCoordScore
```

The score reads one product coordinate and converts its value to `Int`.

C25 proves that this score has a natural range certificate over `[0, p.n]` and routes it through the C23 score-range proof spine.

## New Lean objects

```lean
inactiveCoordScore
```

```lean
inactiveCoordScore_range_zero_top
```

```lean
restrictedParams_inactiveCoordScore_fixedProductState_to_currentBestMainTheorem
```

## Scientific value

C25 moves back from audit to theorem construction.

The milestone does not pretend that all score-side obligations are solved. Instead, it proves the range side for a concrete coordinate-dependent score and leaves exactly one meaningful remaining hypothesis:

```lean
productScoreInactiveInsensitive p (inactiveCoordScore p i)
```

This is progress over the direct full-ledger route rejected in C24, because the score is narrower and its range is derived from existing coordinate bounds.

## Boundary

C25 does not claim that `inactiveCoordScore` is always inactive-insensitive.

C25 does not prove that the score is nonconstant for all parameter settings.

C25 does not prove the full unconditional VF-H2 theorem.

## Recommended next step

C26 should derive inactive-insensitivity for `inactiveCoordScore` under a precise inactive-index condition, if the current inactive-equivalence relation exposes the needed coordinate equality.

The target should be:

```lean
inactiveCoordScore_inactiveInsensitive_of_inactive_index
```

or a similarly named theorem that removes the remaining score-side hypothesis for coordinates known to be inactive-stable.
