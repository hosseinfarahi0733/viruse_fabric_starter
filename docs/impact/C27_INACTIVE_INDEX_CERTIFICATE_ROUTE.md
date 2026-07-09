# C27 Impact Report: Inactive Index Certificate Route

## Summary

C27 packages the C26 inactive-coordinate route into an explicit parameter-side certificate.

C26 proved that `inactiveCoordScore p i` is inactive-insensitive when:

```lean
¬ i ∈ p.active
```

C27 introduces:

```lean
InactiveIndexCertificate
```

to package the coordinate and its inactive-membership proof.

## New Lean objects

```lean
InactiveIndexCertificate
```

```lean
inactiveIndexCertificateScore
```

```lean
InactiveIndexCertificate.score_inactiveInsensitive
```

```lean
InactiveIndexCertificate.score_range_zero_top
```

```lean
restrictedParams_inactiveIndexCertificate_fixedProductState_to_currentBestMainTheorem
```

## Scientific value

C27 improves the proof architecture without adding unsupported assumptions.

Before C27, the inactive-coordinate route required passing:

```lean
i : ProductIndex p.d
hi : ¬ i ∈ p.active
```

separately.

After C27, the route is driven by:

```lean
cert : InactiveIndexCertificate p
```

This is a cleaner parameter-level interface for the concrete coordinate score route.

## Route now available

Given an inactive-index certificate, VF-H2 now has:

```lean
InactiveIndexCertificate p
->
inactiveIndexCertificateScore
+
derived productScoreInactiveInsensitive
+
derived ScoreRangeCertificate
->
restrictedProofSpineTarget
```

## Boundary

C27 does not prove that every parameter set has an inactive index.

C27 does not prove that the full product ledger score is inactive-insensitive.

C27 does not prove the full unconditional VF-H2 theorem.

## Recommended next step

C28 should investigate when an `InactiveIndexCertificate p` can be constructed.

A likely next target is a cardinality or coverage condition showing that the active list does not cover all product indices.

Possible target names:

```lean
exists_inactiveIndexCertificate
```

or:

```lean
InactiveIndexCertificate.of_not_all_active
```

The proof should only proceed if the current representation of `p.active` and `ProductIndex p.d` exposes enough finite-index/list structure.
