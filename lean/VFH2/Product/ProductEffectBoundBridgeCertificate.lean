import VFH2.Product.ProductEffectBoundBridgeSpecialization

namespace VFH2

namespace ProductEffectBoundBridgeCertificate

/--
Certificate collecting the generalized effect-bound bridge specialization layer.

The certificate packages lower-bound, upper-bound, and exact-threshold effect
condition transport together with their corresponding bridge-target transport
theorems.
-/
structure GeneralizedEffectBoundBridgeCertificate
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
      productScore (productUpdate x)) : Prop where
  lowerBoundCondition :
    (
      ProductEffectBoundBridgeSpecialization.generalizedTypedEffectLowerBoundCondition
          typedUpdate typedScore x threshold
        ↔
      ProductEffectBoundBridgeSpecialization.generalizedProductEffectLowerBoundCondition
          productUpdate productScore x threshold
    )
  upperBoundCondition :
    (
      ProductEffectBoundBridgeSpecialization.generalizedTypedEffectUpperBoundCondition
          typedUpdate typedScore x threshold
        ↔
      ProductEffectBoundBridgeSpecialization.generalizedProductEffectUpperBoundCondition
          productUpdate productScore x threshold
    )
  exactCondition :
    (
      ProductEffectBoundBridgeSpecialization.generalizedTypedEffectExactCondition
          typedUpdate typedScore x threshold
        ↔
      ProductEffectBoundBridgeSpecialization.generalizedProductEffectExactCondition
          productUpdate productScore x threshold
    )
  lowerBoundBridge :
    (
      ProductConditionBridgeGeneralization.generalizedTypedConditionBridgeTarget
        active x
        (ProductEffectBoundBridgeSpecialization.generalizedTypedEffectLowerBoundCondition
          typedUpdate typedScore x threshold)
        ↔
      ProductConditionBridgeGeneralization.generalizedProductConditionBridgeTarget
        active x
        (ProductEffectBoundBridgeSpecialization.generalizedProductEffectLowerBoundCondition
          productUpdate productScore x threshold)
    )
  upperBoundBridge :
    (
      ProductConditionBridgeGeneralization.generalizedTypedConditionBridgeTarget
        active x
        (ProductEffectBoundBridgeSpecialization.generalizedTypedEffectUpperBoundCondition
          typedUpdate typedScore x threshold)
        ↔
      ProductConditionBridgeGeneralization.generalizedProductConditionBridgeTarget
        active x
        (ProductEffectBoundBridgeSpecialization.generalizedProductEffectUpperBoundCondition
          productUpdate productScore x threshold)
    )
  exactBridge :
    (
      ProductConditionBridgeGeneralization.generalizedTypedConditionBridgeTarget
        active x
        (ProductEffectBoundBridgeSpecialization.generalizedTypedEffectExactCondition
          typedUpdate typedScore x threshold)
        ↔
      ProductConditionBridgeGeneralization.generalizedProductConditionBridgeTarget
        active x
        (ProductEffectBoundBridgeSpecialization.generalizedProductEffectExactCondition
          productUpdate productScore x threshold)
    )

/--
Generalized effect-bound bridge specialization certificate theorem.
-/
theorem generalizedEffectBoundBridge_certificate
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
    GeneralizedEffectBoundBridgeCertificate
      active x productUpdate typedUpdate productScore typedScore threshold
      hUpdate hBase hUpdated := by
  exact {
    lowerBoundCondition :=
      ProductEffectBoundBridgeSpecialization.generalized_effectLowerBoundCondition_transport
        productUpdate typedUpdate productScore typedScore x threshold
        hUpdate hBase hUpdated,
    upperBoundCondition :=
      ProductEffectBoundBridgeSpecialization.generalized_effectUpperBoundCondition_transport
        productUpdate typedUpdate productScore typedScore x threshold
        hUpdate hBase hUpdated,
    exactCondition :=
      ProductEffectBoundBridgeSpecialization.generalized_effectExactCondition_transport
        productUpdate typedUpdate productScore typedScore x threshold
        hUpdate hBase hUpdated,
    lowerBoundBridge :=
      ProductEffectBoundBridgeSpecialization.generalized_effectLowerBoundBridgeTarget_transport
        active x productUpdate typedUpdate productScore typedScore threshold
        hUpdate hBase hUpdated,
    upperBoundBridge :=
      ProductEffectBoundBridgeSpecialization.generalized_effectUpperBoundBridgeTarget_transport
        active x productUpdate typedUpdate productScore typedScore threshold
        hUpdate hBase hUpdated,
    exactBridge :=
      ProductEffectBoundBridgeSpecialization.generalized_effectExactBridgeTarget_transport
        active x productUpdate typedUpdate productScore typedScore threshold
        hUpdate hBase hUpdated
  }

/--
Certificate collecting the restricted effect-bound bridge specialization layer.

