import VFH2.Product.ProductRestrictedParamsUpdateScoreBridge

namespace VFH2

namespace ProductRestrictedParamsUpdateScoreTransport

abbrev restrictedParamsUpdateScoreTransportCarrier
    (p : VFH2.ProductRestrictedParams)
    (x : p.State)
    (productUpdate : p.State → p.State) :=
  VFH2.ProductRestrictedParamsUpdateScoreBridge.restrictedParamsTypedUpdateScoreCarrier
    p x productUpdate

def restrictedParamsRawUpdateScoreTransportCertificate
    (p : VFH2.ProductRestrictedParams)
    (x : p.State)
    (productUpdate : p.State → p.State)
    (productScore : p.State → Int)
    (typedUpdate :
      restrictedParamsUpdateScoreTransportCarrier p x productUpdate →
        restrictedParamsUpdateScoreTransportCarrier p x productUpdate)
    (typedScore :
      restrictedParamsUpdateScoreTransportCarrier p x productUpdate → Int) : Prop :=
  typedUpdate ⟨VFH2.ProductStateTransport.productToTyped x, Or.inl rfl⟩ =
      ⟨VFH2.ProductStateTransport.productToTyped (productUpdate x), Or.inr rfl⟩ ∧
    typedScore ⟨VFH2.ProductStateTransport.productToTyped x, Or.inl rfl⟩ =
      productScore x ∧
    typedScore ⟨VFH2.ProductStateTransport.productToTyped (productUpdate x), Or.inr rfl⟩ =
      productScore (productUpdate x)

def restrictedParamsRawUpdateScoreTransportSource
    (p : VFH2.ProductRestrictedParams)
    (x : p.State)
    (productUpdate : p.State → p.State)
    (productScore : p.State → Int)
    (typedUpdate :
      restrictedParamsUpdateScoreTransportCarrier p x productUpdate →
        restrictedParamsUpdateScoreTransportCarrier p x productUpdate)
    (typedScore :
      restrictedParamsUpdateScoreTransportCarrier p x productUpdate → Int)
    (fixed : Prop)
    (effect thresholdLo thresholdHi : Int) : Prop :=
  restrictedParamsRawUpdateScoreTransportCertificate
      p x productUpdate productScore typedUpdate typedScore ∧
    ProductBridgeGeneralization.genericBridgeTarget fixed
      (thresholdHi ≤ effect) ∧
    ProductBridgeGeneralization.genericBridgeTarget fixed
      (effect ≤ thresholdLo)

def restrictedParamsUpdateScoreTransportBridgeTarget
    (p : VFH2.ProductRestrictedParams)
    (x : p.State)
    (productUpdate : p.State → p.State)
    (productScore : p.State → Int)
    (typedUpdate :
      restrictedParamsUpdateScoreTransportCarrier p x productUpdate →
        restrictedParamsUpdateScoreTransportCarrier p x productUpdate)
    (typedScore :
      restrictedParamsUpdateScoreTransportCarrier p x productUpdate → Int)
    (fixed : Prop)
    (effect thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi) : Prop :=
  restrictedParamsRawUpdateScoreTransportCertificate
      p x productUpdate productScore typedUpdate typedScore ∧
    VFH2.ProductRestrictedParamsUpdateScoreBridge.restrictedParamsUpdateScoreBridgeTarget
      p x productUpdate productScore typedUpdate typedScore
      fixed effect thresholdLo thresholdHi hThreshold

