import VFH2.Product.ProductRestrictedThresholdConditionedBridgeTransport

namespace VFH2

namespace ProductRestrictedThresholdConditionedBridgeRecovery

theorem restricted_typedToProductLowerThresholdConditionedBridge_recovery
    (typedFixed productFixed : Prop)
    (typedLedgerEffect productLedgerEffect thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi)
    (hRecoverStrong :
      ProductBridgeGeneralization.genericBridgeTarget typedFixed
        (thresholdHi ≤ typedLedgerEffect) →
      ProductBridgeGeneralization.genericBridgeTarget productFixed
        (thresholdHi ≤ productLedgerEffect))
    (hTypedBridgeStrong :
      ProductBridgeGeneralization.genericBridgeTarget typedFixed
        (thresholdHi ≤ typedLedgerEffect)) :
    ProductBridgeGeneralization.genericBridgeTarget productFixed
      (thresholdLo ≤ productLedgerEffect) := by
  have hProductBridgeStrong :
      ProductBridgeGeneralization.genericBridgeTarget productFixed
        (thresholdHi ≤ productLedgerEffect) :=
    hRecoverStrong hTypedBridgeStrong
  exact VFH2.ProductRestrictedThresholdConditionedBridgeTheorem.restricted_productLowerThresholdConditionedBridge_theorem
    productFixed productLedgerEffect thresholdLo thresholdHi hThreshold hProductBridgeStrong

theorem restricted_typedToProductUpperThresholdConditionedBridge_recovery
    (typedFixed productFixed : Prop)
    (typedLedgerEffect productLedgerEffect thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi)
    (hRecoverStrong :
      ProductBridgeGeneralization.genericBridgeTarget typedFixed
        (typedLedgerEffect ≤ thresholdLo) →
      ProductBridgeGeneralization.genericBridgeTarget productFixed
        (productLedgerEffect ≤ thresholdLo))
    (hTypedBridgeStrong :
      ProductBridgeGeneralization.genericBridgeTarget typedFixed
        (typedLedgerEffect ≤ thresholdLo)) :
    ProductBridgeGeneralization.genericBridgeTarget productFixed
      (productLedgerEffect ≤ thresholdHi) := by
  have hProductBridgeStrong :
      ProductBridgeGeneralization.genericBridgeTarget productFixed
        (productLedgerEffect ≤ thresholdLo) :=
    hRecoverStrong hTypedBridgeStrong
  exact VFH2.ProductRestrictedThresholdConditionedBridgeTheorem.restricted_productUpperThresholdConditionedBridge_theorem
    productFixed productLedgerEffect thresholdLo thresholdHi hThreshold hProductBridgeStrong

theorem restricted_productToTypedLowerThresholdConditionedBridge_recovery
    (typedFixed productFixed : Prop)
    (typedLedgerEffect productLedgerEffect thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi)
    (hRecoverStrong :
      ProductBridgeGeneralization.genericBridgeTarget productFixed
        (thresholdHi ≤ productLedgerEffect) →
      ProductBridgeGeneralization.genericBridgeTarget typedFixed
        (thresholdHi ≤ typedLedgerEffect))
    (hProductBridgeStrong :
      ProductBridgeGeneralization.genericBridgeTarget productFixed
        (thresholdHi ≤ productLedgerEffect)) :
    ProductBridgeGeneralization.genericBridgeTarget typedFixed
      (thresholdLo ≤ typedLedgerEffect) := by
  have hTypedBridgeStrong :
      ProductBridgeGeneralization.genericBridgeTarget typedFixed
        (thresholdHi ≤ typedLedgerEffect) :=
    hRecoverStrong hProductBridgeStrong
  exact VFH2.ProductRestrictedThresholdConditionedBridgeTheorem.restricted_typedLowerThresholdConditionedBridge_theorem
    typedFixed typedLedgerEffect thresholdLo thresholdHi hThreshold hTypedBridgeStrong