The restricted layer uses ledger-effect transport as its effect source.
-/
structure RestrictedEffectBoundBridgeCertificate
    (p : ProductRestrictedParams)
    (x : p.State)
    (threshold : Int) : Prop where
  lowerBoundCondition :
    (
      ProductEffectBoundBridgeSpecialization.restrictedTypedLedgerEffectLowerBoundCondition
          p x threshold
        ↔
      ProductEffectBoundBridgeSpecialization.restrictedProductLedgerEffectLowerBoundCondition
          p x threshold
    )
  upperBoundCondition :
    (
      ProductEffectBoundBridgeSpecialization.restrictedTypedLedgerEffectUpperBoundCondition
          p x threshold
        ↔
      ProductEffectBoundBridgeSpecialization.restrictedProductLedgerEffectUpperBoundCondition
          p x threshold
    )
  exactCondition :
    (
      ProductRestrictedEffectConditionBridgeRecovery.restrictedTypedLedgerEffectCondition
          p x (ProductEffectBoundBridgeSpecialization.effectExactPredicate threshold)
        ↔
      ProductRestrictedEffectConditionBridgeRecovery.restrictedProductLedgerEffectCondition
          p x (ProductEffectBoundBridgeSpecialization.effectExactPredicate threshold)
    )
  lowerBoundBridge :
    (
      ProductConditionBridgeGeneralization.restrictedTypedConditionBridgeTarget
        p x
        (ProductEffectBoundBridgeSpecialization.restrictedTypedLedgerEffectLowerBoundCondition
          p x threshold)
        ↔
      ProductConditionBridgeGeneralization.restrictedProductConditionBridgeTarget
        p x
        (ProductEffectBoundBridgeSpecialization.restrictedProductLedgerEffectLowerBoundCondition
          p x threshold)
    )
  upperBoundBridge :
    (
      ProductConditionBridgeGeneralization.restrictedTypedConditionBridgeTarget
        p x
        (ProductEffectBoundBridgeSpecialization.restrictedTypedLedgerEffectUpperBoundCondition
          p x threshold)
        ↔
      ProductConditionBridgeGeneralization.restrictedProductConditionBridgeTarget
        p x
        (ProductEffectBoundBridgeSpecialization.restrictedProductLedgerEffectUpperBoundCondition
          p x threshold)
    )
  exactBridge :
    (
      ProductConditionBridgeGeneralization.restrictedTypedConditionBridgeTarget
        p x
        (ProductRestrictedEffectConditionBridgeRecovery.restrictedTypedLedgerEffectCondition
          p x (ProductEffectBoundBridgeSpecialization.effectExactPredicate threshold))
        ↔
      ProductConditionBridgeGeneralization.restrictedProductConditionBridgeTarget
        p x
        (ProductRestrictedEffectConditionBridgeRecovery.restrictedProductLedgerEffectCondition
          p x (ProductEffectBoundBridgeSpecialization.effectExactPredicate threshold))
    )

/--
Restricted effect-bound bridge specialization certificate theorem.
-/
theorem restrictedEffectBoundBridge_certificate
    (p : ProductRestrictedParams)
    (x : p.State)
    (threshold : Int) :
    RestrictedEffectBoundBridgeCertificate p x threshold := by
  exact {
    lowerBoundCondition :=
      ProductEffectBoundBridgeSpecialization.restricted_ledgerEffectLowerBoundCondition_transport
        p x threshold,
    upperBoundCondition :=
      ProductEffectBoundBridgeSpecialization.restricted_ledgerEffectUpperBoundCondition_transport
        p x threshold,
    exactCondition :=
      ProductRestrictedEffectConditionBridgeRecovery.restricted_ledgerEffectCondition_transport
        p x (ProductEffectBoundBridgeSpecialization.effectExactPredicate threshold),
    lowerBoundBridge :=
      ProductEffectBoundBridgeSpecialization.restricted_ledgerEffectLowerBoundBridgeTarget_transport
        p x threshold,
    upperBoundBridge :=
      ProductEffectBoundBridgeSpecialization.restricted_ledgerEffectUpperBoundBridgeTarget_transport
        p x threshold,
    exactBridge :=
      ProductRestrictedEffectConditionBridgeRecovery.restricted_ledgerEffectConditionBridgeTarget_transport
        p x (ProductEffectBoundBridgeSpecialization.effectExactPredicate threshold)
  }

/--
Compact combined certificate collecting both generalized and restricted
effect-bound bridge specialization layers.
-/
structure CombinedEffectBoundBridgeCertificate
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
      productScore (productUpdate x))
    (p : ProductRestrictedParams)
    (rx : p.State) : Prop where
  generalized :
    GeneralizedEffectBoundBridgeCertificate
      active x productUpdate typedUpdate productScore typedScore threshold
      hUpdate hBase hUpdated
  restricted :
    RestrictedEffectBoundBridgeCertificate p rx threshold

/--
Combined effect-bound bridge specialization certificate theorem.
-/
theorem combinedEffectBoundBridge_certificate
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
      productScore (productUpdate x))
    (p : ProductRestrictedParams)
    (rx : p.State) :
    CombinedEffectBoundBridgeCertificate
      active x productUpdate typedUpdate productScore typedScore threshold
      hUpdate hBase hUpdated p rx := by
  exact {
    generalized :=
      generalizedEffectBoundBridge_certificate
        active x productUpdate typedUpdate productScore typedScore threshold
        hUpdate hBase hUpdated,
    restricted :=
      restrictedEffectBoundBridge_certificate p rx threshold
  }

end ProductEffectBoundBridgeCertificate

end VFH2
