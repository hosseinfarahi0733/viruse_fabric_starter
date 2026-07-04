import VFH2.Product.ProductBridgeAssemblyCertificate

namespace VFH2

namespace ProductEffectBoundBridgeSpecialization

/--
Lower-bound predicate for integer effects: the effect is at least the threshold.
-/
def effectLowerBoundPredicate (threshold : Int) : Int → Prop :=
  fun e => threshold ≤ e

/--
Upper-bound predicate for integer effects: the effect is at most the threshold.
-/
def effectUpperBoundPredicate (threshold : Int) : Int → Prop :=
  fun e => e ≤ threshold

/--
Exact-threshold predicate for integer effects.
-/
def effectExactPredicate (threshold : Int) : Int → Prop :=
  fun e => e = threshold

/--
Typed-side lower-bound effect condition for the generalized layer.
-/
def generalizedTypedEffectLowerBoundCondition {n d : Nat}
    (typedUpdate : Typed.TypedState n d → Typed.TypedState n d)
    (typedScore : Typed.TypedState n d → Int)
    (x : ProductTypedState n d)
    (threshold : Int) : Prop :=
  ProductEffectConditionBridgeGeneralization.generalizedTypedEffectCondition
    typedUpdate typedScore x (effectLowerBoundPredicate threshold)

/--
Product-side lower-bound effect condition for the generalized layer.
-/
def generalizedProductEffectLowerBoundCondition {n d : Nat}
    (productUpdate : ProductTypedState n d → ProductTypedState n d)
    (productScore : ProductTypedState n d → Int)
    (x : ProductTypedState n d)
    (threshold : Int) : Prop :=
  ProductEffectConditionBridgeGeneralization.generalizedProductEffectCondition
    productUpdate productScore x (effectLowerBoundPredicate threshold)

/--
Typed-side upper-bound effect condition for the generalized layer.
-/
def generalizedTypedEffectUpperBoundCondition {n d : Nat}
    (typedUpdate : Typed.TypedState n d → Typed.TypedState n d)
    (typedScore : Typed.TypedState n d → Int)
    (x : ProductTypedState n d)
    (threshold : Int) : Prop :=
  ProductEffectConditionBridgeGeneralization.generalizedTypedEffectCondition
    typedUpdate typedScore x (effectUpperBoundPredicate threshold)

/--
Product-side upper-bound effect condition for the generalized layer.
-/
def generalizedProductEffectUpperBoundCondition {n d : Nat}
    (productUpdate : ProductTypedState n d → ProductTypedState n d)
    (productScore : ProductTypedState n d → Int)
    (x : ProductTypedState n d)
    (threshold : Int) : Prop :=
  ProductEffectConditionBridgeGeneralization.generalizedProductEffectCondition
    productUpdate productScore x (effectUpperBoundPredicate threshold)

/--
Typed-side exact-threshold effect condition for the generalized layer.
-/
def generalizedTypedEffectExactCondition {n d : Nat}
    (typedUpdate : Typed.TypedState n d → Typed.TypedState n d)
    (typedScore : Typed.TypedState n d → Int)
    (x : ProductTypedState n d)
    (threshold : Int) : Prop :=
  ProductEffectConditionBridgeGeneralization.generalizedTypedEffectCondition
    typedUpdate typedScore x (effectExactPredicate threshold)

/--
Product-side exact-threshold effect condition for the generalized layer.
-/
def generalizedProductEffectExactCondition {n d : Nat}
    (productUpdate : ProductTypedState n d → ProductTypedState n d)
    (productScore : ProductTypedState n d → Int)
    (x : ProductTypedState n d)
    (threshold : Int) : Prop :=
  ProductEffectConditionBridgeGeneralization.generalizedProductEffectCondition
    productUpdate productScore x (effectExactPredicate threshold)

/--
Generalized lower-bound effect condition transport.
-/
theorem generalized_effectLowerBoundCondition_transport
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
    (
      generalizedTypedEffectLowerBoundCondition
          typedUpdate typedScore x threshold
        ↔
      generalizedProductEffectLowerBoundCondition
          productUpdate productScore x threshold
    ) := by
  unfold generalizedTypedEffectLowerBoundCondition generalizedProductEffectLowerBoundCondition
  exact
    ProductEffectConditionBridgeGeneralization.generalized_effectCondition_transport
      productUpdate typedUpdate productScore typedScore x
      (effectLowerBoundPredicate threshold)
      hUpdate hBase hUpdated

