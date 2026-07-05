import VFH2.Product.ProductRestrictedParamsUpdateScoreTransport
import VFH2.Product.ProductRestrictedParamsRestrictedProofSpineFreeze
import VFH2.Product.ProductRestrictedParamsScorePreservationDischarge

namespace VFH2
namespace ProductRestrictedParamsRawTransportFrozenSpine

/--
v16.2.0 bridge:
A restricted raw update-score transport source supplies the three raw equalities
needed by the frozen restricted proof spine target.
-/
theorem restrictedParams_rawUpdateScoreTransportSource_to_restrictedProofSpineTarget
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
  (hEffectBase : baseEffect = productScore x)
  (hPolicy :
    VFH2.ProductRestrictedParamsScorePreservationDischarge.restrictedParamsScorePreservingUpdatePolicy
      p productUpdate productScore)
  (hSource :
    VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsRawUpdateScoreTransportSource
      p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi)
  (hBaseLowerBridgeStrong :
    VFH2.ProductBridgeGeneralization.genericBridgeTarget fixed (thresholdHi ≤ baseEffect))
  (hBaseUpperBridgeStrong :
    VFH2.ProductBridgeGeneralization.genericBridgeTarget fixed (baseEffect ≤ thresholdLo)) :
  VFH2.ProductRestrictedParamsRestrictedProofSpineFreeze.restrictedProofSpineTarget
    p x productUpdate productScore typedUpdate typedScore fixed thresholdLo thresholdHi hThreshold := by
  exact
    VFH2.ProductRestrictedParamsRestrictedProofSpineFreeze.restrictedProofSpine_rawEqualities_to_target
      p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi hThreshold
      hEffectBase
      hPolicy
      (VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParams_rawUpdateScoreTransport_update_projection
        p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi hThreshold
        hSource)
      (VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParams_rawUpdateScoreTransport_baseScore_projection
        p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi hThreshold
        hSource)
      (VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParams_rawUpdateScoreTransport_updatedScore_projection
        p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi hThreshold
        hSource)
      hBaseLowerBridgeStrong
      hBaseUpperBridgeStrong

/--
v16.2.0 bridge:
A restricted raw update-score transport source discharges the frozen restricted
updated score-window bounds once the base strong bridge assumptions are provided.
-/
theorem restrictedParams_rawUpdateScoreTransportSource_to_updatedBounds
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
  (hEffectBase : baseEffect = productScore x)
  (hPolicy :
    VFH2.ProductRestrictedParamsScorePreservationDischarge.restrictedParamsScorePreservingUpdatePolicy
      p productUpdate productScore)
  (hSource :
    VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsRawUpdateScoreTransportSource
      p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi)
  (hBaseLowerBridgeStrong :
    VFH2.ProductBridgeGeneralization.genericBridgeTarget fixed (thresholdHi ≤ baseEffect))
  (hBaseUpperBridgeStrong :
    VFH2.ProductBridgeGeneralization.genericBridgeTarget fixed (baseEffect ≤ thresholdLo)) :
  VFH2.ProductRestrictedParamsRestrictedProofSpineFreeze.restrictedProofSpineUpdatedScoreWindowBounds
    p x productUpdate productScore fixed thresholdLo thresholdHi := by
  exact
    VFH2.ProductRestrictedParamsRestrictedProofSpineFreeze.restrictedProofSpine_rawEqualities_to_updatedBounds
      p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi hThreshold
      hEffectBase
      hPolicy
      (VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParams_rawUpdateScoreTransport_update_projection
        p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi hThreshold
        hSource)
      (VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParams_rawUpdateScoreTransport_baseScore_projection
        p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi hThreshold
        hSource)
      (VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParams_rawUpdateScoreTransport_updatedScore_projection
        p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi hThreshold
        hSource)
      hBaseLowerBridgeStrong
      hBaseUpperBridgeStrong

/--
v16.2.0 bridge:
Lower updated score-window side from the restricted raw transport source.
-/
theorem restrictedParams_rawUpdateScoreTransportSource_to_updatedLower
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
  (hEffectBase : baseEffect = productScore x)
  (hPolicy :
    VFH2.ProductRestrictedParamsScorePreservationDischarge.restrictedParamsScorePreservingUpdatePolicy
      p productUpdate productScore)
  (hSource :
    VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsRawUpdateScoreTransportSource
      p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi)
  (hBaseLowerBridgeStrong :
    VFH2.ProductBridgeGeneralization.genericBridgeTarget fixed (thresholdHi ≤ baseEffect))
  (hBaseUpperBridgeStrong :
    VFH2.ProductBridgeGeneralization.genericBridgeTarget fixed (baseEffect ≤ thresholdLo)) :
  VFH2.ProductBridgeGeneralization.genericBridgeTarget fixed
    (thresholdLo ≤ productScore (productUpdate x)) := by
  exact
    VFH2.ProductRestrictedParamsRestrictedProofSpineFreeze.restrictedProofSpine_rawEqualities_to_updatedLower
      p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi hThreshold
      hEffectBase
      hPolicy
      (VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParams_rawUpdateScoreTransport_update_projection
        p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi hThreshold
        hSource)
      (VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParams_rawUpdateScoreTransport_baseScore_projection
        p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi hThreshold
        hSource)
      (VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParams_rawUpdateScoreTransport_updatedScore_projection
        p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi hThreshold
        hSource)
      hBaseLowerBridgeStrong
      hBaseUpperBridgeStrong

/--
v16.2.0 bridge:
Upper updated score-window side from the restricted raw transport source.
-/
theorem restrictedParams_rawUpdateScoreTransportSource_to_updatedUpper
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
  (hEffectBase : baseEffect = productScore x)
  (hPolicy :
    VFH2.ProductRestrictedParamsScorePreservationDischarge.restrictedParamsScorePreservingUpdatePolicy
      p productUpdate productScore)
  (hSource :
    VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsRawUpdateScoreTransportSource
      p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi)
  (hBaseLowerBridgeStrong :
    VFH2.ProductBridgeGeneralization.genericBridgeTarget fixed (thresholdHi ≤ baseEffect))
  (hBaseUpperBridgeStrong :
    VFH2.ProductBridgeGeneralization.genericBridgeTarget fixed (baseEffect ≤ thresholdLo)) :
  VFH2.ProductBridgeGeneralization.genericBridgeTarget fixed
    (productScore (productUpdate x) ≤ thresholdHi) := by
  exact
    VFH2.ProductRestrictedParamsRestrictedProofSpineFreeze.restrictedProofSpine_rawEqualities_to_updatedUpper
      p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi hThreshold
      hEffectBase
      hPolicy
      (VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParams_rawUpdateScoreTransport_update_projection
        p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi hThreshold
        hSource)
      (VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParams_rawUpdateScoreTransport_baseScore_projection
        p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi hThreshold
        hSource)
      (VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParams_rawUpdateScoreTransport_updatedScore_projection
        p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi hThreshold
        hSource)
      hBaseLowerBridgeStrong
      hBaseUpperBridgeStrong

end ProductRestrictedParamsRawTransportFrozenSpine
end VFH2
