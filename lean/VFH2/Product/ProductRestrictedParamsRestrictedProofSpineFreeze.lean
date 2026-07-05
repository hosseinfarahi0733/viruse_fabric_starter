import VFH2.Product.ProductRestrictedParamsPolicyEndToEndScoreWindow

namespace VFH2

namespace ProductRestrictedParamsRestrictedProofSpineFreeze

abbrev restrictedProofSpineSource
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
    (baseEffect thresholdLo thresholdHi : Int) : Prop :=
  VFH2.ProductRestrictedParamsPolicyEndToEndScoreWindow.restrictedParamsPolicyEndToEndScoreWindowSource
    p x productUpdate productScore typedUpdate typedScore
    fixed baseEffect thresholdLo thresholdHi

abbrev restrictedProofSpineTarget
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
  VFH2.ProductRestrictedParamsPolicyEndToEndScoreWindow.restrictedParamsPolicyEndToEndScoreWindowTarget
    p x productUpdate productScore typedUpdate typedScore
    fixed thresholdLo thresholdHi hThreshold

abbrev restrictedProofSpineUpdatedScoreWindowBounds
    (p : VFH2.ProductRestrictedParams)
    (x : p.State)
    (productUpdate : p.State → p.State)
    (productScore : p.State → Int)
    (fixed : Prop)
    (thresholdLo thresholdHi : Int) : Prop :=
  VFH2.ProductRestrictedParamsPolicyEndToEndScoreWindow.restrictedParamsPolicyEndToEndUpdatedScoreWindowBounds
    p x productUpdate productScore fixed thresholdLo thresholdHi

theorem restrictedProofSpine_source_to_target
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
      restrictedProofSpineSource
        p x productUpdate productScore typedUpdate typedScore
        fixed baseEffect thresholdLo thresholdHi) :
    restrictedProofSpineTarget
      p x productUpdate productScore typedUpdate typedScore
      fixed thresholdLo thresholdHi hThreshold := by
  exact VFH2.ProductRestrictedParamsPolicyEndToEndScoreWindow.restrictedParams_policyEndToEnd_source_to_target
    p x productUpdate productScore typedUpdate typedScore
    fixed baseEffect thresholdLo thresholdHi hThreshold hSource

theorem restrictedProofSpine_source_to_updatedBounds
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
      restrictedProofSpineSource
        p x productUpdate productScore typedUpdate typedScore
        fixed baseEffect thresholdLo thresholdHi) :
    restrictedProofSpineUpdatedScoreWindowBounds
      p x productUpdate productScore fixed thresholdLo thresholdHi := by
  exact VFH2.ProductRestrictedParamsPolicyEndToEndScoreWindow.restrictedParams_policyEndToEnd_source_to_updatedBounds
    p x productUpdate productScore typedUpdate typedScore
    fixed baseEffect thresholdLo thresholdHi hThreshold hSource

theorem restrictedProofSpine_rawEqualities_to_target
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
    restrictedProofSpineTarget
      p x productUpdate productScore typedUpdate typedScore
      fixed thresholdLo thresholdHi hThreshold := by
  exact VFH2.ProductRestrictedParamsPolicyEndToEndScoreWindow.restrictedParams_policyEndToEnd_rawEqualities_to_target
    p x productUpdate productScore typedUpdate typedScore
    fixed baseEffect thresholdLo thresholdHi hThreshold hEffectBase hPolicy
    hTypedUpdate hBaseScore hUpdatedScore hBaseLowerBridgeStrong hBaseUpperBridgeStrong

theorem restrictedProofSpine_rawEqualities_to_updatedBounds
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
    restrictedProofSpineUpdatedScoreWindowBounds
      p x productUpdate productScore fixed thresholdLo thresholdHi := by
  exact VFH2.ProductRestrictedParamsPolicyEndToEndScoreWindow.restrictedParams_policyEndToEnd_rawEqualities_to_updatedBounds
    p x productUpdate productScore typedUpdate typedScore
    fixed baseEffect thresholdLo thresholdHi hThreshold hEffectBase hPolicy
    hTypedUpdate hBaseScore hUpdatedScore hBaseLowerBridgeStrong hBaseUpperBridgeStrong

theorem restrictedProofSpine_rawEqualities_to_updatedLower
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
    (restrictedProofSpine_rawEqualities_to_updatedBounds
      p x productUpdate productScore typedUpdate typedScore
      fixed baseEffect thresholdLo thresholdHi hThreshold hEffectBase hPolicy
      hTypedUpdate hBaseScore hUpdatedScore hBaseLowerBridgeStrong hBaseUpperBridgeStrong).1

theorem restrictedProofSpine_rawEqualities_to_updatedUpper
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
    (restrictedProofSpine_rawEqualities_to_updatedBounds
      p x productUpdate productScore typedUpdate typedScore
      fixed baseEffect thresholdLo thresholdHi hThreshold hEffectBase hPolicy
      hTypedUpdate hBaseScore hUpdatedScore hBaseLowerBridgeStrong hBaseUpperBridgeStrong).2

end ProductRestrictedParamsRestrictedProofSpineFreeze

end VFH2
