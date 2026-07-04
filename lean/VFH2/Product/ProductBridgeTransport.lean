import VFH2.Product.ProductFixedSetTransport
import VFH2.Product.ProductRestrictedBridge
import VFH2.Typed.TypedRestrictedBridge


namespace VFH2

namespace ProductBridgeTransport

/--
Transport of the restricted bridge target from the product presentation to the
flattened typed presentation, for the current restricted VF-H2 scaffold.

This is intentionally a transport theorem only: it does not claim the full
unrestricted VF-H2 theory, empirical validation, or biological validation.
-/
theorem typedRestrictedBridgeTarget_iff_productRestrictedBridgeTarget
    (p : ProductRestrictedParams)
    (x : p.State) :
    Typed.typedRestrictedBridgeTarget
        (ProductParamsTransport.typedParamsOfProduct p)
        (ProductStateTransport.productToTyped x)
      ↔
    productRestrictedBridgeTarget p x := by
  simp [Typed.typedRestrictedBridgeTarget, productRestrictedBridgeTarget,
    ProductFixedSetTransport.typedFixedSet_iff_productFixedSet,
    ProductLedgerEffectTransport.typedLedgerEffect_eq_productLedgerEffect]

/-- Reverse direction, exposed under the product-first reading. -/
theorem productRestrictedBridgeTarget_iff_typedRestrictedBridgeTarget
    (p : ProductRestrictedParams)
    (x : p.State) :
    productRestrictedBridgeTarget p x
      ↔
    Typed.typedRestrictedBridgeTarget
        (ProductParamsTransport.typedParamsOfProduct p)
        (ProductStateTransport.productToTyped x) := by
  exact (typedRestrictedBridgeTarget_iff_productRestrictedBridgeTarget p x).symm

end ProductBridgeTransport

end VFH2
