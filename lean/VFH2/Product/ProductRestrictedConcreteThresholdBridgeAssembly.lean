import VFH2.Product.ProductRestrictedConcreteRecoveryInstantiation

namespace VFH2

namespace ProductRestrictedConcreteThresholdBridgeAssembly

def restrictedConcreteTypedBridgeAssemblySource
    (typedFixed : Prop)
    (typedLedgerEffect thresholdLo thresholdHi : Int) : Prop :=
  ProductBridgeGeneralization.genericBridgeTarget typedFixed
      (thresholdHi ≤ typedLedgerEffect) ∧
    ProductBridgeGeneralization.genericBridgeTarget typedFixed
      (typedLedgerEffect ≤ thresholdLo)

def restrictedConcreteProductBridgeAssemblySource
    (productFixed : Prop)
    (productLedgerEffect thresholdLo thresholdHi : Int) : Prop :=
  ProductBridgeGeneralization.genericBridgeTarget productFixed
      (thresholdHi ≤ productLedgerEffect) ∧
    ProductBridgeGeneralization.genericBridgeTarget productFixed
      (productLedgerEffect ≤ thresholdLo)

def restrictedConcreteBidirectionalBridgeAssemblySource
    (typedFixed productFixed : Prop)
    (typedLedgerEffect productLedgerEffect thresholdLo thresholdHi : Int) : Prop :=
  restrictedConcreteTypedBridgeAssemblySource
      typedFixed typedLedgerEffect thresholdLo thresholdHi ∧
    restrictedConcreteProductBridgeAssemblySource
      productFixed productLedgerEffect thresholdLo thresholdHi

def restrictedConcreteTypedToProductBridgeAssemblyTarget
    (productFixed : Prop)
    (productLedgerEffect thresholdLo thresholdHi : Int) : Prop :=
  ProductBridgeGeneralization.genericBridgeTarget productFixed
      (thresholdLo ≤ productLedgerEffect) ∧
    ProductBridgeGeneralization.genericBridgeTarget productFixed
      (productLedgerEffect ≤ thresholdHi)

def restrictedConcreteProductToTypedBridgeAssemblyTarget
    (typedFixed : Prop)
    (typedLedgerEffect thresholdLo thresholdHi : Int) : Prop :=
  ProductBridgeGeneralization.genericBridgeTarget typedFixed
      (thresholdLo ≤ typedLedgerEffect) ∧
    ProductBridgeGeneralization.genericBridgeTarget typedFixed
      (typedLedgerEffect ≤ thresholdHi)

def restrictedConcreteBidirectionalBridgeAssemblyTarget
    (typedFixed productFixed : Prop)
    (typedLedgerEffect productLedgerEffect thresholdLo thresholdHi : Int) : Prop :=
  restrictedConcreteTypedToProductBridgeAssemblyTarget
      productFixed productLedgerEffect thresholdLo thresholdHi ∧
    restrictedConcreteProductToTypedBridgeAssemblyTarget
      typedFixed typedLedgerEffect thresholdLo thresholdHi

theorem restricted_typedToProductConcreteThresholdBridgeAssembly_theorem
    (typedFixed productFixed : Prop)
    (typedLedgerEffect productLedgerEffect thresholdLo thresholdHi : Int)
    (hFixed : typedFixed → productFixed)
    (hEffect : typedLedgerEffect = productLedgerEffect)
    (hThreshold : thresholdLo ≤ thresholdHi)
    (hSource :
      restrictedConcreteTypedBridgeAssemblySource
        typedFixed typedLedgerEffect thresholdLo thresholdHi) :
    restrictedConcreteTypedToProductBridgeAssemblyTarget
      productFixed productLedgerEffect thresholdLo thresholdHi := by
  unfold restrictedConcreteTypedBridgeAssemblySource at hSource
  unfold restrictedConcreteTypedToProductBridgeAssemblyTarget
  exact VFH2.ProductRestrictedConcreteRecoveryInstantiation.restricted_typedToProductThresholdConditionedBridge_concreteRecovery
    typedFixed productFixed typedLedgerEffect productLedgerEffect
    thresholdLo thresholdHi hFixed hEffect hThreshold hSource.1 hSource.2

