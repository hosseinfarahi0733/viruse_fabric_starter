import VFH2.Product.ProductRestrictedParamsScorePreservingUpdate

namespace VFH2

namespace ProductRestrictedParamsScorePreservationDischarge

def restrictedParamsScorePreservingUpdatePolicy
    (p : VFH2.ProductRestrictedParams)
    (productUpdate : p.State → p.State)
    (productScore : p.State → Int) : Prop :=
  ∀ y : p.State, productScore (productUpdate y) = productScore y

def restrictedParamsScorePreservationDischargeSource
    (p : VFH2.ProductRestrictedParams)
    (x : p.State)
    (productUpdate : p.State → p.State)
    (productScore : p.State → Int)
    (typedUpdate :
      VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsUpdateScoreTransportCarrier p x productUpdate →
        VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsUpdateScoreTransportCarrier p x productUpdate)
    (typedScore :
      VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsUpdateScoreTransportCarrier p x productUpdate → Int)
    (fixed : Prop)
    (thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi) : Prop :=
  VFH2.ProductRestrictedParamsScoreWindow.restrictedParamsBaseScoreWindowTarget
      p x productUpdate productScore typedUpdate typedScore
      fixed thresholdLo thresholdHi hThreshold ∧
    VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsRawUpdateScoreTransportCertificate
      p x productUpdate productScore typedUpdate typedScore ∧
    restrictedParamsScorePreservingUpdatePolicy p productUpdate productScore

def restrictedParamsScorePreservationDischargeTarget
    (p : VFH2.ProductRestrictedParams)
    (x : p.State)
    (productUpdate : p.State → p.State)
    (productScore : p.State → Int)
    (typedUpdate :
      VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsUpdateScoreTransportCarrier p x productUpdate →
        VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsUpdateScoreTransportCarrier p x productUpdate)
    (typedScore :
      VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsUpdateScoreTransportCarrier p x productUpdate → Int)
    (fixed : Prop)
    (thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi) : Prop :=
  VFH2.ProductRestrictedParamsScorePreservingUpdate.restrictedParamsScorePreservingUpdateWindowTarget
      p x productUpdate productScore typedUpdate typedScore
      fixed thresholdLo thresholdHi hThreshold

theorem restrictedParams_scorePreservingUpdatePolicy_to_point
    (p : VFH2.ProductRestrictedParams)
    (x : p.State)
    (productUpdate : p.State → p.State)
    (productScore : p.State → Int)
    (hPolicy :
      restrictedParamsScorePreservingUpdatePolicy
        p productUpdate productScore) :
    productScore (productUpdate x) = productScore x := by
  unfold restrictedParamsScorePreservingUpdatePolicy at hPolicy
  exact hPolicy x

theorem restrictedParams_scorePreservationDischarge_source_to_v15_7_source
    (p : VFH2.ProductRestrictedParams)
    (x : p.State)
    (productUpdate : p.State → p.State)
    (productScore : p.State → Int)
    (typedUpdate :
      VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsUpdateScoreTransportCarrier p x productUpdate →
        VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsUpdateScoreTransportCarrier p x productUpdate)
    (typedScore :
      VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsUpdateScoreTransportCarrier p x productUpdate → Int)
    (fixed : Prop)
    (thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi)
    (hSource :
      restrictedParamsScorePreservationDischargeSource
        p x productUpdate productScore typedUpdate typedScore
        fixed thresholdLo thresholdHi hThreshold) :
    VFH2.ProductRestrictedParamsScorePreservingUpdate.restrictedParamsScorePreservingUpdateWindowSource
      p x productUpdate productScore typedUpdate typedScore
      fixed thresholdLo thresholdHi hThreshold := by
  unfold restrictedParamsScorePreservationDischargeSource at hSource
  unfold VFH2.ProductRestrictedParamsScorePreservingUpdate.restrictedParamsScorePreservingUpdateWindowSource
  exact ⟨
    hSource.1,
    ⟨hSource.2.1,
      restrictedParams_scorePreservingUpdatePolicy_to_point
        p x productUpdate productScore hSource.2.2⟩
  ⟩

