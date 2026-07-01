import VFH2.Typed.TypedFixedSet

/-!
# VF-H2 v10 Typed Update Scaffold

This file defines the typed scaffold update map for v10.

Boundary:
- This is a typed-formalization scaffold component.
- It does not prove the restricted bridge theorem.
- It does not prove the full Viruse Fabric theory.
- It does not prove unrestricted TTP-VF-H2-004.
- It is not empirical validation.
- It is not biological validation.

Purpose:
The v9 scaffold updated list-backed raw Nat coordinates using external range
and bound guards.

In v10, active indices are typed as valid width indices and coordinates are
bounded by construction.
-/

namespace VFH2
namespace Typed

/-- Boolean active-index test over typed active indices. -/
def typedIsActive
    (p : TypedRestrictedParams)
    (i : WidthIndex p.d) : Bool :=
  decide (i ∈ p.active)

/-- Typed active-index test is true for active members. -/
theorem typedIsActive_true_of_mem
    (p : TypedRestrictedParams)
    {i : WidthIndex p.d}
    (hi : i ∈ p.active) :
    typedIsActive p i = true := by
  simp [typedIsActive, hi]

/-- Typed active-index test is false for inactive members. -/
theorem typedIsActive_false_of_not_mem
    (p : TypedRestrictedParams)
    {i : WidthIndex p.d}
    (hnot : i ∉ p.active) :
    typedIsActive p i = false := by
  simp [typedIsActive, hnot]

/-- Coordinate update for the typed scaffold.

Active coordinates are sent to top. Inactive coordinates are preserved.
-/
def typedUpdateCoord
    (p : TypedRestrictedParams)
    (x : p.State)
    (i : WidthIndex p.d) :
    BoundedCoord p.n :=
  if i ∈ p.active then BoundedCoord.top p.n else x i

/-- Active typed coordinates update to top. -/
theorem typedUpdateCoord_active
    (p : TypedRestrictedParams)
    (x : p.State)
    {i : WidthIndex p.d}
    (hi : i ∈ p.active) :
    typedUpdateCoord p x i = BoundedCoord.top p.n := by
  unfold typedUpdateCoord
  simp [hi]

/-- Inactive typed coordinates are preserved. -/
theorem typedUpdateCoord_inactive
    (p : TypedRestrictedParams)
    (x : p.State)
    {i : WidthIndex p.d}
    (hnot : i ∉ p.active) :
    typedUpdateCoord p x i = x i := by
  unfold typedUpdateCoord
  simp [hnot]

/-- Active typed coordinates update to top value. -/
theorem typedUpdateCoord_active_val
    (p : TypedRestrictedParams)
    (x : p.State)
    {i : WidthIndex p.d}
    (hi : i ∈ p.active) :
    (typedUpdateCoord p x i).val = p.n := by
  rw [typedUpdateCoord_active p x hi]
  rfl

/-- Inactive typed coordinates preserve their value. -/
theorem typedUpdateCoord_inactive_val
    (p : TypedRestrictedParams)
    (x : p.State)
    {i : WidthIndex p.d}
    (hnot : i ∉ p.active) :
    (typedUpdateCoord p x i).val = (x i).val := by
  rw [typedUpdateCoord_inactive p x hnot]

/-- Updated typed coordinates remain bounded by top by construction. -/
theorem typedUpdateCoord_val_le_top
    (p : TypedRestrictedParams)
    (x : p.State)
    (i : WidthIndex p.d) :
    (typedUpdateCoord p x i).val ≤ p.n := by
  exact (typedUpdateCoord p x i).bound

/-- Typed update map over an entire typed state. -/
def typedUpdateState
    (p : TypedRestrictedParams)
    (x : p.State) :
    p.State :=
  fun i => typedUpdateCoord p x i

/-- Applying the typed update state is the same as updating the coordinate. -/
theorem typedUpdateState_apply
    (p : TypedRestrictedParams)
    (x : p.State)
    (i : WidthIndex p.d) :
    typedUpdateState p x i = typedUpdateCoord p x i := by
  rfl

/-- Active typed state coordinates update to top value. -/
theorem typedUpdateState_active_val
    (p : TypedRestrictedParams)
    (x : p.State)
    {i : WidthIndex p.d}
    (hi : i ∈ p.active) :
    (typedUpdateState p x i).val = p.n := by
  exact typedUpdateCoord_active_val p x hi

/-- Inactive typed state coordinates preserve their value. -/
theorem typedUpdateState_inactive_val
    (p : TypedRestrictedParams)
    (x : p.State)
    {i : WidthIndex p.d}
    (hnot : i ∉ p.active) :
    (typedUpdateState p x i).val = (x i).val := by
  exact typedUpdateCoord_inactive_val p x hnot

/-- Updated typed states still return bounded coordinates by construction. -/
theorem typedUpdateState_apply_val_le_top
    (p : TypedRestrictedParams)
    (x : p.State)
    (i : WidthIndex p.d) :
    (typedUpdateState p x i).val ≤ p.n := by
  exact (typedUpdateState p x i).bound

/-- If a typed state is fixed, every coordinate value is preserved by update. -/
theorem typedUpdateState_val_eq_self_of_fixed
    {p : TypedRestrictedParams}
    {x : p.State}
    (hfixed : TypedFixedSet p x)
    (i : WidthIndex p.d) :
    (typedUpdateState p x i).val = (x i).val := by
  by_cases hi : i ∈ p.active
  · rw [typedUpdateState_active_val p x hi]
    exact (hfixed i hi).symm
  · exact typedUpdateState_inactive_val p x hi

/-- If a typed coordinate is active and below top, update strictly increases its value. -/
theorem typedUpdateState_active_below_top_val_lt
    {p : TypedRestrictedParams}
    {x : p.State}
    {i : WidthIndex p.d}
    (hi : i ∈ p.active)
    (hbelow : (x i).val < p.n) :
    (x i).val < (typedUpdateState p x i).val := by
  rw [typedUpdateState_active_val p x hi]
  exact hbelow

end Typed
end VFH2