theorem restrictedParams_rawUpdateScoreTransport_to_bridgeTarget
    (p : VFH2.ProductRestrictedParams)
    (x : p.State)
    (productUpdate : p.State → p.State)
    (productScore : p.State → Int)
    (typedUpdate :
      restrictedParamsUpdateScoreTransportCarrier p x productUpdate →
        restrictedParamsUpdateScoreTransportCarrier p x productUpdate)
    (typedScore :
      restrictedParamsUpdateScoreTransportCarrier p x productUpdate → Int)
    (fixed : Prop)
    (effect thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi)
    (hSource :
      restrictedParamsRawUpdateScoreTransportSource
        p x productUpdate productScore typedUpdate typedScore
        fixed effect thresholdLo thresholdHi) :
    restrictedParamsUpdateScoreTransportBridgeTarget
      p x productUpdate productScore typedUpdate typedScore
      fixed effect thresholdLo thresholdHi hThreshold := by
  unfold restrictedParamsRawUpdateScoreTransportSource at hSource
  unfold restrictedParamsUpdateScoreTransportBridgeTarget
  exact ⟨
    hSource.1,
    VFH2.ProductRestrictedParamsUpdateScoreBridge.restrictedParams_updateScoreBridgePivot_from_existingRestrictedTransport
      p x productUpdate productScore typedUpdate typedScore
      fixed effect thresholdLo thresholdHi hThreshold
      hSource.1.1 hSource.1.2.1 hSource.1.2.2
      hSource.2.1 hSource.2.2
  ⟩

theorem restrictedParams_rawUpdateScoreTransport_certificate_preserved
    (p : VFH2.ProductRestrictedParams)
    (x : p.State)
    (productUpdate : p.State → p.State)
    (productScore : p.State → Int)
    (typedUpdate :
      restrictedParamsUpdateScoreTransportCarrier p x productUpdate →
        restrictedParamsUpdateScoreTransportCarrier p x productUpdate)
    (typedScore :
      restrictedParamsUpdateScoreTransportCarrier p x productUpdate → Int)
    (fixed : Prop)
    (effect thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi)
    (hSource :
      restrictedParamsRawUpdateScoreTransportSource
        p x productUpdate productScore typedUpdate typedScore
        fixed effect thresholdLo thresholdHi) :
    restrictedParamsRawUpdateScoreTransportCertificate
      p x productUpdate productScore typedUpdate typedScore := by
  have hTarget :
      restrictedParamsUpdateScoreTransportBridgeTarget
        p x productUpdate productScore typedUpdate typedScore
        fixed effect thresholdLo thresholdHi hThreshold :=
    restrictedParams_rawUpdateScoreTransport_to_bridgeTarget
      p x productUpdate productScore typedUpdate typedScore
      fixed effect thresholdLo thresholdHi hThreshold hSource
  unfold restrictedParamsUpdateScoreTransportBridgeTarget at hTarget
  exact hTarget.1

theorem restrictedParams_rawUpdateScoreTransport_update_projection
    (p : VFH2.ProductRestrictedParams)
    (x : p.State)
    (productUpdate : p.State → p.State)
    (productScore : p.State → Int)
    (typedUpdate :
      restrictedParamsUpdateScoreTransportCarrier p x productUpdate →
        restrictedParamsUpdateScoreTransportCarrier p x productUpdate)
    (typedScore :
      restrictedParamsUpdateScoreTransportCarrier p x productUpdate → Int)
    (fixed : Prop)
    (effect thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi)
    (hSource :
      restrictedParamsRawUpdateScoreTransportSource
        p x productUpdate productScore typedUpdate typedScore
        fixed effect thresholdLo thresholdHi) :
    typedUpdate ⟨VFH2.ProductStateTransport.productToTyped x, Or.inl rfl⟩ =
      ⟨VFH2.ProductStateTransport.productToTyped (productUpdate x), Or.inr rfl⟩ := by
  exact (restrictedParams_rawUpdateScoreTransport_certificate_preserved
    p x productUpdate productScore typedUpdate typedScore
    fixed effect thresholdLo thresholdHi hThreshold hSource).1

theorem restrictedParams_rawUpdateScoreTransport_baseScore_projection
    (p : VFH2.ProductRestrictedParams)
    (x : p.State)
    (productUpdate : p.State → p.State)
    (productScore : p.State → Int)
    (typedUpdate :
      restrictedParamsUpdateScoreTransportCarrier p x productUpdate →
        restrictedParamsUpdateScoreTransportCarrier p x productUpdate)
    (typedScore :
      restrictedParamsUpdateScoreTransportCarrier p x productUpdate → Int)
    (fixed : Prop)
    (effect thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi)
    (hSource :
      restrictedParamsRawUpdateScoreTransportSource
        p x productUpdate productScore typedUpdate typedScore
        fixed effect thresholdLo thresholdHi) :
    typedScore ⟨VFH2.ProductStateTransport.productToTyped x, Or.inl rfl⟩ =
      productScore x := by
  exact (restrictedParams_rawUpdateScoreTransport_certificate_preserved
    p x productUpdate productScore typedUpdate typedScore
    fixed effect thresholdLo thresholdHi hThreshold hSource).2.1

