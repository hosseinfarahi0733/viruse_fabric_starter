import VFH2.Product.ProductRestrictedParamsPolicyEndToEndScoreWindow
import VFH2.Product.ProductRestrictedParamsSourceCertificateFrozenSpine
import VFH2.Product.ProductRestrictedParamsEffectBaseSourceFrozenSpine

namespace VFH2
namespace ProductRestrictedParamsPolicyEndToEndFrozenSpineBridge

/--
v16.8.0:
An existing policy end-to-end score-window source contains the raw update-score
transport source material: raw equalities plus the two bridge-side assumptions.
This is an upstream derivation of the raw transport source, not a new wrapper.
-/
theorem restrictedParams_policyEndToEndSource_to_rawUpdateScoreTransportSource
  (p : VFH2.ProductRestrictedParams)
  (x : p.State)
  (productUpdate : p.State → p.State)
  (productScore : p.State → Int)
  (typedUpdate :
    VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsUpdateScoreTransportCarrier
      p x productUpdate →
    VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsUpdateScoreTransportCarrier
      p x productUpdate)
  (typedScore :
    VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsUpdateScoreTransportCarrier
      p x productUpdate →
    Int)
  (fixed : Prop)
  (baseEffect thresholdLo thresholdHi : Int)
  (hSource :
    VFH2.ProductRestrictedParamsPolicyEndToEndScoreWindow.restrictedParamsPolicyEndToEndScoreWindowSource
      p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi) :
  VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsRawUpdateScoreTransportSource
    p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi := by
  exact
    ⟨⟨hSource.hTypedUpdate, hSource.hBaseScore, hSource.hUpdatedScore⟩,
      hSource.hBaseLowerBridgeStrong,
      hSource.hBaseUpperBridgeStrong⟩

/--
v16.8.0:
The policy end-to-end score-window source also derives the v16.6 effect-base
source, because it contains both `baseEffect = productScore x` and the raw
update-score transport source material.
-/
theorem restrictedParams_policyEndToEndSource_to_effectBaseSource
  (p : VFH2.ProductRestrictedParams)
  (x : p.State)
  (productUpdate : p.State → p.State)
  (productScore : p.State → Int)
  (typedUpdate :
    VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsUpdateScoreTransportCarrier
      p x productUpdate →
    VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsUpdateScoreTransportCarrier
      p x productUpdate)
  (typedScore :
    VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsUpdateScoreTransportCarrier
      p x productUpdate →
    Int)
  (fixed : Prop)
  (baseEffect thresholdLo thresholdHi : Int)
  (hSource :
    VFH2.ProductRestrictedParamsPolicyEndToEndScoreWindow.restrictedParamsPolicyEndToEndScoreWindowSource
      p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi) :
  VFH2.ProductRestrictedParamsEffectBaseSourceFrozenSpine.restrictedParamsEffectBaseSource
    p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi := by
  exact
    ⟨hSource.hEffectBase,
      restrictedParams_policyEndToEndSource_to_rawUpdateScoreTransportSource
        p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi hSource⟩

/--
v16.8.0:
Policy end-to-end source directly reaches the frozen restricted proof spine
target by deriving the raw transport source and reusing the v16.4 source bridge.
-/
theorem restrictedParams_policyEndToEndSource_to_restrictedProofSpineTarget
  (p : VFH2.ProductRestrictedParams)
  (x : p.State)
  (productUpdate : p.State → p.State)
  (productScore : p.State → Int)
  (typedUpdate :
    VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsUpdateScoreTransportCarrier
      p x productUpdate →
    VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsUpdateScoreTransportCarrier
      p x productUpdate)
  (typedScore :
    VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsUpdateScoreTransportCarrier
      p x productUpdate →
    Int)
  (fixed : Prop)
  (baseEffect thresholdLo thresholdHi : Int)
  (hThreshold : thresholdLo ≤ thresholdHi)
  (hSource :
    VFH2.ProductRestrictedParamsPolicyEndToEndScoreWindow.restrictedParamsPolicyEndToEndScoreWindowSource
      p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi) :
  VFH2.ProductRestrictedParamsRestrictedProofSpineFreeze.restrictedProofSpineTarget
    p x productUpdate productScore typedUpdate typedScore fixed thresholdLo thresholdHi hThreshold := by
  exact
    VFH2.ProductRestrictedParamsSourceCertificateFrozenSpine.restrictedParams_rawUpdateScoreTransportSource_to_restrictedProofSpineTarget_noExtraBridge
      p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi hThreshold
      hSource.hEffectBase
      hSource.hPolicy
      (restrictedParams_policyEndToEndSource_to_rawUpdateScoreTransportSource
        p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi hSource)

