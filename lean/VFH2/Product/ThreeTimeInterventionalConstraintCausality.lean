import VFH2.Product.ThreeTimeCausalSemanticRecovery

/-!
# C134: Interventional Causality Under a Fixed Three-Time Constraint

This module gives an exact semantic connection between the executable Boolean
constraint recovered in C133 and a deterministic intervention model.  Both
the propositional and executable parity constraints are proved to be exactly
the graph of the Boolean parity SCM's structural future law.  A separate
theorem characterizes its fixed-past present-to-future intervention contrasts.

The imported non-chain geometry theorem and the intervention theorem remain
logically separate: non-chain geometry is not used to infer causality.

Claim boundary: this is a theorem about one abstract deterministic finite SCM.
It does not establish causal discovery from data, biological or physical
causation, retrocausality, three physical time dimensions, empirical validity,
or a calibrated real-world mapping.
-/

namespace VFH2
namespace ThreeTime

/--
A present intervention has a causal contrast at a fixed past exactly when the
two recomputed future outcomes differ.
-/
def PresentCausalContrastAt
    (model : DeterministicTriTemporalSCM)
    (past : model.Past)
    (presentOne presentTwo : model.Present) : Prop :=
  (model.doPresent past presentOne).future ≠
    (model.doPresent past presentTwo).future

/-- There exists a fixed-past present intervention that changes the future. -/
def PresentHasCausalEffectOnFuture
    (model : DeterministicTriTemporalSCM) : Prop :=
  ∃ past presentOne presentTwo,
    PresentCausalContrastAt model past presentOne presentTwo

/--
A fixed ternary constraint characterizes a model's structural future law when
it accepts exactly one future at every past/present pair: the generated one.
-/
def ConstraintCharacterizesFutureLaw
    (model : DeterministicTriTemporalSCM)
    (constraint :
      model.Past → model.Present → model.Future → Prop) : Prop :=
  ∀ past present future,
    constraint past present future ↔
      future = model.futureLaw past present

/-- The propositional parity geometry is exactly the graph of the SCM law. -/
theorem booleanParitySCM_evenParity_characterizesFutureLaw :
    ConstraintCharacterizesFutureLaw booleanParitySCM evenParity := by
  intro past present future
  cases past <;> cases present <;> rfl

/--
C133's executable parity relation is exactly the graph of the same SCM law.
This is a direct executable-constraint-to-intervention-semantics transport.
-/
theorem booleanParitySCM_executableParity_characterizesFutureLaw :
    ConstraintCharacterizesFutureLaw booleanParitySCM
      (relationOfBooleanConstraint evenParityBooleanConstraint) := by
  intro past present future
  cases past <;> cases present <;> cases future <;>
    unfold relationOfBooleanConstraint evenParityBooleanConstraint
      booleanParitySCM <;>
    decide

/--
For the Boolean parity SCM, a fixed-past present contrast occurs exactly when
the two intervened present values are distinct.
-/
theorem booleanParitySCM_presentCausalContrastAt_iff_present_ne
    (past presentOne presentTwo : Bool) :
    PresentCausalContrastAt booleanParitySCM past presentOne presentTwo ↔
      presentOne ≠ presentTwo := by
  cases past <;> cases presentOne <;> cases presentTwo <;>
    unfold PresentCausalContrastAt
      DeterministicTriTemporalSCM.doPresent booleanParitySCM <;>
    decide

/-- The Boolean parity SCM has a concrete present-to-future causal effect. -/
theorem booleanParitySCM_presentHasCausalEffectOnFuture :
    PresentHasCausalEffectOnFuture booleanParitySCM := by
  exact ⟨
    false,
    false,
    true,
    (booleanParitySCM_presentCausalContrastAt_iff_present_ne
      false false true).2 (by decide)
  ⟩

end ThreeTime
end VFH2
