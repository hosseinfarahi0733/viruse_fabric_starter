import VFH2.Product.ThreeTimeOperationalObservers

/-!
# C121: Formal Falsifiability Contract

A mathematically nontrivial prediction must have both a supporting outcome and
a falsifying outcome, and each concrete observation must be decidably
classified.  This supplies an explicit interface for an empirical bridge.

It does not supply experimental data or prove that a physical system is mapped
to this formal model.  Those remain external scientific obligations.
-/

namespace VFH2
namespace ThreeTime

/-- A decidable, nontrivial prediction over an observation type. -/
structure FalsifiablePrediction (Observation : Type) where
  accepts : Observation -> Prop
  decideAccepts : forall observation, Decidable (accepts observation)
  supportiveCase : exists observation, accepts observation
  falsifyingCase : exists observation, ¬ accepts observation

/-- The observation supports the prediction. -/
def Supports
    {Observation : Type}
    (prediction : FalsifiablePrediction Observation)
    (observation : Observation) : Prop :=
  prediction.accepts observation

/-- The observation falsifies the prediction. -/
def Falsifies
    {Observation : Type}
    (prediction : FalsifiablePrediction Observation)
    (observation : Observation) : Prop :=
  ¬ prediction.accepts observation

/-- Every observation is classified as supporting or falsifying. -/
theorem observation_supports_or_falsifies
    {Observation : Type}
    (prediction : FalsifiablePrediction Observation)
    (observation : Observation) :
    Supports prediction observation \/
      Falsifies prediction observation := by
  match prediction.decideAccepts observation with
  | isTrue haccepts => exact Or.inl haccepts
  | isFalse hrejected => exact Or.inr hrejected

/-- Every falsifiable prediction has an explicit possible falsifier. -/
theorem falsifiablePrediction_has_falsifier
    {Observation : Type}
    (prediction : FalsifiablePrediction Observation) :
    exists observation, Falsifies prediction observation := by
  exact prediction.falsifyingCase

/-- An external measurement map plus a formal prediction. -/
structure EmpiricalBridge (State Observation : Type) where
  measure : State -> Observation
  prediction : FalsifiablePrediction Observation

/-- A measured state falsifies the prediction attached to the bridge. -/
def FalsifiedAt
    {State Observation : Type}
    (bridge : EmpiricalBridge State Observation)
    (state : State) : Prop :=
  Falsifies bridge.prediction (bridge.measure state)

/-- Every measured state is decidably supporting or falsifying. -/
theorem empiricalBridge_state_classified
    {State Observation : Type}
    (bridge : EmpiricalBridge State Observation)
    (state : State) :
    Supports bridge.prediction (bridge.measure state) \/
      FalsifiedAt bridge state := by
  exact
    observation_supports_or_falsifies
      bridge.prediction (bridge.measure state)

/-- A concrete nontrivial Boolean prediction used by the completion certificate. -/
def boolTruePrediction : FalsifiablePrediction Bool where
  accepts := fun observation => observation = true
  decideAccepts := fun observation => inferInstance
  supportiveCase := ⟨true, rfl⟩
  falsifyingCase := ⟨false, by decide⟩

theorem boolTruePrediction_support_and_falsifier :
    Supports boolTruePrediction true /\
      Falsifies boolTruePrediction false := by
  simp [Supports, Falsifies, boolTruePrediction]

/-- Recorded outcomes of one operational test of the middle rectangle law. -/
structure RectangleTrial where
  firstAdmissible : Bool
  secondAdmissible : Bool
  mixedAdmissible : Bool

/-- A trial supports chain reduction when two accepted corners force the mix. -/
def rectangleLawAccepts (trial : RectangleTrial) : Prop :=
  trial.firstAdmissible = true ->
    trial.secondAdmissible = true ->
      trial.mixedAdmissible = true

/-- The rectangle law as a decidable and nontrivial operational prediction. -/
def rectangleLawPrediction : FalsifiablePrediction RectangleTrial where
  accepts := rectangleLawAccepts
  decideAccepts := by
    intro trial
    unfold rectangleLawAccepts
    infer_instance
  supportiveCase := by
    refine ⟨⟨false, false, false⟩, ?_⟩
    intro hfirst
    simp at hfirst
  falsifyingCase := by
    refine ⟨⟨true, true, false⟩, ?_⟩
    intro haccepts
    have hmixed := haccepts rfl rfl
    simp at hmixed

/-- The Boolean parity rectangle witness encoded as an operational trial. -/
def evenParityRectangleTrial : RectangleTrial where
  firstAdmissible := true
  secondAdmissible := true
  mixedAdmissible := false

/-- The recorded bits exactly match the three parity propositions used in C117. -/
theorem evenParityRectangleTrial_matches_constraint :
    (evenParityRectangleTrial.firstAdmissible = true <->
      evenParity false false false) /\
    (evenParityRectangleTrial.secondAdmissible = true <->
      evenParity true false true) /\
    (evenParityRectangleTrial.mixedAdmissible = true <->
      evenParity false false true) := by
  simp [evenParityRectangleTrial, evenParity]

/-- The concrete parity observation falsifies adjacent-chain rectangle closure. -/
theorem evenParityRectangleTrial_falsifies_chainPrediction :
    Falsifies rectangleLawPrediction evenParityRectangleTrial := by
  intro haccepts
  have hmixed := haccepts rfl rfl
  simp [evenParityRectangleTrial] at hmixed

end ThreeTime
end VFH2
