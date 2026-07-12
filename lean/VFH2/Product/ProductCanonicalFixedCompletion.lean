import VFH2.Product.ProductFixedPointCharacterization

/-!
# VF-H2 Canonical Restricted Product Fixed Completion

This file characterizes the output of the current restricted product update as
the fixed completion that preserves all inactive coordinates of the source
state.

Boundary:
- The result is only for `ProductRestrictedParams`, `productUpdateState`, and
  `ProductFixedSet`.
- It does not prove unrestricted TTP-VF-H2-004 or the full Viruse Fabric theory.
- It does not establish global uniqueness of fixed states, nontrivial
  multi-step dynamics, or empirical validation.
-/

namespace VFH2

/--
The restricted product update of `x` is exactly a state `y` when `y` is fixed
on the active set and agrees with `x` on every inactive coordinate.
-/
theorem productUpdateState_eq_iff_productFixedSet_and_inactive_eq
    (p : ProductRestrictedParams)
    (x y : p.State) :
    productUpdateState p x = y ↔
      ProductFixedSet p y ∧
      ∀ i : ProductIndex p.d, i ∉ p.active → y i = x i := by
  constructor
  · intro hxy
    constructor
    · rw [← hxy]
      exact productUpdateState_ProductFixedSet p x
    · intro i hi
      rw [← hxy]
      exact productUpdateState_inactive p x hi
  · rintro ⟨hyfixed, hinactive⟩
    have hyupdate : productUpdateState p y = y :=
      (productFixedSet_iff_productUpdateState_eq_self p y).mp hyfixed
    funext i
    by_cases hi : i ∈ p.active
    · calc
        productUpdateState p x i = p.topCoord :=
          productUpdateState_active p x hi
        _ = productUpdateState p y i :=
          (productUpdateState_active p y hi).symm
        _ = y i := congrFun hyupdate i
    · calc
        productUpdateState p x i = x i :=
          productUpdateState_inactive p x hi
        _ = y i := (hinactive i hi).symm

end VFH2