theorem restrictedParams_rawUpdateScoreTransport_updatedScore_projection
    (p : VFH2.ProductRestrictedParams)
    (x : p.State)
    (productUpdate : p.State → p.State)
    (productScore : p.State → Int)
    (typedUpdate :
      restrictedParamsUpdateScoreTransportCarrier p x productUpdate →
        restrictedParamsUpdateScoreTransportCarrier p x productUpdate)
    (typedScore :
      restrictedParamsUpdateScoreTransportCarrier p x productUpdate → Int)
    (fixed : Prop)
    (effect thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi)
    (hSource :
      restrictedParamsRawUpdateScoreTransportSource
        p x productUpdate productScore typedUpdate typedScore
        fixed effect thresholdLo thresholdHi) :
    typedScore ⟨VFH2.ProductStateTransport.productToTyped (productUpdate x), Or.inr rfl⟩ =
      productScore (productUpdate x) := by
  exact (restrictedParams_rawUpdateScoreTransport_certificate_preserved
    p x productUpdate productScore typedUpdate typedScore
    fixed effect thresholdLo thresholdHi hThreshold hSource).2.2

theorem restrictedParams_rawUpdateScoreTransport_bridgeTarget_projection
    (p : VFH2.ProductRestrictedParams)
    (x : p.State)
    (productUpdate : p.State → p.State)
    (productScore : p.State → Int)
    (typedUpdate :
      restrictedParamsUpdateScoreTransportCarrier p x productUpdate →
        restrictedParamsUpdateScoreTransportCarrier p x productUpdate)
    (typedScore :
      restrictedParamsUpdateScoreTransportCarrier p x productUpdate → Int)
    (fixed : Prop)
    (effect thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi)
    (hSource :
      restrictedParamsRawUpdateScoreTransportSource
        p x productUpdate productScore typedUpdate typedScore
        fixed effect thresholdLo thresholdHi) :
    VFH2.ProductRestrictedParamsUpdateScoreBridge.restrictedParamsUpdateScoreBridgeTarget
      p x productUpdate productScore typedUpdate typedScore
      fixed effect thresholdLo thresholdHi hThreshold := by
  have hTarget :
      restrictedParamsUpdateScoreTransportBridgeTarget
        p x productUpdate productScore typedUpdate typedScore
        fixed effect thresholdLo thresholdHi hThreshold :=
    restrictedParams_rawUpdateScoreTransport_to_bridgeTarget
      p x productUpdate productScore typedUpdate typedScore
      fixed effect thresholdLo thresholdHi hThreshold hSource
  unfold restrictedParamsUpdateScoreTransportBridgeTarget at hTarget
  exact hTarget.2

theorem restrictedParams_rawUpdateScoreTransport_lower_projection
    (p : VFH2.ProductRestrictedParams)
    (x : p.State)
    (productUpdate : p.State → p.State)
    (productScore : p.State → Int)
    (typedUpdate :
      restrictedParamsUpdateScoreTransportCarrier p x productUpdate →
        restrictedParamsUpdateScoreTransportCarrier p x productUpdate)
    (typedScore :
      restrictedParamsUpdateScoreTransportCarrier p x productUpdate → Int)
    (fixed : Prop)
    (effect thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi)
    (hSource :
      restrictedParamsRawUpdateScoreTransportSource
        p x productUpdate productScore typedUpdate typedScore
        fixed effect thresholdLo thresholdHi) :
    ProductBridgeGeneralization.genericBridgeTarget fixed
      (thresholdLo ≤ effect) := by
  have hBridge :
      VFH2.ProductRestrictedParamsUpdateScoreBridge.restrictedParamsUpdateScoreBridgeTarget
        p x productUpdate productScore typedUpdate typedScore
        fixed effect thresholdLo thresholdHi hThreshold :=
    restrictedParams_rawUpdateScoreTransport_bridgeTarget_projection
      p x productUpdate productScore typedUpdate typedScore
      fixed effect thresholdLo thresholdHi hThreshold hSource
  unfold VFH2.ProductRestrictedParamsUpdateScoreBridge.restrictedParamsUpdateScoreBridgeTarget at hBridge
  unfold VFH2.ProductRestrictedParamsBridgeCorePivot.restrictedParamsSelfBridgeCoreTarget at hBridge
  exact hBridge.2.2.1