/--
v16.8.0:
Policy end-to-end source directly reaches frozen updated score-window bounds.
-/
theorem restrictedParams_policyEndToEndSource_to_frozenUpdatedBounds
  (p : VFH2.ProductRestrictedParams)
  (x : p.State)
  (productUpdate : p.State → p.State)
  (productScore : p.State → Int)
  (typedUpdate :
    VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsUpdateScoreTransportCarrier
      p x productUpdate →
    VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsUpdateScoreTransportCarrier
      p x productUpdate)
  (typedScore :
    VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsUpdateScoreTransportCarrier
      p x productUpdate →
    Int)
  (fixed : Prop)
  (baseEffect thresholdLo thresholdHi : Int)
  (hThreshold : thresholdLo ≤ thresholdHi)
  (hSource :
    VFH2.ProductRestrictedParamsPolicyEndToEndScoreWindow.restrictedParamsPolicyEndToEndScoreWindowSource
      p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi) :
  VFH2.ProductRestrictedParamsRestrictedProofSpineFreeze.restrictedProofSpineUpdatedScoreWindowBounds
    p x productUpdate productScore fixed thresholdLo thresholdHi := by
  exact
    VFH2.ProductRestrictedParamsSourceCertificateFrozenSpine.restrictedParams_rawUpdateScoreTransportSource_to_updatedBounds_noExtraBridge
      p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi hThreshold
      hSource.hEffectBase
      hSource.hPolicy
      (restrictedParams_policyEndToEndSource_to_rawUpdateScoreTransportSource
        p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi hSource)

/--
v16.8.0:
Policy end-to-end source directly reaches the lower frozen updated score-window side.
-/
theorem restrictedParams_policyEndToEndSource_to_frozenUpdatedLower
  (p : VFH2.ProductRestrictedParams)
  (x : p.State)
  (productUpdate : p.State → p.State)
  (productScore : p.State → Int)
  (typedUpdate :
    VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsUpdateScoreTransportCarrier
      p x productUpdate →
    VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsUpdateScoreTransportCarrier
      p x productUpdate)
  (typedScore :
    VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsUpdateScoreTransportCarrier
      p x productUpdate →
    Int)
  (fixed : Prop)
  (baseEffect thresholdLo thresholdHi : Int)
  (hThreshold : thresholdLo ≤ thresholdHi)
  (hSource :
    VFH2.ProductRestrictedParamsPolicyEndToEndScoreWindow.restrictedParamsPolicyEndToEndScoreWindowSource
      p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi) :
  VFH2.ProductBridgeGeneralization.genericBridgeTarget fixed
    (thresholdLo ≤ productScore (productUpdate x)) := by
  exact
    VFH2.ProductRestrictedParamsSourceCertificateFrozenSpine.restrictedParams_rawUpdateScoreTransportSource_to_updatedLower_noExtraBridge
      p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi hThreshold
      hSource.hEffectBase
      hSource.hPolicy
      (restrictedParams_policyEndToEndSource_to_rawUpdateScoreTransportSource
        p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi hSource)

/--
v16.8.0:
Policy end-to-end source directly reaches the upper frozen updated score-window side.
-/
theorem restrictedParams_policyEndToEndSource_to_frozenUpdatedUpper
  (p : VFH2.ProductRestrictedParams)
  (x : p.State)
  (productUpdate : p.State → p.State)
  (productScore : p.State → Int)
  (typedUpdate :
    VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsUpdateScoreTransportCarrier
      p x productUpdate →
    VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsUpdateScoreTransportCarrier
      p x productUpdate)
  (typedScore :
    VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsUpdateScoreTransportCarrier
      p x productUpdate →
    Int)
  (fixed : Prop)
  (baseEffect thresholdLo thresholdHi : Int)
  (hThreshold : thresholdLo ≤ thresholdHi)
  (hSource :
    VFH2.ProductRestrictedParamsPolicyEndToEndScoreWindow.restrictedParamsPolicyEndToEndScoreWindowSource
      p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi) :
  VFH2.ProductBridgeGeneralization.genericBridgeTarget fixed
    (productScore (productUpdate x) ≤ thresholdHi) := by
  exact
    VFH2.ProductRestrictedParamsSourceCertificateFrozenSpine.restrictedParams_rawUpdateScoreTransportSource_to_updatedUpper_noExtraBridge
      p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi hThreshold
      hSource.hEffectBase
      hSource.hPolicy
      (restrictedParams_policyEndToEndSource_to_rawUpdateScoreTransportSource
        p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi hSource)

end ProductRestrictedParamsPolicyEndToEndFrozenSpineBridge
end VFH2
