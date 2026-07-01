import VFH2.RestrictedBridge.Scaffold

/-!
# VF-H2 Restricted Bridge Proof Basics

This file adds the first small machine-checked Lean lemmas for the restricted
bridge formalization scaffold.

Boundary:
- These are basic scaffold lemmas only.
- This is not yet a machine-checked proof of `RBRIDGE-VF-H2-001-R`.
- This is not a proof of the full Viruse Fabric theory.
- This is not a proof of unrestricted `TTP-VF-H2-004`.
- This is not empirical validation.
- This is not biological validation.
-/

namespace VFH2
namespace RestrictedBridge

theorem expectedWidth_eq (p : RestrictedParams) :
    expectedWidth p = 3 * p.d := by
  rfl

theorem hasExpectedWidth_iff (p : RestrictedParams) (x : State) :
    hasExpectedWidth p x ↔ x.length = expectedWidth p := by
  rfl

theorem hasLnBounds_iff (p : RestrictedParams) (x : State) :
    hasLnBounds p x ↔ ∀ a ∈ x, a ≤ p.n := by
  rfl

theorem inRestrictedStateSpace_intro
    {p : RestrictedParams} {x : State}
    (hw : hasExpectedWidth p x)
    (hb : hasLnBounds p x) :
    inRestrictedStateSpace p x := by
  exact And.intro hw hb

theorem inRestrictedStateSpace_width
    {p : RestrictedParams} {x : State}
    (h : inRestrictedStateSpace p x) :
    hasExpectedWidth p x := by
  exact h.1

theorem inRestrictedStateSpace_bounds
    {p : RestrictedParams} {x : State}
    (h : inRestrictedStateSpace p x) :
    hasLnBounds p x := by
  exact h.2

theorem ledgerVR_nil :
    ledgerVR ([] : State) = 0 := by
  rfl

theorem ledgerVR_singleton (a : Nat) :
    ledgerVR [a] = a := by
  simp [ledgerVR]

theorem inFixedSetR_iff (p : RestrictedParams) (x : State) :
    inFixedSetR p x ↔ ∀ i ∈ p.active, x.getD i 0 = p.n := by
  rfl

theorem restrictedBridgeTheoremTarget_nonfixed_part
    {p : RestrictedParams} {x : State} {effect : Int}
    (h : restrictedBridgeTheoremTarget p x effect) :
    nonfixedPositiveEffectTarget p x effect := by
  exact h.1

theorem restrictedBridgeTheoremTarget_fixed_part
    {p : RestrictedParams} {x : State} {effect : Int}
    (h : restrictedBridgeTheoremTarget p x effect) :
    fixedZeroEffectTarget p x effect := by
  exact h.2

theorem currentBoundary_restricted_scaffold_true :
    currentBoundary.restrictedFiniteScaffold = true := by
  rfl

theorem currentBoundary_full_theory_false :
    currentBoundary.fullTheoryProved = false := by
  rfl

theorem currentBoundary_unrestricted_ttp_false :
    currentBoundary.unrestrictedTTPProved = false := by
  rfl

theorem currentBoundary_empirical_false :
    currentBoundary.empiricalValidation = false := by
  rfl

theorem currentBoundary_biological_false :
    currentBoundary.biologicalValidation = false := by
  rfl

end RestrictedBridge
end VFH2
