import VFH2.Product.ThreeTimeObserverProjection

/-!
# C114: Constraint Geometry Is Not Determined by a Chain

This module gives a finite counterexample to pairwise reduction.  Two genuinely
different ternary constraints have identical existential shadows on every pair
of time layers.  Consequently, even all pairwise information—and therefore an
adjacent causal chain—does not determine the global three-way constraint.

This is a mathematical insufficiency theorem, not a definition that assumes
the desired conclusion.
-/

namespace VFH2
namespace ThreeTime

/-- A constraint whose admissibility depends jointly on three temporal values. -/
abbrev TernaryConstraint (α : Type) : Type :=
  α → α → α → Prop

/-- Existential shadow on the past/present pair. -/
def pastPresentShadow
    {α : Type}
    (r : TernaryConstraint α)
    (past present : α) : Prop :=
  ∃ future : α, r past present future

/-- Existential shadow on the present/future pair. -/
def presentFutureShadow
    {α : Type}
    (r : TernaryConstraint α)
    (present future : α) : Prop :=
  ∃ past : α, r past present future

/-- Existential shadow on the past/future pair. -/
def pastFutureShadow
    {α : Type}
    (r : TernaryConstraint α)
    (past future : α) : Prop :=
  ∃ present : α, r past present future

/-- Equality of the two adjacent shadows carried by a temporal chain. -/
def AdjacentChainIndistinguishable
    {α : Type}
    (r s : TernaryConstraint α) : Prop :=
  (∀ past present,
      pastPresentShadow r past present ↔
        pastPresentShadow s past present) ∧
    (∀ present future,
      presentFutureShadow r present future ↔
        presentFutureShadow s present future)

/-- Equality of all three pairwise existential shadows. -/
def PairwiseIndistinguishable
    {α : Type}
    (r s : TernaryConstraint α) : Prop :=
  AdjacentChainIndistinguishable r s ∧
    ∀ past future,
      pastFutureShadow r past future ↔
        pastFutureShadow s past future

/-- Pointwise equality of the complete ternary admissibility geometry. -/
def GloballyEquivalent
    {α : Type}
    (r s : TernaryConstraint α) : Prop :=
  ∀ past present future,
    r past present future ↔ s past present future

/-- Even Boolean parity, written without any external algebra dependency. -/
def evenParity : TernaryConstraint Bool
  | false, false, future => future = false
  | false, true, future => future = true
  | true, false, future => future = true
  | true, true, future => future = false

/-- The complementary odd-parity constraint. -/
def oddParity : TernaryConstraint Bool :=
  fun past present future => ¬ evenParity past present future

theorem evenParity_pastPresentShadow
    (past present : Bool) :
    pastPresentShadow evenParity past present := by
  cases past <;> cases present
  · exact ⟨false, rfl⟩
  · exact ⟨true, rfl⟩
  · exact ⟨true, rfl⟩
  · exact ⟨false, rfl⟩

theorem oddParity_pastPresentShadow
    (past present : Bool) :
    pastPresentShadow oddParity past present := by
  cases past <;> cases present
  · exact ⟨true, by simp [oddParity, evenParity]⟩
  · exact ⟨false, by simp [oddParity, evenParity]⟩
  · exact ⟨false, by simp [oddParity, evenParity]⟩
  · exact ⟨true, by simp [oddParity, evenParity]⟩

theorem evenParity_presentFutureShadow
    (present future : Bool) :
    presentFutureShadow evenParity present future := by
  cases present <;> cases future
  · exact ⟨false, rfl⟩
  · exact ⟨true, rfl⟩
  · exact ⟨true, rfl⟩
  · exact ⟨false, rfl⟩

theorem oddParity_presentFutureShadow
    (present future : Bool) :
    presentFutureShadow oddParity present future := by
  cases present <;> cases future
  · exact ⟨true, by simp [oddParity, evenParity]⟩
  · exact ⟨false, by simp [oddParity, evenParity]⟩
  · exact ⟨false, by simp [oddParity, evenParity]⟩
  · exact ⟨true, by simp [oddParity, evenParity]⟩

theorem evenParity_pastFutureShadow
    (past future : Bool) :
    pastFutureShadow evenParity past future := by
  cases past <;> cases future
  · exact ⟨false, rfl⟩
  · exact ⟨true, rfl⟩
  · exact ⟨true, rfl⟩
  · exact ⟨false, rfl⟩

theorem oddParity_pastFutureShadow
    (past future : Bool) :
    pastFutureShadow oddParity past future := by
  cases past <;> cases future
  · exact ⟨true, by simp [oddParity, evenParity]⟩
  · exact ⟨false, by simp [oddParity, evenParity]⟩
  · exact ⟨false, by simp [oddParity, evenParity]⟩
  · exact ⟨true, by simp [oddParity, evenParity]⟩

/-- Even and odd parity expose exactly the same data to an adjacent chain. -/
theorem even_odd_adjacentChain_indistinguishable :
    AdjacentChainIndistinguishable evenParity oddParity := by
  constructor
  · intro past present
    exact iff_of_true
      (evenParity_pastPresentShadow past present)
      (oddParity_pastPresentShadow past present)
  · intro present future
    exact iff_of_true
      (evenParity_presentFutureShadow present future)
      (oddParity_presentFutureShadow present future)

/-- They remain indistinguishable even after adding the nonadjacent pair. -/
theorem even_odd_pairwise_indistinguishable :
    PairwiseIndistinguishable evenParity oddParity := by
  constructor
  · exact even_odd_adjacentChain_indistinguishable
  · intro past future
    exact iff_of_true
      (evenParity_pastFutureShadow past future)
      (oddParity_pastFutureShadow past future)

/-- Nevertheless, their complete three-way admissibility differs. -/
theorem even_odd_not_globallyEquivalent :
    ¬ GloballyEquivalent evenParity oddParity := by
  intro hglobal
  have heven : evenParity false false false := rfl
  have hnotOdd : ¬ oddParity false false false := by
    intro hodd
    exact hodd rfl
  exact hnotOdd ((hglobal false false false).mp heven)

/--
All pairwise shadows can agree while the global constraint geometries differ.
This is the formal non-chain witness.
-/
theorem pairwise_shadows_do_not_determine_global_constraint :
    ∃ r s : TernaryConstraint Bool,
      PairwiseIndistinguishable r s ∧
        ¬ GloballyEquivalent r s := by
  exact ⟨
    evenParity,
    oddParity,
    even_odd_pairwise_indistinguishable,
    even_odd_not_globallyEquivalent
  ⟩

/-- The weaker adjacent-chain insufficiency follows immediately. -/
theorem adjacent_chain_does_not_determine_global_constraint :
    ∃ r s : TernaryConstraint Bool,
      AdjacentChainIndistinguishable r s ∧
        ¬ GloballyEquivalent r s := by
  exact ⟨
    evenParity,
    oddParity,
    even_odd_adjacentChain_indistinguishable,
    even_odd_not_globallyEquivalent
  ⟩

end ThreeTime
end VFH2
