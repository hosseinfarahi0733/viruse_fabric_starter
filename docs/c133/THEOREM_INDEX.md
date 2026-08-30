# C133 theorem index

Source: `lean/VFH2/Product/ThreeTimeCausalSemanticRecovery.lean`

## Structural causal semantics

- `realize_past`
- `doPresent_past`
- `doFuture_past`
- `downstreamIntervention_preserves_past`
- `doFuture_preserves_generated_present`

## Observer recontextualization

- `candidatePast_antitone_of_evidenceRefines`
- `evenParityEvidence_refines_unconstrained`
- `booleanParitySCM_realize_satisfies_evenParity`
- `evenParityEvidence_strict_candidatePast_refinement`
- `evenParityEvidence_retains_actualPast`
- `exists_strict_recontextualization_without_pastChange`

## Constraint geometry

- `naturalRectangleDefect_eq_zero_iff`
- `relationOfBooleanConstraint_chainRepresentable_iff_all_defects_zero`
- `relationOfBooleanConstraint_chainRepresentable_iff_all_weightedDefects_zero`
- `evenParityBooleanConstraint_defect_witness`
- `evenParityBooleanConstraint_not_chainRepresentable`
- `relationOfEvenParityBooleanConstraint_iff_evenParity`

The explicit parity bridge proves that the SCM evidence relation and the
executable defect relation are the same geometry; they are not independent
witnesses. The first observer theorem is generic; the strict result is a finite witness.
The defect factorization theorem is generic over the state type but requires a
Boolean-decidable constraint representation. None of these declarations are
aliases of the final proposition they prove.
