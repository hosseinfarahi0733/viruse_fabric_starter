import VFH2.Product.ProductRestrictedConcreteThresholdBridgeAssembly

namespace VFH2

namespace ProductRestrictedConcreteBridgeAssemblySpecialization

def restrictedConcreteSelfBridgeAssemblySource
    (fixed : Prop)
    (effect thresholdLo thresholdHi : Int) : Prop :=
  ProductBridgeGeneralization.genericBridgeTarget fixed
      (thresholdHi ≤ effect) ∧
    ProductBridgeGeneralization.genericBridgeTarget fixed
      (effect ≤ thresholdLo)

def restrictedConcreteSelfBridgeAssemblyTarget
    (fixed : Prop)
    (effect thresholdLo thresholdHi : Int) : Prop :=
  ProductBridgeGeneralization.genericBridgeTarget fixed
      (thresholdLo ≤ effect) ∧
    ProductBridgeGeneralization.genericBridgeTarget fixed
      (effect ≤ thresholdHi)

theorem restricted_selfConcreteThresholdBridgeAssembly_theorem
    (fixed : Prop)
    (effect thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi)
    (hSource :
      restrictedConcreteSelfBridgeAssemblySource
        fixed effect thresholdLo thresholdHi) :
    restrictedConcreteSelfBridgeAssemblyTarget
      fixed effect thresholdLo thresholdHi := by
  unfold restrictedConcreteSelfBridgeAssemblySource at hSource
  unfold restrictedConcreteSelfBridgeAssemblyTarget
  exact VFH2.ProductRestrictedConcreteThresholdBridgeAssembly.restricted_typedToProductConcreteThresholdBridgeAssembly_theorem
    fixed fixed effect effect thresholdLo thresholdHi
    (fun h => h) rfl hThreshold hSource

theorem restricted_selfConcreteThresholdBridgeAssembly_lower_projection
    (fixed : Prop)
    (effect thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi)
    (hSource :
      restrictedConcreteSelfBridgeAssemblySource
        fixed effect thresholdLo thresholdHi) :
    ProductBridgeGeneralization.genericBridgeTarget fixed
      (thresholdLo ≤ effect) := by
  exact (restricted_selfConcreteThresholdBridgeAssembly_theorem
    fixed effect thresholdLo thresholdHi hThreshold hSource).1

theorem restricted_selfConcreteThresholdBridgeAssembly_upper_projection
    (fixed : Prop)
    (effect thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi)
    (hSource :
      restrictedConcreteSelfBridgeAssemblySource
        fixed effect thresholdLo thresholdHi) :
    ProductBridgeGeneralization.genericBridgeTarget fixed
      (effect ≤ thresholdHi) := by
  exact (restricted_selfConcreteThresholdBridgeAssembly_theorem
    fixed effect thresholdLo thresholdHi hThreshold hSource).2

theorem restricted_selfConcreteThresholdBridgeAssembly_direct_theorem
    (fixed : Prop)
    (effect thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi)
    (hLowerBridgeStrong :
      ProductBridgeGeneralization.genericBridgeTarget fixed
        (thresholdHi ≤ effect))
    (hUpperBridgeStrong :
      ProductBridgeGeneralization.genericBridgeTarget fixed
        (effect ≤ thresholdLo)) :
    restrictedConcreteSelfBridgeAssemblyTarget
      fixed effect thresholdLo thresholdHi := by
  exact restricted_selfConcreteThresholdBridgeAssembly_theorem
    fixed effect thresholdLo thresholdHi hThreshold
    ⟨hLowerBridgeStrong, hUpperBridgeStrong⟩

theorem restricted_selfConcreteThresholdBridgeAssembly_implication_theorem
    (fixed : Prop)
    (effect thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi) :
    restrictedConcreteSelfBridgeAssemblySource
        fixed effect thresholdLo thresholdHi →
      restrictedConcreteSelfBridgeAssemblyTarget
        fixed effect thresholdLo thresholdHi := by
  intro hSource
  exact restricted_selfConcreteThresholdBridgeAssembly_theorem
    fixed effect thresholdLo thresholdHi hThreshold hSource

theorem restricted_identityTypedToProductConcreteThresholdBridgeAssembly_theorem
    (fixed : Prop)
    (effect thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi)
    (hSource :
      VFH2.ProductRestrictedConcreteThresholdBridgeAssembly.restrictedConcreteTypedBridgeAssemblySource
        fixed effect thresholdLo thresholdHi) :
    VFH2.ProductRestrictedConcreteThresholdBridgeAssembly.restrictedConcreteTypedToProductBridgeAssemblyTarget
      fixed effect thresholdLo thresholdHi := by
  exact VFH2.ProductRestrictedConcreteThresholdBridgeAssembly.restricted_typedToProductConcreteThresholdBridgeAssembly_theorem
    fixed fixed effect effect thresholdLo thresholdHi
    (fun h => h) rfl hThreshold hSource