/--
Generalized upper-bound effect condition transport.
-/
theorem generalized_effectUpperBoundCondition_transport
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
    (
      generalizedTypedEffectUpperBoundCondition
          typedUpdate typedScore x threshold
        ↔
      generalizedProductEffectUpperBoundCondition
          productUpdate productScore x threshold
    ) := by
  unfold generalizedTypedEffectUpperBoundCondition generalizedProductEffectUpperBoundCondition
  exact
    ProductEffectConditionBridgeGeneralization.generalized_effectCondition_transport
      productUpdate typedUpdate productScore typedScore x
      (effectUpperBoundPredicate threshold)
      hUpdate hBase hUpdated

/--
Generalized exact-threshold effect condition transport.
-/
theorem generalized_effectExactCondition_transport
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
    (
      generalizedTypedEffectExactCondition
          typedUpdate typedScore x threshold
        ↔
      generalizedProductEffectExactCondition
          productUpdate productScore x threshold
    ) := by
  unfold generalizedTypedEffectExactCondition generalizedProductEffectExactCondition
  exact
    ProductEffectConditionBridgeGeneralization.generalized_effectCondition_transport
      productUpdate typedUpdate productScore typedScore x
      (effectExactPredicate threshold)
      hUpdate hBase hUpdated

/--
Generalized lower-bound effect-conditioned bridge transport.
-/
theorem generalized_effectLowerBoundBridgeTarget_transport
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
        (generalizedTypedEffectLowerBoundCondition
          typedUpdate typedScore x threshold)
        ↔
      ProductConditionBridgeGeneralization.generalizedProductConditionBridgeTarget
        active x
        (generalizedProductEffectLowerBoundCondition
          productUpdate productScore x threshold)
    ) := by
  unfold generalizedTypedEffectLowerBoundCondition generalizedProductEffectLowerBoundCondition
  exact
    ProductEffectConditionBridgeGeneralization.generalized_effectConditionBridgeTarget_transport
      active x productUpdate typedUpdate productScore typedScore
      (effectLowerBoundPredicate threshold)
      hUpdate hBase hUpdated

/--
Generalized upper-bound effect-conditioned bridge transport.
-/
theorem generalized_effectUpperBoundBridgeTarget_transport
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
        (generalizedTypedEffectUpperBoundCondition
          typedUpdate typedScore x threshold)
        ↔
      ProductConditionBridgeGeneralization.generalizedProductConditionBridgeTarget
        active x
        (generalizedProductEffectUpperBoundCondition
          productUpdate productScore x threshold)
    ) := by
  unfold generalizedTypedEffectUpperBoundCondition generalizedProductEffectUpperBoundCondition
  exact
    ProductEffectConditionBridgeGeneralization.generalized_effectConditionBridgeTarget_transport
      active x productUpdate typedUpdate productScore typedScore
      (effectUpperBoundPredicate threshold)
      hUpdate hBase hUpdated

/--
Generalized exact-threshold effect-conditioned bridge transport.
-/
theorem generalized_effectExactBridgeTarget_transport
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
        (generalizedTypedEffectExactCondition
          typedUpdate typedScore x threshold)
        ↔
      ProductConditionBridgeGeneralization.generalizedProductConditionBridgeTarget
        active x
        (generalizedProductEffectExactCondition
          productUpdate productScore x threshold)
    ) := by
  unfold generalizedTypedEffectExactCondition generalizedProductEffectExactCondition
  exact
    ProductEffectConditionBridgeGeneralization.generalized_effectConditionBridgeTarget_transport
      active x productUpdate typedUpdate productScore typedScore
      (effectExactPredicate threshold)
      hUpdate hBase hUpdated

/--
Typed-side lower-bound ledger-effect condition for the restricted layer.
-/
def restrictedTypedLedgerEffectLowerBoundCondition
    (p : ProductRestrictedParams)
    (x : p.State)
    (threshold : Int) : Prop :=
  ProductRestrictedEffectConditionBridgeRecovery.restrictedTypedLedgerEffectCondition
    p x (effectLowerBoundPredicate threshold)

/--
Product-side lower-bound ledger-effect condition for the restricted layer.
-/
def restrictedProductLedgerEffectLowerBoundCondition
    (p : ProductRestrictedParams)
    (x : p.State)
    (threshold : Int) : Prop :=
  ProductRestrictedEffectConditionBridgeRecovery.restrictedProductLedgerEffectCondition
    p x (effectLowerBoundPredicate threshold)

