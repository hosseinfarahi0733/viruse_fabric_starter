# C11 - Score Preservation Source Gap Audit

## Objective

Determine whether the current repository can derive score preservation for the concrete product update semantics.

Target obligation:

For every y : p.State, productScore (productUpdateState p y) = productScore y.

Equivalent policy-level obligation:

restrictedParamsScoreKeyPreservingUpdateCondition p (productUpdateState p) productScore.

## Verdict

C11 is classified as Outcome B: score-preservation source gap.

The current repository does not contain a theorem that derives score preservation for concrete productUpdateState from meaningful model, update, or domain semantics.

No fundamental assumption is discharged by C11.

No scientific tag is justified.

## Verified audit findings

The audit found many generic score-preservation candidates, but these candidates either assume score preservation, convert score-key preservation to pointwise score preservation, or forward existing policy assumptions.

The audit found no concrete productUpdateState score-preservation candidates.

The concrete product update semantics are: active coordinates are updated to topCoord, inactive coordinates are preserved.

Therefore productUpdateState is not identity-like in general.

The existing theorem productUpdateState_val_eq_of_fixed proves value preservation only under hfixed : ProductFixedSet p x. This does not derive score preservation for arbitrary states and arbitrary productScore.

## Candidate classification

ProductRestrictedParamsScorePreservingPolicyInstantiation.lean:
Classification: DERIVES-GENERIC / ASSUMES.
It derives pointwise score preservation from identity-like update or from score-key preserving condition. It does not derive either condition from productUpdateState semantics.

ProductRestrictedParamsScoreKeyConditionClassification.lean:
Classification: EQUIVALENCE.
It classifies score-key preservation as equivalent to pointwise score preservation. It does not derive score preservation from concrete update semantics.

ProductRestrictedParamsScorePreservingUpdate.lean:
Classification: ASSUMES / CONSEQUENCE.
It uses productScore (productUpdate x) = productScore x as input to derive updated window consequences.

ProductRestrictedParamsScorePreservationDischarge.lean:
Classification: POLICY DISCHARGE FROM ASSUMED POLICY.
It defines restrictedParamsScorePreservingUpdatePolicy as pointwise score preservation and projects consequences from it.

ProductUpdate.lean:
Classification: UPDATE SEMANTICS, NOT SCORE DERIVATION.
It defines productUpdateState and proves active/top and inactive/preservation facts, plus value preservation under ProductFixedSet.

## Scientific interpretation

C11 confirms that A1 remains a fundamental score-preservation assumption.

The project currently proves the restricted proof spine under score-preserving policy routes, but it does not derive score preservation from concrete productUpdateState semantics.

This prevents overclaiming that score preservation has been discharged.

## Assumption impact

Reduced assumptions: none.

Clarified assumptions:
- A1: score preservation remains undischarged.
- A2: ProductFixedSet remains undischarged from C10.
- A3: natural base bounds remain undischarged.

## Recommended next target

C12 should not create wrapper theorems.

The highest-value next path is to define a meaningful score class that is provably insensitive to active-coordinate updates, or to define a domain-specific productScore whose preservation under productUpdateState can be formally proved.

Possible meaningful direction:

If productScore depends only on inactive coordinates, then productUpdateState should preserve it because inactive coordinates are preserved.

This would require a real semantic assumption about productScore, not merely renaming the existing preservation premise.

## Tag policy

No tag is justified.

Reason: no fundamental assumption was discharged.

Last scientific tag remains v17.4.0.
