import VFH2.Product.ProductParams

/-!
# VF-H2 v11 Product Fixed-Set Scaffold

This file defines fixed-set semantics for the v11 product-index typed model.

Boundary:
- This is a restricted product-index fixed-set definition.
- It does not define product update semantics.
- It does not define product ledger semantics.
- It does not prove the product restricted bridge theorem.
- It does not prove the full Viruse Fabric theory.
- It does not prove unrestricted TTP-VF-H2-004.
- It is not empirical validation.
- It is not biological validation.
-/

namespace VFH2

/--
A product-index state is fixed on the active set when every active
time×space coordinate already has top value `p.n`.

This is the direct product-index analogue of the v10 typed fixed-set layer,
but over

  ProductIndex d = TimeLayer × SpaceIndex d

rather than the flattened

  WidthIndex d = Fin (3 * d).
-/
def ProductFixedSet
    (p : ProductRestrictedParams)
    (x : p.State) : Prop :=
  ∀ i : ProductIndex p.d,
    i ∈ p.active →
    (x i).val = p.n

namespace ProductFixedSet

/-- Active coordinates of a product fixed state have top value. -/
theorem active_val_eq_top
    {p : ProductRestrictedParams}
    {x : p.State}
    (hfixed : ProductFixedSet p x)
    {i : ProductIndex p.d}
    (hi : i ∈ p.active) :
    (x i).val = p.n := by
  exact hfixed i hi

/--
Equivalent value statement using the parameter object's top coordinate.
This is intentionally value-level only; coordinate equality is not needed here.
-/
theorem active_val_eq_topCoord_val
    {p : ProductRestrictedParams}
    {x : p.State}
    (hfixed : ProductFixedSet p x)
    {i : ProductIndex p.d}
    (hi : i ∈ p.active) :
    (x i).val = (p.topCoord).val := by
  rw [ProductRestrictedParams.topCoord_val]
  exact hfixed i hi

end ProductFixedSet

end VFH2