theorem restricted_productToTypedConcreteThresholdBridgeAssembly_theorem
    (typedFixed productFixed : Prop)
    (typedLedgerEffect productLedgerEffect thresholdLo thresholdHi : Int)
    (hFixed : productFixed → typedFixed)
    (hEffect : typedLedgerEffect = productLedgerEffect)
    (hThreshold : thresholdLo ≤ thresholdHi)
    (hSource :
      restrictedConcreteProductBridgeAssemblySource
        productFixed productLedgerEffect thresholdLo thresholdHi) :
    restrictedConcreteProductToTypedBridgeAssemblyTarget
      typedFixed typedLedgerEffect thresholdLo thresholdHi := by
  unfold restrictedConcreteProductBridgeAssemblySource at hSource
  unfold restrictedConcreteProductToTypedBridgeAssemblyTarget
  exact VFH2.ProductRestrictedConcreteRecoveryInstantiation.restricted_productToTypedThresholdConditionedBridge_concreteRecovery
    typedFixed productFixed typedLedgerEffect productLedgerEffect
    thresholdLo thresholdHi hFixed hEffect hThreshold hSource.1 hSource.2

theorem restricted_bidirectionalConcreteThresholdBridgeAssembly_theorem
    (typedFixed productFixed : Prop)
    (typedLedgerEffect productLedgerEffect thresholdLo thresholdHi : Int)
    (hFixedTypedToProduct : typedFixed → productFixed)
    (hFixedProductToTyped : productFixed → typedFixed)
    (hEffect : typedLedgerEffect = productLedgerEffect)
    (hThreshold : thresholdLo ≤ thresholdHi)
    (hSource :
      restrictedConcreteBidirectionalBridgeAssemblySource
        typedFixed productFixed typedLedgerEffect productLedgerEffect
        thresholdLo thresholdHi) :
    restrictedConcreteBidirectionalBridgeAssemblyTarget
      typedFixed productFixed typedLedgerEffect productLedgerEffect
      thresholdLo thresholdHi := by
  unfold restrictedConcreteBidirectionalBridgeAssemblySource at hSource
  unfold restrictedConcreteBidirectionalBridgeAssemblyTarget
  exact ⟨
    restricted_typedToProductConcreteThresholdBridgeAssembly_theorem
      typedFixed productFixed typedLedgerEffect productLedgerEffect
      thresholdLo thresholdHi hFixedTypedToProduct hEffect hThreshold hSource.1,
    restricted_productToTypedConcreteThresholdBridgeAssembly_theorem
      typedFixed productFixed typedLedgerEffect productLedgerEffect
      thresholdLo thresholdHi hFixedProductToTyped hEffect hThreshold hSource.2
  ⟩

theorem restricted_bidirectionalConcreteThresholdBridgeAssembly_direct_theorem
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
    restrictedConcreteBidirectionalBridgeAssemblyTarget
      typedFixed productFixed typedLedgerEffect productLedgerEffect
      thresholdLo thresholdHi := by
  exact restricted_bidirectionalConcreteThresholdBridgeAssembly_theorem
    typedFixed productFixed typedLedgerEffect productLedgerEffect
    thresholdLo thresholdHi hFixedTypedToProduct hFixedProductToTyped
    hEffect hThreshold
    ⟨⟨hTypedLowerBridgeStrong, hTypedUpperBridgeStrong⟩,
      ⟨hProductLowerBridgeStrong, hProductUpperBridgeStrong⟩⟩

theorem restricted_bidirectionalConcreteThresholdBridgeAssembly_implication_theorem
    (typedFixed productFixed : Prop)
    (typedLedgerEffect productLedgerEffect thresholdLo thresholdHi : Int)
    (hFixedTypedToProduct : typedFixed → productFixed)
    (hFixedProductToTyped : productFixed → typedFixed)
    (hEffect : typedLedgerEffect = productLedgerEffect)
    (hThreshold : thresholdLo ≤ thresholdHi) :
    restrictedConcreteBidirectionalBridgeAssemblySource
        typedFixed productFixed typedLedgerEffect productLedgerEffect
        thresholdLo thresholdHi →
      restrictedConcreteBidirectionalBridgeAssemblyTarget
        typedFixed productFixed typedLedgerEffect productLedgerEffect
        thresholdLo thresholdHi := by
  intro hSource
  exact restricted_bidirectionalConcreteThresholdBridgeAssembly_theorem
    typedFixed productFixed typedLedgerEffect productLedgerEffect
    thresholdLo thresholdHi hFixedTypedToProduct hFixedProductToTyped
    hEffect hThreshold hSource

