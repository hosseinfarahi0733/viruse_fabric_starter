import VFH2.Product.ProductConditionBridgeGeneralization

namespace VFH2

namespace ProductEffectConditionBridgeGeneralization

/--
Typed-side condition induced by a generic update-effect expression.

The condition is parameterized by an arbitrary predicate over integer effects.
This keeps the theorem more general than a threshold-only condition.
-/
def generalizedTypedEffectCondition {n d : Nat}
    (typedUpdate : Typed.TypedState n d → Typed.TypedState n d)
    (typedScore : Typed.TypedState n d → Int)
    (x : ProductTypedState n d)
    (effectPredicate : Int → Prop) : Prop :=
  effectPredicate
    (ProductEffectTransportGeneralization.genericEffect
      typedUpdate typedScore
      (ProductStateTransport.productToTyped x))

/--
Product-side condition induced by a generic update-effect expression.
-/
def generalizedProductEffectCondition {n d : Nat}
    (productUpdate : ProductTypedState n d → ProductTypedState n d)
    (productScore : ProductTypedState n d → Int)
    (x : ProductTypedState n d)
    (effectPredicate : Int → Prop) : Prop :=
  effectPredicate
    (ProductEffectTransportGeneralization.genericEffect
      productUpdate productScore x)

/--
The effect-induced condition is transported whenever the update commutes with
transport and the score is preserved at both the base and updated states.
-/
theorem generalized_effectCondition_transport
    {n d : Nat}
    (productUpdate : ProductTypedState n d → ProductTypedState n d)
    (typedUpdate : Typed.TypedState n d → Typed.TypedState n d)
    (productScore : ProductTypedState n d → Int)
    (typedScore : Typed.TypedState n d → Int)
    (x : ProductTypedState n d)
    (effectPredicate : Int → Prop)
    (hUpdate :
      ProductStateTransport.productToTyped (productUpdate x)
        =
      typedUpdate (ProductStateTransport.productToTyped x))
    (hBase :
      typedScore (ProductStateTransport.productToTyped x)
        =
      productScore x)
    (hUpdated :
      typedScore (ProductStateTransport.productToTyped (productUpdate x))
        =
      productScore (productUpdate x)) :
    generalizedTypedEffectCondition typedUpdate typedScore x effectPredicate
      ↔
    generalizedProductEffectCondition productUpdate productScore x effectPredicate := by
  have hEffect :
      ProductEffectTransportGeneralization.genericEffect
          typedUpdate typedScore
          (ProductStateTransport.productToTyped x)
        =
      ProductEffectTransportGeneralization.genericEffect
          productUpdate productScore x := by
    exact
      ProductEffectTransportGeneralization.genericEffect_transport
        ProductStateTransport.productToTyped
        productUpdate
        typedUpdate
        productScore
        typedScore
        x
        hUpdate
        hBase
        hUpdated
  unfold generalizedTypedEffectCondition generalizedProductEffectCondition
  rw [hEffect]

/--
Main v13.2 theorem: an effect-conditioned bridge target is transported.

This assembles:
1. generic update-effect transport,
2. effect-induced condition transport, and
3. the v13.1 condition-aware bridge theorem.
-/
theorem generalized_effectConditionBridgeTarget_transport
    {n d : Nat}
    (active : List (ProductIndex d))
    (x : ProductTypedState n d)
    (productUpdate : ProductTypedState n d → ProductTypedState n d)
    (typedUpdate : Typed.TypedState n d → Typed.TypedState n d)
    (productScore : ProductTypedState n d → Int)
    (typedScore : Typed.TypedState n d → Int)
    (effectPredicate : Int → Prop)
    (hUpdate :
      ProductStateTransport.productToTyped (productUpdate x)
        =
      typedUpdate (ProductStateTransport.productToTyped x))
    (hBase :
      typedScore (ProductStateTransport.productToTyped x)
        =
      productScore x)
    (hUpdated :
      typedScore (ProductStateTransport.productToTyped (productUpdate x))
        =
      productScore (productUpdate x)) :
    (
      ProductConditionBridgeGeneralization.generalizedTypedConditionBridgeTarget
        active x
        (generalizedTypedEffectCondition
          typedUpdate typedScore x effectPredicate)
        ↔
      ProductConditionBridgeGeneralization.generalizedProductConditionBridgeTarget
        active x
        (generalizedProductEffectCondition
          productUpdate productScore x effectPredicate)
    ) := by
  exact
    ProductConditionBridgeGeneralization.generalized_conditionBridgeTarget_transport
      active
      x
      (generalized_effectCondition_transport
        productUpdate
        typedUpdate
        productScore
        typedScore
        x
        effectPredicate
        hUpdate
        hBase
        hUpdated)

