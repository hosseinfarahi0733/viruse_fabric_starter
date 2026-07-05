import VFH2.Product.ProductRestrictedParamsScorePreservationDischarge

namespace VFH2

namespace ProductRestrictedParamsPolicyEndToEndScoreWindow

structure restrictedParamsPolicyEndToEndScoreWindowSource
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
    (baseEffect thresholdLo thresholdHi : Int) : Prop where
  hEffectBase :
    baseEffect = productScore x
  hPolicy :
    VFH2.ProductRestrictedParamsScorePreservationDischarge.restrictedParamsScorePreservingUpdatePolicy
      p productUpdate productScore
  hTypedUpdate :
    typedUpdate ⟨VFH2.ProductStateTransport.productToTyped x, Or.inl rfl⟩ =
      ⟨VFH2.ProductStateTransport.productToTyped (productUpdate x), Or.inr rfl⟩
  hBaseScore :
    typedScore ⟨VFH2.ProductStateTransport.productToTyped x, Or.inl rfl⟩ =
      productScore x
  hUpdatedScore :
    typedScore ⟨VFH2.ProductStateTransport.productToTyped (productUpdate x), Or.inr rfl⟩ =
      productScore (productUpdate x)
  hBaseLowerBridgeStrong :
    ProductBridgeGeneralization.genericBridgeTarget fixed
      (thresholdHi ≤ baseEffect)
  hBaseUpperBridgeStrong :
    ProductBridgeGeneralization.genericBridgeTarget fixed
      (baseEffect ≤ thresholdLo)

def restrictedParamsPolicyEndToEndScoreWindowTarget
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
  VFH2.ProductRestrictedParamsScorePreservationDischarge.restrictedParamsScorePreservationDischargeTarget
    p x productUpdate productScore typedUpdate typedScore
    fixed thresholdLo thresholdHi hThreshold

def restrictedParamsPolicyEndToEndUpdatedScoreWindowBounds
    (p : VFH2.ProductRestrictedParams)
    (x : p.State)
    (productUpdate : p.State → p.State)
    (productScore : p.State → Int)
    (fixed : Prop)
    (thresholdLo thresholdHi : Int) : Prop :=
  ProductBridgeGeneralization.genericBridgeTarget fixed
      (thresholdLo ≤ productScore (productUpdate x)) ∧
    ProductBridgeGeneralization.genericBridgeTarget fixed
      (productScore (productUpdate x) ≤ thresholdHi)

theorem restrictedParams_policyEndToEnd_source_to_target
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
    (hSource :
      restrictedParamsPolicyEndToEndScoreWindowSource
        p x productUpdate productScore typedUpdate typedScore
        fixed baseEffect thresholdLo thresholdHi) :
    restrictedParamsPolicyEndToEndScoreWindowTarget
      p x productUpdate productScore typedUpdate typedScore
      fixed thresholdLo thresholdHi hThreshold := by
  unfold restrictedParamsPolicyEndToEndScoreWindowTarget
  exact VFH2.ProductRestrictedParamsScorePreservationDischarge.restrictedParams_rawUpdateScoreEqualities_and_policy_to_target
    p x productUpdate productScore typedUpdate typedScore
    fixed baseEffect thresholdLo thresholdHi hThreshold
    hSource.hEffectBase hSource.hPolicy
    hSource.hTypedUpdate hSource.hBaseScore hSource.hUpdatedScore
    hSource.hBaseLowerBridgeStrong hSource.hBaseUpperBridgeStrong

theorem restrictedParams_policyEndToEnd_rawEqualities_to_target
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
      VFH2.ProductRestrictedParamsScorePreservationDischarge.restrictedParamsScorePreservingUpdatePolicy
        p productUpdate productScore)
    (hTypedUpdate :
      typedUpdate ⟨VFH2.ProductStateTransport.productToTyped x, Or.inl rfl⟩ =
        ⟨VFH2.ProductStateTransport.productToTyped (productUpdate x), Or.inr rfl⟩)
    (hBaseScore :
      typedScore ⟨VFH2.ProductStateTransport.productToTyped x, Or.inl rfl⟩ =
        productScore x)
    (hUpdatedScore :
      typedScore ⟨VFH2.ProductStateTransport.productToTyped (productUpdate x), Or.inr rfl⟩ =
        productScore (productUpdate x))
    (hBaseLowerBridgeStrong :
      ProductBridgeGeneralization.genericBridgeTarget fixed
        (thresholdHi ≤ baseEffect))
    (hBaseUpperBridgeStrong :
      ProductBridgeGeneralization.genericBridgeTarget fixed
        (baseEffect ≤ thresholdLo)) :
    restrictedParamsPolicyEndToEndScoreWindowTarget
      p x productUpdate productScore typedUpdate typedScore
      fixed thresholdLo thresholdHi hThreshold := by
  exact restrictedParams_policyEndToEnd_source_to_target
    p x productUpdate productScore typedUpdate typedScore
    fixed baseEffect thresholdLo thresholdHi hThreshold
    {
      hEffectBase := hEffectBase
      hPolicy := hPolicy
      hTypedUpdate := hTypedUpdate
      hBaseScore := hBaseScore
      hUpdatedScore := hUpdatedScore
      hBaseLowerBridgeStrong := hBaseLowerBridgeStrong
      hBaseUpperBridgeStrong := hBaseUpperBridgeStrong
    }

