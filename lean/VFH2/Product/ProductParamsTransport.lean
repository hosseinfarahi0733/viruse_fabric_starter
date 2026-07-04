import VFH2.Product.ProductParams
import VFH2.Product.ProductFlattenFullInjective
import VFH2.Typed.TypedParams

/-!
# VF-H2 v11 Product/Typed Parameter Transport

This file transports v11 product restricted parameters to v10 typed
restricted parameters by flattening active product indices.

Boundary:
- This proves parameter-level transport facts.
- It does not prove ledger equivalence.
- It does not prove update equivalence.
- It does not prove the full VF-H2 theory.
-/

namespace VFH2

namespace ProductParamsTransport

/--
Transport product restricted parameters to typed restricted parameters.

The active product indices are flattened into typed width indices.
-/
def typedParamsOfProduct
    (p : ProductRestrictedParams) :
    Typed.TypedRestrictedParams :=
  { n := p.n
    d := p.d
    active := p.active.map ProductIndex.flatten }

/-- The transported typed parameter has the same coordinate bound. -/
@[simp]
theorem typedParamsOfProduct_n
    (p : ProductRestrictedParams) :
    (typedParamsOfProduct p).n = p.n := by
  rfl

/-- The transported typed parameter has the same spatial width. -/
@[simp]
theorem typedParamsOfProduct_d
    (p : ProductRestrictedParams) :
    (typedParamsOfProduct p).d = p.d := by
  rfl

/-- The transported typed parameter's active set is the flattened active list. -/
@[simp]
theorem typedParamsOfProduct_active
    (p : ProductRestrictedParams) :
    (typedParamsOfProduct p).active = p.active.map ProductIndex.flatten := by
  rfl

/--
Every active product index becomes an active typed width index after
parameter transport.
-/
theorem flatten_mem_typed_active_of_mem_product_active
    {p : ProductRestrictedParams}
    {i : ProductIndex p.d}
    (h : i ∈ p.active) :
    ProductIndex.flatten i ∈ (typedParamsOfProduct p).active := by
  unfold typedParamsOfProduct
  exact (List.mem_map).mpr ⟨i, h, rfl⟩

/--
Membership in the transported active list is exactly membership in the
image of the product active list under `flatten`.
-/
theorem mem_typed_active_iff_exists_product_active
    {p : ProductRestrictedParams}
    {w : Typed.WidthIndex p.d} :
    w ∈ (typedParamsOfProduct p).active ↔
      ∃ i : ProductIndex p.d,
        i ∈ p.active ∧ ProductIndex.flatten i = w := by
  unfold typedParamsOfProduct
  constructor
  · intro h
    rcases (List.mem_map).mp h with ⟨i, hi, hflat⟩
    exact ⟨i, hi, hflat⟩
  · intro h
    rcases h with ⟨i, hi, hflat⟩
    exact (List.mem_map).mpr ⟨i, hi, hflat⟩

/--
For a concrete product index, flattened active membership is equivalent
to product active membership.

This uses the injectivity of `ProductIndex.flatten`.
-/
theorem flatten_mem_typed_active_iff_mem_product_active
    {p : ProductRestrictedParams}
    {i : ProductIndex p.d} :
    ProductIndex.flatten i ∈ (typedParamsOfProduct p).active ↔
      i ∈ p.active := by
  constructor
  · intro h
    rcases (mem_typed_active_iff_exists_product_active).mp h with
      ⟨j, hj, hji⟩
    have hij : j = i := ProductIndex.flatten_injective hji
    cases hij
    exact hj
  · intro h
    exact flatten_mem_typed_active_of_mem_product_active h

end ProductParamsTransport

end VFH2
