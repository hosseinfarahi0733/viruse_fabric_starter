import VFH2.Typed.TypedParams

/-!
# VF-H2 v10 Typed Fixed Set Scaffold

This file defines the typed fixed-set predicate for v10.

Boundary:
- This is a typed-formalization scaffold component.
- It does not prove the restricted bridge theorem.
- It does not prove the full Viruse Fabric theory.
- It does not prove unrestricted TTP-VF-H2-004.
- It is not empirical validation.
- It is not biological validation.

Purpose:
The v9 scaffold defined the fixed set over raw list states and raw Nat active
indices.

In v10, active indices are typed and valid by construction, and state
coordinates are bounded by construction.
-/

namespace VFH2
namespace Typed

/-- Typed fixed-set predicate.

A typed state is fixed when every typed active coordinate is already at top.
-/
def TypedFixedSet
    (p : TypedRestrictedParams)
    (x : p.State) : Prop :=
  ∀ i : WidthIndex p.d, i ∈ p.active → (x i).val = p.n

namespace TypedFixedSet

/-- Eliminate typed fixed-set membership at an active index. -/
theorem elim
    {p : TypedRestrictedParams}
    {x : p.State}
    (hfixed : TypedFixedSet p x)
    {i : WidthIndex p.d}
    (hi : i ∈ p.active) :
    (x i).val = p.n := by
  exact hfixed i hi

/-- The typed top state is fixed for any typed parameter record. -/
theorem topState
    (p : TypedRestrictedParams) :
    TypedFixedSet p (TypedRestrictedParams.topState p) := by
  intro i _hi
  exact TypedRestrictedParams.topState_apply_val p i

/-- If there are no active coordinates, every typed state is fixed. -/
theorem of_active_nil
    (p : TypedRestrictedParams)
    (x : p.State)
    (hactive : p.active = []) :
    TypedFixedSet p x := by
  intro i hi
  rw [hactive] at hi
  cases hi

/-- If a typed state is not fixed, there is an active coordinate that is not top. -/
theorem exists_active_not_top_of_not_fixed
    {p : TypedRestrictedParams}
    {x : p.State}
    (hnotfixed : ¬ TypedFixedSet p x) :
    ∃ i : WidthIndex p.d, i ∈ p.active ∧ (x i).val ≠ p.n := by
  classical
  by_cases hwit :
      ∃ i : WidthIndex p.d, i ∈ p.active ∧ (x i).val ≠ p.n
  · exact hwit
  · exfalso
    apply hnotfixed
    intro i hi
    by_cases htop : (x i).val = p.n
    · exact htop
    · exact False.elim (hwit ⟨i, hi, htop⟩)

/-- A nonfixed typed state implies that the active list is nonempty. -/
theorem active_ne_nil_of_not_fixed
    {p : TypedRestrictedParams}
    {x : p.State}
    (hnotfixed : ¬ TypedFixedSet p x) :
    p.active ≠ [] := by
  intro hactive
  exact hnotfixed (of_active_nil p x hactive)

/-- A bounded coordinate that is not top is strictly below top. -/
theorem val_lt_top_of_ne_top
    {p : TypedRestrictedParams}
    {x : p.State}
    {i : WidthIndex p.d}
    (hne : (x i).val ≠ p.n) :
    (x i).val < p.n := by
  have hle : (x i).val ≤ p.n := (x i).bound
  have hlt_or_eq : (x i).val < p.n ∨ (x i).val = p.n :=
    Nat.lt_or_eq_of_le hle
  cases hlt_or_eq with
  | inl hlt =>
      exact hlt
  | inr heq =>
      exact False.elim (hne heq)

/-- If a typed state is not fixed, there is an active coordinate strictly below top. -/
theorem exists_active_below_top_of_not_fixed
    {p : TypedRestrictedParams}
    {x : p.State}
    (hnotfixed : ¬ TypedFixedSet p x) :
    ∃ i : WidthIndex p.d, i ∈ p.active ∧ (x i).val < p.n := by
  obtain ⟨i, hi, hne⟩ :=
    exists_active_not_top_of_not_fixed hnotfixed
  exact ⟨i, hi, val_lt_top_of_ne_top hne⟩

end TypedFixedSet

end Typed
end VFH2
