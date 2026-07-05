import VFH2.Product.ProductRestrictedParamsBridgeCorePivot
import VFH2.Product.ProductUpdateTransport

namespace VFH2

namespace ProductRestrictedParamsUpdateScoreBridge

abbrev restrictedParamsTypedUpdateScoreCarrier
    (p : VFH2.ProductRestrictedParams)
    (x : p.State)
    (productUpdate : p.State → p.State) :=
  { t //
      t = VFH2.ProductStateTransport.productToTyped x ∨
        t = VFH2.ProductStateTransport.productToTyped (productUpdate x) }

def restrictedParamsUpdateScoreAlignment
    (p : VFH2.ProductRestrictedParams)
    (x : p.State)
    (productUpdate : p.State → p.State)
    (productScore : p.State → Int)
    (typedUpdate :
      restrictedParamsTypedUpdateScoreCarrier p x productUpdate →
        restrictedParamsTypedUpdateScoreCarrier p x productUpdate)
    (typedScore :
      restrictedParamsTypedUpdateScoreCarrier p x productUpdate → Int) : Prop :=
  typedUpdate ⟨VFH2.ProductStateTransport.productToTyped x, Or.inl rfl⟩ =
      ⟨VFH2.ProductStateTransport.productToTyped (productUpdate x), Or.inr rfl⟩ ∧
    typedScore ⟨VFH2.ProductStateTransport.productToTyped x, Or.inl rfl⟩ =
      productScore x ∧
    typedScore ⟨VFH2.ProductStateTransport.productToTyped (productUpdate x), Or.inr rfl⟩ =
      productScore (productUpdate x)

def restrictedParamsUpdateScoreBridgeSource
    (p : VFH2.ProductRestrictedParams)
    (x : p.State)
    (productUpdate : p.State → p.State)
    (productScore : p.State → Int)
    (typedUpdate :
      restrictedParamsTypedUpdateScoreCarrier p x productUpdate →
        restrictedParamsTypedUpdateScoreCarrier p x productUpdate)
    (typedScore :
      restrictedParamsTypedUpdateScoreCarrier p x productUpdate → Int)
    (fixed : Prop)
    (effect thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi) : Prop :=
  restrictedParamsUpdateScoreAlignment
      p x productUpdate productScore typedUpdate typedScore ∧
    VFH2.ProductRestrictedParamsBridgeCorePivot.restrictedParamsSelfBridgeCoreSource
      p x fixed effect thresholdLo thresholdHi hThreshold

def restrictedParamsUpdateScoreBridgeTarget
    (p : VFH2.ProductRestrictedParams)
    (x : p.State)
    (productUpdate : p.State → p.State)
    (productScore : p.State → Int)
    (typedUpdate :
      restrictedParamsTypedUpdateScoreCarrier p x productUpdate →
        restrictedParamsTypedUpdateScoreCarrier p x productUpdate)
    (typedScore :
      restrictedParamsTypedUpdateScoreCarrier p x productUpdate → Int)
    (fixed : Prop)
    (effect thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi) : Prop :=
  restrictedParamsUpdateScoreAlignment
      p x productUpdate productScore typedUpdate typedScore ∧
    VFH2.ProductRestrictedParamsBridgeCorePivot.restrictedParamsSelfBridgeCoreTarget
      p x fixed effect thresholdLo thresholdHi hThreshold

theorem restrictedParams_updateScoreBridgePivot_theorem
    (p : VFH2.ProductRestrictedParams)
    (x : p.State)
    (productUpdate : p.State → p.State)
    (productScore : p.State → Int)
    (typedUpdate :
      restrictedParamsTypedUpdateScoreCarrier p x productUpdate →
        restrictedParamsTypedUpdateScoreCarrier p x productUpdate)
    (typedScore :
      restrictedParamsTypedUpdateScoreCarrier p x productUpdate → Int)
    (fixed : Prop)
    (effect thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi)
    (hSource :
      restrictedParamsUpdateScoreBridgeSource
        p x productUpdate productScore typedUpdate typedScore
        fixed effect thresholdLo thresholdHi hThreshold) :
    restrictedParamsUpdateScoreBridgeTarget
      p x productUpdate productScore typedUpdate typedScore
      fixed effect thresholdLo thresholdHi hThreshold := by
  unfold restrictedParamsUpdateScoreBridgeSource at hSource
  unfold restrictedParamsUpdateScoreBridgeTarget
  exact ⟨
    hSource.1,
    VFH2.ProductRestrictedParamsBridgeCorePivot.restrictedParams_selfBridgeCorePivot_theorem
      p x fixed effect thresholdLo thresholdHi hThreshold hSource.2
  ⟩

