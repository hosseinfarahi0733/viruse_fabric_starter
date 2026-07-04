import VFH2.Product.ProductPointwiseTransportGeneralization

namespace VFH2

namespace ProductFixedSetGeneralization

/--
General fixed-set transport over an arbitrary product active list.

This is the v12 generalized form behind the restricted fixed-set theorem:
it is stated for any `active : List (ProductIndex d)` and any product-typed
state, rather than for a `ProductRestrictedParams` record.
-/
theorem generalized_fixedSet_transport
    {n d : Nat}
    (active : List (ProductIndex d))
    (x : ProductTypedState n d) :
    (∀ w : Typed.WidthIndex d,
        w ∈ List.map ProductIndex.flatten active →
          ((ProductStateTransport.productToTyped x) w).val = n) ↔
      (∀ i : ProductIndex d, i ∈ active → (x i).val = n) := by
  simpa [ProductStateTransport.productToTyped] using
    (ProductPointwiseTransportGeneralization.forall_width_mem_map_iff_forall_product_mem
      (active := active)
      (P := fun i : ProductIndex d => (x i).val = n))

/--
Product-first restatement of the generalized fixed-set transport theorem.
-/
theorem generalized_fixedSet_transport_product_first
    {n d : Nat}
    (active : List (ProductIndex d))
    (x : ProductTypedState n d) :
    (∀ i : ProductIndex d, i ∈ active → (x i).val = n) ↔
      (∀ w : Typed.WidthIndex d,
        w ∈ List.map ProductIndex.flatten active →
          ((ProductStateTransport.productToTyped x) w).val = n) := by
  exact (generalized_fixedSet_transport active x).symm

/--
The previous restricted Product/Typed fixed-set transport is recovered as an
instance of the generalized active-list theorem.
-/
theorem restricted_fixedSet_transport_from_general
    (p : ProductRestrictedParams)
    (x : p.State) :
    Typed.TypedFixedSet
        (ProductParamsTransport.typedParamsOfProduct p)
        (ProductStateTransport.productToTyped x)
      ↔
    ProductFixedSet p x := by
  unfold Typed.TypedFixedSet ProductFixedSet
  change
    (∀ w : Typed.WidthIndex p.d,
        w ∈ List.map ProductIndex.flatten p.active →
          ((ProductStateTransport.productToTyped x) w).val = p.n) ↔
      (∀ i : ProductIndex p.d, i ∈ p.active → (x i).val = p.n)
  exact generalized_fixedSet_transport p.active x

/--
Product-first restricted restatement recovered from the generalized theorem.
-/
theorem restricted_fixedSet_transport_from_general_product_first
    (p : ProductRestrictedParams)
    (x : p.State) :
    ProductFixedSet p x
      ↔
    Typed.TypedFixedSet
        (ProductParamsTransport.typedParamsOfProduct p)
        (ProductStateTransport.productToTyped x) := by
  exact (restricted_fixedSet_transport_from_general p x).symm

end ProductFixedSetGeneralization

end VFH2