/--
Product-first orientation of the effect-conditioned bridge theorem.
-/
theorem generalized_effectConditionBridgeTarget_transport_product_first
    {n d : Nat}
    (active : List (ProductIndex d))
    (x : ProductTypedState n d)
    (productUpdate : ProductTypedState n d → ProductTypedState n d)
    (typedUpdate : Typed.TypedState n d → Typed.TypedState n d)
    (productScore : ProductTypedState n d → Int)
    (typedScore : Typed.TypedState n d → Int)
    (effectPredicate : Int → Prop)
    (hUpdate :
      ProductStateTransport.productToTyped (productUpdate x)
        =
      typedUpdate (ProductStateTransport.productToTyped x))
    (hBase :
      typedScore (ProductStateTransport.productToTyped x)
        =
      productScore x)
    (hUpdated :
      typedScore (ProductStateTransport.productToTyped (productUpdate x))
        =
      productScore (productUpdate x)) :
    (
      ProductConditionBridgeGeneralization.generalizedProductConditionBridgeTarget
        active x
        (generalizedProductEffectCondition
          productUpdate productScore x effectPredicate)
        ↔
      ProductConditionBridgeGeneralization.generalizedTypedConditionBridgeTarget
        active x
        (generalizedTypedEffectCondition
          typedUpdate typedScore x effectPredicate)
    ) := by
  exact
    (generalized_effectConditionBridgeTarget_transport
      active
      x
      productUpdate
      typedUpdate
      productScore
      typedScore
      effectPredicate
      hUpdate
      hBase
      hUpdated).symm

/--
A threshold-style specialization of the effect-condition theorem.
-/
theorem generalized_effectThresholdCondition_transport
    {n d : Nat}
    (productUpdate : ProductTypedState n d → ProductTypedState n d)
    (typedUpdate : Typed.TypedState n d → Typed.TypedState n d)
    (productScore : ProductTypedState n d → Int)
    (typedScore : Typed.TypedState n d → Int)
    (x : ProductTypedState n d)
    (threshold : Int)
    (hUpdate :
      ProductStateTransport.productToTyped (productUpdate x)
        =
      typedUpdate (ProductStateTransport.productToTyped x))
    (hBase :
      typedScore (ProductStateTransport.productToTyped x)
        =
      productScore x)
    (hUpdated :
      typedScore (ProductStateTransport.productToTyped (productUpdate x))
        =
      productScore (productUpdate x)) :
    generalizedTypedEffectCondition typedUpdate typedScore x
        (fun e => e = threshold)
      ↔
    generalizedProductEffectCondition productUpdate productScore x
        (fun e => e = threshold) := by
  exact
    generalized_effectCondition_transport
      productUpdate
      typedUpdate
      productScore
      typedScore
      x
      (fun e => e = threshold)
      hUpdate
      hBase
      hUpdated

/--
Threshold-style specialization of the effect-conditioned bridge theorem.
-/
theorem generalized_effectThresholdBridgeTarget_transport
    {n d : Nat}
    (active : List (ProductIndex d))
    (x : ProductTypedState n d)
    (productUpdate : ProductTypedState n d → ProductTypedState n d)
    (typedUpdate : Typed.TypedState n d → Typed.TypedState n d)
    (productScore : ProductTypedState n d → Int)
    (typedScore : Typed.TypedState n d → Int)
    (threshold : Int)
    (hUpdate :
      ProductStateTransport.productToTyped (productUpdate x)
        =
      typedUpdate (ProductStateTransport.productToTyped x))
    (hBase :
      typedScore (ProductStateTransport.productToTyped x)
        =
      productScore x)
    (hUpdated :
      typedScore (ProductStateTransport.productToTyped (productUpdate x))
        =
      productScore (productUpdate x)) :
    (
      ProductConditionBridgeGeneralization.generalizedTypedConditionBridgeTarget
        active x
        (generalizedTypedEffectCondition
          typedUpdate typedScore x (fun e => e = threshold))
        ↔
      ProductConditionBridgeGeneralization.generalizedProductConditionBridgeTarget
        active x
        (generalizedProductEffectCondition
          productUpdate productScore x (fun e => e = threshold))
    ) := by
  exact
    generalized_effectConditionBridgeTarget_transport
      active
      x
      productUpdate
      typedUpdate
      productScore
      typedScore
      (fun e => e = threshold)
      hUpdate
      hBase
      hUpdated

end ProductEffectConditionBridgeGeneralization

end VFH2
