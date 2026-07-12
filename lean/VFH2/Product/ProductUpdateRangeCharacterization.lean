import VFH2.Product.ProductUpdateFiberCharacterization

/-!
# VF-H2 Restricted Product Update Range Characterization

This file characterizes the range of the current restricted product update.

Boundary:
- The result is only for `ProductRestrictedParams`, `productUpdateState`, and
  `ProductFixedSet`.
- It does not prove unrestricted TTP-VF-H2-004 or the full Viruse Fabric theory.
- It does not establish nontrivial multi-step dynamics, global convergence, or
  empirical validation.
-/

namespace VFH2

/--
A restricted product state lies in the range of `productUpdateState` exactly
when it is fixed on the active set.
-/
theorem productUpdateState_mem_range_iff_productFixedSet
    (p : ProductRestrictedParams)
    (y : p.State) :
    (∃ x : p.State, productUpdateState p x = y) ↔
      ProductFixedSet p y := by
  constructor
  · rintro ⟨x, hxy⟩
    rw [← hxy]
    exact productUpdateState_ProductFixedSet p x
  · intro hyfixed
    refine ⟨y, ?_⟩
    exact
      (productFixedSet_iff_productUpdateState_eq_self p y).mp hyfixed

end VFH2
