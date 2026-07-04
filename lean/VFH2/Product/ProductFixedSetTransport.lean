import VFH2.Product.ProductLedgerEffectTransport
import VFH2.Product.ProductUpdateTransport

namespace VFH2

namespace ProductFixedSetTransport

/--
Transport of the fixed-set predicate from the product presentation to the
flattened typed presentation, for the current restricted VF-H2 scaffold.

This is intentionally a transport theorem only: it does not claim the full
unrestricted VF-H2 theory, empirical validation, or biological validation.
-/
theorem typedFixedSet_iff_productFixedSet
    (p : ProductRestrictedParams)
    (x : p.State) :
    Typed.TypedFixedSet
        (ProductParamsTransport.typedParamsOfProduct p)
        (ProductStateTransport.productToTyped x)
      ↔
    ProductFixedSet p x := by
  unfold Typed.TypedFixedSet ProductFixedSet
  constructor
  · intro h i hi
    have hmem :
        ProductIndex.flatten i ∈
          (ProductParamsTransport.typedParamsOfProduct p).active :=
      ProductParamsTransport.flatten_mem_typed_active_of_mem_product_active
        (p := p) (i := i) hi
    have hfixed :=
      h (ProductIndex.flatten i) hmem
    simpa [
      ProductStateTransport.productToTyped,
      ProductIndex.unflatten_flatten,
      ProductParamsTransport.typedParamsOfProduct
    ] using hfixed
  · intro h w hw
    have hmem : ProductIndex.unflatten w ∈ p.active :=
      (ProductUpdateTransport.mem_typed_active_iff_unflatten_mem_product_active
        p w).mp hw
    have hfixed :=
      h (ProductIndex.unflatten w) hmem
    simpa [
      ProductStateTransport.productToTyped,
      ProductParamsTransport.typedParamsOfProduct
    ] using hfixed

/-- Reverse direction, exposed under the product-first reading. -/
theorem productFixedSet_iff_typedFixedSet
    (p : ProductRestrictedParams)
    (x : p.State) :
    ProductFixedSet p x
      ↔
    Typed.TypedFixedSet
        (ProductParamsTransport.typedParamsOfProduct p)
        (ProductStateTransport.productToTyped x) := by
  exact (typedFixedSet_iff_productFixedSet p x).symm

end ProductFixedSetTransport

end VFH2
