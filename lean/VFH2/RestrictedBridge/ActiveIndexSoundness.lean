import VFH2.RestrictedBridge.FixedSetBridge

/-!
# VF-H2 Restricted Bridge Active Index Soundness

This file removes the explicit `activeIndexSound p` assumption for the
current scaffold path by proving soundness of `isActiveIndex`.

Boundary:
- This proves scaffold-level active-index soundness.
- This proves the fixed-set zero-effect scaffold path without the previous
  explicit `activeIndexSound p` assumption.
- This is not yet the full machine-checked proof of `RBRIDGE-VF-H2-001-R`.
- This is not a proof of the full Viruse Fabric theory.
- This is not a proof of unrestricted `TTP-VF-H2-004`.
- This is not empirical validation.
- This is not biological validation.
-/

namespace VFH2
namespace RestrictedBridge

/-- The Boolean active-index test is sound with respect to list membership. -/
theorem activeIndexSound_of_isActiveIndex (p : RestrictedParams) :
    activeIndexSound p := by
  intro i h
  unfold isActiveIndex at h
  exact of_decide_eq_true h

/-- Fixed-set states have zero scaffold ledger effect without an explicit
active-index soundness assumption.
-/
theorem ledgerEffectR_zero_of_inFixedSetR_no_assumption
    (p : RestrictedParams) (x : State)
    (hfixed : inFixedSetR p x) :
    ledgerEffectR p x = 0 := by
  exact ledgerEffectR_zero_of_inFixedSetR
    p x
    (activeIndexSound_of_isActiveIndex p)
    hfixed

/-- Fixed-set states satisfy the fixed-zero-effect target without an explicit
active-index soundness assumption.
-/
theorem updateFixedZeroEffectTarget_of_inFixedSetR_no_assumption
    (p : RestrictedParams) (x : State) :
    updateFixedZeroEffectTarget p x := by
  intro _hspace hfixed
  exact ledgerEffectR_zero_of_inFixedSetR_no_assumption p x hfixed

end RestrictedBridge
end VFH2