theorem restrictedParams_scorePreservationDischarge_source_to_target
    (p : VFH2.ProductRestrictedParams)
    (x : p.State)
    (productUpdate : p.State → p.State)
    (productScore : p.State → Int)
    (typedUpdate :
      VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsUpdateScoreTransportCarrier p x productUpdate →
        VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsUpdateScoreTransportCarrier p x productUpdate)
    (typedScore :
      VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsUpdateScoreTransportCarrier p x productUpdate → Int)
    (fixed : Prop)
    (thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi)
    (hSource :
      restrictedParamsScorePreservationDischargeSource
        p x productUpdate productScore typedUpdate typedScore
        fixed thresholdLo thresholdHi hThreshold) :
    restrictedParamsScorePreservationDischargeTarget
      p x productUpdate productScore typedUpdate typedScore
      fixed thresholdLo thresholdHi hThreshold := by
  unfold restrictedParamsScorePreservationDischargeTarget
  exact VFH2.ProductRestrictedParamsScorePreservingUpdate.restrictedParams_scorePreservingUpdate_source_to_target
    p x productUpdate productScore typedUpdate typedScore
    fixed thresholdLo thresholdHi hThreshold
    (restrictedParams_scorePreservationDischarge_source_to_v15_7_source
      p x productUpdate productScore typedUpdate typedScore
      fixed thresholdLo thresholdHi hThreshold hSource)

theorem restrictedParams_scorePreservationDischarge_policy_baseWindow_to_target
    (p : VFH2.ProductRestrictedParams)
    (x : p.State)
    (productUpdate : p.State → p.State)
    (productScore : p.State → Int)
    (typedUpdate :
      VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsUpdateScoreTransportCarrier p x productUpdate →
        VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsUpdateScoreTransportCarrier p x productUpdate)
    (typedScore :
      VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsUpdateScoreTransportCarrier p x productUpdate → Int)
    (fixed : Prop)
    (thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi)
    (hBaseTarget :
      VFH2.ProductRestrictedParamsScoreWindow.restrictedParamsBaseScoreWindowTarget
        p x productUpdate productScore typedUpdate typedScore
        fixed thresholdLo thresholdHi hThreshold)
    (hRawTransport :
      VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsRawUpdateScoreTransportCertificate
        p x productUpdate productScore typedUpdate typedScore)
    (hPolicy :
      restrictedParamsScorePreservingUpdatePolicy
        p productUpdate productScore) :
    restrictedParamsScorePreservationDischargeTarget
      p x productUpdate productScore typedUpdate typedScore
      fixed thresholdLo thresholdHi hThreshold := by
  exact restrictedParams_scorePreservationDischarge_source_to_target
    p x productUpdate productScore typedUpdate typedScore
    fixed thresholdLo thresholdHi hThreshold
    ⟨hBaseTarget, ⟨hRawTransport, hPolicy⟩⟩

theorem restrictedParams_rawUpdateScoreEqualities_and_policy_to_target
    (p : VFH2.ProductRestrictedParams)
    (x : p.State)
    (productUpdate : p.State → p.State)
    (productScore : p.State → Int)
    (typedUpdate :
      VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsUpdateScoreTransportCarrier p x productUpdate →
        VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsUpdateScoreTransportCarrier p x productUpdate)
    (typedScore :
      VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsUpdateScoreTransportCarrier p x productUpdate → Int)
    (fixed : Prop)
    (baseEffect thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi)
    (hEffectBase : baseEffect = productScore x)
    (hPolicy :
      restrictedParamsScorePreservingUpdatePolicy
        p productUpdate productScore)
    (hTypedUpdate :
      typedUpdate ⟨VFH2.ProductStateTransport.productToTyped x, Or.inl rfl⟩ =
        ⟨VFH2.ProductStateTransport.productToTyped (productUpdate x), Or.inr rfl⟩)
    (hBase :
      typedScore ⟨VFH2.ProductStateTransport.productToTyped x, Or.inl rfl⟩ =
        productScore x)
    (hUpdated :
      typedScore ⟨VFH2.ProductStateTransport.productToTyped (productUpdate x), Or.inr rfl⟩ =
        productScore (productUpdate x))
    (hBaseLowerBridgeStrong :
      ProductBridgeGeneralization.genericBridgeTarget fixed
        (thresholdHi ≤ baseEffect))
    (hBaseUpperBridgeStrong :
      ProductBridgeGeneralization.genericBridgeTarget fixed
        (baseEffect ≤ thresholdLo)) :
    restrictedParamsScorePreservationDischargeTarget
      p x productUpdate productScore typedUpdate typedScore
      fixed thresholdLo thresholdHi hThreshold := by
  unfold restrictedParamsScorePreservationDischargeTarget
  exact VFH2.ProductRestrictedParamsScorePreservingUpdate.restrictedParams_rawUpdateScoreEqualities_and_scorePreservation_to_target
    p x productUpdate productScore typedUpdate typedScore
    fixed baseEffect thresholdLo thresholdHi hThreshold hEffectBase
    (restrictedParams_scorePreservingUpdatePolicy_to_point
      p x productUpdate productScore hPolicy)
    hTypedUpdate hBase hUpdated hBaseLowerBridgeStrong hBaseUpperBridgeStrong

