import VFH2.Product.ProductFixedSet

/-!
# VF-H2 v11 Product Update Scaffold

This file defines the restricted product-index update operation for the v11
typed model.

Boundary:
- This defines product update semantics for the restricted scaffold.
- It does not define product ledger semantics.
- It does not prove the product restricted bridge theorem.
- It does not prove the full Viruse Fabric theory.
- It does not prove unrestricted TTP-VF-H2-004.
- It is not empirical validation.
- It is not biological validation.
-/

namespace VFH2

/--
Update a product-index typed state by sending every active time×space coordinate
to the parameter object's top coordinate and leaving inactive coordinates
unchanged.
-/
def productUpdateState
    (p : ProductRestrictedParams)
    (x : p.State) :
    p.State :=
  fun i =>
    if i ∈ p.active then
      p.topCoord
    else
      x i

/-- Active product indices are updated to the top coordinate. -/
theorem productUpdateState_active
    (p : ProductRestrictedParams)
    (x : p.State)
    {i : ProductIndex p.d}
    (hi : i ∈ p.active) :
    productUpdateState p x i = p.topCoord := by
  unfold productUpdateState
  simp [hi]

/-- Inactive product indices are preserved by the update. -/
theorem productUpdateState_inactive
    (p : ProductRestrictedParams)
    (x : p.State)
    {i : ProductIndex p.d}
    (hi : i ∉ p.active) :
    productUpdateState p x i = x i := by
  unfold productUpdateState
  simp [hi]

/-- Active product indices have top value after update. -/
theorem productUpdateState_active_val_eq_top
    (p : ProductRestrictedParams)
    (x : p.State)
    {i : ProductIndex p.d}
    (hi : i ∈ p.active) :
    (productUpdateState p x i).val = p.n := by
  rw [productUpdateState_active p x hi]
  exact ProductRestrictedParams.topCoord_val p

/-- Inactive product indices preserve their value after update. -/
theorem productUpdateState_inactive_val_eq
    (p : ProductRestrictedParams)
    (x : p.State)
    {i : ProductIndex p.d}
    (hi : i ∉ p.active) :
    (productUpdateState p x i).val = (x i).val := by
  rw [productUpdateState_inactive p x hi]

/--
The product update is pointwise monotone at the value level.

Active coordinates move to the top value `p.n`; inactive coordinates are
unchanged.
-/
theorem productUpdateState_pointwise_monotone
    (p : ProductRestrictedParams)
    (x : p.State) :
    ∀ i : ProductIndex p.d,
      (x i).val ≤ (productUpdateState p x i).val := by
  intro i
  by_cases hi : i ∈ p.active
  · rw [productUpdateState_active_val_eq_top p x hi]
    exact (x i).bound
  · rw [productUpdateState_inactive_val_eq p x hi]
    exact Nat.le_refl (x i).val

/--
If a state is fixed on active product indices, then update preserves all
coordinate values.

This is value-level preservation, not coordinate-structure equality.
-/
theorem productUpdateState_val_eq_of_fixed
    {p : ProductRestrictedParams}
    {x : p.State}
    (hfixed : ProductFixedSet p x) :
    ∀ i : ProductIndex p.d,
      (productUpdateState p x i).val = (x i).val := by
  intro i
  by_cases hi : i ∈ p.active
  · rw [productUpdateState_active_val_eq_top p x hi]
    exact (hfixed i hi).symm
  · rw [productUpdateState_inactive_val_eq p x hi]

end VFH2
