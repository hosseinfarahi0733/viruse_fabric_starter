import VFH2.Product.ProductRestrictedParamsActiveInsensitiveScore
import VFH2.Product.ProductRestrictedParamsFullNaturalProofSpine

/-!
# C12.1 — Active-insensitive score route to the restricted proof spine

This file integrates the C12 active-insensitive score semantics into the
restricted proof-spine route.

Scientific role:
- It specializes the update to the concrete `productUpdateState p`.
- It replaces the abstract score-key preservation condition with the semantic
  assumption that the score is inactive-insensitive.
- It still assumes fixedness and natural base bounds.
- It does not discharge ProductFixedSet.
- It does not discharge natural base bounds.
-/

namespace VFH2

namespace ProductRestrictedParamsActiveInsensitiveProofSpine

/--
Concrete active-insensitive score route to the full natural restricted proof
spine target.

This theorem removes the abstract score-key preservation premise for the
concrete update `productUpdateState p`, replacing it with the semantic condition
that the score is insensitive to active-coordinate changes.
-/
theorem restrictedParams_activeInsensitiveScore_naturalBase_to_restrictedProofSpineTarget
    (p : ProductRestrictedParams)
    (x : p.State)
    (productScore : p.State → Int)
    (fixed : Prop)
    (thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi)
    (hScoreInactive :
      ProductRestrictedParamsActiveInsensitiveScore.productScoreInactiveInsensitive
        p productScore)
    (hFixed : fixed)
    (hBaseLowerNatural : thresholdLo ≤ productScore x)
    (hBaseUpperNatural : productScore x ≤ thresholdHi) :
    ProductRestrictedParamsRestrictedProofSpineFreeze.restrictedProofSpineTarget
      p x (productUpdateState p) productScore
      (ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedUpdate
        p x (productUpdateState p))
      (ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedScore
        p x (productUpdateState p) productScore)
      fixed thresholdLo thresholdHi hThreshold := by
  have hPolicy :
    ProductRestrictedParamsScorePreservationDischarge.restrictedParamsScorePreservingUpdatePolicy
      p (productUpdateState p) productScore :=
    ProductRestrictedParamsActiveInsensitiveScore.productUpdateState_scorePreservingPolicy_of_inactiveInsensitive
      p productScore hScoreInactive

  have hScorePreserved :
    productScore (productUpdateState p x) = productScore x :=
    hPolicy x

  have hBaseTarget :
    ProductRestrictedParamsScoreWindow.restrictedParamsBaseScoreWindowTarget
      p x (productUpdateState p) productScore
      (ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedUpdate
        p x (productUpdateState p))
      (ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedScore
        p x (productUpdateState p) productScore)
      fixed thresholdLo thresholdHi hThreshold := by
    unfold ProductRestrictedParamsScoreWindow.restrictedParamsBaseScoreWindowTarget
    constructor
    · exact
        ProductRestrictedParamsFullNaturalProofSpine.restrictedParams_naturalBaseScoreWindow_of_components
          p x productScore fixed thresholdLo thresholdHi
          hFixed hBaseLowerNatural hBaseUpperNatural
    constructor
    · exact
        ProductEffectBoundConditionMonotonicity.restrictedEffectBoundMonotoneTransport_certificate
          p x thresholdLo thresholdHi hThreshold
    · exact
        ProductRestrictedParamsFullNaturalProofSpine.restrictedParams_canonicalRawUpdateScoreTransportCertificate_of_policy
          p x (productUpdateState p) productScore hPolicy

  unfold ProductRestrictedParamsRestrictedProofSpineFreeze.restrictedProofSpineTarget
  unfold ProductRestrictedParamsPolicyEndToEndScoreWindow.restrictedParamsPolicyEndToEndScoreWindowTarget
  unfold ProductRestrictedParamsScorePreservationDischarge.restrictedParamsScorePreservationDischargeTarget

  exact
    ProductRestrictedParamsScorePreservingUpdate.restrictedParams_scorePreservingUpdate_baseWindow_to_baseAndUpdatedWindowTarget
      p x (productUpdateState p) productScore
      (ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedUpdate
        p x (productUpdateState p))
      (ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedScore
        p x (productUpdateState p) productScore)
      fixed thresholdLo thresholdHi hThreshold
      hBaseTarget hScorePreserved

end ProductRestrictedParamsActiveInsensitiveProofSpine

end VFH2
