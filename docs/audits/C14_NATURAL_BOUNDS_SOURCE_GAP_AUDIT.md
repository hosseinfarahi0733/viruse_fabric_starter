# C14 - Natural Bounds Source Gap Audit

## Objective

Determine whether the current repository can derive the natural base bounds used by the current best main theorem.

Target obligations:
- thresholdLo <= productScore x
- productScore x <= thresholdHi

## Verdict

C14 is classified as Outcome B: natural base bounds source gap.

The current repository does not contain a theorem that derives the natural base bounds from meaningful admissibility, score construction, threshold construction, or domain semantics.

No fundamental assumption is discharged by C14.

No scientific tag is justified.

## Verified audit findings

The current best main theorem still assumes:
- hBaseLowerNatural : thresholdLo <= productScore x
- hBaseUpperNatural : productScore x <= thresholdHi

The theorem restrictedParams_naturalBaseScoreWindow_of_components does not derive these bounds. It takes hBaseLowerNatural and hBaseUpperNatural as inputs and packages them into restrictedParamsBaseScoreWindow.

The definition restrictedParamsBaseScoreWindow is a bridge/window representation of the same two inequalities under genericBridgeTarget.

The NaturalUpdatedBounds route transfers base bounds to updated bounds under score preservation, but it still assumes the base bounds.

The candidate search found many bridge, monotonicity, transport, projection, and score-window theorems, but no theorem that derives the base natural bounds from domain semantics.

The admissibility/window definition search found score-window and effect-bound structures, but no independent semantic admissibility condition that produces the natural base bounds.

## Candidate classification

ProductRestrictedParamsScoreWindow.lean
Classification: PACKAGES / PROJECTS bounds.
It does not derive thresholdLo <= productScore x or productScore x <= thresholdHi.

ProductRestrictedParamsNaturalUpdatedBounds.lean
Classification: TRANSFERS base bounds to updated bounds.
It assumes the natural base bounds and uses score preservation to obtain updated bounds.

Bridge, transport, monotonicity, and threshold-conditioned files
Classification: TRANSPORTS / RELAXES / PROJECTS bounds.
They do not provide a semantic source for the base score window.

## Assumption impact

A1 - Score Preservation
Status: partially discharged by v17.5.0 for concrete productUpdateState under active-insensitive score semantics.

A2 - ProductFixedSet
Status: still undischarged.

A3 - Natural base bounds
Status: still undischarged.

## Scientific interpretation

C14 confirms that the current best theorem remains conditional on the natural base score interval.

The project should not claim that natural bounds are derived from the model.

A future meaningful discharge would require a real domain-level source, such as a score construction whose range is provably contained in the threshold interval, or an admissible-state semantics that implies the two inequalities.

Simply defining a predicate that contains the same two inequalities would not reduce assumptions.

## Recommended next target

C15 should either:
1. define a meaningful bounded score construction and derive natural bounds from it, or
2. keep A3 explicit and return to A2 ProductFixedSet, which remains the other major blocker.

No wrapper theorem should be added merely to rename the natural bounds.

## Tag policy

No tag is justified.

Reason: C14 records a gap and does not discharge a fundamental assumption.

Last scientific tag remains v17.5.0.
