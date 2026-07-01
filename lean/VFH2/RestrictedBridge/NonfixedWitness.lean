import VFH2.RestrictedBridge.ActiveIndexSoundness

/-!
# VF-H2 Restricted Bridge Nonfixed Active Witness

This file proves the first witness lemma needed for the positive-effect half
of the restricted bridge theorem.

Boundary:
- This proves a scaffold-level nonfixed active witness lemma.
- This is not yet the full machine-checked proof of `RBRIDGE-VF-H2-001-R`.
- This is not a proof of the full Viruse Fabric theory.
- This is not a proof of unrestricted `TTP-VF-H2-004`.
- This is not empirical validation.
- This is not biological validation.

Next proof obligations:
- connect the witness with state-space bounds;
- prove that a witnessed active coordinate increases under the update;
- lift coordinate increase to positive ledger effect.
-/

namespace VFH2
namespace RestrictedBridge

/-- If a state is not in the scaffold fixed set, then there exists an active
coordinate whose value is not top.

This is the witness needed for the positive-effect half of the restricted
bridge theorem.
-/
theorem exists_active_not_top_of_not_inFixedSetR
    (p : RestrictedParams) (x : State)
    (hnotfixed : ¬ inFixedSetR p x) :
    ∃ i : Nat, i ∈ p.active ∧ x.getD i 0 ≠ p.n := by
  classical
  by_cases hwit : ∃ i : Nat, i ∈ p.active ∧ x.getD i 0 ≠ p.n
  · exact hwit
  · exfalso
    apply hnotfixed
    intro i hi
    by_cases htop : x.getD i 0 = p.n
    · exact htop
    · exact False.elim (hwit ⟨i, hi, htop⟩)

/-- A nonfixed state implies that the active list has at least one member. -/
theorem exists_active_index_of_not_inFixedSetR
    (p : RestrictedParams) (x : State)
    (hnotfixed : ¬ inFixedSetR p x) :
    ∃ i : Nat, i ∈ p.active := by
  obtain ⟨i, hi, _hne⟩ :=
    exists_active_not_top_of_not_inFixedSetR p x hnotfixed
  exact ⟨i, hi⟩

/-- If there are no active coordinates, every state is in the scaffold fixed set. -/
theorem inFixedSetR_of_active_nil
    (p : RestrictedParams) (x : State)
    (hactive : p.active = []) :
    inFixedSetR p x := by
  intro i hi
  rw [hactive] at hi
  cases hi

/-- A nonfixed state rules out the degenerate no-active case. -/
theorem active_ne_nil_of_not_inFixedSetR
    (p : RestrictedParams) (x : State)
    (hnotfixed : ¬ inFixedSetR p x) :
    p.active ≠ [] := by
  intro hactive
  exact hnotfixed (inFixedSetR_of_active_nil p x hactive)

end RestrictedBridge
end VFH2
