# Restricted Bridge Lean Formalization Scaffold

## Scope

This artifact starts a Lean 4 scaffold for the restricted finite bridge theorem:

`RBRIDGE-VF-H2-001-R`

## Boundary

This is not a completed machine-checked proof.

It does not prove the full Viruse Fabric theory.

It does not prove unrestricted `TTP-VF-H2-004`.

It is not empirical validation.

It is not biological validation.

It does not make the manuscript submission-ready.

## Current Lean content

The scaffold defines:

- `RestrictedParams`
- `State`
- `expectedWidth`
- `hasExpectedWidth`
- `hasLnBounds`
- `inRestrictedStateSpace`
- `ledgerVR`
- `inFixedSetR`
- `nonfixedPositiveEffectTarget`
- `fixedZeroEffectTarget`
- `restrictedBridgeTheoremTarget`

## Next formalization step

Replace list-level guards with dependent finite types:

`P_R(n,d)=L_n^(T_3 × I_d)`

Then define a bounded update map `f_R` and prove:

`x ∉ F_R => ledger_effect_size_R(x)>0`

and:

`x ∈ F_R => ledger_effect_size_R(x)=0`
