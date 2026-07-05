import VFH2.Product.ProductRestrictedThresholdConditionedBridgeRecovery

namespace VFH2

namespace ProductRestrictedConcreteRecoveryInstantiation

theorem restricted_typedToProductLowerStrongRecovery_from_transport
    (typedFixed productFixed : Prop)
    (typedLedgerEffect productLedgerEffect thresholdHi : Int)
    (hFixed : typedFixed → productFixed)
    (hEffect : typedLedgerEffect = productLedgerEffect) :
    ProductBridgeGeneralization.genericBridgeTarget typedFixed
        (thresholdHi ≤ typedLedgerEffect) →
      ProductBridgeGeneralization.genericBridgeTarget productFixed
        (thresholdHi ≤ productLedgerEffect) := by
  intro hBridge
  exact VFH2.ProductRestrictedThresholdConditionedBridgeTransport.restricted_typedToProductLowerThresholdConditionedBridge_transport
    typedFixed productFixed typedLedgerEffect productLedgerEffect
    thresholdHi thresholdHi hFixed hEffect (Int.le_refl thresholdHi) hBridge

theorem restricted_typedToProductUpperStrongRecovery_from_transport
    (typedFixed productFixed : Prop)
    (typedLedgerEffect productLedgerEffect thresholdLo : Int)
    (hFixed : typedFixed → productFixed)
    (hEffect : typedLedgerEffect = productLedgerEffect) :
    ProductBridgeGeneralization.genericBridgeTarget typedFixed
        (typedLedgerEffect ≤ thresholdLo) →
      ProductBridgeGeneralization.genericBridgeTarget productFixed
        (productLedgerEffect ≤ thresholdLo) := by
  intro hBridge
  exact VFH2.ProductRestrictedThresholdConditionedBridgeTransport.restricted_typedToProductUpperThresholdConditionedBridge_transport
    typedFixed productFixed typedLedgerEffect productLedgerEffect
    thresholdLo thresholdLo hFixed hEffect (Int.le_refl thresholdLo) hBridge

theorem restricted_productToTypedLowerStrongRecovery_from_transport
    (typedFixed productFixed : Prop)
    (typedLedgerEffect productLedgerEffect thresholdHi : Int)
    (hFixed : productFixed → typedFixed)
    (hEffect : typedLedgerEffect = productLedgerEffect) :
    ProductBridgeGeneralization.genericBridgeTarget productFixed
        (thresholdHi ≤ productLedgerEffect) →
      ProductBridgeGeneralization.genericBridgeTarget typedFixed
        (thresholdHi ≤ typedLedgerEffect) := by
  intro hBridge
  exact VFH2.ProductRestrictedThresholdConditionedBridgeTransport.restricted_productToTypedLowerThresholdConditionedBridge_transport
    typedFixed productFixed typedLedgerEffect productLedgerEffect
    thresholdHi thresholdHi hFixed hEffect (Int.le_refl thresholdHi) hBridge

theorem restricted_productToTypedUpperStrongRecovery_from_transport
    (typedFixed productFixed : Prop)
    (typedLedgerEffect productLedgerEffect thresholdLo : Int)
    (hFixed : productFixed → typedFixed)
    (hEffect : typedLedgerEffect = productLedgerEffect) :
    ProductBridgeGeneralization.genericBridgeTarget productFixed
        (productLedgerEffect ≤ thresholdLo) →
      ProductBridgeGeneralization.genericBridgeTarget typedFixed
        (typedLedgerEffect ≤ thresholdLo) := by
  intro hBridge
  exact VFH2.ProductRestrictedThresholdConditionedBridgeTransport.restricted_productToTypedUpperThresholdConditionedBridge_transport
    typedFixed productFixed typedLedgerEffect productLedgerEffect
    thresholdLo thresholdLo hFixed hEffect (Int.le_refl thresholdLo) hBridge

theorem restricted_typedToProductThresholdConditionedBridge_concreteRecovery
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
  exact VFH2.ProductRestrictedThresholdConditionedBridgeRecovery.restricted_typedToProductThresholdConditionedBridge_pair_recovery
    typedFixed productFixed typedLedgerEffect productLedgerEffect
    thresholdLo thresholdHi hThreshold
    (restricted_typedToProductLowerStrongRecovery_from_transport
      typedFixed productFixed typedLedgerEffect productLedgerEffect
      thresholdHi hFixed hEffect)
    (restricted_typedToProductUpperStrongRecovery_from_transport
      typedFixed productFixed typedLedgerEffect productLedgerEffect
      thresholdLo hFixed hEffect)
    hTypedLowerBridgeStrong
    hTypedUpperBridgeStrong

theorem restricted_productToTypedThresholdConditionedBridge_concreteRecovery
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
  exact VFH2.ProductRestrictedThresholdConditionedBridgeRecovery.restricted_productToTypedThresholdConditionedBridge_pair_recovery
    typedFixed productFixed typedLedgerEffect productLedgerEffect
    thresholdLo thresholdHi hThreshold
    (restricted_productToTypedLowerStrongRecovery_from_transport
      typedFixed productFixed typedLedgerEffect productLedgerEffect
      thresholdHi hFixed hEffect)
    (restricted_productToTypedUpperStrongRecovery_from_transport
      typedFixed productFixed typedLedgerEffect productLedgerEffect
      thresholdLo hFixed hEffect)
    hProductLowerBridgeStrong
    hProductUpperBridgeStrong

theorem restricted_thresholdConditionedBridge_bidirectionalConcreteRecovery_theorem
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
    restricted_typedToProductThresholdConditionedBridge_concreteRecovery
      typedFixed productFixed typedLedgerEffect productLedgerEffect
      thresholdLo thresholdHi hFixedTypedToProduct hEffect hThreshold
      hTypedLowerBridgeStrong hTypedUpperBridgeStrong,
    restricted_productToTypedThresholdConditionedBridge_concreteRecovery
      typedFixed productFixed typedLedgerEffect productLedgerEffect
      thresholdLo thresholdHi hFixedProductToTyped hEffect hThreshold
      hProductLowerBridgeStrong hProductUpperBridgeStrong
  ⟩

theorem restricted_thresholdConditionedBridge_concreteRecovery_implication_theorem
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
        VFH2.ProductRestrictedThresholdConditionedBridgeTransport.restricted_typedToProductLowerThresholdConditionedBridge_transport
          typedFixed productFixed typedLedgerEffect productLedgerEffect
          thresholdLo thresholdHi hFixedTypedToProduct hEffect hThreshold hBridge,
      fun hBridge =>
        VFH2.ProductRestrictedThresholdConditionedBridgeTransport.restricted_typedToProductUpperThresholdConditionedBridge_transport
          typedFixed productFixed typedLedgerEffect productLedgerEffect
          thresholdLo thresholdHi hFixedTypedToProduct hEffect hThreshold hBridge
    ⟩,
    ⟨
      fun hBridge =>
        VFH2.ProductRestrictedThresholdConditionedBridgeTransport.restricted_productToTypedLowerThresholdConditionedBridge_transport
          typedFixed productFixed typedLedgerEffect productLedgerEffect
          thresholdLo thresholdHi hFixedProductToTyped hEffect hThreshold hBridge,
      fun hBridge =>
        VFH2.ProductRestrictedThresholdConditionedBridgeTransport.restricted_productToTypedUpperThresholdConditionedBridge_transport
          typedFixed productFixed typedLedgerEffect productLedgerEffect
          thresholdLo thresholdHi hFixedProductToTyped hEffect hThreshold hBridge
    ⟩
  ⟩

end ProductRestrictedConcreteRecoveryInstantiation

end VFH2
