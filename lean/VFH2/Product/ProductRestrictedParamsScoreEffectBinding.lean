import VFH2.Product.ProductRestrictedParamsUpdateScoreBound

namespace VFH2

namespace ProductRestrictedParamsScoreEffectBinding

def restrictedParamsBaseScoreBoundTarget
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
  ProductBridgeGeneralization.genericBridgeTarget fixed
      (thresholdLo ≤ productScore x) ∧
    ProductBridgeGeneralization.genericBridgeTarget fixed
      (productScore x ≤ thresholdHi) ∧
    VFH2.ProductEffectBoundConditionMonotonicity.RestrictedEffectBoundMonotoneTransportCertificate
      p x thresholdLo thresholdHi hThreshold ∧
    VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsRawUpdateScoreTransportCertificate
      p x productUpdate productScore typedUpdate typedScore

def restrictedParamsUpdatedScoreBoundTarget
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
  ProductBridgeGeneralization.genericBridgeTarget fixed
      (thresholdLo ≤ productScore (productUpdate x)) ∧
    ProductBridgeGeneralization.genericBridgeTarget fixed
      (productScore (productUpdate x) ≤ thresholdHi) ∧
    VFH2.ProductEffectBoundConditionMonotonicity.RestrictedEffectBoundMonotoneTransportCertificate
      p x thresholdLo thresholdHi hThreshold ∧
    VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsRawUpdateScoreTransportCertificate
      p x productUpdate productScore typedUpdate typedScore

theorem restrictedParams_effectBoundTarget_to_baseScoreBoundTarget
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
    (effect thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi)
    (hEffectBase : effect = productScore x)
    (hBound :
      VFH2.ProductRestrictedParamsUpdateScoreBound.restrictedParamsUpdateScoreBoundTarget
        p x productUpdate productScore typedUpdate typedScore
        fixed effect thresholdLo thresholdHi hThreshold) :
    restrictedParamsBaseScoreBoundTarget
      p x productUpdate productScore typedUpdate typedScore
      fixed thresholdLo thresholdHi hThreshold := by
  subst effect
  unfold restrictedParamsBaseScoreBoundTarget
  exact ⟨
    VFH2.ProductRestrictedParamsUpdateScoreBound.restrictedParams_updateScoreBound_lower_projection
      p x productUpdate productScore typedUpdate typedScore
      fixed (productScore x) thresholdLo thresholdHi hThreshold hBound,
    VFH2.ProductRestrictedParamsUpdateScoreBound.restrictedParams_updateScoreBound_upper_projection
      p x productUpdate productScore typedUpdate typedScore
      fixed (productScore x) thresholdLo thresholdHi hThreshold hBound,
    VFH2.ProductRestrictedParamsUpdateScoreBound.restrictedParams_updateScoreBound_restrictedCertificate_projection
      p x productUpdate productScore typedUpdate typedScore
      fixed (productScore x) thresholdLo thresholdHi hThreshold hBound,
    VFH2.ProductRestrictedParamsUpdateScoreBound.restrictedParams_updateScoreBound_rawTransportCertificate_projection
      p x productUpdate productScore typedUpdate typedScore
      fixed (productScore x) thresholdLo thresholdHi hThreshold hBound
  ⟩

