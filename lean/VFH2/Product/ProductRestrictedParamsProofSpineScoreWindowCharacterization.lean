import VFH2.Product.ProductFixedPointCharacterization
import VFH2.Product.ProductRestrictedParamsFullNaturalProofSpine

/-!
# VF-H2 Restricted Proof-Spine Score-Window Characterization

This file characterizes the current restricted proof-spine target for arbitrary
restricted parameters and an arbitrary integer-valued score. At a fixed state,
the update itself supplies the only score preservation needed by the target.

Boundary:
- The result is restricted to `ProductRestrictedParams` and
  `productUpdateState`.
- It introduces no global score-preservation or preferred-parameter assumption.
- It does not claim an unrestricted or empirical result.
-/

namespace VFH2

namespace ProductRestrictedParamsProofSpineScoreWindowCharacterization

/--
For the canonical restricted update and raw equalities, the proof-spine target
holds exactly when the state is fixed and its base score lies in the requested
window.
-/
theorem restrictedParams_restrictedProofSpineTarget_iff_fixedSet_and_baseScoreBounds
    (p : ProductRestrictedParams)
    (y : p.State)
    (productScore : p.State → Int)
    (thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi) :
    ProductRestrictedParamsRestrictedProofSpineFreeze.restrictedProofSpineTarget
        p
        y
        (productUpdateState p)
        productScore
        (ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedUpdate
          p
          y
          (productUpdateState p))
        (ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedScore
          p
          y
          (productUpdateState p)
          productScore)
        (ProductFixedSet p y)
        thresholdLo
        thresholdHi
        hThreshold
      ↔
    ProductFixedSet p y ∧
      thresholdLo ≤ productScore y ∧
      productScore y ≤ thresholdHi := by
  constructor

  · intro hTarget

    have hBaseTarget :
        ProductRestrictedParamsScoreWindow.restrictedParamsBaseScoreWindowTarget
          p
          y
          (productUpdateState p)
          productScore
          (ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedUpdate
            p
            y
            (productUpdateState p))
          (ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedScore
            p
            y
            (productUpdateState p)
            productScore)
          (ProductFixedSet p y)
          thresholdLo
          thresholdHi
          hThreshold :=
      ProductRestrictedParamsPolicyEndToEndScoreWindow.restrictedParams_policyEndToEnd_baseTarget_projection
        p
        y
        (productUpdateState p)
        productScore
        (ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedUpdate
          p
          y
          (productUpdateState p))
        (ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedScore
          p
          y
          (productUpdateState p)
          productScore)
        (ProductFixedSet p y)
        thresholdLo
        thresholdHi
        hThreshold
        hTarget

    have hWindow :
        ProductRestrictedParamsScoreWindow.restrictedParamsBaseScoreWindow
          p
          y
          productScore
          (ProductFixedSet p y)
          thresholdLo
          thresholdHi :=
      ProductRestrictedParamsScoreWindow.restrictedParams_baseScoreWindowTarget_window_projection
        p
        y
        (productUpdateState p)
        productScore
        (ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedUpdate
          p
          y
          (productUpdateState p))
        (ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedScore
          p
          y
          (productUpdateState p)
          productScore)
        (ProductFixedSet p y)
        thresholdLo
        thresholdHi
        hThreshold
        hBaseTarget

    have hLower :
        ProductBridgeGeneralization.genericBridgeTarget
          (ProductFixedSet p y)
          (thresholdLo ≤ productScore y) :=
      ProductRestrictedParamsScoreWindow.restrictedParams_baseScoreWindow_lower_projection
        p
        y
        productScore
        (ProductFixedSet p y)
        thresholdLo
        thresholdHi
        hWindow

    have hUpper :
        ProductBridgeGeneralization.genericBridgeTarget
          (ProductFixedSet p y)
          (productScore y ≤ thresholdHi) :=
      ProductRestrictedParamsScoreWindow.restrictedParams_baseScoreWindow_upper_projection
        p
        y
        productScore
        (ProductFixedSet p y)
        thresholdLo
        thresholdHi
        hWindow

    unfold ProductBridgeGeneralization.genericBridgeTarget at hLower hUpper
    exact ⟨hLower.1, hLower.2, hUpper.2⟩

  · rintro ⟨hFixed, hBaseLower, hBaseUpper⟩

    have hUpdate :
        productUpdateState p y = y :=
      (productFixedSet_iff_productUpdateState_eq_self p y).mp hFixed

    have hScorePreserved :
        productScore (productUpdateState p y) = productScore y := by
      rw [hUpdate]

    have hRawTransport :
        ProductRestrictedParamsUpdateScoreTransport.restrictedParamsRawUpdateScoreTransportCertificate
          p
          y
          (productUpdateState p)
          productScore
          (ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedUpdate
            p
            y
            (productUpdateState p))
          (ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedScore
            p
            y
            (productUpdateState p)
            productScore) := by
      unfold ProductRestrictedParamsUpdateScoreTransport.restrictedParamsRawUpdateScoreTransportCertificate
      constructor
      · exact
          ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedUpdate_base_to_updated
            p y (productUpdateState p)
      constructor
      · exact
          ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedScore_base
            p y (productUpdateState p) productScore
      · change productScore y = productScore (productUpdateState p y)
        exact hScorePreserved.symm

    have hBaseTarget :
        ProductRestrictedParamsScoreWindow.restrictedParamsBaseScoreWindowTarget
          p
          y
          (productUpdateState p)
          productScore
          (ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedUpdate
            p
            y
            (productUpdateState p))
          (ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedScore
            p
            y
            (productUpdateState p)
            productScore)
          (ProductFixedSet p y)
          thresholdLo
          thresholdHi
          hThreshold := by
      unfold ProductRestrictedParamsScoreWindow.restrictedParamsBaseScoreWindowTarget
      constructor
      · exact
          ProductRestrictedParamsFullNaturalProofSpine.restrictedParams_naturalBaseScoreWindow_of_components
            p
            y
            productScore
            (ProductFixedSet p y)
            thresholdLo
            thresholdHi
            hFixed
            hBaseLower
            hBaseUpper
      constructor
      · exact
          ProductEffectBoundConditionMonotonicity.restrictedEffectBoundMonotoneTransport_certificate
            p y thresholdLo thresholdHi hThreshold
      · exact hRawTransport

    unfold ProductRestrictedParamsRestrictedProofSpineFreeze.restrictedProofSpineTarget
    unfold ProductRestrictedParamsPolicyEndToEndScoreWindow.restrictedParamsPolicyEndToEndScoreWindowTarget
    unfold ProductRestrictedParamsScorePreservationDischarge.restrictedParamsScorePreservationDischargeTarget

    exact
      ProductRestrictedParamsScorePreservingUpdate.restrictedParams_scorePreservingUpdate_baseWindow_to_baseAndUpdatedWindowTarget
        p
        y
        (productUpdateState p)
        productScore
        (ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedUpdate
          p
          y
          (productUpdateState p))
        (ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedScore
          p
          y
          (productUpdateState p)
          productScore)
        (ProductFixedSet p y)
        thresholdLo
        thresholdHi
        hThreshold
        hBaseTarget
        hScorePreserved

end ProductRestrictedParamsProofSpineScoreWindowCharacterization

end VFH2
