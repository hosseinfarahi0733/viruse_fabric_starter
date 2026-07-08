import VFH2.Product.ProductRestrictedParamsActiveInsensitiveProofSpine

/-!
# C13 — Current best main theorem front door

This file exposes the current best theorem route after v17.5.0.

Scientific role:
- It specializes the update to concrete `productUpdateState p`.
- It uses active-insensitive score semantics instead of the abstract score-key
  preservation condition.
- It specializes fixedness to the concrete semantic predicate
  `ProductFixedSet p x`.
- It still assumes ProductFixedSet and natural base bounds.
- It does not discharge ProductFixedSet.
- It does not discharge natural base bounds.
- It is a front-door theorem for review and exposition, not a new assumption
  reduction milestone by itself.
-/

namespace VFH2

namespace ProductRestrictedParamsCurrentBestMainTheorem

/--
Current best front-door theorem for the restricted proof-spine target.

This theorem is the cleanest current statement of the project after v17.5.0:

- concrete update: `productUpdateState p`;
- semantic score condition: inactive-insensitive score;
- semantic fixedness: `ProductFixedSet p x`;
- natural base score bounds.

It avoids the abstract score-key preservation premise by using the C12 route.
-/
theorem restrictedParams_currentBestMainTheorem
    (p : ProductRestrictedParams)
    (x : p.State)
    (productScore : p.State → Int)
    (thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi)
    (hScoreInactive :
      ProductRestrictedParamsActiveInsensitiveScore.productScoreInactiveInsensitive
        p productScore)
    (hFixedSet : ProductFixedSet p x)
    (hBaseLowerNatural : thresholdLo ≤ productScore x)
    (hBaseUpperNatural : productScore x ≤ thresholdHi) :
    ProductRestrictedParamsRestrictedProofSpineFreeze.restrictedProofSpineTarget
      p x (productUpdateState p) productScore
      (ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedUpdate
        p x (productUpdateState p))
      (ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedScore
        p x (productUpdateState p) productScore)
      (ProductFixedSet p x) thresholdLo thresholdHi hThreshold := by
  exact
    VFH2.ProductRestrictedParamsActiveInsensitiveProofSpine.restrictedParams_activeInsensitiveScore_naturalBase_to_restrictedProofSpineTarget
      p x productScore
      (ProductFixedSet p x)
      thresholdLo thresholdHi hThreshold
      hScoreInactive hFixedSet hBaseLowerNatural hBaseUpperNatural

end ProductRestrictedParamsCurrentBestMainTheorem

end VFH2
