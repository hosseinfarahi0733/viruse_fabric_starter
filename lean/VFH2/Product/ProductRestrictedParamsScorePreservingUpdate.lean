import VFH2.Product.ProductRestrictedParamsScoreWindowPreservation

namespace VFH2

namespace ProductRestrictedParamsScorePreservingUpdate

def restrictedParamsScorePreservingUpdateWindowSource
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
    productScore (productUpdate x) = productScore x

def restrictedParamsScorePreservingUpdateWindowTarget
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

theorem restrictedParams_scorePreservingUpdate_baseWindow_to_updatedWindowTarget
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
    (hScorePreserved :
      productScore (productUpdate x) = productScore x) :
    VFH2.ProductRestrictedParamsScoreWindow.restrictedParamsUpdatedScoreWindowTarget
      p x productUpdate productScore typedUpdate typedScore
      fixed thresholdLo thresholdHi hThreshold := by
  have hBaseWindow :
      VFH2.ProductRestrictedParamsScoreWindow.restrictedParamsBaseScoreWindow
        p x productScore fixed thresholdLo thresholdHi :=
    VFH2.ProductRestrictedParamsScoreWindow.restrictedParams_baseScoreWindowTarget_window_projection
      p x productUpdate productScore typedUpdate typedScore
      fixed thresholdLo thresholdHi hThreshold hBaseTarget
  have hUpdatedLower :
      ProductBridgeGeneralization.genericBridgeTarget fixed
        (thresholdLo ≤ productScore (productUpdate x)) := by
    exact
      (by
        simpa [hScorePreserved] using
          (VFH2.ProductRestrictedParamsScoreWindow.restrictedParams_baseScoreWindow_lower_projection
            p x productScore fixed thresholdLo thresholdHi hBaseWindow))
  have hUpdatedUpper :
      ProductBridgeGeneralization.genericBridgeTarget fixed
        (productScore (productUpdate x) ≤ thresholdHi) := by
    exact
      (by
        simpa [hScorePreserved] using
          (VFH2.ProductRestrictedParamsScoreWindow.restrictedParams_baseScoreWindow_upper_projection
            p x productScore fixed thresholdLo thresholdHi hBaseWindow))
  unfold VFH2.ProductRestrictedParamsScoreWindow.restrictedParamsBaseScoreWindowTarget at hBaseTarget
  unfold VFH2.ProductRestrictedParamsScoreWindow.restrictedParamsUpdatedScoreWindowTarget
  exact ⟨
    ⟨hUpdatedLower, hUpdatedUpper⟩,
    ⟨hBaseTarget.2.1, hBaseTarget.2.2⟩
  ⟩

theorem restrictedParams_scorePreservingUpdate_baseWindow_to_baseAndUpdatedWindowTarget
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
    (hScorePreserved :
      productScore (productUpdate x) = productScore x) :
    restrictedParamsScorePreservingUpdateWindowTarget
      p x productUpdate productScore typedUpdate typedScore
      fixed thresholdLo thresholdHi hThreshold := by
  unfold restrictedParamsScorePreservingUpdateWindowTarget
  unfold VFH2.ProductRestrictedParamsScoreWindow.restrictedParamsBaseAndUpdatedScoreWindowTarget
  exact ⟨
    hBaseTarget,
    restrictedParams_scorePreservingUpdate_baseWindow_to_updatedWindowTarget
      p x productUpdate productScore typedUpdate typedScore
      fixed thresholdLo thresholdHi hThreshold hBaseTarget hScorePreserved
  ⟩

theorem restrictedParams_scorePreservingUpdate_source_to_target
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
      restrictedParamsScorePreservingUpdateWindowSource
        p x productUpdate productScore typedUpdate typedScore
        fixed thresholdLo thresholdHi hThreshold) :
    restrictedParamsScorePreservingUpdateWindowTarget
      p x productUpdate productScore typedUpdate typedScore
      fixed thresholdLo thresholdHi hThreshold := by
  unfold restrictedParamsScorePreservingUpdateWindowSource at hSource
  unfold restrictedParamsScorePreservingUpdateWindowTarget
  unfold VFH2.ProductRestrictedParamsScoreWindow.restrictedParamsBaseAndUpdatedScoreWindowTarget
  have hBaseTarget :
      VFH2.ProductRestrictedParamsScoreWindow.restrictedParamsBaseScoreWindowTarget
        p x productUpdate productScore typedUpdate typedScore
        fixed thresholdLo thresholdHi hThreshold := hSource.1
  have hScorePreserved :
      productScore (productUpdate x) = productScore x := hSource.2.2
  have hUpdated :
      VFH2.ProductRestrictedParamsScoreWindow.restrictedParamsUpdatedScoreWindowTarget
        p x productUpdate productScore typedUpdate typedScore
        fixed thresholdLo thresholdHi hThreshold :=
    restrictedParams_scorePreservingUpdate_baseWindow_to_updatedWindowTarget
      p x productUpdate productScore typedUpdate typedScore
      fixed thresholdLo thresholdHi hThreshold hBaseTarget hScorePreserved
  unfold VFH2.ProductRestrictedParamsScoreWindow.restrictedParamsUpdatedScoreWindowTarget at hUpdated
  exact ⟨
    hBaseTarget,
    ⟨hUpdated.1, ⟨hSource.1.2.1, hSource.2.1⟩⟩
  ⟩

