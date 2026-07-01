import VFH2.Typed.WidthIndex

/-!
# VF-H2 v10 Typed State Scaffold

This file adds the first typed state representation for v10.

Boundary:
- This is a typed-formalization scaffold component.
- It does not prove the restricted bridge theorem.
- It does not prove the full Viruse Fabric theory.
- It does not prove unrestricted TTP-VF-H2-004.
- It is not empirical validation.
- It is not biological validation.

Purpose:
The v9 scaffold represented states as `List Nat` plus external guards for
width and coordinate bounds.

In v10, a typed state is represented as a function from valid width indices
to bounded coordinates.
-/

namespace VFH2
namespace Typed

/-- A typed restricted state.

For top value `n` and spatial width parameter `d`, a state maps every valid
flattened coordinate index to a coordinate bounded by `n`.
-/
abbrev TypedState (n d : Nat) :=
  WidthIndex d → BoundedCoord n

namespace TypedState

/-- Get a coordinate from a typed state. -/
def get
    {n d : Nat}
    (x : TypedState n d)
    (i : WidthIndex d) :
    BoundedCoord n :=
  x i

/-- A typed state's coordinate value is bounded by top by construction. -/
theorem get_val_le_top
    {n d : Nat}
    (x : TypedState n d)
    (i : WidthIndex d) :
    (get x i).val ≤ n := by
  exact (get x i).bound

/-- Direct application form of coordinate boundedness. -/
theorem apply_val_le_top
    {n d : Nat}
    (x : TypedState n d)
    (i : WidthIndex d) :
    (x i).val ≤ n := by
  exact (x i).bound

/-- Constant typed state. -/
def const
    (n d : Nat)
    (c : BoundedCoord n) :
    TypedState n d :=
  fun _ => c

/-- Zero typed state. -/
def zero
    (n d : Nat) :
    TypedState n d :=
  fun _ => BoundedCoord.zero n

/-- Top typed state. -/
def top
    (n d : Nat) :
    TypedState n d :=
  fun _ => BoundedCoord.top n

/-- Constant state returns the given coordinate at every index. -/
theorem const_apply
    {n d : Nat}
    (c : BoundedCoord n)
    (i : WidthIndex d) :
    const n d c i = c := by
  rfl

/-- Constant state value projection. -/
theorem const_apply_val
    {n d : Nat}
    (c : BoundedCoord n)
    (i : WidthIndex d) :
    (const n d c i).val = c.val := by
  rfl

/-- Zero state has value zero at every index. -/
theorem zero_apply_val
    (n d : Nat)
    (i : WidthIndex d) :
    (zero n d i).val = 0 := by
  rfl

/-- Top state has value `n` at every index. -/
theorem top_apply_val
    (n d : Nat)
    (i : WidthIndex d) :
    (top n d i).val = n := by
  rfl

/-- Update one coordinate of a typed state.

The replacement coordinate is already bounded by construction, so the updated
state remains typed without a separate bounds proof.
-/
def updateAt
    {n d : Nat}
    (x : TypedState n d)
    (i : WidthIndex d)
    (c : BoundedCoord n) :
    TypedState n d :=
  fun j => if j = i then c else x j

/-- Updating at an index returns the replacement coordinate at that index. -/
theorem updateAt_same
    {n d : Nat}
    (x : TypedState n d)
    (i : WidthIndex d)
    (c : BoundedCoord n) :
    updateAt x i c i = c := by
  unfold updateAt
  simp

/-- Updating at one index leaves every different index unchanged. -/
theorem updateAt_other
    {n d : Nat}
    (x : TypedState n d)
    {i j : WidthIndex d}
    (c : BoundedCoord n)
    (h : j ≠ i) :
    updateAt x i c j = x j := by
  unfold updateAt
  simp [h]

/-- Updated states still return bounded coordinates by construction. -/
theorem updateAt_apply_val_le_top
    {n d : Nat}
    (x : TypedState n d)
    (i j : WidthIndex d)
    (c : BoundedCoord n) :
    (updateAt x i c j).val ≤ n := by
  exact (updateAt x i c j).bound

end TypedState

end Typed
end VFH2
