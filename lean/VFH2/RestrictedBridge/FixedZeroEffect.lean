import VFH2.RestrictedBridge.UpdateMapBasics

/-!
# VF-H2 Restricted Bridge Fixed Zero Effect Basics

This file adds proof-bearing Lean lemmas toward the fixed-set zero-effect
half of the restricted bridge theorem.

Boundary:
- This proves scaffold-level fixed-update/zero-effect lemmas under a
  pointwise update-fixed predicate.
- This is not yet the full machine-checked proof of `RBRIDGE-VF-H2-001-R`.
- This is not a proof of the full Viruse Fabric theory.
- This is not a proof of unrestricted `TTP-VF-H2-004`.
- This is not empirical validation.
- This is not biological validation.

Next bridge still needed:
connect `inFixedSetR p x` to `pointwiseFixedForUpdate p 0 x`
under suitable active-index well-formedness assumptions.
-/

namespace VFH2
namespace RestrictedBridge

/-- Pointwise predicate saying every coordinate visited by the scaffold update
is left unchanged by `updateCoordinateR`.

This is stronger and more operational than `inFixedSetR`.
It is designed as a proof bridge toward fixed-set zero effect.
-/
def pointwiseFixedForUpdate (p : RestrictedParams) : Nat → State → Prop
  | _, [] => True
  | i, a :: xs =>
      updateCoordinateR p i a = a ∧ pointwiseFixedForUpdate p (i + 1) xs

theorem pointwiseFixedForUpdate_nil (p : RestrictedParams) (i : Nat) :
    pointwiseFixedForUpdate p i ([] : State) := by
  simp [pointwiseFixedForUpdate]

theorem pointwiseFixedForUpdate_cons_head
    {p : RestrictedParams} {i a : Nat} {xs : State}
    (h : pointwiseFixedForUpdate p i (a :: xs)) :
    updateCoordinateR p i a = a := by
  exact h.1

theorem pointwiseFixedForUpdate_cons_tail
    {p : RestrictedParams} {i a : Nat} {xs : State}
    (h : pointwiseFixedForUpdate p i (a :: xs)) :
    pointwiseFixedForUpdate p (i + 1) xs := by
  exact h.2

/-- If the pointwise update-fixed predicate holds, the recursive update helper
returns the original state.
-/
theorem updateStateAuxR_eq_self_of_pointwiseFixed
    (p : RestrictedParams) (x : State) (i : Nat)
    (h : pointwiseFixedForUpdate p i x) :
    updateStateAuxR p i x = x := by
  induction x generalizing i with
  | nil =>
      simp [updateStateAuxR]
  | cons a xs ih =>
      have hhead : updateCoordinateR p i a = a := h.1
      have htail : pointwiseFixedForUpdate p (i + 1) xs := h.2
      simp [updateStateAuxR, hhead, ih (i + 1) htail]

/-- If the pointwise update-fixed predicate holds from index zero, the scaffold
state update is the identity.
-/
theorem updateStateR_eq_self_of_pointwiseFixed
    (p : RestrictedParams) (x : State)
    (h : pointwiseFixedForUpdate p 0 x) :
    updateStateR p x = x := by
  unfold updateStateR
  exact updateStateAuxR_eq_self_of_pointwiseFixed p x 0 h

/-- Any state unchanged by the scaffold update has zero ledger effect. -/
theorem ledgerEffectR_zero_of_updateStateR_eq_self
    (p : RestrictedParams) (x : State)
    (h : updateStateR p x = x) :
    ledgerEffectR p x = 0 := by
  unfold ledgerEffectR
  rw [h]
  simp

/-- Pointwise update-fixed states have zero scaffold ledger effect. -/
theorem ledgerEffectR_zero_of_pointwiseFixed
    (p : RestrictedParams) (x : State)
    (h : pointwiseFixedForUpdate p 0 x) :
    ledgerEffectR p x = 0 := by
  exact ledgerEffectR_zero_of_updateStateR_eq_self
    p x
    (updateStateR_eq_self_of_pointwiseFixed p x h)

/-- Pointwise update-fixed states satisfy the fixed-zero-effect target.

This is a genuine scaffold proof step toward:

`x ∈ F_R => ledger_effect_size_R(x)=0`

The remaining future bridge is proving that the current fixed-set predicate
implies `pointwiseFixedForUpdate` under suitable active-index assumptions.
-/
theorem updateFixedZeroEffectTarget_of_pointwiseFixed
    (p : RestrictedParams) (x : State)
    (h : pointwiseFixedForUpdate p 0 x) :
    updateFixedZeroEffectTarget p x := by
  intro _hspace _hfixed
  exact ledgerEffectR_zero_of_pointwiseFixed p x h

end RestrictedBridge
end VFH2