theorem restricted_productToTypedUpperThresholdConditionedBridge_recovery
    (typedFixed productFixed : Prop)
    (typedLedgerEffect productLedgerEffect thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi)
    (hRecoverStrong :
      ProductBridgeGeneralization.genericBridgeTarget productFixed
        (productLedgerEffect ≤ thresholdLo) →
      ProductBridgeGeneralization.genericBridgeTarget typedFixed
        (typedLedgerEffect ≤ thresholdLo))
    (hProductBridgeStrong :
      ProductBridgeGeneralization.genericBridgeTarget productFixed
        (productLedgerEffect ≤ thresholdLo)) :
    ProductBridgeGeneralization.genericBridgeTarget typedFixed
      (typedLedgerEffect ≤ thresholdHi) := by
  have hTypedBridgeStrong :
      ProductBridgeGeneralization.genericBridgeTarget typedFixed
        (typedLedgerEffect ≤ thresholdLo) :=
    hRecoverStrong hProductBridgeStrong
  exact VFH2.ProductRestrictedThresholdConditionedBridgeTheorem.restricted_typedUpperThresholdConditionedBridge_theorem
    typedFixed typedLedgerEffect thresholdLo thresholdHi hThreshold hTypedBridgeStrong

theorem restricted_typedToProductThresholdConditionedBridge_pair_recovery
    (typedFixed productFixed : Prop)
    (typedLedgerEffect productLedgerEffect thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi)
    (hRecoverLowerStrong :
      ProductBridgeGeneralization.genericBridgeTarget typedFixed
        (thresholdHi ≤ typedLedgerEffect) →
      ProductBridgeGeneralization.genericBridgeTarget productFixed
        (thresholdHi ≤ productLedgerEffect))
    (hRecoverUpperStrong :
      ProductBridgeGeneralization.genericBridgeTarget typedFixed
        (typedLedgerEffect ≤ thresholdLo) →
      ProductBridgeGeneralization.genericBridgeTarget productFixed
        (productLedgerEffect ≤ thresholdLo))
    (hTypedLowerBridgeStrong :
      ProductBridgeGeneralization.genericBridgeTarget typedFixed
        (thresholdHi ≤ typedLedgerEffect))
    (hTypedUpperBridgeStrong :
      ProductBridgeGeneralization.genericBridgeTarget typedFixed
        (typedLedgerEffect ≤ thresholdLo)) :
    ProductBridgeGeneralization.genericBridgeTarget productFixed
        (thresholdLo ≤ productLedgerEffect) ∧
      ProductBridgeGeneralization.genericBridgeTarget productFixed
        (productLedgerEffect ≤ thresholdHi) := by
  exact ⟨
    restricted_typedToProductLowerThresholdConditionedBridge_recovery
      typedFixed productFixed typedLedgerEffect productLedgerEffect
      thresholdLo thresholdHi hThreshold hRecoverLowerStrong
      hTypedLowerBridgeStrong,
    restricted_typedToProductUpperThresholdConditionedBridge_recovery
      typedFixed productFixed typedLedgerEffect productLedgerEffect
      thresholdLo thresholdHi hThreshold hRecoverUpperStrong
      hTypedUpperBridgeStrong
  ⟩

theorem restricted_productToTypedThresholdConditionedBridge_pair_recovery
    (typedFixed productFixed : Prop)
    (typedLedgerEffect productLedgerEffect thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi)
    (hRecoverLowerStrong :
      ProductBridgeGeneralization.genericBridgeTarget productFixed
        (thresholdHi ≤ productLedgerEffect) →
      ProductBridgeGeneralization.genericBridgeTarget typedFixed
        (thresholdHi ≤ typedLedgerEffect))
    (hRecoverUpperStrong :
      ProductBridgeGeneralization.genericBridgeTarget productFixed
        (productLedgerEffect ≤ thresholdLo) →
      ProductBridgeGeneralization.genericBridgeTarget typedFixed
        (typedLedgerEffect ≤ thresholdLo))
    (hProductLowerBridgeStrong :
      ProductBridgeGeneralization.genericBridgeTarget productFixed
        (thresholdHi ≤ productLedgerEffect))
    (hProductUpperBridgeStrong :
      ProductBridgeGeneralization.genericBridgeTarget productFixed
        (productLedgerEffect ≤ thresholdLo)) :
    ProductBridgeGeneralization.genericBridgeTarget typedFixed
        (thresholdLo ≤ typedLedgerEffect) ∧
      ProductBridgeGeneralization.genericBridgeTarget typedFixed
        (typedLedgerEffect ≤ thresholdHi) := by
  exact ⟨
    restricted_productToTypedLowerThresholdConditionedBridge_recovery
      typedFixed productFixed typedLedgerEffect productLedgerEffect
      thresholdLo thresholdHi hThreshold hRecoverLowerStrong
      hProductLowerBridgeStrong,
    restricted_productToTypedUpperThresholdConditionedBridge_recovery
      typedFixed productFixed typedLedgerEffect productLedgerEffect
      thresholdLo thresholdHi hThreshold hRecoverUpperStrong
      hProductUpperBridgeStrong
  ⟩

