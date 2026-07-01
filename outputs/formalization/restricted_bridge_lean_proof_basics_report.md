# Restricted Bridge Lean Proof Basics

## Scope

This artifact adds the first small Lean 4 lemmas for the restricted bridge formalization scaffold.

## What is now machine-checked

The following scaffold-level facts are checked by Lean:

- `expectedWidth_eq`
- `hasExpectedWidth_iff`
- `hasLnBounds_iff`
- `inRestrictedStateSpace_intro`
- `inRestrictedStateSpace_width`
- `inRestrictedStateSpace_bounds`
- `ledgerVR_nil`
- `ledgerVR_singleton`
- `inFixedSetR_iff`
- target-splitting lemmas for `restrictedBridgeTheoremTarget`
- boundary-status lemmas showing full-theory, unrestricted-TTP, empirical, and biological claims remain false

## Boundary

This is not yet a machine-checked proof of `RBRIDGE-VF-H2-001-R`.

It does not prove the full Viruse Fabric theory.

It does not prove unrestricted `TTP-VF-H2-004`.

It is not empirical validation.

It is not biological validation.

It does not make the manuscript submission-ready.

## Next formalization step

Define a bounded update map `f_R` and prove its basic properties:

- maps restricted states to restricted states
- preserves or increases coordinates
- fixed-set states have zero ledger effect
- non-fixed states have positive ledger effect