theorem restrictedParams_rawUpdateScoreEqualities_and_scorePreservation_to_target
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
    (hScorePreserved :
      productScore (productUpdate x) = productScore x)
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
    restrictedParamsScorePreservingUpdateWindowTarget
      p x productUpdate productScore typedUpdate typedScore
      fixed thresholdLo thresholdHi hThreshold := by
  have hBaseTarget :
      VFH2.ProductRestrictedParamsScoreWindow.restrictedParamsBaseScoreWindowTarget
        p x productUpdate productScore typedUpdate typedScore
        fixed thresholdLo thresholdHi hThreshold :=
    VFH2.ProductRestrictedParamsScoreWindow.restrictedParams_rawUpdateScoreEqualities_to_baseScoreWindowTarget
      p x productUpdate productScore typedUpdate typedScore
      fixed baseEffect thresholdLo thresholdHi hThreshold hEffectBase
      hTypedUpdate hBase hUpdated hBaseLowerBridgeStrong hBaseUpperBridgeStrong
  exact restrictedParams_scorePreservingUpdate_baseWindow_to_baseAndUpdatedWindowTarget
    p x productUpdate productScore typedUpdate typedScore
    fixed thresholdLo thresholdHi hThreshold hBaseTarget hScorePreserved

theorem restrictedParams_scorePreservingUpdate_target_base_projection
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
      restrictedParamsScorePreservingUpdateWindowTarget
        p x productUpdate productScore typedUpdate typedScore
        fixed thresholdLo thresholdHi hThreshold) :
    VFH2.ProductRestrictedParamsScoreWindow.restrictedParamsBaseScoreWindowTarget
      p x productUpdate productScore typedUpdate typedScore
      fixed thresholdLo thresholdHi hThreshold := by
  unfold restrictedParamsScorePreservingUpdateWindowTarget at hTarget
  unfold VFH2.ProductRestrictedParamsScoreWindow.restrictedParamsBaseAndUpdatedScoreWindowTarget at hTarget
  exact hTarget.1

theorem restrictedParams_scorePreservingUpdate_target_updated_projection
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
      restrictedParamsScorePreservingUpdateWindowTarget
        p x productUpdate productScore typedUpdate typedScore
        fixed thresholdLo thresholdHi hThreshold) :
    VFH2.ProductRestrictedParamsScoreWindow.restrictedParamsUpdatedScoreWindowTarget
      p x productUpdate productScore typedUpdate typedScore
      fixed thresholdLo thresholdHi hThreshold := by
  unfold restrictedParamsScorePreservingUpdateWindowTarget at hTarget
  unfold VFH2.ProductRestrictedParamsScoreWindow.restrictedParamsBaseAndUpdatedScoreWindowTarget at hTarget
  exact hTarget.2

theorem restrictedParams_scorePreservingUpdate_updatedLower_projection
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
      restrictedParamsScorePreservingUpdateWindowTarget
        p x productUpdate productScore typedUpdate typedScore
        fixed thresholdLo thresholdHi hThreshold) :
    ProductBridgeGeneralization.genericBridgeTarget fixed
      (thresholdLo ≤ productScore (productUpdate x)) := by
  exact VFH2.ProductRestrictedParamsScoreWindowPreservation.restrictedParams_scoreWindowPreservation_updatedLower_projection
    p x productUpdate productScore typedUpdate typedScore
    fixed thresholdLo thresholdHi hThreshold hTarget

theorem restrictedParams_scorePreservingUpdate_updatedUpper_projection
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
      restrictedParamsScorePreservingUpdateWindowTarget
        p x productUpdate productScore typedUpdate typedScore
        fixed thresholdLo thresholdHi hThreshold) :
    ProductBridgeGeneralization.genericBridgeTarget fixed
      (productScore (productUpdate x) ≤ thresholdHi) := by
  exact VFH2.ProductRestrictedParamsScoreWindowPreservation.restrictedParams_scoreWindowPreservation_updatedUpper_projection
    p x productUpdate productScore typedUpdate typedScore
    fixed thresholdLo thresholdHi hThreshold hTarget

theorem restrictedParams_rawUpdateScoreEqualities_and_scorePreservation_to_updatedLower
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
    (hScorePreserved :
      productScore (productUpdate x) = productScore x)
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
  exact restrictedParams_scorePreservingUpdate_updatedLower_projection
    p x productUpdate productScore typedUpdate typedScore
    fixed thresholdLo thresholdHi hThreshold
    (restrictedParams_rawUpdateScoreEqualities_and_scorePreservation_to_target
      p x productUpdate productScore typedUpdate typedScore
      fixed baseEffect thresholdLo thresholdHi hThreshold hEffectBase hScorePreserved
      hTypedUpdate hBase hUpdated hBaseLowerBridgeStrong hBaseUpperBridgeStrong)

theorem restrictedParams_rawUpdateScoreEqualities_and_scorePreservation_to_updatedUpper
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
    (hScorePreserved :
      productScore (productUpdate x) = productScore x)
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
  exact restrictedParams_scorePreservingUpdate_updatedUpper_projection
    p x productUpdate productScore typedUpdate typedScore
    fixed thresholdLo thresholdHi hThreshold
    (restrictedParams_rawUpdateScoreEqualities_and_scorePreservation_to_target
      p x productUpdate productScore typedUpdate typedScore
      fixed baseEffect thresholdLo thresholdHi hThreshold hEffectBase hScorePreserved
      hTypedUpdate hBase hUpdated hBaseLowerBridgeStrong hBaseUpperBridgeStrong)

end ProductRestrictedParamsScorePreservingUpdate

end VFH2
