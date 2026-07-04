import VFH2.Product.ProductTransportLadderCertificate

namespace VFH2

namespace ProductActiveSetGeneralization

/--
General active-set membership transport for the product/typed index
bijection, independent of `ProductRestrictedParams`.

This theorem is the first controlled v12 generalization step: it factors the
active-set membership argument out of the restricted parameter record and proves
it for any product-index active list.
-/
theorem mem_map_flatten_iff_unflatten_mem
    {d : Nat}
    (active : List (ProductIndex d))
    (w : Typed.WidthIndex d) :
    w ∈ List.map ProductIndex.flatten active ↔
      ProductIndex.unflatten w ∈ active := by
  constructor
  · intro hw
    rcases List.mem_map.mp hw with ⟨i, hi, hflat⟩
    have hunflatten : ProductIndex.unflatten w = i := by
      rw [← hflat]
      exact ProductIndex.unflatten_flatten i
    simpa [hunflatten] using hi
  · intro hw
    exact List.mem_map.mpr
      ⟨ProductIndex.unflatten w, hw, ProductIndex.flatten_unflatten w⟩

/--
The existing restricted active-set transport is recovered as a direct instance
of the generalized list-level theorem.
-/
theorem restricted_mem_typed_active_iff_unflatten_mem
    (p : ProductRestrictedParams)
    (w : Typed.WidthIndex p.d) :
    w ∈ (ProductParamsTransport.typedParamsOfProduct p).active ↔
      ProductIndex.unflatten w ∈ p.active := by
  change
    w ∈ List.map ProductIndex.flatten p.active ↔
      ProductIndex.unflatten w ∈ p.active
  exact mem_map_flatten_iff_unflatten_mem p.active w

/--
Product-first restatement of the generalized theorem.
-/
theorem unflatten_mem_iff_mem_map_flatten
    {d : Nat}
    (active : List (ProductIndex d))
    (w : Typed.WidthIndex d) :
    ProductIndex.unflatten w ∈ active ↔
      w ∈ List.map ProductIndex.flatten active := by
  exact (mem_map_flatten_iff_unflatten_mem active w).symm

end ProductActiveSetGeneralization

end VFH2
