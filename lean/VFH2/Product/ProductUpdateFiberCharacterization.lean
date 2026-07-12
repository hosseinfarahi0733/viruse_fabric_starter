import VFH2.Product.ProductCanonicalFixedCompletion

/-!
# VF-H2 Restricted Product Update Fiber Characterization

This file characterizes when two restricted product states have the same
one-step update.

Boundary:
- The result is only for `ProductRestrictedParams` and `productUpdateState`.
- It characterizes fibers of the current restricted product update through
  equality on inactive coordinates.
- It does not prove unrestricted TTP-VF-H2-004 or the full Viruse Fabric theory.
- It does not establish nontrivial multi-step dynamics or empirical validation.
-/

namespace VFH2

/--
Two states have the same restricted product update exactly when they agree on
every inactive coordinate.
-/
theorem productUpdateState_eq_productUpdateState_iff_inactive_eq
    (p : ProductRestrictedParams)
    (x z : p.State) :
    productUpdateState p x = productUpdateState p z ↔
      ∀ i : ProductIndex p.d,
        i ∉ p.active → x i = z i := by
  constructor
  · intro hupdates
    intro i hi
    have hpoint := congrFun hupdates i
    rw [
      productUpdateState_inactive p x hi,
      productUpdateState_inactive p z hi
    ] at hpoint
    exact hpoint
  · intro hinactive
    apply
      (productUpdateState_eq_iff_productFixedSet_and_inactive_eq
        p x (productUpdateState p z)).2
    constructor
    · exact productUpdateState_ProductFixedSet p z
    · intro i hi
      rw [productUpdateState_inactive p z hi]
      exact (hinactive i hi).symm

end VFH2
