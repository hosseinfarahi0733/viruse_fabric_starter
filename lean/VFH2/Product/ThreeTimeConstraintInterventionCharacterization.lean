import VFH2.Product.ThreeTimeInterventionalConstraintCausality

/-!
# C135: Constraint-Defined Intervention Characterization

This module characterizes present-to-future intervention contrasts whenever a
ternary constraint is exactly the graph of a deterministic three-time model's
future law.  It treats both the fixed-past and global existential forms.

Claim boundary: these are general semantic equivalences inside the abstract
deterministic SCM interface.  They do not identify a structural law from
observations and do not establish empirical, biological, or physical causation.
-/

namespace VFH2
namespace ThreeTime

/--
Under an exact graph characterization of the future law, an intervention
contrast is equivalent to two constraint-compatible, distinct futures.
-/
theorem constraintCharacterizesFutureLaw_presentCausalContrastAt_iff
    (model : DeterministicTriTemporalSCM)
    (constraint : model.Past → model.Present → model.Future → Prop)
    (hLaw : ConstraintCharacterizesFutureLaw model constraint)
    (past : model.Past)
    (presentOne presentTwo : model.Present) :
    PresentCausalContrastAt model past presentOne presentTwo ↔
      ∃ futureOne futureTwo : model.Future,
        constraint past presentOne futureOne ∧
        constraint past presentTwo futureTwo ∧
        futureOne ≠ futureTwo := by
  constructor
  · intro hContrast
    refine ⟨model.futureLaw past presentOne,
      model.futureLaw past presentTwo,
      (hLaw past presentOne _).2 rfl,
      (hLaw past presentTwo _).2 rfl, ?_⟩
    simpa [PresentCausalContrastAt,
      DeterministicTriTemporalSCM.doPresent] using hContrast
  · rintro ⟨futureOne, futureTwo, hOne, hTwo, hNe⟩
    have hOneEq : futureOne = model.futureLaw past presentOne :=
      (hLaw past presentOne futureOne).1 hOne
    have hTwoEq : futureTwo = model.futureLaw past presentTwo :=
      (hLaw past presentTwo futureTwo).1 hTwo
    simp only [PresentCausalContrastAt,
      DeterministicTriTemporalSCM.doPresent]
    intro hOutputsEq
    apply hNe
    calc
      futureOne = model.futureLaw past presentOne := hOneEq
      _ = model.futureLaw past presentTwo := hOutputsEq
      _ = futureTwo := hTwoEq.symm

/--
The model has some present-to-future causal contrast exactly when its graph
constraint contains two distinct futures at a shared past.
-/
theorem constraintCharacterizesFutureLaw_presentHasCausalEffectOnFuture_iff
    (model : DeterministicTriTemporalSCM)
    (constraint : model.Past → model.Present → model.Future → Prop)
    (hLaw : ConstraintCharacterizesFutureLaw model constraint) :
    PresentHasCausalEffectOnFuture model ↔
      ∃ (past : model.Past)
        (presentOne presentTwo : model.Present)
        (futureOne futureTwo : model.Future),
        constraint past presentOne futureOne ∧
        constraint past presentTwo futureTwo ∧
        futureOne ≠ futureTwo := by
  constructor
  · rintro ⟨past, presentOne, presentTwo, hContrast⟩
    rcases
      (constraintCharacterizesFutureLaw_presentCausalContrastAt_iff
        model constraint hLaw past presentOne presentTwo).1 hContrast with
      ⟨futureOne, futureTwo, hOne, hTwo, hNe⟩
    exact ⟨past, presentOne, presentTwo,
      futureOne, futureTwo, hOne, hTwo, hNe⟩
  · rintro ⟨past, presentOne, presentTwo,
      futureOne, futureTwo, hOne, hTwo, hNe⟩
    exact ⟨past, presentOne, presentTwo,
      (constraintCharacterizesFutureLaw_presentCausalContrastAt_iff
        model constraint hLaw past presentOne presentTwo).2
        ⟨futureOne, futureTwo, hOne, hTwo, hNe⟩⟩

end ThreeTime
end VFH2