theorem restrictedParams_policyEndToEnd_baseTarget_projection
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
      restrictedParamsPolicyEndToEndScoreWindowTarget
        p x productUpdate productScore typedUpdate typedScore
        fixed thresholdLo thresholdHi hThreshold) :
    VFH2.ProductRestrictedParamsScoreWindow.restrictedParamsBaseScoreWindowTarget
      p x productUpdate productScore typedUpdate typedScore
      fixed thresholdLo thresholdHi hThreshold := by
  unfold restrictedParamsPolicyEndToEndScoreWindowTarget at hTarget
  exact VFH2.ProductRestrictedParamsScorePreservationDischarge.restrictedParams_scorePreservationDischarge_baseTarget_projection
    p x productUpdate productScore typedUpdate typedScore
    fixed thresholdLo thresholdHi hThreshold hTarget

theorem restrictedParams_policyEndToEnd_updatedTarget_projection
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
      restrictedParamsPolicyEndToEndScoreWindowTarget
        p x productUpdate productScore typedUpdate typedScore
        fixed thresholdLo thresholdHi hThreshold) :
    VFH2.ProductRestrictedParamsScoreWindow.restrictedParamsUpdatedScoreWindowTarget
      p x productUpdate productScore typedUpdate typedScore
      fixed thresholdLo thresholdHi hThreshold := by
  unfold restrictedParamsPolicyEndToEndScoreWindowTarget at hTarget
  exact VFH2.ProductRestrictedParamsScorePreservationDischarge.restrictedParams_scorePreservationDischarge_updatedTarget_projection
    p x productUpdate productScore typedUpdate typedScore
    fixed thresholdLo thresholdHi hThreshold hTarget

theorem restrictedParams_policyEndToEnd_updatedLower_projection
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
      restrictedParamsPolicyEndToEndScoreWindowTarget
        p x productUpdate productScore typedUpdate typedScore
        fixed thresholdLo thresholdHi hThreshold) :
    ProductBridgeGeneralization.genericBridgeTarget fixed
      (thresholdLo ≤ productScore (productUpdate x)) := by
  unfold restrictedParamsPolicyEndToEndScoreWindowTarget at hTarget
  exact VFH2.ProductRestrictedParamsScorePreservationDischarge.restrictedParams_scorePreservationDischarge_updatedLower_projection
    p x productUpdate productScore typedUpdate typedScore
    fixed thresholdLo thresholdHi hThreshold hTarget

theorem restrictedParams_policyEndToEnd_updatedUpper_projection
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
      restrictedParamsPolicyEndToEndScoreWindowTarget
        p x productUpdate productScore typedUpdate typedScore
        fixed thresholdLo thresholdHi hThreshold) :
    ProductBridgeGeneralization.genericBridgeTarget fixed
      (productScore (productUpdate x) ≤ thresholdHi) := by
  unfold restrictedParamsPolicyEndToEndScoreWindowTarget at hTarget
  exact VFH2.ProductRestrictedParamsScorePreservationDischarge.restrictedParams_scorePreservationDischarge_updatedUpper_projection
    p x productUpdate productScore typedUpdate typedScore
    fixed thresholdLo thresholdHi hThreshold hTarget

theorem restrictedParams_policyEndToEnd_source_to_updatedBounds
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
    (hSource :
      restrictedParamsPolicyEndToEndScoreWindowSource
        p x productUpdate productScore typedUpdate typedScore
        fixed baseEffect thresholdLo thresholdHi) :
    restrictedParamsPolicyEndToEndUpdatedScoreWindowBounds
      p x productUpdate productScore fixed thresholdLo thresholdHi := by
  unfold restrictedParamsPolicyEndToEndUpdatedScoreWindowBounds
  have hTarget :
      restrictedParamsPolicyEndToEndScoreWindowTarget
        p x productUpdate productScore typedUpdate typedScore
        fixed thresholdLo thresholdHi hThreshold :=
    restrictedParams_policyEndToEnd_source_to_target
      p x productUpdate productScore typedUpdate typedScore
      fixed baseEffect thresholdLo thresholdHi hThreshold hSource
  exact ⟨
    restrictedParams_policyEndToEnd_updatedLower_projection
      p x productUpdate productScore typedUpdate typedScore
      fixed thresholdLo thresholdHi hThreshold hTarget,
    restrictedParams_policyEndToEnd_updatedUpper_projection
      p x productUpdate productScore typedUpdate typedScore
      fixed thresholdLo thresholdHi hThreshold hTarget
  ⟩

