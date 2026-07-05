import VFH2.Product.ProductBridgeRelaxationCertificate

namespace VFH2

namespace ProductRestrictedThresholdConditionedBridgeTheorem

theorem restricted_productLowerThresholdConditionedBridge_theorem
    (fixed : Prop)
    (productLedgerEffect thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi)
    (hBridgeStrong :
      ProductBridgeGeneralization.genericBridgeTarget fixed
        (thresholdHi ≤ productLedgerEffect)) :
    ProductBridgeGeneralization.genericBridgeTarget fixed
      (thresholdLo ≤ productLedgerEffect) := by
  exact ProductBridgeRelaxationCertificate.bridgeRelaxation_restrictedProductLowerMono
    fixed productLedgerEffect thresholdLo thresholdHi hThreshold hBridgeStrong

theorem restricted_productUpperThresholdConditionedBridge_theorem
    (fixed : Prop)
    (productLedgerEffect thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi)
    (hBridgeStrong :
      ProductBridgeGeneralization.genericBridgeTarget fixed
        (productLedgerEffect ≤ thresholdLo)) :
    ProductBridgeGeneralization.genericBridgeTarget fixed
      (productLedgerEffect ≤ thresholdHi) := by
  exact ProductBridgeRelaxationCertificate.bridgeRelaxation_restrictedProductUpperMono
    fixed productLedgerEffect thresholdLo thresholdHi hThreshold hBridgeStrong

theorem restricted_typedLowerThresholdConditionedBridge_theorem
    (fixed : Prop)
    (typedLedgerEffect thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi)
    (hBridgeStrong :
      ProductBridgeGeneralization.genericBridgeTarget fixed
        (thresholdHi ≤ typedLedgerEffect)) :
    ProductBridgeGeneralization.genericBridgeTarget fixed
      (thresholdLo ≤ typedLedgerEffect) := by
  exact ProductBridgeRelaxationCertificate.bridgeRelaxation_certificate.restrictedTypedLowerMono
    fixed typedLedgerEffect thresholdLo thresholdHi hThreshold hBridgeStrong

theorem restricted_typedUpperThresholdConditionedBridge_theorem
    (fixed : Prop)
    (typedLedgerEffect thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi)
    (hBridgeStrong :
      ProductBridgeGeneralization.genericBridgeTarget fixed
        (typedLedgerEffect ≤ thresholdLo)) :
    ProductBridgeGeneralization.genericBridgeTarget fixed
      (typedLedgerEffect ≤ thresholdHi) := by
  exact ProductBridgeRelaxationCertificate.bridgeRelaxation_certificate.restrictedTypedUpperMono
    fixed typedLedgerEffect thresholdLo thresholdHi hThreshold hBridgeStrong

theorem restricted_productThresholdConditionedBridge_pair_theorem
    (fixed : Prop)
    (productLedgerEffect thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi)
    (hLowerBridgeStrong :
      ProductBridgeGeneralization.genericBridgeTarget fixed
        (thresholdHi ≤ productLedgerEffect))
    (hUpperBridgeStrong :
      ProductBridgeGeneralization.genericBridgeTarget fixed
        (productLedgerEffect ≤ thresholdLo)) :
    ProductBridgeGeneralization.genericBridgeTarget fixed
        (thresholdLo ≤ productLedgerEffect) ∧
      ProductBridgeGeneralization.genericBridgeTarget fixed
        (productLedgerEffect ≤ thresholdHi) := by
  exact ⟨
    restricted_productLowerThresholdConditionedBridge_theorem
      fixed productLedgerEffect thresholdLo thresholdHi hThreshold hLowerBridgeStrong,
    restricted_productUpperThresholdConditionedBridge_theorem
      fixed productLedgerEffect thresholdLo thresholdHi hThreshold hUpperBridgeStrong
  ⟩

theorem restricted_typedThresholdConditionedBridge_pair_theorem
    (fixed : Prop)
    (typedLedgerEffect thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi)
    (hLowerBridgeStrong :
      ProductBridgeGeneralization.genericBridgeTarget fixed
        (thresholdHi ≤ typedLedgerEffect))
    (hUpperBridgeStrong :
      ProductBridgeGeneralization.genericBridgeTarget fixed
        (typedLedgerEffect ≤ thresholdLo)) :
    ProductBridgeGeneralization.genericBridgeTarget fixed
        (thresholdLo ≤ typedLedgerEffect) ∧
      ProductBridgeGeneralization.genericBridgeTarget fixed
        (typedLedgerEffect ≤ thresholdHi) := by
  exact ⟨
    restricted_typedLowerThresholdConditionedBridge_theorem
      fixed typedLedgerEffect thresholdLo thresholdHi hThreshold hLowerBridgeStrong,
    restricted_typedUpperThresholdConditionedBridge_theorem
      fixed typedLedgerEffect thresholdLo thresholdHi hThreshold hUpperBridgeStrong
  ⟩

