import VFH2.Typed.TypedFixedZero

/-!
# VF-H2 v10 Typed Nonfixed Coordinate Increase

This file proves the witness-level positive direction for the v10 typed
scaffold.

Boundary:
- This proves coordinate-level increase for a nonfixed typed state.
- It does not yet prove positive typed ledger effect.
- It does not prove the full restricted typed bridge theorem.
- It does not prove the full Viruse Fabric theory.
- It does not prove unrestricted TTP-VF-H2-004.
- It is not empirical validation.
- It is not biological validation.
-/

namespace VFH2
namespace Typed

/-- A nonfixed typed state has an active coordinate below top. -/
theorem typed_exists_active_below_top_of_not_fixed
    {p : TypedRestrictedParams}
    {x : p.State}
    (hnotfixed : ¬ TypedFixedSet p x) :
    ∃ i : WidthIndex p.d, i ∈ p.active ∧ (x i).val < p.n := by
  exact TypedFixedSet.exists_active_below_top_of_not_fixed hnotfixed

/-- A nonfixed typed state has an active coordinate that strictly increases
under the typed update.
-/
theorem typed_exists_active_update_val_lt_of_not_fixed
    {p : TypedRestrictedParams}
    {x : p.State}
    (hnotfixed : ¬ TypedFixedSet p x) :
    ∃ i : WidthIndex p.d,
      i ∈ p.active ∧
      (x i).val < (typedUpdateState p x i).val := by
  obtain ⟨i, hi, hbelow⟩ :=
    typed_exists_active_below_top_of_not_fixed hnotfixed
  exact ⟨
    i,
    hi,
    typedUpdateState_active_below_top_val_lt hi hbelow
  ⟩

/-- Nonfixed typed states have a coordinate-level positive witness. -/
def typedNonfixedCoordinateIncreaseTarget
    (p : TypedRestrictedParams)
    (x : p.State) : Prop :=
  ¬ TypedFixedSet p x →
    ∃ i : WidthIndex p.d,
      i ∈ p.active ∧
      (x i).val < (typedUpdateState p x i).val

/-- The current v10 typed scaffold proves the nonfixed coordinate-increase
target.
-/
theorem typedNonfixedCoordinateIncreaseTarget_proved
    (p : TypedRestrictedParams)
    (x : p.State) :
    typedNonfixedCoordinateIncreaseTarget p x := by
  intro hnotfixed
  exact typed_exists_active_update_val_lt_of_not_fixed hnotfixed

end Typed
end VFH2