theorem restrictedParams_scorePreservationDischarge_baseTarget_projection
    (p : VFH2.ProductRestrictedParams)
    (x : p.State)
    (productUpdate : p.State → p.State)
    (productScore : p.State → Int)
    (typedUpdate :
      VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsUpdateScoreTransportCarrier p x productUpdate →
        VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsUpdateScoreTransportCarrier p x productUpdate)
    (typedScore :
      VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsUpdateScoreTransportCarrier p x productUpdate → Int)
    (fixed : Prop)
    (thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi)
    (hTarget :
      restrictedParamsScorePreservationDischargeTarget
        p x productUpdate productScore typedUpdate typedScore
        fixed thresholdLo thresholdHi hThreshold) :
    VFH2.ProductRestrictedParamsScoreWindow.restrictedParamsBaseScoreWindowTarget
      p x productUpdate productScore typedUpdate typedScore
      fixed thresholdLo thresholdHi hThreshold := by
  unfold restrictedParamsScorePreservationDischargeTarget at hTarget
  exact VFH2.ProductRestrictedParamsScorePreservingUpdate.restrictedParams_scorePreservingUpdate_target_base_projection
    p x productUpdate productScore typedUpdate typedScore
    fixed thresholdLo thresholdHi hThreshold hTarget

theorem restrictedParams_scorePreservationDischarge_updatedTarget_projection
    (p : VFH2.ProductRestrictedParams)
    (x : p.State)
    (productUpdate : p.State → p.State)
    (productScore : p.State → Int)
    (typedUpdate :
      VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsUpdateScoreTransportCarrier p x productUpdate →
        VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsUpdateScoreTransportCarrier p x productUpdate)
    (typedScore :
      VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsUpdateScoreTransportCarrier p x productUpdate → Int)
    (fixed : Prop)
    (thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi)
    (hTarget :
      restrictedParamsScorePreservationDischargeTarget
        p x productUpdate productScore typedUpdate typedScore
        fixed thresholdLo thresholdHi hThreshold) :
    VFH2.ProductRestrictedParamsScoreWindow.restrictedParamsUpdatedScoreWindowTarget
      p x productUpdate productScore typedUpdate typedScore
      fixed thresholdLo thresholdHi hThreshold := by
  unfold restrictedParamsScorePreservationDischargeTarget at hTarget
  exact VFH2.ProductRestrictedParamsScorePreservingUpdate.restrictedParams_scorePreservingUpdate_target_updated_projection
    p x productUpdate productScore typedUpdate typedScore
    fixed thresholdLo thresholdHi hThreshold hTarget

theorem restrictedParams_scorePreservationDischarge_updatedLower_projection
    (p : VFH2.ProductRestrictedParams)
    (x : p.State)
    (productUpdate : p.State → p.State)
    (productScore : p.State → Int)
    (typedUpdate :
      VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsUpdateScoreTransportCarrier p x productUpdate →
        VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsUpdateScoreTransportCarrier p x productUpdate)
    (typedScore :
      VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsUpdateScoreTransportCarrier p x productUpdate → Int)
    (fixed : Prop)
    (thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi)
    (hTarget :
      restrictedParamsScorePreservationDischargeTarget
        p x productUpdate productScore typedUpdate typedScore
        fixed thresholdLo thresholdHi hThreshold) :
    ProductBridgeGeneralization.genericBridgeTarget fixed
      (thresholdLo ≤ productScore (productUpdate x)) := by
  unfold restrictedParamsScorePreservationDischargeTarget at hTarget
  exact VFH2.ProductRestrictedParamsScorePreservingUpdate.restrictedParams_scorePreservingUpdate_updatedLower_projection
    p x productUpdate productScore typedUpdate typedScore
    fixed thresholdLo thresholdHi hThreshold hTarget

theorem restrictedParams_scorePreservationDischarge_updatedUpper_projection
    (p : VFH2.ProductRestrictedParams)
    (x : p.State)
    (productUpdate : p.State → p.State)
    (productScore : p.State → Int)
    (typedUpdate :
      VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsUpdateScoreTransportCarrier p x productUpdate →
        VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsUpdateScoreTransportCarrier p x productUpdate)
    (typedScore :
      VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsUpdateScoreTransportCarrier p x productUpdate → Int)
    (fixed : Prop)
    (thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi)
    (hTarget :
      restrictedParamsScorePreservationDischargeTarget
        p x productUpdate productScore typedUpdate typedScore
        fixed thresholdLo thresholdHi hThreshold) :
    ProductBridgeGeneralization.genericBridgeTarget fixed
      (productScore (productUpdate x) ≤ thresholdHi) := by
  unfold restrictedParamsScorePreservationDischargeTarget at hTarget
  exact VFH2.ProductRestrictedParamsScorePreservingUpdate.restrictedParams_scorePreservingUpdate_updatedUpper_projection
    p x productUpdate productScore typedUpdate typedScore
    fixed thresholdLo thresholdHi hThreshold hTarget

