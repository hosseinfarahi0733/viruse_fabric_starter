import VFH2.Product.ProductRestrictedParamsFullNaturalProofSpine

/-!
# VF-H2 Canonical Restricted Proof-Spine Characterization

This file gives an exact component-level characterization of the restricted
proof-spine target when its typed update and typed score are the canonical raw
equalities.

The characterization is pointwise. It requires only score preservation at the
selected state, not a global score-preserving policy.

Boundary:
- The carrier remains `ProductRestrictedParams.State`.
- `fixed` is the proposition supplied to the proof-spine target.
- The result is specific to the canonical typed update and typed score.
- It does not claim unrestricted, empirical, or biological validation.
-/

namespace VFH2

namespace ProductRestrictedParamsCanonicalProofSpineCharacterization

/--
With the canonical raw equalities, the restricted proof-spine target holds
exactly when its fixed proposition, both base-score bounds, and pointwise score
preservation all hold.
-/
theorem restrictedParams_canonicalProofSpineTarget_iff_fixed_baseBounds_and_scorePreserved
    (p : ProductRestrictedParams)
    (x : p.State)
    (productUpdate : p.State → p.State)
    (productScore : p.State → Int)
    (fixed : Prop)
    (thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi) :
    ProductRestrictedParamsRestrictedProofSpineFreeze.restrictedProofSpineTarget
        p
        x
        productUpdate
        productScore
        (ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedUpdate
          p
          x
          productUpdate)
        (ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedScore
          p
          x
          productUpdate
          productScore)
        fixed
        thresholdLo
        thresholdHi
        hThreshold
      ↔
    fixed ∧
      thresholdLo ≤ productScore x ∧
      productScore x ≤ thresholdHi ∧
      productScore (productUpdate x) = productScore x := by
  constructor

  · intro hTarget

    have hBaseTarget :
        ProductRestrictedParamsScoreWindow.restrictedParamsBaseScoreWindowTarget
          p
          x
          productUpdate
          productScore
          (ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedUpdate
            p
            x
            productUpdate)
          (ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedScore
            p
            x
            productUpdate
            productScore)
          fixed
          thresholdLo
          thresholdHi
          hThreshold :=
      ProductRestrictedParamsPolicyEndToEndScoreWindow.restrictedParams_policyEndToEnd_baseTarget_projection
        p
        x
        productUpdate
        productScore
        (ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedUpdate
          p
          x
          productUpdate)
        (ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedScore
          p
          x
          productUpdate
          productScore)
        fixed
        thresholdLo
        thresholdHi
        hThreshold
        hTarget

    have hWindow :
        ProductRestrictedParamsScoreWindow.restrictedParamsBaseScoreWindow
          p
          x
          productScore
          fixed
          thresholdLo
          thresholdHi :=
      ProductRestrictedParamsScoreWindow.restrictedParams_baseScoreWindowTarget_window_projection
        p
        x
        productUpdate
        productScore
        (ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedUpdate
          p
          x
          productUpdate)
        (ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedScore
          p
          x
          productUpdate
          productScore)
        fixed
        thresholdLo
        thresholdHi
        hThreshold
        hBaseTarget

    have hLower :
        ProductBridgeGeneralization.genericBridgeTarget
          fixed
          (thresholdLo ≤ productScore x) :=
      ProductRestrictedParamsScoreWindow.restrictedParams_baseScoreWindow_lower_projection
        p
        x
        productScore
        fixed
        thresholdLo
        thresholdHi
        hWindow

    have hUpper :
        ProductBridgeGeneralization.genericBridgeTarget
          fixed
          (productScore x ≤ thresholdHi) :=
      ProductRestrictedParamsScoreWindow.restrictedParams_baseScoreWindow_upper_projection
        p
        x
        productScore
        fixed
        thresholdLo
        thresholdHi
        hWindow

    have hRawTransport :
        ProductRestrictedParamsUpdateScoreTransport.restrictedParamsRawUpdateScoreTransportCertificate
          p
          x
          productUpdate
          productScore
          (ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedUpdate
            p
            x
            productUpdate)
          (ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedScore
            p
            x
            productUpdate
            productScore) := by
      unfold ProductRestrictedParamsScoreWindow.restrictedParamsBaseScoreWindowTarget at hBaseTarget
      exact hBaseTarget.2.2

    have hUpdatedScore := hRawTransport.2.2
    change productScore x = productScore (productUpdate x) at hUpdatedScore

    unfold ProductBridgeGeneralization.genericBridgeTarget at hLower hUpper
    exact ⟨hLower.1, hLower.2, hUpper.2, hUpdatedScore.symm⟩

  · rintro ⟨hFixed, hBaseLower, hBaseUpper, hScorePreserved⟩

    have hRawTransport :
        ProductRestrictedParamsUpdateScoreTransport.restrictedParamsRawUpdateScoreTransportCertificate
          p
          x
          productUpdate
          productScore
          (ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedUpdate
            p
            x
            productUpdate)
          (ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedScore
            p
            x
            productUpdate
            productScore) := by
      unfold ProductRestrictedParamsUpdateScoreTransport.restrictedParamsRawUpdateScoreTransportCertificate
      constructor
      · exact
          ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedUpdate_base_to_updated
            p x productUpdate
      constructor
      · exact
          ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedScore_base
            p x productUpdate productScore
      · change productScore x = productScore (productUpdate x)
        exact hScorePreserved.symm

    have hBaseTarget :
        ProductRestrictedParamsScoreWindow.restrictedParamsBaseScoreWindowTarget
          p
          x
          productUpdate
          productScore
          (ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedUpdate
            p
            x
            productUpdate)
          (ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedScore
            p
            x
            productUpdate
            productScore)
          fixed
          thresholdLo
          thresholdHi
          hThreshold := by
      unfold ProductRestrictedParamsScoreWindow.restrictedParamsBaseScoreWindowTarget
      constructor
      · exact
          ProductRestrictedParamsFullNaturalProofSpine.restrictedParams_naturalBaseScoreWindow_of_components
            p
            x
            productScore
            fixed
            thresholdLo
            thresholdHi
            hFixed
            hBaseLower
            hBaseUpper
      constructor
      · exact
          ProductEffectBoundConditionMonotonicity.restrictedEffectBoundMonotoneTransport_certificate
            p x thresholdLo thresholdHi hThreshold
      · exact hRawTransport

    unfold ProductRestrictedParamsRestrictedProofSpineFreeze.restrictedProofSpineTarget
    unfold ProductRestrictedParamsPolicyEndToEndScoreWindow.restrictedParamsPolicyEndToEndScoreWindowTarget
    unfold ProductRestrictedParamsScorePreservationDischarge.restrictedParamsScorePreservationDischargeTarget

    exact
      ProductRestrictedParamsScorePreservingUpdate.restrictedParams_scorePreservingUpdate_baseWindow_to_baseAndUpdatedWindowTarget
        p
        x
        productUpdate
        productScore
        (ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedUpdate
          p
          x
          productUpdate)
        (ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedScore
          p
          x
          productUpdate
          productScore)
        fixed
        thresholdLo
        thresholdHi
        hThreshold
        hBaseTarget
        hScorePreserved

end ProductRestrictedParamsCanonicalProofSpineCharacterization

end VFH2
