import VFH2.Typed.TypedNonfixedIncrease

/-!
# VF-H2 v10 Typed Update Pointwise Monotonicity

This file proves that the v10 typed update never decreases any coordinate.

Boundary:
- This proves pointwise monotonicity of the typed update.
- It does not yet prove positive typed ledger effect.
- It does not prove the full restricted typed bridge theorem.
- It does not prove the full Viruse Fabric theory.
- It does not prove unrestricted TTP-VF-H2-004.
- It is not empirical validation.
- It is not biological validation.

Purpose:
To prove positive ledger effect later, we need:
1. every coordinate is nondecreasing under update;
2. at least one coordinate strictly increases for nonfixed states.

The strict witness was proved in `TypedNonfixedIncrease`.
This file proves the pointwise nondecrease half.
-/

namespace VFH2
namespace Typed

/-- Typed update never decreases any coordinate value. -/
theorem typedUpdateState_val_ge_self
    (p : TypedRestrictedParams)
    (x : p.State)
    (i : WidthIndex p.d) :
    (x i).val ≤ (typedUpdateState p x i).val := by
  by_cases hi : i ∈ p.active
  · rw [typedUpdateState_active_val p x hi]
    exact (x i).bound
  · rw [typedUpdateState_inactive_val p x hi]
    exact Nat.le_refl (x i).val

/-- Typed update is pointwise monotone over all valid typed indices. -/
theorem typedUpdateState_pointwise_monotone
    (p : TypedRestrictedParams)
    (x : p.State) :
    ∀ i : WidthIndex p.d,
      (x i).val ≤ (typedUpdateState p x i).val := by
  intro i
  exact typedUpdateState_val_ge_self p x i

/-- A nonfixed typed state has both pointwise nondecrease and a strict
coordinate-level increase witness.
-/
theorem typed_nonfixed_pointwise_and_strict_witness
    {p : TypedRestrictedParams}
    {x : p.State}
    (hnotfixed : ¬ TypedFixedSet p x) :
    (∀ i : WidthIndex p.d,
      (x i).val ≤ (typedUpdateState p x i).val)
    ∧
    (∃ i : WidthIndex p.d,
      i ∈ p.active ∧
      (x i).val < (typedUpdateState p x i).val) := by
  constructor
  · exact typedUpdateState_pointwise_monotone p x
  · exact typed_exists_active_update_val_lt_of_not_fixed hnotfixed

/-- Target packaging for the ledger-positive prerequisites. -/
def typedLedgerPositivePrereqTarget
    (p : TypedRestrictedParams)
    (x : p.State) : Prop :=
  ¬ TypedFixedSet p x →
    (∀ i : WidthIndex p.d,
      (x i).val ≤ (typedUpdateState p x i).val)
    ∧
    (∃ i : WidthIndex p.d,
      i ∈ p.active ∧
      (x i).val < (typedUpdateState p x i).val)

/-- The current v10 typed scaffold proves the ledger-positive prerequisites. -/
theorem typedLedgerPositivePrereqTarget_proved
    (p : TypedRestrictedParams)
    (x : p.State) :
    typedLedgerPositivePrereqTarget p x := by
  intro hnotfixed
  exact typed_nonfixed_pointwise_and_strict_witness hnotfixed

end Typed
end VFH2
