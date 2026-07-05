import VFH2.Product.ProductRestrictedParamsScoreWindow

namespace VFH2

namespace ProductRestrictedParamsScoreWindowPreservation

def restrictedParamsScoreWindowPreservationSource
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
    (updatedEffect thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi) : Prop :=
  VFH2.ProductRestrictedParamsScoreWindow.restrictedParamsBaseScoreWindowTarget
      p x productUpdate productScore typedUpdate typedScore
      fixed thresholdLo thresholdHi hThreshold ∧
    VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsRawUpdateScoreTransportCertificate
      p x productUpdate productScore typedUpdate typedScore ∧
    updatedEffect = productScore (productUpdate x) ∧
    ProductBridgeGeneralization.genericBridgeTarget fixed
      (thresholdHi ≤ updatedEffect) ∧
    ProductBridgeGeneralization.genericBridgeTarget fixed
      (updatedEffect ≤ thresholdLo)

def restrictedParamsScoreWindowPreservationTarget
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
  VFH2.ProductRestrictedParamsScoreWindow.restrictedParamsBaseAndUpdatedScoreWindowTarget
      p x productUpdate productScore typedUpdate typedScore
      fixed thresholdLo thresholdHi hThreshold

theorem restrictedParams_scoreWindowPreservation_from_baseWindowTarget
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
    (updatedEffect thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi)
    (hSource :
      restrictedParamsScoreWindowPreservationSource
        p x productUpdate productScore typedUpdate typedScore
        fixed updatedEffect thresholdLo thresholdHi hThreshold) :
    restrictedParamsScoreWindowPreservationTarget
      p x productUpdate productScore typedUpdate typedScore
      fixed thresholdLo thresholdHi hThreshold := by
  unfold restrictedParamsScoreWindowPreservationSource at hSource
  unfold restrictedParamsScoreWindowPreservationTarget
  exact ⟨
    hSource.1,
    VFH2.ProductRestrictedParamsScoreWindow.restrictedParams_rawUpdateScoreEqualities_to_updatedScoreWindowTarget
      p x productUpdate productScore typedUpdate typedScore
      fixed updatedEffect thresholdLo thresholdHi hThreshold
      hSource.2.2.1
      hSource.2.1.1
      hSource.2.1.2.1
      hSource.2.1.2.2
      hSource.2.2.2.1
      hSource.2.2.2.2
  ⟩

theorem restrictedParams_scoreWindowPreservation_from_rawEqualities
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
    (updatedEffect thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi)
    (hBaseWindowTarget :
      VFH2.ProductRestrictedParamsScoreWindow.restrictedParamsBaseScoreWindowTarget
        p x productUpdate productScore typedUpdate typedScore
        fixed thresholdLo thresholdHi hThreshold)
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
    (hUpdatedLowerBridgeStrong :
      ProductBridgeGeneralization.genericBridgeTarget fixed
        (thresholdHi ≤ updatedEffect))
    (hUpdatedUpperBridgeStrong :
      ProductBridgeGeneralization.genericBridgeTarget fixed
        (updatedEffect ≤ thresholdLo)) :
    restrictedParamsScoreWindowPreservationTarget
      p x productUpdate productScore typedUpdate typedScore
      fixed thresholdLo thresholdHi hThreshold := by
  exact restrictedParams_scoreWindowPreservation_from_baseWindowTarget
    p x productUpdate productScore typedUpdate typedScore
    fixed updatedEffect thresholdLo thresholdHi hThreshold
    ⟨hBaseWindowTarget,
      ⟨⟨hTypedUpdate, ⟨hBase, hUpdated⟩⟩,
        ⟨hEffectUpdated, ⟨hUpdatedLowerBridgeStrong, hUpdatedUpperBridgeStrong⟩⟩⟩⟩

theorem restrictedParams_scoreWindowPreservation_baseTarget_projection
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
      restrictedParamsScoreWindowPreservationTarget
        p x productUpdate productScore typedUpdate typedScore
        fixed thresholdLo thresholdHi hThreshold) :
    VFH2.ProductRestrictedParamsScoreWindow.restrictedParamsBaseScoreWindowTarget
      p x productUpdate productScore typedUpdate typedScore
      fixed thresholdLo thresholdHi hThreshold := by
  unfold restrictedParamsScoreWindowPreservationTarget at hTarget
  unfold VFH2.ProductRestrictedParamsScoreWindow.restrictedParamsBaseAndUpdatedScoreWindowTarget at hTarget
  exact hTarget.1

theorem restrictedParams_scoreWindowPreservation_updatedTarget_projection
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
      restrictedParamsScoreWindowPreservationTarget
        p x productUpdate productScore typedUpdate typedScore
        fixed thresholdLo thresholdHi hThreshold) :
    VFH2.ProductRestrictedParamsScoreWindow.restrictedParamsUpdatedScoreWindowTarget
      p x productUpdate productScore typedUpdate typedScore
      fixed thresholdLo thresholdHi hThreshold := by
  unfold restrictedParamsScoreWindowPreservationTarget at hTarget
  unfold VFH2.ProductRestrictedParamsScoreWindow.restrictedParamsBaseAndUpdatedScoreWindowTarget at hTarget
  exact hTarget.2

theorem restrictedParams_scoreWindowPreservation_baseWindow_projection
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
      restrictedParamsScoreWindowPreservationTarget
        p x productUpdate productScore typedUpdate typedScore
        fixed thresholdLo thresholdHi hThreshold) :
    VFH2.ProductRestrictedParamsScoreWindow.restrictedParamsBaseScoreWindow
      p x productScore fixed thresholdLo thresholdHi := by
  exact VFH2.ProductRestrictedParamsScoreWindow.restrictedParams_baseScoreWindowTarget_window_projection
    p x productUpdate productScore typedUpdate typedScore
    fixed thresholdLo thresholdHi hThreshold
    (restrictedParams_scoreWindowPreservation_baseTarget_projection
      p x productUpdate productScore typedUpdate typedScore
      fixed thresholdLo thresholdHi hThreshold hTarget)

