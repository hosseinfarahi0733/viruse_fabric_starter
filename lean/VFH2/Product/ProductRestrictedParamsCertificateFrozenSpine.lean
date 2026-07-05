import VFH2.Product.ProductRestrictedParamsUpdateScoreTransport
import VFH2.Product.ProductRestrictedParamsRestrictedProofSpineFreeze
import VFH2.Product.ProductRestrictedParamsScorePreservationDischarge

namespace VFH2
namespace ProductRestrictedParamsCertificateFrozenSpine

/--
v16.3.0 certificate-only bridge:
A restricted raw update-score transport certificate directly supplies the three
raw equalities required by the frozen restricted proof spine target.
-/
theorem restrictedParams_rawUpdateScoreTransportCertificate_to_restrictedProofSpineTarget
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
  (hCert :
    VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsRawUpdateScoreTransportCertificate
      p x productUpdate productScore typedUpdate typedScore)
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
      hCert.1
      hCert.2.1
      hCert.2.2
      hBaseLowerBridgeStrong
      hBaseUpperBridgeStrong

/--
v16.3.0 certificate-only bridge:
A restricted raw update-score transport certificate discharges the frozen
restricted updated score-window bounds, given the remaining base-side assumptions.
-/
theorem restrictedParams_rawUpdateScoreTransportCertificate_to_updatedBounds
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
  (hCert :
    VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsRawUpdateScoreTransportCertificate
      p x productUpdate productScore typedUpdate typedScore)
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
      hCert.1
      hCert.2.1
      hCert.2.2
      hBaseLowerBridgeStrong
      hBaseUpperBridgeStrong

/--
v16.3.0 certificate-only bridge:
Lower updated score-window side from a restricted raw update-score transport certificate.
-/
theorem restrictedParams_rawUpdateScoreTransportCertificate_to_updatedLower
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
  (hCert :
    VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsRawUpdateScoreTransportCertificate
      p x productUpdate productScore typedUpdate typedScore)
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
      hCert.1
      hCert.2.1
      hCert.2.2
      hBaseLowerBridgeStrong
      hBaseUpperBridgeStrong

/--
v16.3.0 certificate-only bridge:
Upper updated score-window side from a restricted raw update-score transport certificate.
-/
theorem restrictedParams_rawUpdateScoreTransportCertificate_to_updatedUpper
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
  (hCert :
    VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsRawUpdateScoreTransportCertificate
      p x productUpdate productScore typedUpdate typedScore)
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
      hCert.1
      hCert.2.1
      hCert.2.2
      hBaseLowerBridgeStrong
      hBaseUpperBridgeStrong

end ProductRestrictedParamsCertificateFrozenSpine
end VFH2