theorem restrictedParams_rawUpdateScoreTransport_upper_projection
    (p : VFH2.ProductRestrictedParams)
    (x : p.State)
    (productUpdate : p.State → p.State)
    (productScore : p.State → Int)
    (typedUpdate :
      restrictedParamsUpdateScoreTransportCarrier p x productUpdate →
        restrictedParamsUpdateScoreTransportCarrier p x productUpdate)
    (typedScore :
      restrictedParamsUpdateScoreTransportCarrier p x productUpdate → Int)
    (fixed : Prop)
    (effect thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi)
    (hSource :
      restrictedParamsRawUpdateScoreTransportSource
        p x productUpdate productScore typedUpdate typedScore
        fixed effect thresholdLo thresholdHi) :
    ProductBridgeGeneralization.genericBridgeTarget fixed
      (effect ≤ thresholdHi) := by
  have hBridge :
      VFH2.ProductRestrictedParamsUpdateScoreBridge.restrictedParamsUpdateScoreBridgeTarget
        p x productUpdate productScore typedUpdate typedScore
        fixed effect thresholdLo thresholdHi hThreshold :=
    restrictedParams_rawUpdateScoreTransport_bridgeTarget_projection
      p x productUpdate productScore typedUpdate typedScore
      fixed effect thresholdLo thresholdHi hThreshold hSource
  unfold VFH2.ProductRestrictedParamsUpdateScoreBridge.restrictedParamsUpdateScoreBridgeTarget at hBridge
  unfold VFH2.ProductRestrictedParamsBridgeCorePivot.restrictedParamsSelfBridgeCoreTarget at hBridge
  exact hBridge.2.2.2

theorem restrictedParams_rawUpdateScoreTransport_restrictedCertificate_projection
    (p : VFH2.ProductRestrictedParams)
    (x : p.State)
    (productUpdate : p.State → p.State)
    (productScore : p.State → Int)
    (typedUpdate :
      restrictedParamsUpdateScoreTransportCarrier p x productUpdate →
        restrictedParamsUpdateScoreTransportCarrier p x productUpdate)
    (typedScore :
      restrictedParamsUpdateScoreTransportCarrier p x productUpdate → Int)
    (fixed : Prop)
    (effect thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi)
    (hSource :
      restrictedParamsRawUpdateScoreTransportSource
        p x productUpdate productScore typedUpdate typedScore
        fixed effect thresholdLo thresholdHi) :
    VFH2.ProductEffectBoundConditionMonotonicity.RestrictedEffectBoundMonotoneTransportCertificate
      p x thresholdLo thresholdHi hThreshold := by
  have hBridge :
      VFH2.ProductRestrictedParamsUpdateScoreBridge.restrictedParamsUpdateScoreBridgeTarget
        p x productUpdate productScore typedUpdate typedScore
        fixed effect thresholdLo thresholdHi hThreshold :=
    restrictedParams_rawUpdateScoreTransport_bridgeTarget_projection
      p x productUpdate productScore typedUpdate typedScore
      fixed effect thresholdLo thresholdHi hThreshold hSource
  unfold VFH2.ProductRestrictedParamsUpdateScoreBridge.restrictedParamsUpdateScoreBridgeTarget at hBridge
  unfold VFH2.ProductRestrictedParamsBridgeCorePivot.restrictedParamsSelfBridgeCoreTarget at hBridge
  exact hBridge.2.1

end ProductRestrictedParamsUpdateScoreTransport

end VFH2
