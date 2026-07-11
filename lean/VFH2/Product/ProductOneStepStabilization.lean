import VFH2.Product.ProductRestrictedBridge

/-!
# VF-H2 Product One-Step Stabilization

This file proves the one-step stabilization semantics of the current restricted
product update.

Boundary:
- The result is only for `ProductRestrictedParams` and `productUpdateState`.
- It does not prove unrestricted TTP-VF-H2-004 or the full Viruse Fabric theory.
- It does not establish a nontrivial multi-step trajectory or empirical model.
-/

namespace VFH2

/-- Every product state is fixed on the active set after one update. -/
theorem productUpdateState_ProductFixedSet
    (p : ProductRestrictedParams)
    (x : p.State) :
    ProductFixedSet p (productUpdateState p x) := by
  intro i hi
  exact productUpdateState_active_val_eq_top p x hi

/-- The restricted product update is idempotent. -/
theorem productUpdateState_idempotent
    (p : ProductRestrictedParams)
    (x : p.State) :
    productUpdateState p (productUpdateState p x) =
      productUpdateState p x := by
  funext i
  by_cases hi : i ∈ p.active
  · rw [productUpdateState_active p (productUpdateState p x) hi]
    rw [productUpdateState_active p x hi]
  · rw [productUpdateState_inactive p (productUpdateState p x) hi]

/-- The ledger effect of the state produced by one update is zero. -/
theorem productLedgerEffect_after_update_zero
    (p : ProductRestrictedParams)
    (x : p.State) :
    productLedgerEffect p (productUpdateState p x) = 0 := by
  exact productLedgerEffect_zero_of_fixed
    (productUpdateState_ProductFixedSet p x)

/--
Two-phase semantics for a nonfixed initial state: the first ledger effect is
positive, while one update reaches a fixed point whose next ledger effect is
zero.
-/
theorem productOneStepStabilization_of_not_fixed
    {p : ProductRestrictedParams}
    {x : p.State}
    (hnotfixed : ¬ ProductFixedSet p x) :
    0 < productLedgerEffect p x ∧
      ProductFixedSet p (productUpdateState p x) ∧
      productUpdateState p (productUpdateState p x) =
        productUpdateState p x ∧
      productLedgerEffect p (productUpdateState p x) = 0 := by
  constructor
  · exact productLedgerEffect_pos_of_not_fixed hnotfixed
  · constructor
    · exact productUpdateState_ProductFixedSet p x
    · constructor
      · exact productUpdateState_idempotent p x
      · exact productLedgerEffect_after_update_zero p x

end VFH2
