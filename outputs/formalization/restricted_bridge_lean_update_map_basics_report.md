# Restricted Bridge Lean Update Map Basics

## Scope

This artifact adds small Lean 4 lemmas about the scaffold-level restricted update map.

## What is now machine-checked

Lean now checks:

- `updateStateAuxR_nil`
- `updateStateAuxR_cons`
- `updateStateR_nil`
- `ledgerEffectR_nil`
- `updateCoordinateR_active_top`
- `updateCoordinateR_inactive_top`
- `updateStateAuxR_no_active`
- `updateStateR_no_active`
- `ledgerEffectR_no_active`
- `inFixedSetR_no_active`
- `updateFixedZeroEffectTarget_no_active`
- `updateNonfixedPositiveEffectTarget_no_active`
- `restrictedBridgeUpdateMapTarget_no_active`

## Boundary

This is not yet a machine-checked proof of `RBRIDGE-VF-H2-001-R`.

The proved no-active case is degenerate and does not replace the intended nonempty-active restricted theorem.

It does not prove the full Viruse Fabric theory.

It does not prove unrestricted `TTP-VF-H2-004`.

It is not empirical validation.

It is not biological validation.

It does not make the manuscript submission-ready.

## Next formalization step

Move from the degenerate no-active case to the intended nonempty-active jump-to-top scaffold:

- prove active-coordinate fixed behavior
- prove fixed-set states are unchanged by `updateStateR`
- prove fixed-set states have zero `ledgerEffectR`
- then approach nonfixed positive effect under nonempty active coordinates
