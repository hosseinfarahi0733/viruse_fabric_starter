import VFH2.Product.ProductRestrictedThresholdConditionedBridgeTheorem

namespace VFH2

namespace ProductRestrictedThresholdConditionedBridgeTransport

theorem restricted_typedToProductLowerThresholdConditionedBridge_transport
    (typedFixed productFixed : Prop)
    (typedLedgerEffect productLedgerEffect thresholdLo thresholdHi : Int)
    (hFixed : typedFixed → productFixed)
    (hEffect : typedLedgerEffect = productLedgerEffect)
    (hThreshold : thresholdLo ≤ thresholdHi)
    (hTypedBridgeStrong :
      ProductBridgeGeneralization.genericBridgeTarget typedFixed
        (thresholdHi ≤ typedLedgerEffect)) :
    ProductBridgeGeneralization.genericBridgeTarget productFixed
      (thresholdLo ≤ productLedgerEffect) := by
  have hTypedRelaxed :
      ProductBridgeGeneralization.genericBridgeTarget typedFixed
        (thresholdLo ≤ typedLedgerEffect) :=
    VFH2.ProductRestrictedThresholdConditionedBridgeTheorem.restricted_typedLowerThresholdConditionedBridge_theorem
      typedFixed typedLedgerEffect thresholdLo thresholdHi hThreshold hTypedBridgeStrong
  unfold ProductBridgeGeneralization.genericBridgeTarget at hTypedRelaxed ⊢
  exact ⟨hFixed hTypedRelaxed.1, by
    simpa [hEffect] using hTypedRelaxed.2⟩

theorem restricted_typedToProductUpperThresholdConditionedBridge_transport
    (typedFixed productFixed : Prop)
    (typedLedgerEffect productLedgerEffect thresholdLo thresholdHi : Int)
    (hFixed : typedFixed → productFixed)
    (hEffect : typedLedgerEffect = productLedgerEffect)
    (hThreshold : thresholdLo ≤ thresholdHi)
    (hTypedBridgeStrong :
      ProductBridgeGeneralization.genericBridgeTarget typedFixed
        (typedLedgerEffect ≤ thresholdLo)) :
    ProductBridgeGeneralization.genericBridgeTarget productFixed
      (productLedgerEffect ≤ thresholdHi) := by
  have hTypedRelaxed :
      ProductBridgeGeneralization.genericBridgeTarget typedFixed
        (typedLedgerEffect ≤ thresholdHi) :=
    VFH2.ProductRestrictedThresholdConditionedBridgeTheorem.restricted_typedUpperThresholdConditionedBridge_theorem
      typedFixed typedLedgerEffect thresholdLo thresholdHi hThreshold hTypedBridgeStrong
  unfold ProductBridgeGeneralization.genericBridgeTarget at hTypedRelaxed ⊢
  exact ⟨hFixed hTypedRelaxed.1, by
    simpa [hEffect] using hTypedRelaxed.2⟩

theorem restricted_productToTypedLowerThresholdConditionedBridge_transport
    (typedFixed productFixed : Prop)
    (typedLedgerEffect productLedgerEffect thresholdLo thresholdHi : Int)
    (hFixed : productFixed → typedFixed)
    (hEffect : typedLedgerEffect = productLedgerEffect)
    (hThreshold : thresholdLo ≤ thresholdHi)
    (hProductBridgeStrong :
      ProductBridgeGeneralization.genericBridgeTarget productFixed
        (thresholdHi ≤ productLedgerEffect)) :
    ProductBridgeGeneralization.genericBridgeTarget typedFixed
      (thresholdLo ≤ typedLedgerEffect) := by
  have hProductRelaxed :
      ProductBridgeGeneralization.genericBridgeTarget productFixed
        (thresholdLo ≤ productLedgerEffect) :=
    VFH2.ProductRestrictedThresholdConditionedBridgeTheorem.restricted_productLowerThresholdConditionedBridge_theorem
      productFixed productLedgerEffect thresholdLo thresholdHi hThreshold hProductBridgeStrong
  unfold ProductBridgeGeneralization.genericBridgeTarget at hProductRelaxed ⊢
  exact ⟨hFixed hProductRelaxed.1, by
    simpa [hEffect] using hProductRelaxed.2⟩

theorem restricted_productToTypedUpperThresholdConditionedBridge_transport
    (typedFixed productFixed : Prop)
    (typedLedgerEffect productLedgerEffect thresholdLo thresholdHi : Int)
    (hFixed : productFixed → typedFixed)
    (hEffect : typedLedgerEffect = productLedgerEffect)
    (hThreshold : thresholdLo ≤ thresholdHi)
    (hProductBridgeStrong :
      ProductBridgeGeneralization.genericBridgeTarget productFixed
        (productLedgerEffect ≤ thresholdLo)) :
    ProductBridgeGeneralization.genericBridgeTarget typedFixed
      (typedLedgerEffect ≤ thresholdHi) := by
  have hProductRelaxed :
      ProductBridgeGeneralization.genericBridgeTarget productFixed
        (productLedgerEffect ≤ thresholdHi) :=
    VFH2.ProductRestrictedThresholdConditionedBridgeTheorem.restricted_productUpperThresholdConditionedBridge_theorem
      productFixed productLedgerEffect thresholdLo thresholdHi hThreshold hProductBridgeStrong
  unfold ProductBridgeGeneralization.genericBridgeTarget at hProductRelaxed ⊢
  exact ⟨hFixed hProductRelaxed.1, by
    simpa [hEffect] using hProductRelaxed.2⟩

