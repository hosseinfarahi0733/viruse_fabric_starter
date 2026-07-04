import VFH2.Product.ProductRestrictedEffectConditionBridgeRecovery

namespace VFH2

namespace ProductBridgeAssemblyCertificate

/--
Certificate collecting the generalized v13 bridge-assembly layer.

This certificate is theorem-bearing: it packages the condition-aware bridge
transport, effect-condition transport, and effect-conditioned bridge transport
for the generalized scaffold under explicit update/score hypotheses.
-/
structure GeneralizedEffectBridgeAssemblyCertificate
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
      productScore (productUpdate x)) : Prop where
  fixedComponent :
    (
      ProductConditionBridgeGeneralization.generalizedTypedFixedComponent
          active x
        ↔
      ProductConditionBridgeGeneralization.generalizedProductFixedComponent
          active x
    )
  conditionAwareBridge :
    ∀ (typedCondition productCondition : Prop),
      (typedCondition ↔ productCondition) →
      (
        ProductConditionBridgeGeneralization.generalizedTypedConditionBridgeTarget
          active x typedCondition
          ↔
        ProductConditionBridgeGeneralization.generalizedProductConditionBridgeTarget
          active x productCondition
      )
  effectCondition :
    (
      ProductEffectConditionBridgeGeneralization.generalizedTypedEffectCondition
          typedUpdate typedScore x effectPredicate
        ↔
      ProductEffectConditionBridgeGeneralization.generalizedProductEffectCondition
          productUpdate productScore x effectPredicate
    )
  effectConditionBridge :
    (
      ProductConditionBridgeGeneralization.generalizedTypedConditionBridgeTarget
        active x
        (ProductEffectConditionBridgeGeneralization.generalizedTypedEffectCondition
          typedUpdate typedScore x effectPredicate)
        ↔
      ProductConditionBridgeGeneralization.generalizedProductConditionBridgeTarget
        active x
        (ProductEffectConditionBridgeGeneralization.generalizedProductEffectCondition
          productUpdate productScore x effectPredicate)
    )
  effectConditionBridgeProductFirst :
    (
      ProductConditionBridgeGeneralization.generalizedProductConditionBridgeTarget
        active x
        (ProductEffectConditionBridgeGeneralization.generalizedProductEffectCondition
          productUpdate productScore x effectPredicate)
        ↔
      ProductConditionBridgeGeneralization.generalizedTypedConditionBridgeTarget
        active x
        (ProductEffectConditionBridgeGeneralization.generalizedTypedEffectCondition
          typedUpdate typedScore x effectPredicate)
    )
  thresholdCondition :
    ∀ threshold : Int,
      (
        ProductEffectConditionBridgeGeneralization.generalizedTypedEffectCondition
            typedUpdate typedScore x (fun e => e = threshold)
          ↔
        ProductEffectConditionBridgeGeneralization.generalizedProductEffectCondition
            productUpdate productScore x (fun e => e = threshold)
      )
  thresholdBridge :
    ∀ threshold : Int,
      (
        ProductConditionBridgeGeneralization.generalizedTypedConditionBridgeTarget
          active x
          (ProductEffectConditionBridgeGeneralization.generalizedTypedEffectCondition
            typedUpdate typedScore x (fun e => e = threshold))
          ↔
        ProductConditionBridgeGeneralization.generalizedProductConditionBridgeTarget
          active x
          (ProductEffectConditionBridgeGeneralization.generalizedProductEffectCondition
            productUpdate productScore x (fun e => e = threshold))
      )

/--
Generalized v13 bridge-assembly certificate theorem.

This theorem packages the proof surface introduced by v13.1 and v13.2.
-/
theorem generalizedEffectBridgeAssembly_certificate
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
    GeneralizedEffectBridgeAssemblyCertificate
      active x productUpdate typedUpdate productScore typedScore
      effectPredicate hUpdate hBase hUpdated := by
  exact {
    fixedComponent :=
      ProductConditionBridgeGeneralization.generalized_fixedComponent_transport
        active x,
    conditionAwareBridge := by
      intro typedCondition productCondition hCondition
      exact
        ProductConditionBridgeGeneralization.generalized_conditionBridgeTarget_transport
          active x hCondition,
    effectCondition :=
      ProductEffectConditionBridgeGeneralization.generalized_effectCondition_transport
        productUpdate typedUpdate productScore typedScore x effectPredicate
        hUpdate hBase hUpdated,
    effectConditionBridge :=
      ProductEffectConditionBridgeGeneralization.generalized_effectConditionBridgeTarget_transport
        active x productUpdate typedUpdate productScore typedScore effectPredicate
        hUpdate hBase hUpdated,
    effectConditionBridgeProductFirst :=
      ProductEffectConditionBridgeGeneralization.generalized_effectConditionBridgeTarget_transport_product_first
        active x productUpdate typedUpdate productScore typedScore effectPredicate
        hUpdate hBase hUpdated,
    thresholdCondition := by
      intro threshold
      exact
        ProductEffectConditionBridgeGeneralization.generalized_effectThresholdCondition_transport
          productUpdate typedUpdate productScore typedScore x threshold
          hUpdate hBase hUpdated,
    thresholdBridge := by
      intro threshold
      exact
        ProductEffectConditionBridgeGeneralization.generalized_effectThresholdBridgeTarget_transport
          active x productUpdate typedUpdate productScore typedScore threshold
          hUpdate hBase hUpdated
  }

