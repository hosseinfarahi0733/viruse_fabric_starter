import VFH2.Product.ProductActiveSetGeneralization

namespace VFH2

namespace ProductPointwiseTransportGeneralization

/--
General pointwise predicate transport over the product/typed index bijection.

This theorem is independent of `ProductRestrictedParams`: it states that a
predicate pulled back along `ProductIndex.unflatten` holds for every typed
width index iff it holds for every product index.
-/
theorem forall_width_iff_forall_product
    {d : Nat}
    (P : ProductIndex d → Prop) :
    (∀ w : Typed.WidthIndex d, P (ProductIndex.unflatten w)) ↔
      (∀ i : ProductIndex d, P i) := by
  constructor
  · intro h i
    have hw := h (ProductIndex.flatten i)
    simpa [ProductIndex.unflatten_flatten] using hw
  · intro h w
    exact h (ProductIndex.unflatten w)

/--
Product-first restatement of the general pointwise predicate transport theorem.
-/
theorem forall_product_iff_forall_width
    {d : Nat}
    (P : ProductIndex d → Prop) :
    (∀ i : ProductIndex d, P i) ↔
      (∀ w : Typed.WidthIndex d, P (ProductIndex.unflatten w)) := by
  exact (forall_width_iff_forall_product P).symm

/--
Active-list-restricted pointwise predicate transport.

This theorem combines the generalized active-set membership transport from
v12.1.0 with pointwise predicate transport. It is still independent of the
restricted parameter record and works for any active product-index list.
-/
theorem forall_width_mem_map_iff_forall_product_mem
    {d : Nat}
    (active : List (ProductIndex d))
    (P : ProductIndex d → Prop) :
    (∀ w : Typed.WidthIndex d,
        w ∈ List.map ProductIndex.flatten active →
          P (ProductIndex.unflatten w)) ↔
      (∀ i : ProductIndex d, i ∈ active → P i) := by
  constructor
  · intro h i hi
    have hmem : ProductIndex.flatten i ∈
        List.map ProductIndex.flatten active :=
      List.mem_map.mpr ⟨i, hi, rfl⟩
    have hw := h (ProductIndex.flatten i) hmem
    simpa [ProductIndex.unflatten_flatten] using hw
  · intro h w hw
    have hmem : ProductIndex.unflatten w ∈ active :=
      (ProductActiveSetGeneralization.mem_map_flatten_iff_unflatten_mem
        active w).mp hw
    exact h (ProductIndex.unflatten w) hmem

/--
Product-first restatement of the active-list-restricted pointwise transport.
-/
theorem forall_product_mem_iff_forall_width_mem_map
    {d : Nat}
    (active : List (ProductIndex d))
    (P : ProductIndex d → Prop) :
    (∀ i : ProductIndex d, i ∈ active → P i) ↔
      (∀ w : Typed.WidthIndex d,
        w ∈ List.map ProductIndex.flatten active →
          P (ProductIndex.unflatten w)) := by
  exact (forall_width_mem_map_iff_forall_product_mem active P).symm

/--
Restricted-parameter instance of the generalized active pointwise theorem.

This recovers the active-set pointwise transport needed by restricted
Product/Typed proofs while keeping the generalized list-level theorem as the
primary statement.
-/
theorem restricted_forall_typed_active_iff_forall_product_active
    (p : ProductRestrictedParams)
    (P : ProductIndex p.d → Prop) :
    (∀ w : Typed.WidthIndex p.d,
        w ∈ (ProductParamsTransport.typedParamsOfProduct p).active →
          P (ProductIndex.unflatten w)) ↔
      (∀ i : ProductIndex p.d, i ∈ p.active → P i) := by
  change
    (∀ w : Typed.WidthIndex p.d,
        w ∈ List.map ProductIndex.flatten p.active →
          P (ProductIndex.unflatten w)) ↔
      (∀ i : ProductIndex p.d, i ∈ p.active → P i)
  exact forall_width_mem_map_iff_forall_product_mem p.active P

/--
Product-first restricted-parameter restatement.
-/
theorem restricted_forall_product_active_iff_forall_typed_active
    (p : ProductRestrictedParams)
    (P : ProductIndex p.d → Prop) :
    (∀ i : ProductIndex p.d, i ∈ p.active → P i) ↔
      (∀ w : Typed.WidthIndex p.d,
        w ∈ (ProductParamsTransport.typedParamsOfProduct p).active →
          P (ProductIndex.unflatten w)) := by
  exact (restricted_forall_typed_active_iff_forall_product_active p P).symm

end ProductPointwiseTransportGeneralization

end VFH2