theorem restrictedParams_effectBoundTarget_to_updatedScoreBoundTarget
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
    (effect thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi)
    (hEffectUpdated : effect = productScore (productUpdate x))
    (hBound :
      VFH2.ProductRestrictedParamsUpdateScoreBound.restrictedParamsUpdateScoreBoundTarget
        p x productUpdate productScore typedUpdate typedScore
        fixed effect thresholdLo thresholdHi hThreshold) :
    restrictedParamsUpdatedScoreBoundTarget
      p x productUpdate productScore typedUpdate typedScore
      fixed thresholdLo thresholdHi hThreshold := by
  subst effect
  unfold restrictedParamsUpdatedScoreBoundTarget
  exact ⟨
    VFH2.ProductRestrictedParamsUpdateScoreBound.restrictedParams_updateScoreBound_lower_projection
      p x productUpdate productScore typedUpdate typedScore
      fixed (productScore (productUpdate x)) thresholdLo thresholdHi hThreshold hBound,
    VFH2.ProductRestrictedParamsUpdateScoreBound.restrictedParams_updateScoreBound_upper_projection
      p x productUpdate productScore typedUpdate typedScore
      fixed (productScore (productUpdate x)) thresholdLo thresholdHi hThreshold hBound,
    VFH2.ProductRestrictedParamsUpdateScoreBound.restrictedParams_updateScoreBound_restrictedCertificate_projection
      p x productUpdate productScore typedUpdate typedScore
      fixed (productScore (productUpdate x)) thresholdLo thresholdHi hThreshold hBound,
    VFH2.ProductRestrictedParamsUpdateScoreBound.restrictedParams_updateScoreBound_rawTransportCertificate_projection
      p x productUpdate productScore typedUpdate typedScore
      fixed (productScore (productUpdate x)) thresholdLo thresholdHi hThreshold hBound
  ⟩

theorem restrictedParams_rawUpdateScoreEqualities_to_baseScoreBoundTarget
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
    (effect thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi)
    (hEffectBase : effect = productScore x)
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
    restrictedParamsBaseScoreBoundTarget
      p x productUpdate productScore typedUpdate typedScore
      fixed thresholdLo thresholdHi hThreshold := by
  exact restrictedParams_effectBoundTarget_to_baseScoreBoundTarget
    p x productUpdate productScore typedUpdate typedScore
    fixed effect thresholdLo thresholdHi hThreshold hEffectBase
    (VFH2.ProductRestrictedParamsUpdateScoreBound.restrictedParams_rawUpdateScoreEqualities_to_boundTarget
      p x productUpdate productScore typedUpdate typedScore
      fixed effect thresholdLo thresholdHi hThreshold
      hTypedUpdate hBase hUpdated hLowerBridgeStrong hUpperBridgeStrong)

theorem restrictedParams_rawUpdateScoreEqualities_to_updatedScoreBoundTarget
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
    (effect thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi)
    (hEffectUpdated : effect = productScore (productUpdate x))
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
    restrictedParamsUpdatedScoreBoundTarget
      p x productUpdate productScore typedUpdate typedScore
      fixed thresholdLo thresholdHi hThreshold := by
  exact restrictedParams_effectBoundTarget_to_updatedScoreBoundTarget
    p x productUpdate productScore typedUpdate typedScore
    fixed effect thresholdLo thresholdHi hThreshold hEffectUpdated
    (VFH2.ProductRestrictedParamsUpdateScoreBound.restrictedParams_rawUpdateScoreEqualities_to_boundTarget
      p x productUpdate productScore typedUpdate typedScore
      fixed effect thresholdLo thresholdHi hThreshold
      hTypedUpdate hBase hUpdated hLowerBridgeStrong hUpperBridgeStrong)

theorem restrictedParams_baseScoreBound_lower_projection
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
      restrictedParamsBaseScoreBoundTarget
        p x productUpdate productScore typedUpdate typedScore
        fixed thresholdLo thresholdHi hThreshold) :
    ProductBridgeGeneralization.genericBridgeTarget fixed
      (thresholdLo ≤ productScore x) := by
  unfold restrictedParamsBaseScoreBoundTarget at hTarget
  exact hTarget.1

theorem restrictedParams_baseScoreBound_upper_projection
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
      restrictedParamsBaseScoreBoundTarget
        p x productUpdate productScore typedUpdate typedScore
        fixed thresholdLo thresholdHi hThreshold) :
    ProductBridgeGeneralization.genericBridgeTarget fixed
      (productScore x ≤ thresholdHi) := by
  unfold restrictedParamsBaseScoreBoundTarget at hTarget
  exact hTarget.2.1

