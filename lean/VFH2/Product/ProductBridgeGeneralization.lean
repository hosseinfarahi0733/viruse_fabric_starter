import VFH2.Product.ProductEffectTransportGeneralization
import VFH2.Product.ProductBridgeTransport

namespace VFH2

namespace ProductBridgeGeneralization

/--
A representation-agnostic bridge-target pattern.

The intended use is to separate the logical bridge shape from the concrete
VF-H2 restricted bridge definitions. A bridge-like target is modeled as the
conjunction of a fixed/structural component and an effect/condition component.
-/
def genericBridgeTarget
    (fixedComponent : Prop)
    (conditionComponent : Prop) :
    Prop :=
  fixedComponent ∧ conditionComponent

/--
Generic bridge-target transport from componentwise equivalences.

If both bridge components are transported between typed and product
presentations, then the bridge target formed from their conjunction is
transported as well.
-/
theorem genericBridgeTarget_transport
    {typedFixed productFixed typedCondition productCondition : Prop}
    (hFixed : typedFixed ↔ productFixed)
    (hCondition : typedCondition ↔ productCondition) :
    genericBridgeTarget typedFixed typedCondition ↔
      genericBridgeTarget productFixed productCondition := by
  unfold genericBridgeTarget
  constructor
  · intro h
    exact ⟨hFixed.mp h.1, hCondition.mp h.2⟩
  · intro h
    exact ⟨hFixed.mpr h.1, hCondition.mpr h.2⟩

/--
Product-first restatement of generic bridge-target transport.
-/
theorem genericBridgeTarget_transport_product_first
    {typedFixed productFixed typedCondition productCondition : Prop}
    (hFixed : typedFixed ↔ productFixed)
    (hCondition : typedCondition ↔ productCondition) :
    genericBridgeTarget productFixed productCondition ↔
      genericBridgeTarget typedFixed typedCondition := by
  exact (genericBridgeTarget_transport hFixed hCondition).symm

/--
Generic bridge-target transport specialized to product-first component
equivalences.
-/
theorem genericBridgeTarget_transport_of_product_first_components
    {typedFixed productFixed typedCondition productCondition : Prop}
    (hFixed : productFixed ↔ typedFixed)
    (hCondition : productCondition ↔ typedCondition) :
    genericBridgeTarget typedFixed typedCondition ↔
      genericBridgeTarget productFixed productCondition := by
  exact genericBridgeTarget_transport hFixed.symm hCondition.symm

/--
A bridge-target implication transport rule.

This version is useful when a bridge theorem is stated as a one-way
correctness implication rather than as an equivalence.
-/
theorem genericBridgeTarget_imp_transport
    {typedFixed productFixed typedCondition productCondition : Prop}
    (hFixed : typedFixed → productFixed)
    (hCondition : typedCondition → productCondition) :
    genericBridgeTarget typedFixed typedCondition →
      genericBridgeTarget productFixed productCondition := by
  intro h
  exact ⟨hFixed h.1, hCondition h.2⟩

/--
Existing restricted bridge-target transport retained as the VF-H2 restricted
instance associated with the generic bridge-target pattern.

This theorem does not claim an unrestricted VF-H2 bridge theorem. It exposes
the already machine-checked restricted bridge transport at the v12 bridge
abstraction layer.
-/
theorem restricted_bridgeTarget_transport_instance
    (p : ProductRestrictedParams)
    (x : p.State) :
    Typed.typedRestrictedBridgeTarget
        (ProductParamsTransport.typedParamsOfProduct p)
        (ProductStateTransport.productToTyped x)
      ↔
    productRestrictedBridgeTarget p x := by
  exact
    ProductBridgeTransport.typedRestrictedBridgeTarget_iff_productRestrictedBridgeTarget
      p x

/--
Product-first restatement of the restricted bridge-target instance.
-/
theorem restricted_productBridgeTarget_iff_typedBridgeTarget_instance
    (p : ProductRestrictedParams)
    (x : p.State) :
    productRestrictedBridgeTarget p x
      ↔
    Typed.typedRestrictedBridgeTarget
        (ProductParamsTransport.typedParamsOfProduct p)
        (ProductStateTransport.productToTyped x) := by
  exact
    ProductBridgeTransport.productRestrictedBridgeTarget_iff_typedRestrictedBridgeTarget
      p x

end ProductBridgeGeneralization

end VFH2
