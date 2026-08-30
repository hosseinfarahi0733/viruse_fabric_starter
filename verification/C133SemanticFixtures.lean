import VFH2.Product.ThreeTimeCausalSemanticRecovery

open VFH2 ThreeTime

example :
    (booleanParitySCM.doPresent false true).past = false := by
  rfl

example :
    (booleanParitySCM.doFuture false true).past = false := by
  rfl

example :
    (booleanParitySCM.doFuture false true).present = false := by
  rfl

example : CandidatePast evenParityEvidence false false false := by
  rfl

example : evenParityEvidence (booleanParitySCM.realize true) := by
  exact booleanParitySCM_realize_satisfies_evenParity true

example : ¬ CandidatePast evenParityEvidence false false true := by
  simp [CandidatePast, evenParityEvidence, evenParity]

example :
    naturalRectangleDefect
      evenParityBooleanConstraint false true false false true = 1 := by
  rfl

example :
    ¬ ChainRepresentable
      (relationOfBooleanConstraint evenParityBooleanConstraint) := by
  exact evenParityBooleanConstraint_not_chainRepresentable

example :
    relationOfBooleanConstraint evenParityBooleanConstraint true false true ↔
      evenParity true false true := by
  exact relationOfEvenParityBooleanConstraint_iff_evenParity true false true

#check downstreamIntervention_preserves_past
#check candidatePast_antitone_of_evidenceRefines
#check exists_strict_recontextualization_without_pastChange
#check relationOfBooleanConstraint_chainRepresentable_iff_all_defects_zero
#check relationOfEvenParityBooleanConstraint_iff_evenParity
