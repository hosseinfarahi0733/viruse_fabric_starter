import VFH2.Product.ProductRestrictedParamsUpdateScoreTransport

namespace VFH2

namespace ProductRestrictedParamsUpdateScoreBound

def restrictedParamsUpdateScoreBoundTarget
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
    (hThreshold : thresholdLo ≤ thresholdHi) : Prop :=
  ProductBridgeGeneralization.genericBridgeTarget fixed
      (thresholdLo ≤ effect) ∧
    ProductBridgeGeneralization.genericBridgeTarget fixed
      (effect ≤ thresholdHi) ∧
    VFH2.ProductEffectBoundConditionMonotonicity.RestrictedEffectBoundMonotoneTransportCertificate
      p x thresholdLo thresholdHi hThreshold ∧
    VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsRawUpdateScoreTransportCertificate
      p x productUpdate productScore typedUpdate typedScore

theorem restrictedParams_rawUpdateScoreTransportSource_to_boundTarget
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
    (hSource :
      VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsRawUpdateScoreTransportSource
        p x productUpdate productScore typedUpdate typedScore
        fixed effect thresholdLo thresholdHi) :
    restrictedParamsUpdateScoreBoundTarget
      p x productUpdate productScore typedUpdate typedScore
      fixed effect thresholdLo thresholdHi hThreshold := by
  unfold restrictedParamsUpdateScoreBoundTarget
  exact ⟨
    VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParams_rawUpdateScoreTransport_lower_projection
      p x productUpdate productScore typedUpdate typedScore
      fixed effect thresholdLo thresholdHi hThreshold hSource,
    VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParams_rawUpdateScoreTransport_upper_projection
      p x productUpdate productScore typedUpdate typedScore
      fixed effect thresholdLo thresholdHi hThreshold hSource,
    VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParams_rawUpdateScoreTransport_restrictedCertificate_projection
      p x productUpdate productScore typedUpdate typedScore
      fixed effect thresholdLo thresholdHi hThreshold hSource,
    VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParams_rawUpdateScoreTransport_certificate_preserved
      p x productUpdate productScore typedUpdate typedScore
      fixed effect thresholdLo thresholdHi hThreshold hSource
  ⟩

theorem restrictedParams_rawUpdateScoreEqualities_to_boundTarget
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
    restrictedParamsUpdateScoreBoundTarget
      p x productUpdate productScore typedUpdate typedScore
      fixed effect thresholdLo thresholdHi hThreshold := by
  exact restrictedParams_rawUpdateScoreTransportSource_to_boundTarget
    p x productUpdate productScore typedUpdate typedScore
    fixed effect thresholdLo thresholdHi hThreshold
    ⟨⟨hTypedUpdate, ⟨hBase, hUpdated⟩⟩,
      ⟨hLowerBridgeStrong, hUpperBridgeStrong⟩⟩

theorem restrictedParams_updateScoreBound_lower_projection
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
    (hTarget :
      restrictedParamsUpdateScoreBoundTarget
        p x productUpdate productScore typedUpdate typedScore
        fixed effect thresholdLo thresholdHi hThreshold) :
    ProductBridgeGeneralization.genericBridgeTarget fixed
      (thresholdLo ≤ effect) := by
  unfold restrictedParamsUpdateScoreBoundTarget at hTarget
  exact hTarget.1

theorem restrictedParams_updateScoreBound_upper_projection
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
    (hTarget :
      restrictedParamsUpdateScoreBoundTarget
        p x productUpdate productScore typedUpdate typedScore
        fixed effect thresholdLo thresholdHi hThreshold) :
    ProductBridgeGeneralization.genericBridgeTarget fixed
      (effect ≤ thresholdHi) := by
  unfold restrictedParamsUpdateScoreBoundTarget at hTarget
  exact hTarget.2.1

theorem restrictedParams_updateScoreBound_restrictedCertificate_projection
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
    (hTarget :
      restrictedParamsUpdateScoreBoundTarget
        p x productUpdate productScore typedUpdate typedScore
        fixed effect thresholdLo thresholdHi hThreshold) :
    VFH2.ProductEffectBoundConditionMonotonicity.RestrictedEffectBoundMonotoneTransportCertificate
      p x thresholdLo thresholdHi hThreshold := by
  unfold restrictedParamsUpdateScoreBoundTarget at hTarget
  exact hTarget.2.2.1

theorem restrictedParams_updateScoreBound_rawTransportCertificate_projection
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
    (hTarget :
      restrictedParamsUpdateScoreBoundTarget
        p x productUpdate productScore typedUpdate typedScore
        fixed effect thresholdLo thresholdHi hThreshold) :
    VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsRawUpdateScoreTransportCertificate
      p x productUpdate productScore typedUpdate typedScore := by
  unfold restrictedParamsUpdateScoreBoundTarget at hTarget
  exact hTarget.2.2.2

theorem restrictedParams_rawUpdateScoreEqualities_to_lowerBound
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
      (thresholdLo ≤ effect) := by
  exact restrictedParams_updateScoreBound_lower_projection
    p x productUpdate productScore typedUpdate typedScore
    fixed effect thresholdLo thresholdHi hThreshold
    (restrictedParams_rawUpdateScoreEqualities_to_boundTarget
      p x productUpdate productScore typedUpdate typedScore
      fixed effect thresholdLo thresholdHi hThreshold
      hTypedUpdate hBase hUpdated hLowerBridgeStrong hUpperBridgeStrong)

theorem restrictedParams_rawUpdateScoreEqualities_to_upperBound
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
      (effect ≤ thresholdHi) := by
  exact restrictedParams_updateScoreBound_upper_projection
    p x productUpdate productScore typedUpdate typedScore
    fixed effect thresholdLo thresholdHi hThreshold
    (restrictedParams_rawUpdateScoreEqualities_to_boundTarget
      p x productUpdate productScore typedUpdate typedScore
      fixed effect thresholdLo thresholdHi hThreshold
      hTypedUpdate hBase hUpdated hLowerBridgeStrong hUpperBridgeStrong)

theorem restrictedParams_rawUpdateScoreEqualities_to_restrictedCertificate
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
    VFH2.ProductEffectBoundConditionMonotonicity.RestrictedEffectBoundMonotoneTransportCertificate
      p x thresholdLo thresholdHi hThreshold := by
  exact restrictedParams_updateScoreBound_restrictedCertificate_projection
    p x productUpdate productScore typedUpdate typedScore
    fixed effect thresholdLo thresholdHi hThreshold
    (restrictedParams_rawUpdateScoreEqualities_to_boundTarget
      p x productUpdate productScore typedUpdate typedScore
      fixed effect thresholdLo thresholdHi hThreshold
      hTypedUpdate hBase hUpdated hLowerBridgeStrong hUpperBridgeStrong)

end ProductRestrictedParamsUpdateScoreBound

end VFH2
