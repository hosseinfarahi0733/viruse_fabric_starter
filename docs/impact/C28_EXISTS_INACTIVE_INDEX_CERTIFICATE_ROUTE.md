# C28 Impact Report: Exists-Inactive Index Certificate Route

## Summary

C28 converts the minimal non-coverage condition into the C27 inactive-index certificate route.

C27 introduced:

```lean
InactiveIndexCertificate p
```

and proved that such a certificate drives the inactive-coordinate proof-spine route.

C28 adds a noncomputable constructor from the exact existential condition:

```lean
∃ i : ProductIndex p.d, ¬ i ∈ p.active
```

## New Lean objects

```lean
InactiveIndexCertificate.of_exists_inactive
```

```lean
restrictedParams_existsInactiveIndex_fixedProductState_to_currentBestMainTheorem
```

## Scientific value

C28 does not claim an inactive coordinate exists unconditionally.

Instead, it identifies the smallest usable parameter-side condition:

```lean
∃ i, ¬ i ∈ p.active
```

and proves that this condition is sufficient to instantiate the inactive-coordinate proof-spine route.

This keeps the project on the proof path while avoiding a false unconditional existence claim.

## Route now available

Given:

```lean
hExists : ∃ i : ProductIndex p.d, ¬ i ∈ p.active
```

VF-H2 now obtains:

```lean
inactiveIndexCertificateScore
+
derived productScoreInactiveInsensitive
+
derived ScoreRangeCertificate
->
restrictedProofSpineTarget
```

## Boundary

C28 does not prove `∃ i, ¬ i ∈ p.active`.

C28 does not prove a cardinality theorem about `p.active`.

C28 does not prove the full unconditional VF-H2 theorem.

## Recommended next step

C29 should investigate whether the existential inactive-index condition can be derived from a structural active-coverage assumption.

A possible next target is:

```lean
exists_inactive_of_active_length_lt_index_count
```

but only if the repository exposes a finite cardinality or enumeration of `ProductIndex p.d`.
