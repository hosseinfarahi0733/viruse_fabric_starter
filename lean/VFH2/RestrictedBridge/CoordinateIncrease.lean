import VFH2.RestrictedBridge.BoundBasics

/-!
# VF-H2 Restricted Bridge Coordinate Increase

This file proves that an active below-top witness coordinate strictly
increases under the scaffold update coordinate map.

Boundary:
- This proves coordinate-level increase only.
- This is not yet a proof of positive ledger effect.
- This is not yet the full machine-checked proof of `RBRIDGE-VF-H2-001-R`.
- This is not a proof of the full Viruse Fabric theory.
- This is not a proof of unrestricted `TTP-VF-H2-004`.
- This is not empirical validation.
- This is not biological validation.

Next proof obligation:
lift a witnessed coordinate increase to a positive all-coordinate ledger effect.
-/

namespace VFH2
namespace RestrictedBridge

/-- If an index is in the active list, the Boolean active-index test is true. -/
theorem isActiveIndex_true_of_mem
    (p : RestrictedParams) {i : Nat}
    (hi : i ∈ p.active) :
    isActiveIndex p i = true := by
  simp [isActiveIndex, hi]

/-- Active coordinates update to top under the scaffold update coordinate map. -/
theorem updateCoordinateR_eq_top_of_mem
    (p : RestrictedParams) {i a : Nat}
    (hi : i ∈ p.active) :
    updateCoordinateR p i a = p.n := by
  exact updateCoordinateR_active p i a (isActiveIndex_true_of_mem p hi)

/-- An active coordinate below top strictly increases under the scaffold
coordinate update.
-/
theorem updateCoordinateR_gt_of_mem_below_top
    (p : RestrictedParams) {i a : Nat}
    (hi : i ∈ p.active)
    (hlt : a < p.n) :
    a < updateCoordinateR p i a := by
  rw [updateCoordinateR_eq_top_of_mem p hi]
  exact hlt

/-- A nonfixed restricted state has an active coordinate whose coordinate update
strictly increases that coordinate, assuming active indices are in range.
-/
theorem exists_active_updateCoordinateR_gt_of_not_inFixedSetR
    {p : RestrictedParams} {x : State}
    (hspace : inRestrictedStateSpace p x)
    (hrange : activeIndicesInRange p x)
    (hnotfixed : ¬ inFixedSetR p x) :
    ∃ i : Nat,
      i ∈ p.active ∧
      x.getD i 0 < updateCoordinateR p i (x.getD i 0) := by
  obtain ⟨i, hi, hbelow⟩ :=
    exists_active_below_top_of_not_inFixedSetR hspace hrange hnotfixed
  exact ⟨i, hi, updateCoordinateR_gt_of_mem_below_top p hi hbelow⟩

end RestrictedBridge
end VFH2
