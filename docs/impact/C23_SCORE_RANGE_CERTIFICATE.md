# C23 Impact Report: Score Range Certificate

## Summary

C23 introduces a reusable score-range certificate pattern.

The previous milestones established that the strongest constructed fixed-state
route can use a `BoundedInactiveScoreCertificate`, but C22 found no existing
nonconstant score source that naturally provides such a certificate.

C23 responds by adding an intermediate range-certificate pattern.

## New Lean objects

```lean
ScoreRangeCertificate
```

```lean
ScoreRangeCertificate.to_productScoreBoundedBy
```

```lean
ScoreRangeCertificate.to_BoundedInactiveScoreCertificate
```

```lean
restrictedParams_scoreRangeCertificate_fixedProductState_to_currentBestMainTheorem
```

## Scientific value

C23 does not construct a natural nonconstant score.

Instead, it decomposes the boundedness problem into a reusable target:

```lean
∀ y : p.State, thresholdLo ≤ productScore y
∀ y : p.State, productScore y ≤ thresholdHi
```

Together with inactive-insensitivity, this range certificate yields the existing
`BoundedInactiveScoreCertificate`.

This is a real proof-architecture improvement because future score constructions
can target `ScoreRangeCertificate` rather than directly threading the lower-level
boundedness predicate through the proof spine.

## Relation to prior milestones

- C19 generalized the fixed-state route from constant scores to arbitrary bounded inactive scores.
- C20 identified score boundedness as the next source gap.
- C21 packaged score assumptions as `BoundedInactiveScoreCertificate`.
- C22 audited for a nonconstant score source and found none.
- C23 introduces a range-certificate bridge toward future nonconstant score constructions.

## Boundary

C23 still does not prove the full unconditional VF-H2 theorem.

C23 does not derive a range certificate for a concrete nonconstant score.

C23 makes the next target sharper: construct a meaningful nonconstant score and prove its `ScoreRangeCertificate`.

## Recommended next step

C24 should search for or introduce a concrete nonconstant score construction whose range can be bounded by structural properties of `ProductRestrictedParams`.

A conservative candidate is a two-level or coordinate-dependent score, provided it can be proven inactive-insensitive under the existing product-state equivalence conditions.