theorem restrictedParams_updateScoreBridgePivot_from_existingRestrictedTransport
    (p : VFH2.ProductRestrictedParams)
    (x : p.State)
    (productUpdate : p.State → p.State)
    (productScore : p.State → Int)
    (typedUpdate :
      restrictedParamsTypedUpdateScoreCarrier p x productUpdate →
        restrictedParamsTypedUpdateScoreCarrier p x productUpdate)
    (typedScore :
      restrictedParamsTypedUpdateScoreCarrier p x productUpdate → Int)
    (fixed : Prop)
    (effect thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi)
    (hTypedUpdate :
      typedUpdate ⟨VFH2.ProductStateTransport.productToTyped x, Or.inl rfl⟩ =
        ⟨VFH2.ProductStateTransport.productToTyped (productUpdate x), Or.inr rfl⟩)
    (hBase :
      typedScore ⟨VFH2.ProductStateTransport.productToTyped x, Or.inl rfl⟩ =
        productScore x)
    (hUpdated :
      typedScore ⟨VFH2.ProductStateTransport.productToTyped (productUpdate x), Or.inr rfl⟩ =
        productScore (productUpdate x))
    (hLowerBridgeStrong :
      ProductBridgeGeneralization.genericBridgeTarget fixed
        (thresholdHi ≤ effect))
    (hUpperBridgeStrong :
      ProductBridgeGeneralization.genericBridgeTarget fixed
        (effect ≤ thresholdLo)) :
    restrictedParamsUpdateScoreBridgeTarget
      p x productUpdate productScore typedUpdate typedScore
      fixed effect thresholdLo thresholdHi hThreshold := by
  unfold restrictedParamsUpdateScoreBridgeTarget
  exact ⟨
    ⟨hTypedUpdate, hBase, hUpdated⟩,
    VFH2.ProductRestrictedParamsBridgeCorePivot.restrictedParams_selfBridgeCorePivot_from_existingRestrictedTransport
      p x fixed effect thresholdLo thresholdHi hThreshold
      hLowerBridgeStrong hUpperBridgeStrong
  ⟩

theorem restrictedParams_updateScoreAlignment_preserved
    (p : VFH2.ProductRestrictedParams)
    (x : p.State)
    (productUpdate : p.State → p.State)
    (productScore : p.State → Int)
    (typedUpdate :
      restrictedParamsTypedUpdateScoreCarrier p x productUpdate →
        restrictedParamsTypedUpdateScoreCarrier p x productUpdate)
    (typedScore :
      restrictedParamsTypedUpdateScoreCarrier p x productUpdate → Int)
    (fixed : Prop)
    (effect thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi)
    (hSource :
      restrictedParamsUpdateScoreBridgeSource
        p x productUpdate productScore typedUpdate typedScore
        fixed effect thresholdLo thresholdHi hThreshold) :
    restrictedParamsUpdateScoreAlignment
      p x productUpdate productScore typedUpdate typedScore := by
  unfold restrictedParamsUpdateScoreBridgeSource at hSource
  exact hSource.1

theorem restrictedParams_updateScoreBridgePivot_coreTarget_projection
    (p : VFH2.ProductRestrictedParams)
    (x : p.State)
    (productUpdate : p.State → p.State)
    (productScore : p.State → Int)
    (typedUpdate :
      restrictedParamsTypedUpdateScoreCarrier p x productUpdate →
        restrictedParamsTypedUpdateScoreCarrier p x productUpdate)
    (typedScore :
      restrictedParamsTypedUpdateScoreCarrier p x productUpdate → Int)
    (fixed : Prop)
    (effect thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi)
    (hSource :
      restrictedParamsUpdateScoreBridgeSource
        p x productUpdate productScore typedUpdate typedScore
        fixed effect thresholdLo thresholdHi hThreshold) :
    VFH2.ProductRestrictedParamsBridgeCorePivot.restrictedParamsSelfBridgeCoreTarget
      p x fixed effect thresholdLo thresholdHi hThreshold := by
  have hTarget :
      restrictedParamsUpdateScoreBridgeTarget
        p x productUpdate productScore typedUpdate typedScore
        fixed effect thresholdLo thresholdHi hThreshold :=
    restrictedParams_updateScoreBridgePivot_theorem
      p x productUpdate productScore typedUpdate typedScore
      fixed effect thresholdLo thresholdHi hThreshold hSource
  unfold restrictedParamsUpdateScoreBridgeTarget at hTarget
  exact hTarget.2

