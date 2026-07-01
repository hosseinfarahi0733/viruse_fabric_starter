import Std

/-!
# VF-H2 v10 Bounded Coordinate Scaffold

This file starts the v10 dependent / typed formalization phase.

Boundary:
- This is a typed-formalization scaffold component.
- It does not prove the restricted bridge theorem.
- It does not prove the full Viruse Fabric theory.
- It does not prove unrestricted `TTP-VF-H2-004`.
- It is not empirical validation.
- It is not biological validation.

Purpose:
The v9 scaffold represented coordinates as raw `Nat` values guarded by
propositions such as `hasLnBounds`.

In v10, boundedness begins moving into the type itself.
-/

namespace VFH2
namespace Typed

/-- A coordinate value bounded above by `n`.

This is the typed replacement for raw scaffold coordinates that were previously
represented as `Nat` plus an external `a ≤ n` guard.
-/
structure BoundedCoord (n : Nat) where
  val : Nat
  bound : val ≤ n

namespace BoundedCoord

/-- The underlying natural value of a bounded coordinate is bounded by top. -/
theorem val_le_top
    {n : Nat}
    (c : BoundedCoord n) :
    c.val ≤ n := by
  exact c.bound

/-- Natural values are nonnegative, kept as a named helper for later proofs. -/
theorem zero_le_val
    {n : Nat}
    (c : BoundedCoord n) :
    0 ≤ c.val := by
  exact Nat.zero_le c.val

/-- Any bounded coordinate is strictly below `n + 1`. -/
theorem val_lt_succ_top
    {n : Nat}
    (c : BoundedCoord n) :
    c.val < n + 1 := by
  exact Nat.lt_succ_of_le c.bound

/-- The zero coordinate is always valid for any top value `n`. -/
def zero (n : Nat) : BoundedCoord n :=
  { val := 0, bound := Nat.zero_le n }

/-- The top coordinate is always valid for top value `n`. -/
def top (n : Nat) : BoundedCoord n :=
  { val := n, bound := Nat.le_refl n }

/-- The value of the zero coordinate is zero. -/
theorem zero_val
    (n : Nat) :
    (zero n).val = 0 := by
  rfl

/-- The value of the top coordinate is `n`. -/
theorem top_val
    (n : Nat) :
    (top n).val = n := by
  rfl

/-- Constructor value projection helper. -/
theorem mk_val
    {n v : Nat}
    (h : v ≤ n) :
    ({ val := v, bound := h } : BoundedCoord n).val = v := by
  rfl

/-- Equality of bounded coordinates implies equality of their values. -/
theorem val_eq_of_eq
    {n : Nat}
    {a b : BoundedCoord n}
    (h : a = b) :
    a.val = b.val := by
  cases h
  rfl

end BoundedCoord

end Typed
end VFH2
