import VFH2.Product.ProductRestrictedParamsScoreEffectBinding

namespace VFH2

namespace ProductRestrictedParamsScoreWindow

def restrictedParamsBaseScoreWindow
    (p : VFH2.ProductRestrictedParams)
    (x : p.State)
    (productScore : p.State → Int)
    (fixed : Prop)
    (thresholdLo thresholdHi : Int) : Prop :=
  ProductBridgeGeneralization.genericBridgeTarget fixed
      (thresholdLo ≤ productScore x) ∧
    ProductBridgeGeneralization.genericBridgeTarget fixed
      (productScore x ≤ thresholdHi)

def restrictedParamsUpdatedScoreWindow
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

def restrictedParamsBaseScoreWindowTarget
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
  restrictedParamsBaseScoreWindow
      p x productScore fixed thresholdLo thresholdHi ∧
    VFH2.ProductEffectBoundConditionMonotonicity.RestrictedEffectBoundMonotoneTransportCertificate
      p x thresholdLo thresholdHi hThreshold ∧
    VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsRawUpdateScoreTransportCertificate
      p x productUpdate productScore typedUpdate typedScore

def restrictedParamsUpdatedScoreWindowTarget
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
  restrictedParamsUpdatedScoreWindow
      p x productUpdate productScore fixed thresholdLo thresholdHi ∧
    VFH2.ProductEffectBoundConditionMonotonicity.RestrictedEffectBoundMonotoneTransportCertificate
      p x thresholdLo thresholdHi hThreshold ∧
    VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsRawUpdateScoreTransportCertificate
      p x productUpdate productScore typedUpdate typedScore

def restrictedParamsBaseAndUpdatedScoreWindowTarget
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
  restrictedParamsBaseScoreWindowTarget
      p x productUpdate productScore typedUpdate typedScore
      fixed thresholdLo thresholdHi hThreshold ∧
    restrictedParamsUpdatedScoreWindowTarget
      p x productUpdate productScore typedUpdate typedScore
      fixed thresholdLo thresholdHi hThreshold

theorem restrictedParams_baseScoreBoundTarget_to_scoreWindowTarget
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
    (hBound :
      VFH2.ProductRestrictedParamsScoreEffectBinding.restrictedParamsBaseScoreBoundTarget
        p x productUpdate productScore typedUpdate typedScore
        fixed thresholdLo thresholdHi hThreshold) :
    restrictedParamsBaseScoreWindowTarget
      p x productUpdate productScore typedUpdate typedScore
      fixed thresholdLo thresholdHi hThreshold := by
  have hLower :
      ProductBridgeGeneralization.genericBridgeTarget fixed
        (thresholdLo ≤ productScore x) :=
    VFH2.ProductRestrictedParamsScoreEffectBinding.restrictedParams_baseScoreBound_lower_projection
      p x productUpdate productScore typedUpdate typedScore
      fixed thresholdLo thresholdHi hThreshold hBound
  have hUpper :
      ProductBridgeGeneralization.genericBridgeTarget fixed
        (productScore x ≤ thresholdHi) :=
    VFH2.ProductRestrictedParamsScoreEffectBinding.restrictedParams_baseScoreBound_upper_projection
      p x productUpdate productScore typedUpdate typedScore
      fixed thresholdLo thresholdHi hThreshold hBound
  unfold restrictedParamsBaseScoreWindowTarget
  unfold VFH2.ProductRestrictedParamsScoreEffectBinding.restrictedParamsBaseScoreBoundTarget at hBound
  exact ⟨⟨hLower, hUpper⟩, ⟨hBound.2.2.1, hBound.2.2.2⟩⟩

