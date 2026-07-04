import VFH2.Product.ProductBridgeTransport
import VFH2.Product.ProductLedgerEffectTransport
import VFH2.Product.ProductFixedSetTransport
import VFH2.Product.ProductUpdateTransport

namespace VFH2

namespace ProductTransportLadderCertificate

/--
A compact certificate collecting the main Product ↔ Typed transport results
available up to v11.7.0 for the current restricted VF-H2 scaffold.

This theorem is deliberately a restricted-scaffold transport certificate. It does
not assert the unrestricted VF-H2 theory, empirical validation, biological
validation, or manuscript-level completeness.
-/
theorem transportLadder_certificate
    (p : ProductRestrictedParams)
    (x : p.State) :
    (∀ w : Typed.WidthIndex p.d,
      w ∈ (ProductParamsTransport.typedParamsOfProduct p).active ↔
        ProductIndex.unflatten w ∈ p.active)
    ∧
    ProductStateTransport.productToTyped (productUpdateState p x)
      =
    Typed.typedUpdateState
      (ProductParamsTransport.typedParamsOfProduct p)
      (ProductStateTransport.productToTyped x)
    ∧
    Typed.typedLedger
      (ProductParamsTransport.typedParamsOfProduct p)
      (ProductStateTransport.productToTyped x)
      =
    productLedger p x
    ∧
    Typed.typedLedgerEffect
      (ProductParamsTransport.typedParamsOfProduct p)
      (ProductStateTransport.productToTyped x)
      =
    productLedgerEffect p x
    ∧
    (Typed.TypedFixedSet
      (ProductParamsTransport.typedParamsOfProduct p)
      (ProductStateTransport.productToTyped x)
      ↔
    ProductFixedSet p x)
    ∧
    (Typed.typedRestrictedBridgeTarget
      (ProductParamsTransport.typedParamsOfProduct p)
      (ProductStateTransport.productToTyped x)
      ↔
    productRestrictedBridgeTarget p x) := by
  constructor
  · intro w
    exact ProductUpdateTransport.mem_typed_active_iff_unflatten_mem_product_active p w
  constructor
  · exact ProductUpdateTransport.productToTyped_productUpdateState_eq_typedUpdateState p x
  constructor
  · exact ProductLedgerEffectTransport.typedLedger_eq_transport_of_product p x
  constructor
  · exact ProductLedgerEffectTransport.typedLedgerEffect_eq_productLedgerEffect p x
  constructor
  · exact ProductFixedSetTransport.typedFixedSet_iff_productFixedSet p x
  · exact ProductBridgeTransport.typedRestrictedBridgeTarget_iff_productRestrictedBridgeTarget p x

/-- Product-first spelling of the bridge component of the ladder certificate. -/
theorem productBridge_certificate_component
    (p : ProductRestrictedParams)
    (x : p.State) :
    productRestrictedBridgeTarget p x
      ↔
    Typed.typedRestrictedBridgeTarget
      (ProductParamsTransport.typedParamsOfProduct p)
      (ProductStateTransport.productToTyped x) := by
  exact ProductBridgeTransport.productRestrictedBridgeTarget_iff_typedRestrictedBridgeTarget p x

end ProductTransportLadderCertificate

end VFH2
