import VFH2.Product.ProductEffectConditionBridgeGeneralization

namespace VFH2

namespace ProductRestrictedEffectConditionBridgeRecovery

/--
Typed-side ledger-effect condition for the restricted scaffold.

The condition is parameterized by an arbitrary predicate over the integer
ledger effect.
-/
def restrictedTypedLedgerEffectCondition
    (p : ProductRestrictedParams)
    (x : p.State)
    (effectPredicate : Int → Prop) : Prop :=
  effectPredicate
    (Typed.typedLedgerEffect
      (ProductParamsTransport.typedParamsOfProduct p)
      (ProductStateTransport.productToTyped x))

/--
Product-side ledger-effect condition for the restricted scaffold.
-/
def restrictedProductLedgerEffectCondition
    (p : ProductRestrictedParams)
    (x : p.State)
    (effectPredicate : Int → Prop) : Prop :=
  effectPredicate (productLedgerEffect p x)

/--
The ledger-effect condition is transported in the restricted scaffold.

This is the restricted recovery of the effect-condition component using the
already-verified restricted ledger-effect transport theorem.
-/
theorem restricted_ledgerEffectCondition_transport
    (p : ProductRestrictedParams)
    (x : p.State)
    (effectPredicate : Int → Prop) :
    (
      restrictedTypedLedgerEffectCondition p x effectPredicate
        ↔
      restrictedProductLedgerEffectCondition p x effectPredicate
    ) := by
  unfold restrictedTypedLedgerEffectCondition restrictedProductLedgerEffectCondition
  constructor
  · intro hTyped
    simpa [ProductEffectTransportGeneralization.restricted_ledgerEffect_transport_instance p x]
      using hTyped
  · intro hProduct
    simpa [ProductEffectTransportGeneralization.restricted_ledgerEffect_transport_instance p x]
      using hProduct

/--
Main v13.3 theorem: restricted recovery of the effect-conditioned bridge
assembly.

It combines:
1. restricted ledger-effect condition transport, and
2. the restricted condition-aware bridge theorem from v13.1.
-/
theorem restricted_ledgerEffectConditionBridgeTarget_transport
    (p : ProductRestrictedParams)
    (x : p.State)
    (effectPredicate : Int → Prop) :
    (
      ProductConditionBridgeGeneralization.restrictedTypedConditionBridgeTarget
        p x
        (restrictedTypedLedgerEffectCondition p x effectPredicate)
        ↔
      ProductConditionBridgeGeneralization.restrictedProductConditionBridgeTarget
        p x
        (restrictedProductLedgerEffectCondition p x effectPredicate)
    ) := by
  exact
    ProductConditionBridgeGeneralization.restricted_conditionBridgeTarget_transport
      p
      x
      (restricted_ledgerEffectCondition_transport p x effectPredicate)

/--
Product-first orientation of the restricted ledger-effect conditioned bridge
recovery theorem.
-/
theorem restricted_ledgerEffectConditionBridgeTarget_transport_product_first
    (p : ProductRestrictedParams)
    (x : p.State)
    (effectPredicate : Int → Prop) :
    (
      ProductConditionBridgeGeneralization.restrictedProductConditionBridgeTarget
        p x
        (restrictedProductLedgerEffectCondition p x effectPredicate)
        ↔
      ProductConditionBridgeGeneralization.restrictedTypedConditionBridgeTarget
        p x
        (restrictedTypedLedgerEffectCondition p x effectPredicate)
    ) := by
  exact
    (restricted_ledgerEffectConditionBridgeTarget_transport
      p x effectPredicate).symm

/--
Threshold-style restricted ledger-effect condition transport.
-/
theorem restricted_ledgerEffectThresholdCondition_transport
    (p : ProductRestrictedParams)
    (x : p.State)
    (threshold : Int) :
    (
      restrictedTypedLedgerEffectCondition p x (fun e => e = threshold)
        ↔
      restrictedProductLedgerEffectCondition p x (fun e => e = threshold)
    ) := by
  exact
    restricted_ledgerEffectCondition_transport
      p x (fun e => e = threshold)

/--
Threshold-style restricted ledger-effect conditioned bridge recovery.
-/
theorem restricted_ledgerEffectThresholdBridgeTarget_transport
    (p : ProductRestrictedParams)
    (x : p.State)
    (threshold : Int) :
    (
      ProductConditionBridgeGeneralization.restrictedTypedConditionBridgeTarget
        p x
        (restrictedTypedLedgerEffectCondition p x (fun e => e = threshold))
        ↔
      ProductConditionBridgeGeneralization.restrictedProductConditionBridgeTarget
        p x
        (restrictedProductLedgerEffectCondition p x (fun e => e = threshold))
    ) := by
  exact
    restricted_ledgerEffectConditionBridgeTarget_transport
      p x (fun e => e = threshold)

/--
Threshold-style restricted ledger-effect conditioned bridge recovery,
product-first orientation.
-/
theorem restricted_ledgerEffectThresholdBridgeTarget_transport_product_first
    (p : ProductRestrictedParams)
    (x : p.State)
    (threshold : Int) :
    (
      ProductConditionBridgeGeneralization.restrictedProductConditionBridgeTarget
        p x
        (restrictedProductLedgerEffectCondition p x (fun e => e = threshold))
        ↔
      ProductConditionBridgeGeneralization.restrictedTypedConditionBridgeTarget
        p x
        (restrictedTypedLedgerEffectCondition p x (fun e => e = threshold))
    ) := by
  exact
    (restricted_ledgerEffectThresholdBridgeTarget_transport p x threshold).symm

end ProductRestrictedEffectConditionBridgeRecovery

end VFH2