/--
Certificate collecting the restricted v13 bridge-assembly recovery layer.

This certificate packages the restricted ledger-effect condition transport and
the restricted effect-conditioned bridge recovery theorem.
-/
structure RestrictedEffectBridgeAssemblyCertificate
    (p : ProductRestrictedParams)
    (x : p.State)
    (effectPredicate : Int → Prop) : Prop where
  ledgerEffectCondition :
    (
      ProductRestrictedEffectConditionBridgeRecovery.restrictedTypedLedgerEffectCondition
          p x effectPredicate
        ↔
      ProductRestrictedEffectConditionBridgeRecovery.restrictedProductLedgerEffectCondition
          p x effectPredicate
    )
  conditionAwareBridge :
    ∀ (typedCondition productCondition : Prop),
      (typedCondition ↔ productCondition) →
      (
        ProductConditionBridgeGeneralization.restrictedTypedConditionBridgeTarget
          p x typedCondition
          ↔
        ProductConditionBridgeGeneralization.restrictedProductConditionBridgeTarget
          p x productCondition
      )
  ledgerEffectConditionBridge :
    (
      ProductConditionBridgeGeneralization.restrictedTypedConditionBridgeTarget
        p x
        (ProductRestrictedEffectConditionBridgeRecovery.restrictedTypedLedgerEffectCondition
          p x effectPredicate)
        ↔
      ProductConditionBridgeGeneralization.restrictedProductConditionBridgeTarget
        p x
        (ProductRestrictedEffectConditionBridgeRecovery.restrictedProductLedgerEffectCondition
          p x effectPredicate)
    )
  ledgerEffectConditionBridgeProductFirst :
    (
      ProductConditionBridgeGeneralization.restrictedProductConditionBridgeTarget
        p x
        (ProductRestrictedEffectConditionBridgeRecovery.restrictedProductLedgerEffectCondition
          p x effectPredicate)
        ↔
      ProductConditionBridgeGeneralization.restrictedTypedConditionBridgeTarget
        p x
        (ProductRestrictedEffectConditionBridgeRecovery.restrictedTypedLedgerEffectCondition
          p x effectPredicate)
    )
  thresholdCondition :
    ∀ threshold : Int,
      (
        ProductRestrictedEffectConditionBridgeRecovery.restrictedTypedLedgerEffectCondition
            p x (fun e => e = threshold)
          ↔
        ProductRestrictedEffectConditionBridgeRecovery.restrictedProductLedgerEffectCondition
            p x (fun e => e = threshold)
      )
  thresholdBridge :
    ∀ threshold : Int,
      (
        ProductConditionBridgeGeneralization.restrictedTypedConditionBridgeTarget
          p x
          (ProductRestrictedEffectConditionBridgeRecovery.restrictedTypedLedgerEffectCondition
            p x (fun e => e = threshold))
          ↔
        ProductConditionBridgeGeneralization.restrictedProductConditionBridgeTarget
          p x
          (ProductRestrictedEffectConditionBridgeRecovery.restrictedProductLedgerEffectCondition
            p x (fun e => e = threshold))
      )
  thresholdBridgeProductFirst :
    ∀ threshold : Int,
      (
        ProductConditionBridgeGeneralization.restrictedProductConditionBridgeTarget
          p x
          (ProductRestrictedEffectConditionBridgeRecovery.restrictedProductLedgerEffectCondition
            p x (fun e => e = threshold))
          ↔
        ProductConditionBridgeGeneralization.restrictedTypedConditionBridgeTarget
          p x
          (ProductRestrictedEffectConditionBridgeRecovery.restrictedTypedLedgerEffectCondition
            p x (fun e => e = threshold))
      )

/--
Restricted v13 bridge-assembly certificate theorem.

This theorem packages the restricted recovery results introduced by v13.3.
-/
theorem restrictedEffectBridgeAssembly_certificate
    (p : ProductRestrictedParams)
    (x : p.State)
    (effectPredicate : Int → Prop) :
    RestrictedEffectBridgeAssemblyCertificate p x effectPredicate := by
  exact {
    ledgerEffectCondition :=
      ProductRestrictedEffectConditionBridgeRecovery.restricted_ledgerEffectCondition_transport
        p x effectPredicate,
    conditionAwareBridge := by
      intro typedCondition productCondition hCondition
      exact
        ProductConditionBridgeGeneralization.restricted_conditionBridgeTarget_transport
          p x hCondition,
    ledgerEffectConditionBridge :=
      ProductRestrictedEffectConditionBridgeRecovery.restricted_ledgerEffectConditionBridgeTarget_transport
        p x effectPredicate,
    ledgerEffectConditionBridgeProductFirst :=
      ProductRestrictedEffectConditionBridgeRecovery.restricted_ledgerEffectConditionBridgeTarget_transport_product_first
        p x effectPredicate,
    thresholdCondition := by
      intro threshold
      exact
        ProductRestrictedEffectConditionBridgeRecovery.restricted_ledgerEffectThresholdCondition_transport
          p x threshold,
    thresholdBridge := by
      intro threshold
      exact
        ProductRestrictedEffectConditionBridgeRecovery.restricted_ledgerEffectThresholdBridgeTarget_transport
          p x threshold,
    thresholdBridgeProductFirst := by
      intro threshold
      exact
        ProductRestrictedEffectConditionBridgeRecovery.restricted_ledgerEffectThresholdBridgeTarget_transport_product_first
          p x threshold
  }

end ProductBridgeAssemblyCertificate

end VFH2
