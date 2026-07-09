# C24 Impact Report: Product Ledger Score Feasibility Audit

## Summary

C24 records a proof-focused feasibility audit for using `ProductLedger` as a concrete nonconstant score source.

The result is cautious and negative for the direct full-ledger score route.

`ProductLedger` is a promising numerical source because it reads product-state coordinate values and the repository already contains ledger-related bound lemmas. However, the direct score

```lean
fun x => Int.ofNat (productLedger p x)
```

is not yet justified as `productScoreInactiveInsensitive`.

## Why this matters

The project must not drift away from the proof spine.

After C23, the proof architecture has a clean bridge:

```lean
ScoreRangeCertificate
+
productScoreInactiveInsensitive
->
BoundedInactiveScoreCertificate
->
restrictedProofSpineTarget
```

The next real proof objective is therefore not more interpretation. It is a concrete score construction that can discharge the two score-side requirements.

## Audit observation

The update semantics show the key boundary:

- active coordinates are updated to `p.topCoord`;
- inactive coordinates are preserved.

Thus, a score that reads all product coordinates may depend on active coordinates. Such a score is not automatically inactive-insensitive.

A full `productLedger` score appears to read broader coordinate information than the inactive-preserved fragment. Therefore, using it directly would require a new proof that it is invariant under the inactive-equivalence relation. No such proof is currently established.

## Boundary

C24 does not introduce a new theorem.

C24 does not claim that `productLedger` is inactive-insensitive.

C24 does not claim that a concrete nonconstant score has been constructed.

C24 does not weaken the proof spine by adding assumptions that merely restate the desired certificate.

## Scientific value

C24 prevents an unsound or artificial move from C23 to a fake nonconstant score theorem.

The value is proof discipline:

1. identify `ProductLedger` as a plausible numerical source;
2. reject the direct full-ledger route until inactive-insensitivity is proven;
3. define the next formal target more sharply.

## Recommended C25 proof target

C25 should introduce a restricted ledger-style score that reads only inactive-stable coordinates, or another coordinate-dependent score whose inactive-insensitivity can be derived from existing update/transport lemmas.

A conservative target name is:

```lean
inactiveLedgerScore
```

The intended proof route is:

```lean
inactiveLedgerScore
+
derived productScoreInactiveInsensitive
+
derived ScoreRangeCertificate
->
restrictedParams_scoreRangeCertificate_fixedProductState_to_currentBestMainTheorem
```

## Proof-spine commitment

The next milestone should return to Lean theorem construction.

The preferred C25 result is not another audit. It should attempt to construct a concrete nonconstant score candidate and prove the exact requirements needed by the C23 score-range route.