theorem restricted_thresholdConditionedBridge_bidirectionalRecovery_theorem
    (typedFixed productFixed : Prop)
    (typedLedgerEffect productLedgerEffect thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi)
    (hRecoverTypedToProductLowerStrong :
      ProductBridgeGeneralization.genericBridgeTarget typedFixed
        (thresholdHi ≤ typedLedgerEffect) →
      ProductBridgeGeneralization.genericBridgeTarget productFixed
        (thresholdHi ≤ productLedgerEffect))
    (hRecoverTypedToProductUpperStrong :
      ProductBridgeGeneralization.genericBridgeTarget typedFixed
        (typedLedgerEffect ≤ thresholdLo) →
      ProductBridgeGeneralization.genericBridgeTarget productFixed
        (productLedgerEffect ≤ thresholdLo))
    (hRecoverProductToTypedLowerStrong :
      ProductBridgeGeneralization.genericBridgeTarget productFixed
        (thresholdHi ≤ productLedgerEffect) →
      ProductBridgeGeneralization.genericBridgeTarget typedFixed
        (thresholdHi ≤ typedLedgerEffect))
    (hRecoverProductToTypedUpperStrong :
      ProductBridgeGeneralization.genericBridgeTarget productFixed
        (productLedgerEffect ≤ thresholdLo) →
      ProductBridgeGeneralization.genericBridgeTarget typedFixed
        (typedLedgerEffect ≤ thresholdLo))
    (hTypedLowerBridgeStrong :
      ProductBridgeGeneralization.genericBridgeTarget typedFixed
        (thresholdHi ≤ typedLedgerEffect))
    (hTypedUpperBridgeStrong :
      ProductBridgeGeneralization.genericBridgeTarget typedFixed
        (typedLedgerEffect ≤ thresholdLo))
    (hProductLowerBridgeStrong :
      ProductBridgeGeneralization.genericBridgeTarget productFixed
        (thresholdHi ≤ productLedgerEffect))
    (hProductUpperBridgeStrong :
      ProductBridgeGeneralization.genericBridgeTarget productFixed
        (productLedgerEffect ≤ thresholdLo)) :
    (ProductBridgeGeneralization.genericBridgeTarget productFixed
        (thresholdLo ≤ productLedgerEffect) ∧
      ProductBridgeGeneralization.genericBridgeTarget productFixed
        (productLedgerEffect ≤ thresholdHi)) ∧
    (ProductBridgeGeneralization.genericBridgeTarget typedFixed
        (thresholdLo ≤ typedLedgerEffect) ∧
      ProductBridgeGeneralization.genericBridgeTarget typedFixed
        (typedLedgerEffect ≤ thresholdHi)) := by
  exact ⟨
    restricted_typedToProductThresholdConditionedBridge_pair_recovery
      typedFixed productFixed typedLedgerEffect productLedgerEffect
      thresholdLo thresholdHi hThreshold
      hRecoverTypedToProductLowerStrong
      hRecoverTypedToProductUpperStrong
      hTypedLowerBridgeStrong hTypedUpperBridgeStrong,
    restricted_productToTypedThresholdConditionedBridge_pair_recovery
      typedFixed productFixed typedLedgerEffect productLedgerEffect
      thresholdLo thresholdHi hThreshold
      hRecoverProductToTypedLowerStrong
      hRecoverProductToTypedUpperStrong
      hProductLowerBridgeStrong hProductUpperBridgeStrong
  ⟩