theorem restrictedParams_policyEndToEnd_rawEqualities_to_updatedBounds
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
      VFH2.ProductRestrictedParamsScorePreservationDischarge.restrictedParamsScorePreservingUpdatePolicy
        p productUpdate productScore)
    (hTypedUpdate :
      typedUpdate ⟨VFH2.ProductStateTransport.productToTyped x, Or.inl rfl⟩ =
        ⟨VFH2.ProductStateTransport.productToTyped (productUpdate x), Or.inr rfl⟩)
    (hBaseScore :
      typedScore ⟨VFH2.ProductStateTransport.productToTyped x, Or.inl rfl⟩ =
        productScore x)
    (hUpdatedScore :
      typedScore ⟨VFH2.ProductStateTransport.productToTyped (productUpdate x), Or.inr rfl⟩ =
        productScore (productUpdate x))
    (hBaseLowerBridgeStrong :
      ProductBridgeGeneralization.genericBridgeTarget fixed
        (thresholdHi ≤ baseEffect))
    (hBaseUpperBridgeStrong :
      ProductBridgeGeneralization.genericBridgeTarget fixed
        (baseEffect ≤ thresholdLo)) :
    restrictedParamsPolicyEndToEndUpdatedScoreWindowBounds
      p x productUpdate productScore fixed thresholdLo thresholdHi := by
  exact restrictedParams_policyEndToEnd_source_to_updatedBounds
    p x productUpdate productScore typedUpdate typedScore
    fixed baseEffect thresholdLo thresholdHi hThreshold
    {
      hEffectBase := hEffectBase
      hPolicy := hPolicy
      hTypedUpdate := hTypedUpdate
      hBaseScore := hBaseScore
      hUpdatedScore := hUpdatedScore
      hBaseLowerBridgeStrong := hBaseLowerBridgeStrong
      hBaseUpperBridgeStrong := hBaseUpperBridgeStrong
    }

theorem restrictedParams_policyEndToEnd_rawEqualities_to_updatedLower
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
      VFH2.ProductRestrictedParamsScorePreservationDischarge.restrictedParamsScorePreservingUpdatePolicy
        p productUpdate productScore)
    (hTypedUpdate :
      typedUpdate ⟨VFH2.ProductStateTransport.productToTyped x, Or.inl rfl⟩ =
        ⟨VFH2.ProductStateTransport.productToTyped (productUpdate x), Or.inr rfl⟩)
    (hBaseScore :
      typedScore ⟨VFH2.ProductStateTransport.productToTyped x, Or.inl rfl⟩ =
        productScore x)
    (hUpdatedScore :
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
  exact
    (restrictedParams_policyEndToEnd_rawEqualities_to_updatedBounds
      p x productUpdate productScore typedUpdate typedScore
      fixed baseEffect thresholdLo thresholdHi hThreshold hEffectBase hPolicy
      hTypedUpdate hBaseScore hUpdatedScore
      hBaseLowerBridgeStrong hBaseUpperBridgeStrong).1

theorem restrictedParams_policyEndToEnd_rawEqualities_to_updatedUpper
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
      VFH2.ProductRestrictedParamsScorePreservationDischarge.restrictedParamsScorePreservingUpdatePolicy
        p productUpdate productScore)
    (hTypedUpdate :
      typedUpdate ⟨VFH2.ProductStateTransport.productToTyped x, Or.inl rfl⟩ =
        ⟨VFH2.ProductStateTransport.productToTyped (productUpdate x), Or.inr rfl⟩)
    (hBaseScore :
      typedScore ⟨VFH2.ProductStateTransport.productToTyped x, Or.inl rfl⟩ =
        productScore x)
    (hUpdatedScore :
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
  exact
    (restrictedParams_policyEndToEnd_rawEqualities_to_updatedBounds
      p x productUpdate productScore typedUpdate typedScore
      fixed baseEffect thresholdLo thresholdHi hThreshold hEffectBase hPolicy
      hTypedUpdate hBaseScore hUpdatedScore
      hBaseLowerBridgeStrong hBaseUpperBridgeStrong).2

end ProductRestrictedParamsPolicyEndToEndScoreWindow

end VFH2