theorem restrictedParams_updatedScoreBound_lower_projection
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
      restrictedParamsUpdatedScoreBoundTarget
        p x productUpdate productScore typedUpdate typedScore
        fixed thresholdLo thresholdHi hThreshold) :
    ProductBridgeGeneralization.genericBridgeTarget fixed
      (thresholdLo ≤ productScore (productUpdate x)) := by
  unfold restrictedParamsUpdatedScoreBoundTarget at hTarget
  exact hTarget.1

theorem restrictedParams_updatedScoreBound_upper_projection
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
      restrictedParamsUpdatedScoreBoundTarget
        p x productUpdate productScore typedUpdate typedScore
        fixed thresholdLo thresholdHi hThreshold) :
    ProductBridgeGeneralization.genericBridgeTarget fixed
      (productScore (productUpdate x) ≤ thresholdHi) := by
  unfold restrictedParamsUpdatedScoreBoundTarget at hTarget
  exact hTarget.2.1

theorem restrictedParams_rawUpdateScoreEqualities_to_baseScoreLowerBound
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
    (effect thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi)
    (hEffectBase : effect = productScore x)
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
    ProductBridgeGeneralization.genericBridgeTarget fixed
      (thresholdLo ≤ productScore x) := by
  exact restrictedParams_baseScoreBound_lower_projection
    p x productUpdate productScore typedUpdate typedScore
    fixed thresholdLo thresholdHi hThreshold
    (restrictedParams_rawUpdateScoreEqualities_to_baseScoreBoundTarget
      p x productUpdate productScore typedUpdate typedScore
      fixed effect thresholdLo thresholdHi hThreshold hEffectBase
      hTypedUpdate hBase hUpdated hLowerBridgeStrong hUpperBridgeStrong)

theorem restrictedParams_rawUpdateScoreEqualities_to_baseScoreUpperBound
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
    (effect thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi)
    (hEffectBase : effect = productScore x)
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
    ProductBridgeGeneralization.genericBridgeTarget fixed
      (productScore x ≤ thresholdHi) := by
  exact restrictedParams_baseScoreBound_upper_projection
    p x productUpdate productScore typedUpdate typedScore
    fixed thresholdLo thresholdHi hThreshold
    (restrictedParams_rawUpdateScoreEqualities_to_baseScoreBoundTarget
      p x productUpdate productScore typedUpdate typedScore
      fixed effect thresholdLo thresholdHi hThreshold hEffectBase
      hTypedUpdate hBase hUpdated hLowerBridgeStrong hUpperBridgeStrong)

theorem restrictedParams_rawUpdateScoreEqualities_to_updatedScoreLowerBound
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
    (effect thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi)
    (hEffectUpdated : effect = productScore (productUpdate x))
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
    ProductBridgeGeneralization.genericBridgeTarget fixed
      (thresholdLo ≤ productScore (productUpdate x)) := by
  exact restrictedParams_updatedScoreBound_lower_projection
    p x productUpdate productScore typedUpdate typedScore
    fixed thresholdLo thresholdHi hThreshold
    (restrictedParams_rawUpdateScoreEqualities_to_updatedScoreBoundTarget
      p x productUpdate productScore typedUpdate typedScore
      fixed effect thresholdLo thresholdHi hThreshold hEffectUpdated
      hTypedUpdate hBase hUpdated hLowerBridgeStrong hUpperBridgeStrong)

theorem restrictedParams_rawUpdateScoreEqualities_to_updatedScoreUpperBound
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
    (effect thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi)
    (hEffectUpdated : effect = productScore (productUpdate x))
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
    ProductBridgeGeneralization.genericBridgeTarget fixed
      (productScore (productUpdate x) ≤ thresholdHi) := by
  exact restrictedParams_updatedScoreBound_upper_projection
    p x productUpdate productScore typedUpdate typedScore
    fixed thresholdLo thresholdHi hThreshold
    (restrictedParams_rawUpdateScoreEqualities_to_updatedScoreBoundTarget
      p x productUpdate productScore typedUpdate typedScore
      fixed effect thresholdLo thresholdHi hThreshold hEffectUpdated
      hTypedUpdate hBase hUpdated hLowerBridgeStrong hUpperBridgeStrong)

end ProductRestrictedParamsScoreEffectBinding

end VFH2
