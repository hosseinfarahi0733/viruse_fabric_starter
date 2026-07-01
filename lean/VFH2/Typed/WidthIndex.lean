import VFH2.Typed.BoundedCoord

/-!
# VF-H2 v10 Finite Width Index Scaffold

This file adds the typed finite index layer for v10.

Boundary:
- This is a typed-formalization scaffold component.
- It does not prove the restricted bridge theorem.
- It does not prove the full Viruse Fabric theory.
- It does not prove unrestricted TTP-VF-H2-004.
- It is not empirical validation.
- It is not biological validation.

Purpose:
The v9 scaffold represented active indices as raw Nat values and required
external range guards.

In v10, valid coordinate indices begin moving into the type itself through
Fin (3 * d).
-/

namespace VFH2
namespace Typed

/-- Typed flattened width for T_3 x I_d. -/
def typedWidth (d : Nat) : Nat :=
  3 * d

/-- A valid typed coordinate index for width 3 * d. -/
abbrev WidthIndex (d : Nat) :=
  Fin (typedWidth d)

namespace WidthIndex

/-- Any typed width index is below the typed width by construction. -/
theorem val_lt_typedWidth
    {d : Nat}
    (i : WidthIndex d) :
    i.val < typedWidth d := by
  exact i.isLt

/-- Any typed width index is below 3 * d by construction. -/
theorem val_lt_three_mul
    {d : Nat}
    (i : WidthIndex d) :
    i.val < 3 * d := by
  exact i.isLt

/-- Equality of typed width indices follows from equality of their values. -/
theorem ext
    {d : Nat}
    {i j : WidthIndex d}
    (h : i.val = j.val) :
    i = j := by
  exact Fin.ext h

/-- Width is zero when d is zero. -/
theorem typedWidth_zero :
    typedWidth 0 = 0 := by
  rfl

/-- Width increases by three when d increases by one. -/
theorem typedWidth_succ
    (d : Nat) :
    typedWidth (d + 1) = typedWidth d + 3 := by
  unfold typedWidth
  omega

/-- Positive d gives positive typed width. -/
theorem typedWidth_pos_of_pos
    {d : Nat}
    (hd : 0 < d) :
    0 < typedWidth d := by
  unfold typedWidth
  omega

/-- There is no valid index for zero width. -/
theorem no_index_zero_width
    (i : WidthIndex 0) :
    False := by
  exact Nat.not_lt_zero i.val (by simpa [typedWidth] using i.isLt)

/-- The zero index is valid whenever d is positive. -/
def zeroOfPositive
    {d : Nat}
    (hd : 0 < d) :
    WidthIndex d :=
  { val := 0, isLt := typedWidth_pos_of_pos hd }

/-- The zero index is valid for width 3 * (d + 1). -/
def zeroOfSucc
    (d : Nat) :
    WidthIndex (d + 1) :=
  zeroOfPositive (by omega)

/-- The value of zeroOfSucc is zero. -/
theorem zeroOfSucc_val
    (d : Nat) :
    (zeroOfSucc d).val = 0 := by
  rfl

end WidthIndex

end Typed
end VFH2