/--
Typed-side upper-bound ledger-effect condition for the restricted layer.
-/
def restrictedTypedLedgerEffectUpperBoundCondition
    (p : ProductRestrictedParams)
    (x : p.State)
    (threshold : Int) : Prop :=
  ProductRestrictedEffectConditionBridgeRecovery.restrictedTypedLedgerEffectCondition
    p x (effectUpperBoundPredicate threshold)

/--
Product-side upper-bound ledger-effect condition for the restricted layer.
-/
def restrictedProductLedgerEffectUpperBoundCondition
    (p : ProductRestrictedParams)
    (x : p.State)
    (threshold : Int) : Prop :=
  ProductRestrictedEffectConditionBridgeRecovery.restrictedProductLedgerEffectCondition
    p x (effectUpperBoundPredicate threshold)

/--
Restricted lower-bound ledger-effect condition transport.
-/
theorem restricted_ledgerEffectLowerBoundCondition_transport
    (p : ProductRestrictedParams)
    (x : p.State)
    (threshold : Int) :
    (
      restrictedTypedLedgerEffectLowerBoundCondition p x threshold
        ↔
      restrictedProductLedgerEffectLowerBoundCondition p x threshold
    ) := by
  unfold restrictedTypedLedgerEffectLowerBoundCondition
    restrictedProductLedgerEffectLowerBoundCondition
  exact
    ProductRestrictedEffectConditionBridgeRecovery.restricted_ledgerEffectCondition_transport
      p x (effectLowerBoundPredicate threshold)

/--
Restricted upper-bound ledger-effect condition transport.
-/
theorem restricted_ledgerEffectUpperBoundCondition_transport
    (p : ProductRestrictedParams)
    (x : p.State)
    (threshold : Int) :
    (
      restrictedTypedLedgerEffectUpperBoundCondition p x threshold
        ↔
      restrictedProductLedgerEffectUpperBoundCondition p x threshold
    ) := by
  unfold restrictedTypedLedgerEffectUpperBoundCondition
    restrictedProductLedgerEffectUpperBoundCondition
  exact
    ProductRestrictedEffectConditionBridgeRecovery.restricted_ledgerEffectCondition_transport
      p x (effectUpperBoundPredicate threshold)

/--
Restricted lower-bound ledger-effect conditioned bridge transport.
-/
theorem restricted_ledgerEffectLowerBoundBridgeTarget_transport
    (p : ProductRestrictedParams)
    (x : p.State)
    (threshold : Int) :
    (
      ProductConditionBridgeGeneralization.restrictedTypedConditionBridgeTarget
        p x
        (restrictedTypedLedgerEffectLowerBoundCondition p x threshold)
        ↔
      ProductConditionBridgeGeneralization.restrictedProductConditionBridgeTarget
        p x
        (restrictedProductLedgerEffectLowerBoundCondition p x threshold)
    ) := by
  unfold restrictedTypedLedgerEffectLowerBoundCondition
    restrictedProductLedgerEffectLowerBoundCondition
  exact
    ProductRestrictedEffectConditionBridgeRecovery.restricted_ledgerEffectConditionBridgeTarget_transport
      p x (effectLowerBoundPredicate threshold)

/--
Restricted upper-bound ledger-effect conditioned bridge transport.
-/
theorem restricted_ledgerEffectUpperBoundBridgeTarget_transport
    (p : ProductRestrictedParams)
    (x : p.State)
    (threshold : Int) :
    (
      ProductConditionBridgeGeneralization.restrictedTypedConditionBridgeTarget
        p x
        (restrictedTypedLedgerEffectUpperBoundCondition p x threshold)
        ↔
      ProductConditionBridgeGeneralization.restrictedProductConditionBridgeTarget
        p x
        (restrictedProductLedgerEffectUpperBoundCondition p x threshold)
    ) := by
  unfold restrictedTypedLedgerEffectUpperBoundCondition
    restrictedProductLedgerEffectUpperBoundCondition
  exact
    ProductRestrictedEffectConditionBridgeRecovery.restricted_ledgerEffectConditionBridgeTarget_transport
      p x (effectUpperBoundPredicate threshold)

end ProductEffectBoundBridgeSpecialization

end VFH2