theorem restricted_identityProductToTypedConcreteThresholdBridgeAssembly_theorem
    (fixed : Prop)
    (effect thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi)
    (hSource :
      VFH2.ProductRestrictedConcreteThresholdBridgeAssembly.restrictedConcreteProductBridgeAssemblySource
        fixed effect thresholdLo thresholdHi) :
    VFH2.ProductRestrictedConcreteThresholdBridgeAssembly.restrictedConcreteProductToTypedBridgeAssemblyTarget
      fixed effect thresholdLo thresholdHi := by
  exact VFH2.ProductRestrictedConcreteThresholdBridgeAssembly.restricted_productToTypedConcreteThresholdBridgeAssembly_theorem
    fixed fixed effect effect thresholdLo thresholdHi
    (fun h => h) rfl hThreshold hSource

theorem restricted_identityBidirectionalConcreteThresholdBridgeAssembly_theorem
    (fixed : Prop)
    (effect thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi)
    (hSource :
      VFH2.ProductRestrictedConcreteThresholdBridgeAssembly.restrictedConcreteBidirectionalBridgeAssemblySource
        fixed fixed effect effect thresholdLo thresholdHi) :
    VFH2.ProductRestrictedConcreteThresholdBridgeAssembly.restrictedConcreteBidirectionalBridgeAssemblyTarget
      fixed fixed effect effect thresholdLo thresholdHi := by
  exact VFH2.ProductRestrictedConcreteThresholdBridgeAssembly.restricted_bidirectionalConcreteThresholdBridgeAssembly_theorem
    fixed fixed effect effect thresholdLo thresholdHi
    (fun h => h) (fun h => h) rfl hThreshold hSource

theorem restricted_identityBidirectionalConcreteThresholdBridgeAssembly_direct_theorem
    (fixed : Prop)
    (effect thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi)
    (hTypedLowerBridgeStrong :
      ProductBridgeGeneralization.genericBridgeTarget fixed
        (thresholdHi ≤ effect))
    (hTypedUpperBridgeStrong :
      ProductBridgeGeneralization.genericBridgeTarget fixed
        (effect ≤ thresholdLo))
    (hProductLowerBridgeStrong :
      ProductBridgeGeneralization.genericBridgeTarget fixed
        (thresholdHi ≤ effect))
    (hProductUpperBridgeStrong :
      ProductBridgeGeneralization.genericBridgeTarget fixed
        (effect ≤ thresholdLo)) :
    VFH2.ProductRestrictedConcreteThresholdBridgeAssembly.restrictedConcreteBidirectionalBridgeAssemblyTarget
      fixed fixed effect effect thresholdLo thresholdHi := by
  exact VFH2.ProductRestrictedConcreteThresholdBridgeAssembly.restricted_bidirectionalConcreteThresholdBridgeAssembly_direct_theorem
    fixed fixed effect effect thresholdLo thresholdHi
    (fun h => h) (fun h => h) rfl hThreshold
    hTypedLowerBridgeStrong hTypedUpperBridgeStrong
    hProductLowerBridgeStrong hProductUpperBridgeStrong

theorem restricted_identityBidirectionalConcreteThresholdBridgeAssembly_from_selfSource
    (fixed : Prop)
    (effect thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi)
    (hSource :
      restrictedConcreteSelfBridgeAssemblySource
        fixed effect thresholdLo thresholdHi) :
    VFH2.ProductRestrictedConcreteThresholdBridgeAssembly.restrictedConcreteBidirectionalBridgeAssemblyTarget
      fixed fixed effect effect thresholdLo thresholdHi := by
  unfold restrictedConcreteSelfBridgeAssemblySource at hSource
  exact restricted_identityBidirectionalConcreteThresholdBridgeAssembly_direct_theorem
    fixed effect thresholdLo thresholdHi hThreshold
    hSource.1 hSource.2 hSource.1 hSource.2

theorem restricted_selfConcreteThresholdBridgeAssembly_from_identityBidirectional
    (fixed : Prop)
    (effect thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi)
    (hSource :
      restrictedConcreteSelfBridgeAssemblySource
        fixed effect thresholdLo thresholdHi) :
    restrictedConcreteSelfBridgeAssemblyTarget
      fixed effect thresholdLo thresholdHi := by
  exact restricted_selfConcreteThresholdBridgeAssembly_theorem
    fixed effect thresholdLo thresholdHi hThreshold hSource

end ProductRestrictedConcreteBridgeAssemblySpecialization

end VFH2