theorem restricted_typedToProductConcreteThresholdBridgeAssembly_lower_projection
    (typedFixed productFixed : Prop)
    (typedLedgerEffect productLedgerEffect thresholdLo thresholdHi : Int)
    (hFixed : typedFixed → productFixed)
    (hEffect : typedLedgerEffect = productLedgerEffect)
    (hThreshold : thresholdLo ≤ thresholdHi)
    (hSource :
      restrictedConcreteTypedBridgeAssemblySource
        typedFixed typedLedgerEffect thresholdLo thresholdHi) :
    ProductBridgeGeneralization.genericBridgeTarget productFixed
      (thresholdLo ≤ productLedgerEffect) := by
  exact (restricted_typedToProductConcreteThresholdBridgeAssembly_theorem
    typedFixed productFixed typedLedgerEffect productLedgerEffect
    thresholdLo thresholdHi hFixed hEffect hThreshold hSource).1

theorem restricted_typedToProductConcreteThresholdBridgeAssembly_upper_projection
    (typedFixed productFixed : Prop)
    (typedLedgerEffect productLedgerEffect thresholdLo thresholdHi : Int)
    (hFixed : typedFixed → productFixed)
    (hEffect : typedLedgerEffect = productLedgerEffect)
    (hThreshold : thresholdLo ≤ thresholdHi)
    (hSource :
      restrictedConcreteTypedBridgeAssemblySource
        typedFixed typedLedgerEffect thresholdLo thresholdHi) :
    ProductBridgeGeneralization.genericBridgeTarget productFixed
      (productLedgerEffect ≤ thresholdHi) := by
  exact (restricted_typedToProductConcreteThresholdBridgeAssembly_theorem
    typedFixed productFixed typedLedgerEffect productLedgerEffect
    thresholdLo thresholdHi hFixed hEffect hThreshold hSource).2

theorem restricted_productToTypedConcreteThresholdBridgeAssembly_lower_projection
    (typedFixed productFixed : Prop)
    (typedLedgerEffect productLedgerEffect thresholdLo thresholdHi : Int)
    (hFixed : productFixed → typedFixed)
    (hEffect : typedLedgerEffect = productLedgerEffect)
    (hThreshold : thresholdLo ≤ thresholdHi)
    (hSource :
      restrictedConcreteProductBridgeAssemblySource
        productFixed productLedgerEffect thresholdLo thresholdHi) :
    ProductBridgeGeneralization.genericBridgeTarget typedFixed
      (thresholdLo ≤ typedLedgerEffect) := by
  exact (restricted_productToTypedConcreteThresholdBridgeAssembly_theorem
    typedFixed productFixed typedLedgerEffect productLedgerEffect
    thresholdLo thresholdHi hFixed hEffect hThreshold hSource).1

theorem restricted_productToTypedConcreteThresholdBridgeAssembly_upper_projection
    (typedFixed productFixed : Prop)
    (typedLedgerEffect productLedgerEffect thresholdLo thresholdHi : Int)
    (hFixed : productFixed → typedFixed)
    (hEffect : typedLedgerEffect = productLedgerEffect)
    (hThreshold : thresholdLo ≤ thresholdHi)
    (hSource :
      restrictedConcreteProductBridgeAssemblySource
        productFixed productLedgerEffect thresholdLo thresholdHi) :
    ProductBridgeGeneralization.genericBridgeTarget typedFixed
      (typedLedgerEffect ≤ thresholdHi) := by
  exact (restricted_productToTypedConcreteThresholdBridgeAssembly_theorem
    typedFixed productFixed typedLedgerEffect productLedgerEffect
    thresholdLo thresholdHi hFixed hEffect hThreshold hSource).2

end ProductRestrictedConcreteThresholdBridgeAssembly

end VFH2