theorem restrictedParams_updatedScoreBoundTarget_to_scoreWindowTarget
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
    (hBound :
      VFH2.ProductRestrictedParamsScoreEffectBinding.restrictedParamsUpdatedScoreBoundTarget
        p x productUpdate productScore typedUpdate typedScore
        fixed thresholdLo thresholdHi hThreshold) :
    restrictedParamsUpdatedScoreWindowTarget
      p x productUpdate productScore typedUpdate typedScore
      fixed thresholdLo thresholdHi hThreshold := by
  have hLower :
      ProductBridgeGeneralization.genericBridgeTarget fixed
        (thresholdLo ≤ productScore (productUpdate x)) :=
    VFH2.ProductRestrictedParamsScoreEffectBinding.restrictedParams_updatedScoreBound_lower_projection
      p x productUpdate productScore typedUpdate typedScore
      fixed thresholdLo thresholdHi hThreshold hBound
  have hUpper :
      ProductBridgeGeneralization.genericBridgeTarget fixed
        (productScore (productUpdate x) ≤ thresholdHi) :=
    VFH2.ProductRestrictedParamsScoreEffectBinding.restrictedParams_updatedScoreBound_upper_projection
      p x productUpdate productScore typedUpdate typedScore
      fixed thresholdLo thresholdHi hThreshold hBound
  unfold restrictedParamsUpdatedScoreWindowTarget
  unfold VFH2.ProductRestrictedParamsScoreEffectBinding.restrictedParamsUpdatedScoreBoundTarget at hBound
  exact ⟨⟨hLower, hUpper⟩, ⟨hBound.2.2.1, hBound.2.2.2⟩⟩

theorem restrictedParams_rawUpdateScoreEqualities_to_baseScoreWindowTarget
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
    restrictedParamsBaseScoreWindowTarget
      p x productUpdate productScore typedUpdate typedScore
      fixed thresholdLo thresholdHi hThreshold := by
  exact restrictedParams_baseScoreBoundTarget_to_scoreWindowTarget
    p x productUpdate productScore typedUpdate typedScore
    fixed thresholdLo thresholdHi hThreshold
    (VFH2.ProductRestrictedParamsScoreEffectBinding.restrictedParams_rawUpdateScoreEqualities_to_baseScoreBoundTarget
      p x productUpdate productScore typedUpdate typedScore
      fixed effect thresholdLo thresholdHi hThreshold hEffectBase
      hTypedUpdate hBase hUpdated hLowerBridgeStrong hUpperBridgeStrong)

theorem restrictedParams_rawUpdateScoreEqualities_to_updatedScoreWindowTarget
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
    restrictedParamsUpdatedScoreWindowTarget
      p x productUpdate productScore typedUpdate typedScore
      fixed thresholdLo thresholdHi hThreshold := by
  exact restrictedParams_updatedScoreBoundTarget_to_scoreWindowTarget
    p x productUpdate productScore typedUpdate typedScore
    fixed thresholdLo thresholdHi hThreshold
    (VFH2.ProductRestrictedParamsScoreEffectBinding.restrictedParams_rawUpdateScoreEqualities_to_updatedScoreBoundTarget
      p x productUpdate productScore typedUpdate typedScore
      fixed effect thresholdLo thresholdHi hThreshold hEffectUpdated
      hTypedUpdate hBase hUpdated hLowerBridgeStrong hUpperBridgeStrong)

theorem restrictedParams_rawUpdateScoreEqualities_to_baseAndUpdatedScoreWindowTarget
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
    (baseEffect updatedEffect thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi)
    (hEffectBase : baseEffect = productScore x)
    (hEffectUpdated : updatedEffect = productScore (productUpdate x))
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
        (baseEffect ≤ thresholdLo))
    (hUpdatedLowerBridgeStrong :
      ProductBridgeGeneralization.genericBridgeTarget fixed
        (thresholdHi ≤ updatedEffect))
    (hUpdatedUpperBridgeStrong :
      ProductBridgeGeneralization.genericBridgeTarget fixed
        (updatedEffect ≤ thresholdLo)) :
    restrictedParamsBaseAndUpdatedScoreWindowTarget
      p x productUpdate productScore typedUpdate typedScore
      fixed thresholdLo thresholdHi hThreshold := by
  unfold restrictedParamsBaseAndUpdatedScoreWindowTarget
  exact ⟨
    restrictedParams_rawUpdateScoreEqualities_to_baseScoreWindowTarget
      p x productUpdate productScore typedUpdate typedScore
      fixed baseEffect thresholdLo thresholdHi hThreshold hEffectBase
      hTypedUpdate hBase hUpdated hBaseLowerBridgeStrong hBaseUpperBridgeStrong,
    restrictedParams_rawUpdateScoreEqualities_to_updatedScoreWindowTarget
      p x productUpdate productScore typedUpdate typedScore
      fixed updatedEffect thresholdLo thresholdHi hThreshold hEffectUpdated
      hTypedUpdate hBase hUpdated hUpdatedLowerBridgeStrong hUpdatedUpperBridgeStrong
  ⟩

