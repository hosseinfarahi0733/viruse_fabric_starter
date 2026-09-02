import VFH2.Product.ThreeTimeConstraintInterventionCharacterization

/-!
# C136: Independence of Constraint Geometry and Present Causality

This module gives two explicit Boolean countermodels.  A past-driven future law
has non-chain graph geometry but no present-to-future causal effect.  A
present-driven future law has chain-representable graph geometry and does have
a present-to-future causal effect.

Together the examples show that failure of adjacent-chain factorization is
neither sufficient nor necessary for present intervention causality.

Claim boundary: these are finite logical countermodels inside the abstract SCM
semantics.  They are not causal discovery results and make no empirical,
biological, or physical claim.
-/

namespace VFH2
namespace ThreeTime

/-- A Boolean SCM whose observed present and structural future copy the past. -/
def pastDrivenBooleanSCM : DeterministicTriTemporalSCM where
  Past := Bool
  Present := Bool
  Future := Bool
  presentLaw := fun past => past
  futureLaw := fun past _ => past

/--
A Boolean SCM whose observed present copies the past while its structural
future copies the intervened present.
-/
def presentDrivenBooleanSCM : DeterministicTriTemporalSCM where
  Past := Bool
  Present := Bool
  Future := Bool
  presentLaw := fun past => past
  futureLaw := fun _ present => present

/--
The past-driven graph is non-chain, yet changing the present cannot change the
future at any fixed past.
-/
theorem pastDrivenBooleanSCM_nonChain_without_presentCausalEffect :
    ConstraintCharacterizesFutureLaw pastDrivenBooleanSCM
        (fun past _ future => future = past) ∧
      ¬ ChainRepresentable (fun past _ future : Bool => future = past) ∧
      ¬ PresentHasCausalEffectOnFuture pastDrivenBooleanSCM := by
  refine ⟨?_, ?_, ?_⟩
  · intro past present future
    rfl
  · intro hChain
    have hRectangle := chainRepresentable_middleRectangleClosed hChain
    have hMixed :
        (fun past _ future : Bool => future = past) false false true :=
      hRectangle false true false false true rfl rfl
    cases hMixed
  · rintro ⟨past, presentOne, presentTwo, hContrast⟩
    apply hContrast
    rfl

/--
The present-driven graph is chain-representable and changing the present has a
concrete future contrast at a fixed past.
-/
theorem presentDrivenBooleanSCM_chain_with_presentCausalEffect :
    ConstraintCharacterizesFutureLaw presentDrivenBooleanSCM
        (fun _ present future => future = present) ∧
      ChainRepresentable (fun _ present future : Bool => future = present) ∧
      PresentHasCausalEffectOnFuture presentDrivenBooleanSCM := by
  refine ⟨?_, ?_, ?_⟩
  · intro past present future
    rfl
  · refine ⟨fun _ _ => True, fun present future => future = present, ?_⟩
    intro past present future
    constructor
    · intro hFuture
      exact ⟨True.intro, hFuture⟩
    · intro hFactors
      exact hFactors.2
  · refine ⟨false, false, true, ?_⟩
    change false ≠ true
    intro h
    cases h

end ThreeTime
end VFH2
