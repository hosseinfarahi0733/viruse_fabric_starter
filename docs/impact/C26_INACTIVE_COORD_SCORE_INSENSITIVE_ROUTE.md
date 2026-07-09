# C26 Impact Report: Inactive Coordinate Score Insensitive Route

## Summary

C26 discharges the remaining C25 score-side hypothesis for inactive coordinates.

C25 introduced:

```lean
inactiveCoordScore
```

and proved its range certificate. The remaining hypothesis was:

```lean
productScoreInactiveInsensitive p (inactiveCoordScore p i)
```

C26 proves this hypothesis under the precise condition:

```lean
¬ i ∈ p.active
```

## New Lean objects

```lean
inactiveCoordScore_inactiveInsensitive_of_inactive_index
```

```lean
restrictedParams_inactiveCoordScore_inactiveIndex_fixedProductState_to_currentBestMainTheorem
```

## Scientific value

C26 is a genuine proof-spine improvement.

It does not add an assumption that restates inactive-insensitivity. Instead, it derives inactive-insensitivity from the definition of `productScoreInactiveInsensitive` and the fact that the coordinate read by `inactiveCoordScore` is inactive.

This closes the C25 route for inactive coordinates.

## Route closed by C26

For any inactive coordinate `i`, the project now has:

```lean
inactiveCoordScore p i
+
¬ i ∈ p.active
+
derived productScoreInactiveInsensitive
+
derived ScoreRangeCertificate
->
restrictedProofSpineTarget
```

## Boundary

C26 does not claim the coordinate score is inactive-insensitive for active coordinates.

C26 does not claim the full product ledger score is inactive-insensitive.

C26 does not prove the full unconditional VF-H2 theorem.

## Recommended next step

C27 should investigate whether there is always at least one inactive coordinate under meaningful parameter conditions.

A natural next target is:

```lean
exists_inactive_index
```

or a parameter-level certificate that provides an inactive coordinate and packages the C26 route existentially.
