# C21 Impact Report: Bounded Inactive Score Certificate

## Summary

C21 introduces a score-side certificate for the constructed fixed-state proof-spine route.

The certificate packages the two remaining score assumptions identified by C20:

- inactive-insensitivity of the score;
- global boundedness of the score over the threshold interval.

## New Lean objects

```lean
BoundedInactiveScoreCertificate
```

```lean
restrictedParams_scoreCertificate_fixedProductState_to_currentBestMainTheorem
```

```lean
constantProductScore_BoundedInactiveScoreCertificate
```

## Scientific value

C21 does not derive boundedness and does not claim to reduce the score-side assumptions.

Its value is proof-architectural and review-facing: it turns the remaining score requirements into a single explicit certificate target.

Before C21, the C19 route required two separate assumptions:

```lean
productScoreInactiveInsensitive p productScore
productScoreBoundedBy p productScore thresholdLo thresholdHi
```

After C21, the same route can be invoked using:

```lean
BoundedInactiveScoreCertificate p productScore thresholdLo thresholdHi
```

This makes the next assumption-reduction target sharper: future work should construct or derive this certificate for non-trivial score classes.

## Relation to previous milestones

- C17 constructed the canonical fixed state route for constant scores.
- C18 introduced the atemporal platform interpretation boundary.
- C19 generalized the constructed fixed-state route from constant scores to arbitrary bounded inactive-insensitive scores.
- C20 audited and identified score boundedness as the next source gap.
- C21 packages the C20 gap as a reusable certificate target.

## Boundary

C21 is not a full unconditional theorem.

It still depends on a score certificate. The certificate itself contains boundedness and inactive-insensitivity assumptions.

## Recommended next step

C22 should attempt to construct a non-trivial instance of `BoundedInactiveScoreCertificate`, or else formally record why no natural non-constant score construction is available in the current project state.
