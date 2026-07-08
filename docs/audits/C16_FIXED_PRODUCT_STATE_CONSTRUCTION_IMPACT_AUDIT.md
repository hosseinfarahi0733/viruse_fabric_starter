# C16 - Fixed Product State Construction Impact Audit

## Objective

Record the scientific impact of C16 fixed-state construction.

C16 constructs a canonical product state and proves ProductFixedSet for that constructed state.

## Commit

2f9aa9a - Construct fixed product state for proof-spine route

## New definitions and theorems

- ProductRestrictedParamsFixedStateConstruction.fixedProductState
- ProductRestrictedParamsFixedStateConstruction.fixedProductState_ProductFixedSet
- ProductRestrictedParamsFixedStateConstruction.productUpdateState_fixedProductState_val_eq
- ProductRestrictedParamsFixedStateConstruction.restrictedParams_constantScore_fixedProductState_to_currentBestMainTheorem

## Scientific result

Before C16, the current proof-spine routes still required an explicit assumption:
- hFixedSet : ProductFixedSet p x

After C16, the project has a concrete constructed state:
- fixedProductState p

This state is defined by assigning p.topCoord at every product coordinate.

Since p.topCoord.val = p.n, the constructed state satisfies ProductFixedSet p (fixedProductState p).

C16 then connects this constructed fixed state to the C15 constant-score proof-spine route.

Therefore, for the constructed fixed state and constant scores, the proof-spine theorem no longer requires explicit assumptions for:
- ProductFixedSet
- active-insensitive score semantics
- pointwise natural base bounds

It still requires thresholdLo <= c and c <= thresholdHi for the constant score value.

## Assumption impact

A1 - Score Preservation
Status: partially discharged.
For constant scores, inactive-insensitive score semantics is derived directly.

A2 - ProductFixedSet
Status: partially discharged.
ProductFixedSet is derived for fixedProductState p.
ProductFixedSet remains undischarged for arbitrary x.

A3 - Natural base bounds
Status: partially discharged.
For constant scores, boundedness follows from thresholdLo <= c and c <= thresholdHi.
Natural bounds remain undischarged for arbitrary productScore.

## Correct claims

- C16 constructs a canonical fixed product state.
- C16 proves ProductFixedSet for the constructed fixed state.
- C16 provides a proof-spine route for fixedProductState and constantProductScore without explicit hFixedSet, hScoreInactive, hBaseLowerNatural, or hBaseUpperNatural assumptions.

## Forbidden claims

- C16 does not prove ProductFixedSet p x for arbitrary x.
- C16 does not prove arbitrary scores are bounded.
- C16 does not prove VF-H2 unconditionally.
- C16 does not remove the threshold condition thresholdLo <= c <= thresholdHi for constant scores.

## Current strongest concrete route

For p : ProductRestrictedParams, c thresholdLo thresholdHi : Int, if thresholdLo <= thresholdHi, thresholdLo <= c, and c <= thresholdHi, then the restricted proof-spine target holds for:
- x = fixedProductState p
- productUpdate = productUpdateState p
- productScore = constantProductScore p c
- fixed = ProductFixedSet p (fixedProductState p)

## Tag assessment

A scientific tag is justified after this audit.

Recommended tag: v17.7.0

Reason: C16 partially discharges A2 by constructing a fixed product state and proving ProductFixedSet for it, then routes it into the proof spine.
