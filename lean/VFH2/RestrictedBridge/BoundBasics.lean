import VFH2.RestrictedBridge.NonfixedWitness

/-!
# VF-H2 Restricted Bridge Bound Basics

This file proves basic `getD` bounds needed for the positive-effect half
of the restricted bridge theorem.

Boundary:
- This proves scaffold-level bound lemmas for list-backed restricted states.
- This is not yet the full machine-checked proof of `RBRIDGE-VF-H2-001-R`.
- This is not a proof of the full Viruse Fabric theory.
- This is not a proof of unrestricted `TTP-VF-H2-004`.
- This is not empirical validation.
- This is not biological validation.

Next proof obligations:
- prove coordinate increase for a witnessed active below-top coordinate;
- lift coordinate increase to positive ledger effect;
- combine fixed-zero and nonfixed-positive halves.
-/

namespace VFH2
namespace RestrictedBridge

/-- Active indices are in range of the concrete list-backed state. -/
def activeIndicesInRange (p : RestrictedParams) (x : State) : Prop :=
  ∀ i : Nat, i ∈ p.active → i < x.length

/-- If all list values are bounded by `p.n`, then any in-range `getD` value
is also bounded by `p.n`.
-/
theorem getD_le_of_hasLnBounds
    {p : RestrictedParams} {x : State}
    (hb : hasLnBounds p x)
    (i : Nat)
    (hi : i < x.length) :
    x.getD i 0 ≤ p.n := by
  induction x generalizing i with
  | nil =>
      simp at hi
  | cons a xs ih =>
      cases i with
      | zero =>
          unfold hasLnBounds at hb
          have ha : a ≤ p.n := hb a (by simp)
          simpa using ha
      | succ i =>
          have hbxs : hasLnBounds p xs := by
            intro b hbmem
            exact hb b (by simp [hbmem])
          have hi' : i < xs.length := by
            simpa using hi
          simpa using ih hbxs i hi'

/-- Restricted state-space membership gives bounded `getD` values for
in-range indices.
-/
theorem getD_le_of_inRestrictedStateSpace
    {p : RestrictedParams} {x : State}
    (hspace : inRestrictedStateSpace p x)
    (i : Nat)
    (hi : i < x.length) :
    x.getD i 0 ≤ p.n := by
  exact getD_le_of_hasLnBounds hspace.2 i hi

/-- If a natural number is bounded by top but not equal to top, it is below top. -/
theorem nat_lt_top_of_le_and_ne
    {a n : Nat}
    (hle : a ≤ n)
    (hne : a ≠ n) :
    a < n := by
  have hlt_or_eq : a < n ∨ a = n := Nat.lt_or_eq_of_le hle
  cases hlt_or_eq with
  | inl hlt =>
      exact hlt
  | inr heq =>
      exact False.elim (hne heq)

/-- A nonfixed restricted state has an active witness strictly below top,
provided active indices are in range.
-/
theorem exists_active_below_top_of_not_inFixedSetR
    {p : RestrictedParams} {x : State}
    (hspace : inRestrictedStateSpace p x)
    (hrange : activeIndicesInRange p x)
    (hnotfixed : ¬ inFixedSetR p x) :
    ∃ i : Nat, i ∈ p.active ∧ x.getD i 0 < p.n := by
  obtain ⟨i, hi, hne⟩ :=
    exists_active_not_top_of_not_inFixedSetR p x hnotfixed
  have hle : x.getD i 0 ≤ p.n :=
    getD_le_of_inRestrictedStateSpace hspace i (hrange i hi)
  have hlt : x.getD i 0 < p.n :=
    nat_lt_top_of_le_and_ne hle hne
  exact ⟨i, hi, hlt⟩

end RestrictedBridge
end VFH2
