import VFH2.Typed.TypedState

/-!
# VF-H2 v10 Typed Parameters Scaffold

This file adds typed restricted parameters for v10.

Boundary:
- This is a typed-formalization scaffold component.
- It does not prove the restricted bridge theorem.
- It does not prove the full Viruse Fabric theory.
- It does not prove unrestricted TTP-VF-H2-004.
- It is not empirical validation.
- It is not biological validation.

Purpose:
The v9 scaffold used raw active indices:

`active : List Nat`

and then required an external well-formedness predicate proving those indices
were within width.

In v10, active indices are typed as `WidthIndex d`, so out-of-width active
indices cannot be constructed.
-/

namespace VFH2
namespace Typed

/-- Typed restricted parameters.

The active set is represented as a list of valid typed width indices. This
removes the v9 need for a separate active-width guard.
-/
structure TypedRestrictedParams where
  n : Nat
  d : Nat
  active : List (WidthIndex d)

/-- The typed state associated with typed restricted parameters. -/
abbrev TypedRestrictedParams.State
    (p : TypedRestrictedParams) :=
  TypedState p.n p.d

namespace TypedRestrictedParams

/-- The top value of typed restricted parameters. -/
def top
    (p : TypedRestrictedParams) : Nat :=
  p.n

/-- The spatial width parameter. -/
def spatialWidth
    (p : TypedRestrictedParams) : Nat :=
  p.d

/-- The flattened typed width. -/
def width
    (p : TypedRestrictedParams) : Nat :=
  typedWidth p.d

/-- The active list contains only typed valid indices by construction. -/
theorem active_index_lt_width
    (p : TypedRestrictedParams)
    {i : WidthIndex p.d}
    (_hi : i ∈ p.active) :
    i.val < typedWidth p.d := by
  exact i.isLt

/-- Active indices are below the parameter width by construction. -/
theorem active_index_lt_param_width
    (p : TypedRestrictedParams)
    {i : WidthIndex p.d}
    (_hi : i ∈ p.active) :
    i.val < p.width := by
  exact i.isLt

/-- Any coordinate of a typed parameter state is bounded by top. -/
theorem state_apply_val_le_top
    (p : TypedRestrictedParams)
    (x : p.State)
    (i : WidthIndex p.d) :
    (x i).val ≤ p.n := by
  exact (x i).bound

/-- The zero state for typed parameters. -/
def zeroState
    (p : TypedRestrictedParams) :
    p.State :=
  TypedState.zero p.n p.d

/-- The top state for typed parameters. -/
def topState
    (p : TypedRestrictedParams) :
    p.State :=
  TypedState.top p.n p.d

/-- The zero state has value zero at every typed index. -/
theorem zeroState_apply_val
    (p : TypedRestrictedParams)
    (i : WidthIndex p.d) :
    (zeroState p i).val = 0 := by
  rfl

/-- The top state has value `p.n` at every typed index. -/
theorem topState_apply_val
    (p : TypedRestrictedParams)
    (i : WidthIndex p.d) :
    (topState p i).val = p.n := by
  rfl

end TypedRestrictedParams

end Typed
end VFH2
