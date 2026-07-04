import VFH2.Product.ProductGeneralizedTransportCertificate

namespace VFH2

namespace ProductConditionBridgeGeneralization

/--
Typed-side fixed component for a generalized active list.

This is the fixed-set proposition used by the generalized condition-aware
bridge theorem.
-/
def generalizedTypedFixedComponent {n d : Nat}
    (active : List (ProductIndex d))
    (x : ProductTypedState n d) : Prop :=
  ∀ w : Typed.WidthIndex d,
    w ∈ List.map ProductIndex.flatten active →
      ((ProductStateTransport.productToTyped x) w).val = n

/--
Product-side fixed component for a generalized active list.
-/
def generalizedProductFixedComponent {n d : Nat}
    (active : List (ProductIndex d))
    (x : ProductTypedState n d) : Prop :=
  ∀ i : ProductIndex d,
    i ∈ active → (x i).val = n

/--
Typed-side condition-aware bridge target for the generalized layer.
-/
def generalizedTypedConditionBridgeTarget {n d : Nat}
    (active : List (ProductIndex d))
    (x : ProductTypedState n d)
    (typedCondition : Prop) : Prop :=
  ProductBridgeGeneralization.genericBridgeTarget
    (generalizedTypedFixedComponent active x)
    typedCondition

/--
Product-side condition-aware bridge target for the generalized layer.
-/
def generalizedProductConditionBridgeTarget {n d : Nat}
    (active : List (ProductIndex d))
    (x : ProductTypedState n d)
    (productCondition : Prop) : Prop :=
  ProductBridgeGeneralization.genericBridgeTarget
    (generalizedProductFixedComponent active x)
    productCondition

/--
The generalized fixed component is transported from Product to Typed.
-/
theorem generalized_fixedComponent_transport
    {n d : Nat}
    (active : List (ProductIndex d))
    (x : ProductTypedState n d) :
    generalizedTypedFixedComponent active x
      ↔
    generalizedProductFixedComponent active x := by
  unfold generalizedTypedFixedComponent generalizedProductFixedComponent
  exact
    ProductFixedSetGeneralization.generalized_fixedSet_transport active x

/--
Main v13.1 theorem: a condition-aware generalized bridge target is transported
whenever the non-fixed condition component is transported.

This theorem assembles the generalized fixed-set transport theorem with the
generic bridge-target transport theorem.
-/
theorem generalized_conditionBridgeTarget_transport
    {n d : Nat}
    (active : List (ProductIndex d))
    (x : ProductTypedState n d)
    {typedCondition productCondition : Prop}
    (hCondition : typedCondition ↔ productCondition) :
    (
      generalizedTypedConditionBridgeTarget active x typedCondition
        ↔
      generalizedProductConditionBridgeTarget active x productCondition
    ) := by
  unfold generalizedTypedConditionBridgeTarget generalizedProductConditionBridgeTarget
  exact
    ProductBridgeGeneralization.genericBridgeTarget_transport
      (generalized_fixedComponent_transport active x)
      hCondition

/--
Product-first orientation of the generalized condition-aware bridge theorem.
-/
theorem generalized_conditionBridgeTarget_transport_product_first
    {n d : Nat}
    (active : List (ProductIndex d))
    (x : ProductTypedState n d)
    {typedCondition productCondition : Prop}
    (hCondition : typedCondition ↔ productCondition) :
    (
      generalizedProductConditionBridgeTarget active x productCondition
        ↔
      generalizedTypedConditionBridgeTarget active x typedCondition
    ) := by
  exact
    (generalized_conditionBridgeTarget_transport
      active x hCondition).symm

/--
Typed-side condition-aware bridge target for the restricted scaffold.
-/
def restrictedTypedConditionBridgeTarget
    (p : ProductRestrictedParams)
    (x : p.State)
    (typedCondition : Prop) : Prop :=
  ProductBridgeGeneralization.genericBridgeTarget
    (Typed.TypedFixedSet
      (ProductParamsTransport.typedParamsOfProduct p)
      (ProductStateTransport.productToTyped x))
    typedCondition

/--
Product-side condition-aware bridge target for the restricted scaffold.
-/
def restrictedProductConditionBridgeTarget
    (p : ProductRestrictedParams)
    (x : p.State)
    (productCondition : Prop) : Prop :=
  ProductBridgeGeneralization.genericBridgeTarget
    (ProductFixedSet p x)
    productCondition

/--
Restricted instance of the condition-aware bridge theorem.
-/
theorem restricted_conditionBridgeTarget_transport
    (p : ProductRestrictedParams)
    (x : p.State)
    {typedCondition productCondition : Prop}
    (hCondition : typedCondition ↔ productCondition) :
    (
      restrictedTypedConditionBridgeTarget p x typedCondition
        ↔
      restrictedProductConditionBridgeTarget p x productCondition
    ) := by
  unfold restrictedTypedConditionBridgeTarget restrictedProductConditionBridgeTarget
  exact
    ProductBridgeGeneralization.genericBridgeTarget_transport
      (ProductFixedSetGeneralization.restricted_fixedSet_transport_from_general p x)
      hCondition

/--
Product-first orientation of the restricted condition-aware bridge theorem.
-/
theorem restricted_conditionBridgeTarget_transport_product_first
    (p : ProductRestrictedParams)
    (x : p.State)
    {typedCondition productCondition : Prop}
    (hCondition : typedCondition ↔ productCondition) :
    (
      restrictedProductConditionBridgeTarget p x productCondition
        ↔
      restrictedTypedConditionBridgeTarget p x typedCondition
    ) := by
  exact
    (restricted_conditionBridgeTarget_transport p x hCondition).symm

end ProductConditionBridgeGeneralization

end VFH2