theorem restricted_thresholdConditionedBridge_combined_theorem
    (fixed : Prop)
    (typedLedgerEffect productLedgerEffect thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi)
    (hTypedLowerBridgeStrong :
      ProductBridgeGeneralization.genericBridgeTarget fixed
        (thresholdHi ≤ typedLedgerEffect))
    (hTypedUpperBridgeStrong :
      ProductBridgeGeneralization.genericBridgeTarget fixed
        (typedLedgerEffect ≤ thresholdLo))
    (hProductLowerBridgeStrong :
      ProductBridgeGeneralization.genericBridgeTarget fixed
        (thresholdHi ≤ productLedgerEffect))
    (hProductUpperBridgeStrong :
      ProductBridgeGeneralization.genericBridgeTarget fixed
        (productLedgerEffect ≤ thresholdLo)) :
    (ProductBridgeGeneralization.genericBridgeTarget fixed
        (thresholdLo ≤ typedLedgerEffect) ∧
      ProductBridgeGeneralization.genericBridgeTarget fixed
        (typedLedgerEffect ≤ thresholdHi)) ∧
    (ProductBridgeGeneralization.genericBridgeTarget fixed
        (thresholdLo ≤ productLedgerEffect) ∧
      ProductBridgeGeneralization.genericBridgeTarget fixed
        (productLedgerEffect ≤ thresholdHi)) := by
  exact ⟨
    restricted_typedThresholdConditionedBridge_pair_theorem
      fixed typedLedgerEffect thresholdLo thresholdHi hThreshold
      hTypedLowerBridgeStrong hTypedUpperBridgeStrong,
    restricted_productThresholdConditionedBridge_pair_theorem
      fixed productLedgerEffect thresholdLo thresholdHi hThreshold
      hProductLowerBridgeStrong hProductUpperBridgeStrong
  ⟩

theorem restricted_thresholdConditionedBridge_implication_theorem
    (fixed : Prop)
    (typedLedgerEffect productLedgerEffect thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi) :
    ((ProductBridgeGeneralization.genericBridgeTarget fixed
        (thresholdHi ≤ typedLedgerEffect) →
      ProductBridgeGeneralization.genericBridgeTarget fixed
        (thresholdLo ≤ typedLedgerEffect)) ∧
     (ProductBridgeGeneralization.genericBridgeTarget fixed
        (typedLedgerEffect ≤ thresholdLo) →
      ProductBridgeGeneralization.genericBridgeTarget fixed
        (typedLedgerEffect ≤ thresholdHi))) ∧
    ((ProductBridgeGeneralization.genericBridgeTarget fixed
        (thresholdHi ≤ productLedgerEffect) →
      ProductBridgeGeneralization.genericBridgeTarget fixed
        (thresholdLo ≤ productLedgerEffect)) ∧
     (ProductBridgeGeneralization.genericBridgeTarget fixed
        (productLedgerEffect ≤ thresholdLo) →
      ProductBridgeGeneralization.genericBridgeTarget fixed
        (productLedgerEffect ≤ thresholdHi))) := by
  exact ⟨
    ⟨
      fun hBridge =>
        restricted_typedLowerThresholdConditionedBridge_theorem
          fixed typedLedgerEffect thresholdLo thresholdHi hThreshold hBridge,
      fun hBridge =>
        restricted_typedUpperThresholdConditionedBridge_theorem
          fixed typedLedgerEffect thresholdLo thresholdHi hThreshold hBridge
    ⟩,
    ⟨
      fun hBridge =>
        restricted_productLowerThresholdConditionedBridge_theorem
          fixed productLedgerEffect thresholdLo thresholdHi hThreshold hBridge,
      fun hBridge =>
        restricted_productUpperThresholdConditionedBridge_theorem
          fixed productLedgerEffect thresholdLo thresholdHi hThreshold hBridge
    ⟩
  ⟩

end ProductRestrictedThresholdConditionedBridgeTheorem

end VFH2
