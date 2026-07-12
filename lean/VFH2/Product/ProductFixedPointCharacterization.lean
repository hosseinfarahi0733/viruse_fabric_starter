import VFH2.Product.ProductOneStepStabilization

/-!
# VF-H2 Restricted Product Fixed-Point Characterization

This file characterizes fixed points of the current restricted product update
and zero ledger effect.

Boundary:
- The results are only for `ProductRestrictedParams`, `productUpdateState`,
  `productLedgerEffect`, and `ProductFixedSet`.
- They do not prove unrestricted TTP-VF-H2-004 or the full Viruse Fabric theory.
- They do not establish nontrivial multi-step dynamics or empirical validation.
-/

namespace VFH2

/--
A restricted product state is fixed on the active set exactly when the product
update leaves the whole typed state unchanged.
-/
theorem productFixedSet_iff_productUpdateState_eq_self
    (p : ProductRestrictedParams)
    (x : p.State) :
    ProductFixedSet p x ↔ productUpdateState p x = x := by
  constructor
  · intro hfixed
    funext i
    have hval := productUpdateState_val_eq_of_fixed hfixed i
    cases hupdated : productUpdateState p x i with
    | mk updatedVal updatedBound =>
      cases hstate : x i with
      | mk stateVal stateBound =>
        simp only [hupdated, hstate] at hval
        subst stateVal
        rfl
  · intro hupdate
    simpa only [hupdate] using productUpdateState_ProductFixedSet p x

/--
The restricted product ledger effect is zero exactly on the product fixed set.
-/
theorem productLedgerEffect_eq_zero_iff_productFixedSet
    (p : ProductRestrictedParams)
    (x : p.State) :
    productLedgerEffect p x = 0 ↔ ProductFixedSet p x := by
  constructor
  · intro hzero
    apply Classical.byContradiction
    intro hnotfixed
    have hpositive := productLedgerEffect_pos_of_not_fixed hnotfixed
    rw [hzero] at hpositive
    exact (Int.lt_irrefl 0) hpositive
  · intro hfixed
    exact productLedgerEffect_zero_of_fixed hfixed

end VFH2
