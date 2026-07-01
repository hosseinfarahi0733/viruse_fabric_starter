import VFH2.RestrictedBridge.UpdateMap

/-!
# VF-H2 Restricted Bridge Update Map Basics

This file adds small machine-checked Lean lemmas about the scaffold-level
restricted update map.

Boundary:
- These are update-map basics only.
- This is not yet a machine-checked proof of `RBRIDGE-VF-H2-001-R`.
- This is not a proof of the full Viruse Fabric theory.
- This is not a proof of unrestricted `TTP-VF-H2-004`.
- This is not empirical validation.
- This is not biological validation.

The nonempty-active restricted theorem remains future work.
-/

namespace VFH2
namespace RestrictedBridge

theorem updateStateAuxR_nil (p : RestrictedParams) (i : Nat) :
    updateStateAuxR p i ([] : State) = [] := by
  rfl

theorem updateStateAuxR_cons
    (p : RestrictedParams) (i a : Nat) (xs : State) :
    updateStateAuxR p i (a :: xs) =
      updateCoordinateR p i a :: updateStateAuxR p (i + 1) xs := by
  rfl

theorem updateStateR_nil (p : RestrictedParams) :
    updateStateR p ([] : State) = [] := by
  rfl

theorem ledgerEffectR_nil (p : RestrictedParams) :
    ledgerEffectR p ([] : State) = 0 := by
  simp [ledgerEffectR, updateStateR, updateStateAuxR, ledgerVR]

theorem updateCoordinateR_active_top
    (p : RestrictedParams) (i : Nat)
    (h : isActiveIndex p i = true) :
    updateCoordinateR p i p.n = p.n := by
  simp [updateCoordinateR, h]

theorem updateCoordinateR_inactive_top
    (p : RestrictedParams) (i : Nat)
    (h : isActiveIndex p i = false) :
    updateCoordinateR p i p.n = p.n := by
  simp [updateCoordinateR, h]

/-- If there are no active coordinates, the scaffold update is identity. -/
theorem updateStateAuxR_no_active
    (p : RestrictedParams)
    (hactive : p.active = [])
    (x : State)
    (i : Nat) :
    updateStateAuxR p i x = x := by
  induction x generalizing i with
  | nil =>
      simp [updateStateAuxR]
  | cons a xs ih =>
      simp [updateStateAuxR, updateCoordinateR, isActiveIndex, hactive, ih]

/-- If there are no active coordinates, the scaffold state update is identity. -/
theorem updateStateR_no_active
    (p : RestrictedParams)
    (hactive : p.active = [])
    (x : State) :
    updateStateR p x = x := by
  simp [updateStateR, updateStateAuxR_no_active p hactive x 0]

/-- If there are no active coordinates, the ledger effect is zero. -/
theorem ledgerEffectR_no_active
    (p : RestrictedParams)
    (hactive : p.active = [])
    (x : State) :
    ledgerEffectR p x = 0 := by
  unfold ledgerEffectR
  rw [updateStateR_no_active p hactive x]
  simp

/-- With no active coordinates, every state is fixed in the scaffold predicate. -/
theorem inFixedSetR_no_active
    (p : RestrictedParams)
    (hactive : p.active = [])
    (x : State) :
    inFixedSetR p x := by
  intro i hi
  rw [hactive] at hi
  cases hi

/-- Degenerate no-active case: fixed states have zero scaffold ledger effect. -/
theorem updateFixedZeroEffectTarget_no_active
    (p : RestrictedParams)
    (hactive : p.active = [])
    (x : State) :
    updateFixedZeroEffectTarget p x := by
  intro _hspace _hfixed
  exact ledgerEffectR_no_active p hactive x

/-- Degenerate no-active case: nonfixed-positive target holds vacuously. -/
theorem updateNonfixedPositiveEffectTarget_no_active
    (p : RestrictedParams)
    (hactive : p.active = [])
    (x : State) :
    updateNonfixedPositiveEffectTarget p x := by
  intro _hspace hnotfixed
  exact False.elim (hnotfixed (inFixedSetR_no_active p hactive x))

/-- Degenerate no-active case for the combined scaffold update-map target.

This does not prove the intended nonempty-active restricted bridge theorem.
-/
theorem restrictedBridgeUpdateMapTarget_no_active
    (p : RestrictedParams)
    (hactive : p.active = [])
    (x : State) :
    restrictedBridgeUpdateMapTarget p x := by
  exact And.intro
    (updateNonfixedPositiveEffectTarget_no_active p hactive x)
    (updateFixedZeroEffectTarget_no_active p hactive x)

end RestrictedBridge
end VFH2
