# C19 Impact Report: Bounded Inactive Score for Constructed Fixed State

## Summary

C19 generalizes the constructed fixed-state route introduced before v17.8.0.

The previous strongest constructed route used:

- `fixedProductState p`
- `productUpdateState p`
- `constantProductScore p c`

C19 replaces the constant-score restriction with an arbitrary score satisfying:

- `productScoreInactiveInsensitive p productScore`
- `productScoreBoundedBy p productScore thresholdLo thresholdHi`

for the constructed state `fixedProductState p`.

## New Theorem

```lean
restrictedParams_boundedInactiveScore_fixedProductState_to_currentBestMainTheorem
```

## Scientific Value

C19 reduces a real formal restriction.

Before C19, the constructed fixed-state theorem was tied to constant scores.

After C19, the constructed fixed-state theorem works for any score that is:

1. inactive-insensitive;
2. bounded over the threshold interval.

This is stronger than the constant-score route and better matches the atemporal
constraint-platform interpretation introduced in C18.

## Boundary

C19 still does not prove the full unconditional VF-H2 theorem.

It still assumes:

- inactive-insensitivity of the score;
- boundedness of the score.

However, it no longer requires the score to be constant.

## Recommended Next Step

The next target should investigate whether boundedness can be derived from a more
natural score construction rather than assumed globally.
