import VFH2.Product.ThreeTimeObservationalNonidentifiability

open VFH2 ThreeTime

example (past : Bool) :
    (pastDrivenBooleanSCM.realize past).past =
        (presentDrivenBooleanSCM.realize past).past ∧
      (pastDrivenBooleanSCM.realize past).present =
        (presentDrivenBooleanSCM.realize past).present ∧
      (pastDrivenBooleanSCM.realize past).future =
        (presentDrivenBooleanSCM.realize past).future := by
  exact
    pastDriven_presentDriven_same_completeObservations_different_presentCausality.1
      past

example :
    (pastDrivenBooleanSCM.realize false).future = false ∧
      (presentDrivenBooleanSCM.realize false).future = false := by
  exact ⟨rfl, rfl⟩

example :
    (pastDrivenBooleanSCM.realize true).future = true ∧
      (presentDrivenBooleanSCM.realize true).future = true := by
  exact ⟨rfl, rfl⟩

example : ¬ PresentHasCausalEffectOnFuture pastDrivenBooleanSCM := by
  exact
    pastDriven_presentDriven_same_completeObservations_different_presentCausality.2.1

example : PresentHasCausalEffectOnFuture presentDrivenBooleanSCM := by
  exact
    pastDriven_presentDriven_same_completeObservations_different_presentCausality.2.2

example :
    PresentCausalContrastAt presentDrivenBooleanSCM false false true := by
  change false ≠ true
  intro h
  cases h

example :
    ¬ PresentCausalContrastAt pastDrivenBooleanSCM false false true := by
  intro hContrast
  apply hContrast
  rfl

example (past presentOne presentTwo : Bool) :
    PresentCausalContrastAt presentDrivenBooleanSCM
        past presentOne presentTwo ↔
      ∃ futureOne futureTwo : Bool,
        (fun _ present future : Bool => future = present)
            past presentOne futureOne ∧
          (fun _ present future : Bool => future = present)
            past presentTwo futureTwo ∧
          futureOne ≠ futureTwo := by
  exact
    constraintCharacterizesFutureLaw_presentCausalContrastAt_iff
      presentDrivenBooleanSCM
      (fun _ present future : Bool => future = present)
      presentDrivenBooleanSCM_chain_with_presentCausalEffect.1
      past presentOne presentTwo

#check constraintCharacterizesFutureLaw_presentCausalContrastAt_iff
#check constraintCharacterizesFutureLaw_presentHasCausalEffectOnFuture_iff
#check pastDrivenBooleanSCM_nonChain_without_presentCausalEffect
#check presentDrivenBooleanSCM_chain_with_presentCausalEffect
#check pastDriven_presentDriven_same_completeObservations_different_presentCausality