theorem restricted_typedToProductThresholdConditionedBridge_pair_transport
    (typedFixed productFixed : Prop)
    (typedLedgerEffect productLedgerEffect thresholdLo thresholdHi : Int)
    (hFixed : typedFixed → productFixed)
    (hEffect : typedLedgerEffect = productLedgerEffect)
    (hThreshold : thresholdLo ≤ thresholdHi)
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
    restricted_typedToProductLowerThresholdConditionedBridge_transport
      typedFixed productFixed typedLedgerEffect productLedgerEffect
      thresholdLo thresholdHi hFixed hEffect hThreshold hTypedLowerBridgeStrong,
    restricted_typedToProductUpperThresholdConditionedBridge_transport
      typedFixed productFixed typedLedgerEffect productLedgerEffect
      thresholdLo thresholdHi hFixed hEffect hThreshold hTypedUpperBridgeStrong
  ⟩

theorem restricted_productToTypedThresholdConditionedBridge_pair_transport
    (typedFixed productFixed : Prop)
    (typedLedgerEffect productLedgerEffect thresholdLo thresholdHi : Int)
    (hFixed : productFixed → typedFixed)
    (hEffect : typedLedgerEffect = productLedgerEffect)
    (hThreshold : thresholdLo ≤ thresholdHi)
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
    restricted_productToTypedLowerThresholdConditionedBridge_transport
      typedFixed productFixed typedLedgerEffect productLedgerEffect
      thresholdLo thresholdHi hFixed hEffect hThreshold hProductLowerBridgeStrong,
    restricted_productToTypedUpperThresholdConditionedBridge_transport
      typedFixed productFixed typedLedgerEffect productLedgerEffect
      thresholdLo thresholdHi hFixed hEffect hThreshold hProductUpperBridgeStrong
  ⟩

theorem restricted_thresholdConditionedBridge_bidirectionalTransport_theorem
    (typedFixed productFixed : Prop)
    (typedLedgerEffect productLedgerEffect thresholdLo thresholdHi : Int)
    (hFixedTypedToProduct : typedFixed → productFixed)
    (hFixedProductToTyped : productFixed → typedFixed)
    (hEffect : typedLedgerEffect = productLedgerEffect)
    (hThreshold : thresholdLo ≤ thresholdHi)
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
    restricted_typedToProductThresholdConditionedBridge_pair_transport
      typedFixed productFixed typedLedgerEffect productLedgerEffect
      thresholdLo thresholdHi hFixedTypedToProduct hEffect hThreshold
      hTypedLowerBridgeStrong hTypedUpperBridgeStrong,
    restricted_productToTypedThresholdConditionedBridge_pair_transport
      typedFixed productFixed typedLedgerEffect productLedgerEffect
      thresholdLo thresholdHi hFixedProductToTyped hEffect hThreshold
      hProductLowerBridgeStrong hProductUpperBridgeStrong
  ⟩

theorem restricted_thresholdConditionedBridge_transport_implication_theorem
    (typedFixed productFixed : Prop)
    (typedLedgerEffect productLedgerEffect thresholdLo thresholdHi : Int)
    (hFixedTypedToProduct : typedFixed → productFixed)
    (hFixedProductToTyped : productFixed → typedFixed)
    (hEffect : typedLedgerEffect = productLedgerEffect)
    (hThreshold : thresholdLo ≤ thresholdHi) :
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
        restricted_typedToProductLowerThresholdConditionedBridge_transport
          typedFixed productFixed typedLedgerEffect productLedgerEffect
          thresholdLo thresholdHi hFixedTypedToProduct hEffect hThreshold hBridge,
      fun hBridge =>
        restricted_typedToProductUpperThresholdConditionedBridge_transport
          typedFixed productFixed typedLedgerEffect productLedgerEffect
          thresholdLo thresholdHi hFixedTypedToProduct hEffect hThreshold hBridge
    ⟩,
    ⟨
      fun hBridge =>
        restricted_productToTypedLowerThresholdConditionedBridge_transport
          typedFixed productFixed typedLedgerEffect productLedgerEffect
          thresholdLo thresholdHi hFixedProductToTyped hEffect hThreshold hBridge,
      fun hBridge =>
        restricted_productToTypedUpperThresholdConditionedBridge_transport
          typedFixed productFixed typedLedgerEffect productLedgerEffect
          thresholdLo thresholdHi hFixedProductToTyped hEffect hThreshold hBridge
    ⟩
  ⟩

end ProductRestrictedThresholdConditionedBridgeTransport

end VFH2