theorem restricted_thresholdConditionedBridge_recovery_implication_theorem
    (typedFixed productFixed : Prop)
    (typedLedgerEffect productLedgerEffect thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi)
    (hRecoverTypedToProductLowerStrong :
      ProductBridgeGeneralization.genericBridgeTarget typedFixed
        (thresholdHi ≤ typedLedgerEffect) →
      ProductBridgeGeneralization.genericBridgeTarget productFixed
        (thresholdHi ≤ productLedgerEffect))
    (hRecoverTypedToProductUpperStrong :
      ProductBridgeGeneralization.genericBridgeTarget typedFixed
        (typedLedgerEffect ≤ thresholdLo) →
      ProductBridgeGeneralization.genericBridgeTarget productFixed
        (productLedgerEffect ≤ thresholdLo))
    (hRecoverProductToTypedLowerStrong :
      ProductBridgeGeneralization.genericBridgeTarget productFixed
        (thresholdHi ≤ productLedgerEffect) →
      ProductBridgeGeneralization.genericBridgeTarget typedFixed
        (thresholdHi ≤ typedLedgerEffect))
    (hRecoverProductToTypedUpperStrong :
      ProductBridgeGeneralization.genericBridgeTarget productFixed
        (productLedgerEffect ≤ thresholdLo) →
      ProductBridgeGeneralization.genericBridgeTarget typedFixed
        (typedLedgerEffect ≤ thresholdLo)) :
    ((ProductBridgeGeneralization.genericBridgeTarget typedFixed
        (thresholdHi ≤ typedLedgerEffect) →
      ProductBridgeGeneralization.genericBridgeTarget productFixed
        (thresholdLo ≤ productLedgerEffect)) ∧
     (ProductBridgeGeneralization.genericBridgeTarget typedFixed
        (typedLedgerEffect ≤ thresholdLo) →
      ProductBridgeGeneralization.genericBridgeTarget productFixed
        (productLedgerEffect ≤ thresholdHi))) ∧
    ((ProductBridgeGeneralization.genericBridgeTarget productFixed
        (thresholdHi ≤ productLedgerEffect) →
      ProductBridgeGeneralization.genericBridgeTarget typedFixed
        (thresholdLo ≤ typedLedgerEffect)) ∧
     (ProductBridgeGeneralization.genericBridgeTarget productFixed
        (productLedgerEffect ≤ thresholdLo) →
      ProductBridgeGeneralization.genericBridgeTarget typedFixed
        (typedLedgerEffect ≤ thresholdHi))) := by
  exact ⟨
    ⟨
      fun hBridge =>
        restricted_typedToProductLowerThresholdConditionedBridge_recovery
          typedFixed productFixed typedLedgerEffect productLedgerEffect
          thresholdLo thresholdHi hThreshold
          hRecoverTypedToProductLowerStrong hBridge,
      fun hBridge =>
        restricted_typedToProductUpperThresholdConditionedBridge_recovery
          typedFixed productFixed typedLedgerEffect productLedgerEffect
          thresholdLo thresholdHi hThreshold
          hRecoverTypedToProductUpperStrong hBridge
    ⟩,
    ⟨
      fun hBridge =>
        restricted_productToTypedLowerThresholdConditionedBridge_recovery
          typedFixed productFixed typedLedgerEffect productLedgerEffect
          thresholdLo thresholdHi hThreshold
          hRecoverProductToTypedLowerStrong hBridge,
      fun hBridge =>
        restricted_productToTypedUpperThresholdConditionedBridge_recovery
          typedFixed productFixed typedLedgerEffect productLedgerEffect
          thresholdLo thresholdHi hThreshold
          hRecoverProductToTypedUpperStrong hBridge
    ⟩
  ⟩

end ProductRestrictedThresholdConditionedBridgeRecovery

end VFH2
