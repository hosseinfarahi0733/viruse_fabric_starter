import VFH2.Product.ProductRestrictedParamsUpdateScoreTransport
import VFH2.Product.ProductRestrictedParamsRestrictedProofSpineFreeze
import VFH2.Product.ProductRestrictedParamsScorePreservationDischarge

namespace VFH2
namespace ProductRestrictedParamsSourceCertificateFrozenSpine

/--
v16.4.0 source-to-frozen-spine bridge:
A restricted raw update-score transport source already contains both the raw
certificate and the two strong base bridge assumptions. Therefore, once the
base-effect equality and score-preservation policy are supplied, the source can
discharge the frozen restricted proof spine target without separately repeating
the bridge assumptions.
-/
theorem restrictedParams_rawUpdateScoreTransportSource_to_restrictedProofSpineTarget_noExtraBridge
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
      p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi) :
  VFH2.ProductRestrictedParamsRestrictedProofSpineFreeze.restrictedProofSpineTarget
    p x productUpdate productScore typedUpdate typedScore fixed thresholdLo thresholdHi hThreshold := by
  exact
    VFH2.ProductRestrictedParamsRestrictedProofSpineFreeze.restrictedProofSpine_rawEqualities_to_target
      p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi hThreshold
      hEffectBase
      hPolicy
      hSource.1.1
      hSource.1.2.1
      hSource.1.2.2
      hSource.2.1
      hSource.2.2

/--
v16.4.0 source-to-frozen-spine bridge:
The source bundle discharges the frozen restricted updated score-window bounds
without separately repeating the two strong bridge assumptions.
-/
theorem restrictedParams_rawUpdateScoreTransportSource_to_updatedBounds_noExtraBridge
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
      p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi) :
  VFH2.ProductRestrictedParamsRestrictedProofSpineFreeze.restrictedProofSpineUpdatedScoreWindowBounds
    p x productUpdate productScore fixed thresholdLo thresholdHi := by
  exact
    VFH2.ProductRestrictedParamsRestrictedProofSpineFreeze.restrictedProofSpine_rawEqualities_to_updatedBounds
      p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi hThreshold
      hEffectBase
      hPolicy
      hSource.1.1
      hSource.1.2.1
      hSource.1.2.2
      hSource.2.1
      hSource.2.2

/--
v16.4.0 source-to-frozen-spine bridge:
Lower updated score-window side from the source bundle, without separately
repeating the strong bridge assumptions.
-/
theorem restrictedParams_rawUpdateScoreTransportSource_to_updatedLower_noExtraBridge
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
      p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi) :
  VFH2.ProductBridgeGeneralization.genericBridgeTarget fixed
    (thresholdLo ≤ productScore (productUpdate x)) := by
  exact
    VFH2.ProductRestrictedParamsRestrictedProofSpineFreeze.restrictedProofSpine_rawEqualities_to_updatedLower
      p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi hThreshold
      hEffectBase
      hPolicy
      hSource.1.1
      hSource.1.2.1
      hSource.1.2.2
      hSource.2.1
      hSource.2.2

/--
v16.4.0 source-to-frozen-spine bridge:
Upper updated score-window side from the source bundle, without separately
repeating the strong bridge assumptions.
-/
theorem restrictedParams_rawUpdateScoreTransportSource_to_updatedUpper_noExtraBridge
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
      p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi) :
  VFH2.ProductBridgeGeneralization.genericBridgeTarget fixed
    (productScore (productUpdate x) ≤ thresholdHi) := by
  exact
    VFH2.ProductRestrictedParamsRestrictedProofSpineFreeze.restrictedProofSpine_rawEqualities_to_updatedUpper
      p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi hThreshold
      hEffectBase
      hPolicy
      hSource.1.1
      hSource.1.2.1
      hSource.1.2.2
      hSource.2.1
      hSource.2.2

end ProductRestrictedParamsSourceCertificateFrozenSpine
end VFH2