theorem restrictedParams_scoreWindowPreservation_updatedWindow_projection
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
      restrictedParamsScoreWindowPreservationTarget
        p x productUpdate productScore typedUpdate typedScore
        fixed thresholdLo thresholdHi hThreshold) :
    VFH2.ProductRestrictedParamsScoreWindow.restrictedParamsUpdatedScoreWindow
      p x productUpdate productScore fixed thresholdLo thresholdHi := by
  exact VFH2.ProductRestrictedParamsScoreWindow.restrictedParams_updatedScoreWindowTarget_window_projection
    p x productUpdate productScore typedUpdate typedScore
    fixed thresholdLo thresholdHi hThreshold
    (restrictedParams_scoreWindowPreservation_updatedTarget_projection
      p x productUpdate productScore typedUpdate typedScore
      fixed thresholdLo thresholdHi hThreshold hTarget)

theorem restrictedParams_scoreWindowPreservation_updatedLower_projection
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
      restrictedParamsScoreWindowPreservationTarget
        p x productUpdate productScore typedUpdate typedScore
        fixed thresholdLo thresholdHi hThreshold) :
    ProductBridgeGeneralization.genericBridgeTarget fixed
      (thresholdLo ≤ productScore (productUpdate x)) := by
  exact VFH2.ProductRestrictedParamsScoreWindow.restrictedParams_updatedScoreWindow_lower_projection
    p x productUpdate productScore fixed thresholdLo thresholdHi
    (restrictedParams_scoreWindowPreservation_updatedWindow_projection
      p x productUpdate productScore typedUpdate typedScore
      fixed thresholdLo thresholdHi hThreshold hTarget)

theorem restrictedParams_scoreWindowPreservation_updatedUpper_projection
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
      restrictedParamsScoreWindowPreservationTarget
        p x productUpdate productScore typedUpdate typedScore
        fixed thresholdLo thresholdHi hThreshold) :
    ProductBridgeGeneralization.genericBridgeTarget fixed
      (productScore (productUpdate x) ≤ thresholdHi) := by
  exact VFH2.ProductRestrictedParamsScoreWindow.restrictedParams_updatedScoreWindow_upper_projection
    p x productUpdate productScore fixed thresholdLo thresholdHi
    (restrictedParams_scoreWindowPreservation_updatedWindow_projection
      p x productUpdate productScore typedUpdate typedScore
      fixed thresholdLo thresholdHi hThreshold hTarget)

theorem restrictedParams_scoreWindowPreservation_from_rawEqualities_to_updatedLower
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
    (updatedEffect thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi)
    (hBaseWindowTarget :
      VFH2.ProductRestrictedParamsScoreWindow.restrictedParamsBaseScoreWindowTarget
        p x productUpdate productScore typedUpdate typedScore
        fixed thresholdLo thresholdHi hThreshold)
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
    (hUpdatedLowerBridgeStrong :
      ProductBridgeGeneralization.genericBridgeTarget fixed
        (thresholdHi ≤ updatedEffect))
    (hUpdatedUpperBridgeStrong :
      ProductBridgeGeneralization.genericBridgeTarget fixed
        (updatedEffect ≤ thresholdLo)) :
    ProductBridgeGeneralization.genericBridgeTarget fixed
      (thresholdLo ≤ productScore (productUpdate x)) := by
  exact restrictedParams_scoreWindowPreservation_updatedLower_projection
    p x productUpdate productScore typedUpdate typedScore
    fixed thresholdLo thresholdHi hThreshold
    (restrictedParams_scoreWindowPreservation_from_rawEqualities
      p x productUpdate productScore typedUpdate typedScore
      fixed updatedEffect thresholdLo thresholdHi hThreshold
      hBaseWindowTarget hEffectUpdated hTypedUpdate hBase hUpdated
      hUpdatedLowerBridgeStrong hUpdatedUpperBridgeStrong)

theorem restrictedParams_scoreWindowPreservation_from_rawEqualities_to_updatedUpper
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
    (updatedEffect thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi)
    (hBaseWindowTarget :
      VFH2.ProductRestrictedParamsScoreWindow.restrictedParamsBaseScoreWindowTarget
        p x productUpdate productScore typedUpdate typedScore
        fixed thresholdLo thresholdHi hThreshold)
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
    (hUpdatedLowerBridgeStrong :
      ProductBridgeGeneralization.genericBridgeTarget fixed
        (thresholdHi ≤ updatedEffect))
    (hUpdatedUpperBridgeStrong :
      ProductBridgeGeneralization.genericBridgeTarget fixed
        (updatedEffect ≤ thresholdLo)) :
    ProductBridgeGeneralization.genericBridgeTarget fixed
      (productScore (productUpdate x) ≤ thresholdHi) := by
  exact restrictedParams_scoreWindowPreservation_updatedUpper_projection
    p x productUpdate productScore typedUpdate typedScore
    fixed thresholdLo thresholdHi hThreshold
    (restrictedParams_scoreWindowPreservation_from_rawEqualities
      p x productUpdate productScore typedUpdate typedScore
      fixed updatedEffect thresholdLo thresholdHi hThreshold
      hBaseWindowTarget hEffectUpdated hTypedUpdate hBase hUpdated
      hUpdatedLowerBridgeStrong hUpdatedUpperBridgeStrong)

end ProductRestrictedParamsScoreWindowPreservation

end VFH2
