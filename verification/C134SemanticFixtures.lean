import VFH2.Product.ThreeTimeInterventionalConstraintCausality

open VFH2 ThreeTime

example :
    (booleanParitySCM.doPresent false false).future = false := by
  rfl

example :
    (booleanParitySCM.doPresent false true).future = true := by
  rfl

example :
    evenParity false false false := by
  exact
    (booleanParitySCM_evenParity_characterizesFutureLaw
      false false false).2 rfl

example :
    relationOfBooleanConstraint evenParityBooleanConstraint
      false true true := by
  exact
    (booleanParitySCM_executableParity_characterizesFutureLaw
      false true true).2 rfl

example :
    PresentCausalContrastAt booleanParitySCM false false true := by
  exact
    (booleanParitySCM_presentCausalContrastAt_iff_present_ne
      false false true).2 (by decide)

example :
    ¬ PresentCausalContrastAt booleanParitySCM false false false := by
  intro hcontrast
  exact
    ((booleanParitySCM_presentCausalContrastAt_iff_present_ne
      false false false).1 hcontrast) rfl

example :
    PresentHasCausalEffectOnFuture booleanParitySCM := by
  exact booleanParitySCM_presentHasCausalEffectOnFuture

example :
    (booleanParitySCM.doPresent false false).past =
      (booleanParitySCM.doPresent false true).past := by
  rfl

#check ConstraintCharacterizesFutureLaw
#check booleanParitySCM_evenParity_characterizesFutureLaw
#check booleanParitySCM_executableParity_characterizesFutureLaw
#check booleanParitySCM_presentCausalContrastAt_iff_present_ne
#check booleanParitySCM_presentHasCausalEffectOnFuture
#check evenParity_not_chainRepresentable
