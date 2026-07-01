# Restricted Bridge Lean Update Map Scaffold

## Scope

This artifact adds a scaffold-level Lean 4 update map for the restricted finite bridge theorem.

## What is now machine-checked

Lean now checks:

- `isActiveIndex`
- `updateCoordinateR`
- `updateCoordinateR_active`
- `updateCoordinateR_inactive`
- `updateStateR`
- `updateStateR_length`
- `updateStateR_preserves_expected_width`
- `ledgerEffectR`
- `ledgerEffectR_def`
- target split lemmas for `restrictedBridgeUpdateMapTarget`

## Boundary

This is not yet a machine-checked proof of `RBRIDGE-VF-H2-001-R`.

It does not prove the full Viruse Fabric theory.

It does not prove unrestricted `TTP-VF-H2-004`.

It is not empirical validation.

It is not biological validation.

It does not make the manuscript submission-ready.

## Next formalization step

Prove boundedness and fixed-set behavior for the scaffold update map:

- active fixed coordinates remain at top
- inactive coordinates remain unchanged
- fixed-set states have zero ledger effect
- non-fixed states have positive ledger effect under active-coordinate jump-to-top update

The later dependent-type version should replace this list-level scaffold with:

`P_R(n,d)=L_n^(T_3 × I_d)`