theorem restrictedParams_updateScoreBridgePivot_lower_projection
    (p : VFH2.ProductRestrictedParams)
    (x : p.State)
    (productUpdate : p.State → p.State)
    (productScore : p.State → Int)
    (typedUpdate :
      restrictedParamsTypedUpdateScoreCarrier p x productUpdate →
        restrictedParamsTypedUpdateScoreCarrier p x productUpdate)
    (typedScore :
      restrictedParamsTypedUpdateScoreCarrier p x productUpdate → Int)
    (fixed : Prop)
    (effect thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi)
    (hSource :
      restrictedParamsUpdateScoreBridgeSource
        p x productUpdate productScore typedUpdate typedScore
        fixed effect thresholdLo thresholdHi hThreshold) :
    ProductBridgeGeneralization.genericBridgeTarget fixed
      (thresholdLo ≤ effect) := by
  have hCore :
      VFH2.ProductRestrictedParamsBridgeCorePivot.restrictedParamsSelfBridgeCoreTarget
        p x fixed effect thresholdLo thresholdHi hThreshold :=
    restrictedParams_updateScoreBridgePivot_coreTarget_projection
      p x productUpdate productScore typedUpdate typedScore
      fixed effect thresholdLo thresholdHi hThreshold hSource
  unfold VFH2.ProductRestrictedParamsBridgeCorePivot.restrictedParamsSelfBridgeCoreTarget at hCore
  exact hCore.2.1

theorem restrictedParams_updateScoreBridgePivot_upper_projection
    (p : VFH2.ProductRestrictedParams)
    (x : p.State)
    (productUpdate : p.State → p.State)
    (productScore : p.State → Int)
    (typedUpdate :
      restrictedParamsTypedUpdateScoreCarrier p x productUpdate →
        restrictedParamsTypedUpdateScoreCarrier p x productUpdate)
    (typedScore :
      restrictedParamsTypedUpdateScoreCarrier p x productUpdate → Int)
    (fixed : Prop)
    (effect thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi)
    (hSource :
      restrictedParamsUpdateScoreBridgeSource
        p x productUpdate productScore typedUpdate typedScore
        fixed effect thresholdLo thresholdHi hThreshold) :
    ProductBridgeGeneralization.genericBridgeTarget fixed
      (effect ≤ thresholdHi) := by
  have hCore :
      VFH2.ProductRestrictedParamsBridgeCorePivot.restrictedParamsSelfBridgeCoreTarget
        p x fixed effect thresholdLo thresholdHi hThreshold :=
    restrictedParams_updateScoreBridgePivot_coreTarget_projection
      p x productUpdate productScore typedUpdate typedScore
      fixed effect thresholdLo thresholdHi hThreshold hSource
  unfold VFH2.ProductRestrictedParamsBridgeCorePivot.restrictedParamsSelfBridgeCoreTarget at hCore
  exact hCore.2.2

theorem restrictedParams_updateScoreBridgePivot_certificate_projection
    (p : VFH2.ProductRestrictedParams)
    (x : p.State)
    (productUpdate : p.State → p.State)
    (productScore : p.State → Int)
    (typedUpdate :
      restrictedParamsTypedUpdateScoreCarrier p x productUpdate →
        restrictedParamsTypedUpdateScoreCarrier p x productUpdate)
    (typedScore :
      restrictedParamsTypedUpdateScoreCarrier p x productUpdate → Int)
    (fixed : Prop)
    (effect thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi)
    (hSource :
      restrictedParamsUpdateScoreBridgeSource
        p x productUpdate productScore typedUpdate typedScore
        fixed effect thresholdLo thresholdHi hThreshold) :
    VFH2.ProductEffectBoundConditionMonotonicity.RestrictedEffectBoundMonotoneTransportCertificate
      p x thresholdLo thresholdHi hThreshold := by
  have hCore :
      VFH2.ProductRestrictedParamsBridgeCorePivot.restrictedParamsSelfBridgeCoreTarget
        p x fixed effect thresholdLo thresholdHi hThreshold :=
    restrictedParams_updateScoreBridgePivot_coreTarget_projection
      p x productUpdate productScore typedUpdate typedScore
      fixed effect thresholdLo thresholdHi hThreshold hSource
  unfold VFH2.ProductRestrictedParamsBridgeCorePivot.restrictedParamsSelfBridgeCoreTarget at hCore
  exact hCore.1

end ProductRestrictedParamsUpdateScoreBridge

end VFH2