theorem restrictedParams_baseScoreWindow_lower_projection
    (p : VFH2.ProductRestrictedParams)
    (x : p.State)
    (productScore : p.State → Int)
    (fixed : Prop)
    (thresholdLo thresholdHi : Int)
    (hWindow :
      restrictedParamsBaseScoreWindow
        p x productScore fixed thresholdLo thresholdHi) :
    ProductBridgeGeneralization.genericBridgeTarget fixed
      (thresholdLo ≤ productScore x) := by
  unfold restrictedParamsBaseScoreWindow at hWindow
  exact hWindow.1

theorem restrictedParams_baseScoreWindow_upper_projection
    (p : VFH2.ProductRestrictedParams)
    (x : p.State)
    (productScore : p.State → Int)
    (fixed : Prop)
    (thresholdLo thresholdHi : Int)
    (hWindow :
      restrictedParamsBaseScoreWindow
        p x productScore fixed thresholdLo thresholdHi) :
    ProductBridgeGeneralization.genericBridgeTarget fixed
      (productScore x ≤ thresholdHi) := by
  unfold restrictedParamsBaseScoreWindow at hWindow
  exact hWindow.2

theorem restrictedParams_updatedScoreWindow_lower_projection
    (p : VFH2.ProductRestrictedParams)
    (x : p.State)
    (productUpdate : p.State → p.State)
    (productScore : p.State → Int)
    (fixed : Prop)
    (thresholdLo thresholdHi : Int)
    (hWindow :
      restrictedParamsUpdatedScoreWindow
        p x productUpdate productScore fixed thresholdLo thresholdHi) :
    ProductBridgeGeneralization.genericBridgeTarget fixed
      (thresholdLo ≤ productScore (productUpdate x)) := by
  unfold restrictedParamsUpdatedScoreWindow at hWindow
  exact hWindow.1

theorem restrictedParams_updatedScoreWindow_upper_projection
    (p : VFH2.ProductRestrictedParams)
    (x : p.State)
    (productUpdate : p.State → p.State)
    (productScore : p.State → Int)
    (fixed : Prop)
    (thresholdLo thresholdHi : Int)
    (hWindow :
      restrictedParamsUpdatedScoreWindow
        p x productUpdate productScore fixed thresholdLo thresholdHi) :
    ProductBridgeGeneralization.genericBridgeTarget fixed
      (productScore (productUpdate x) ≤ thresholdHi) := by
  unfold restrictedParamsUpdatedScoreWindow at hWindow
  exact hWindow.2

theorem restrictedParams_baseScoreWindowTarget_window_projection
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
      restrictedParamsBaseScoreWindowTarget
        p x productUpdate productScore typedUpdate typedScore
        fixed thresholdLo thresholdHi hThreshold) :
    restrictedParamsBaseScoreWindow
      p x productScore fixed thresholdLo thresholdHi := by
  unfold restrictedParamsBaseScoreWindowTarget at hTarget
  exact hTarget.1

theorem restrictedParams_updatedScoreWindowTarget_window_projection
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
      restrictedParamsUpdatedScoreWindowTarget
        p x productUpdate productScore typedUpdate typedScore
        fixed thresholdLo thresholdHi hThreshold) :
    restrictedParamsUpdatedScoreWindow
      p x productUpdate productScore fixed thresholdLo thresholdHi := by
  unfold restrictedParamsUpdatedScoreWindowTarget at hTarget
  exact hTarget.1

end ProductRestrictedParamsScoreWindow

end VFH2
