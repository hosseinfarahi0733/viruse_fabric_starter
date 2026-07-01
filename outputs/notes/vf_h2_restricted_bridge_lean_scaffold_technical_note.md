# VF-H2 Restricted Bridge Lean Scaffold Technical Note

Status: boundary-aware technical note
Repository checkpoint: HEAD = fbc9ba0
Last tagged stable domain checkpoint: v9.11.0 = 6380b4e
Earlier restricted bridge artifact tag: v9.8.0 = 6773907
Lean build status: passed with 22 jobs at HEAD = fbc9ba0

## Purpose
This note records the current machine-checked Lean scaffold for the restricted VF-H2 bridge theorem.

Canonical theorem alias: RBRIDGE_VF_H2_001_R_Lean_scaffold
Well-formed-params theorem: RBRIDGE_VF_H2_001_R_Lean_scaffold_wellFormedParams

This is restricted, finite, list-backed, and scaffold-level.
It is not a proof of the full Viruse Fabric theory.
It is not a proof of unrestricted TTP-VF-H2-004.

## Main Proved Dichotomy
Over the well-formed restricted domain, Lean proves:
- fixed-set states have zero ledger effect
- nonfixed states have positive ledger effect

The theorem shape is:
wp : WellFormedRestrictedParams
inRestrictedStateSpace wp.params x
inFixedSetR wp.params x -> ledgerEffectR wp.params x = 0
not inFixedSetR wp.params x -> 0 < ledgerEffectR wp.params x

## What Was Proved
1. fixed-set zero-effect path
2. active-index soundness
3. nonfixed active witness
4. witness below top under bounds
5. active coordinate increase
6. positive ledger effect for nonfixed states
7. final restricted bridge scaffold theorem
8. active-range / active-width equivalence
9. counterexample proving active-width is not derivable from raw RestrictedParams
10. well-formed parameter wrapper
11. clean build after warning cleanup

## Why Active-Width Is Necessary
Raw RestrictedParams does not constrain active.
Lean proves not_forall_activeIndicesWithinWidth.
Counterexample: d = 1, expectedWidth = 3, active = [3].
For a state of length 3, valid indices are 0, 1, and 2. Index 3 is out of range.

## Boundaries
The result is restricted, finite, list-backed, scaffold-level, machine-checked, and over a well-formed domain.
The result is not full VF-H2, not unrestricted TTP-VF-H2-004, not empirical validation, not biological validation, and not dependent typed formalization.

## Checkpoints
v9.8.0 = 6773907
v9.9.0 = 357d8d6
v9.10.0 = 3aef682
v9.11.0 = 6380b4e
HEAD = fbc9ba0

## Next Phase
The next phase is v10 dependent / typed formalization.
Goal: move guards from propositions into types.
Do not add more v9 tags, aliases, or reports unless a real proof-strengthening theorem is added.