theorem restrictedParams_rawUpdateScoreEqualities_and_policy_to_updatedLower
    (p : VFH2.ProductRestrictedParams)
    (x : p.State)
    (productUpdate : p.State → p.State)
    (productScore : p.State → Int)
    (typedUpdate :
      VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsUpdateScoreTransportCarrier p x productUpdate →
        VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsUpdateScoreTransportCarrier p x productUpdate)
    (typedScore :
      VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsUpdateScoreTransportCarrier p x productUpdate → Int)
    (fixed : Prop)
    (baseEffect thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi)
    (hEffectBase : baseEffect = productScore x)
    (hPolicy :
      restrictedParamsScorePreservingUpdatePolicy
        p productUpdate productScore)
    (hTypedUpdate :
      typedUpdate ⟨VFH2.ProductStateTransport.productToTyped x, Or.inl rfl⟩ =
        ⟨VFH2.ProductStateTransport.productToTyped (productUpdate x), Or.inr rfl⟩)
    (hBase :
      typedScore ⟨VFH2.ProductStateTransport.productToTyped x, Or.inl rfl⟩ =
        productScore x)
    (hUpdated :
      typedScore ⟨VFH2.ProductStateTransport.productToTyped (productUpdate x), Or.inr rfl⟩ =
        productScore (productUpdate x))
    (hBaseLowerBridgeStrong :
      ProductBridgeGeneralization.genericBridgeTarget fixed
        (thresholdHi ≤ baseEffect))
    (hBaseUpperBridgeStrong :
      ProductBridgeGeneralization.genericBridgeTarget fixed
        (baseEffect ≤ thresholdLo)) :
    ProductBridgeGeneralization.genericBridgeTarget fixed
      (thresholdLo ≤ productScore (productUpdate x)) := by
  exact restrictedParams_scorePreservationDischarge_updatedLower_projection
    p x productUpdate productScore typedUpdate typedScore
    fixed thresholdLo thresholdHi hThreshold
    (restrictedParams_rawUpdateScoreEqualities_and_policy_to_target
      p x productUpdate productScore typedUpdate typedScore
      fixed baseEffect thresholdLo thresholdHi hThreshold hEffectBase hPolicy
      hTypedUpdate hBase hUpdated hBaseLowerBridgeStrong hBaseUpperBridgeStrong)

theorem restrictedParams_rawUpdateScoreEqualities_and_policy_to_updatedUpper
    (p : VFH2.ProductRestrictedParams)
    (x : p.State)
    (productUpdate : p.State → p.State)
    (productScore : p.State → Int)
    (typedUpdate :
      VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsUpdateScoreTransportCarrier p x productUpdate →
        VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsUpdateScoreTransportCarrier p x productUpdate)
    (typedScore :
      VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsUpdateScoreTransportCarrier p x productUpdate → Int)
    (fixed : Prop)
    (baseEffect thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi)
    (hEffectBase : baseEffect = productScore x)
    (hPolicy :
      restrictedParamsScorePreservingUpdatePolicy
        p productUpdate productScore)
    (hTypedUpdate :
      typedUpdate ⟨VFH2.ProductStateTransport.productToTyped x, Or.inl rfl⟩ =
        ⟨VFH2.ProductStateTransport.productToTyped (productUpdate x), Or.inr rfl⟩)
    (hBase :
      typedScore ⟨VFH2.ProductStateTransport.productToTyped x, Or.inl rfl⟩ =
        productScore x)
    (hUpdated :
      typedScore ⟨VFH2.ProductStateTransport.productToTyped (productUpdate x), Or.inr rfl⟩ =
        productScore (productUpdate x))
    (hBaseLowerBridgeStrong :
      ProductBridgeGeneralization.genericBridgeTarget fixed
        (thresholdHi ≤ baseEffect))
    (hBaseUpperBridgeStrong :
      ProductBridgeGeneralization.genericBridgeTarget fixed
        (baseEffect ≤ thresholdLo)) :
    ProductBridgeGeneralization.genericBridgeTarget fixed
      (productScore (productUpdate x) ≤ thresholdHi) := by
  exact restrictedParams_scorePreservationDischarge_updatedUpper_projection
    p x productUpdate productScore typedUpdate typedScore
    fixed thresholdLo thresholdHi hThreshold
    (restrictedParams_rawUpdateScoreEqualities_and_policy_to_target
      p x productUpdate productScore typedUpdate typedScore
      fixed baseEffect thresholdLo thresholdHi hThreshold hEffectBase hPolicy
      hTypedUpdate hBase hUpdated hBaseLowerBridgeStrong hBaseUpperBridgeStrong)

end ProductRestrictedParamsScorePreservationDischarge

end VFH2
