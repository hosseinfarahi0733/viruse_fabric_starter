# VF-H2 v10 Dependent / Typed Formalization Start Plan

Starting point: after HEAD = fbc9ba0
Previous phase: v9 restricted list-backed Lean scaffold
Goal: replace external list guards with typed invariants

## Why v10 Exists
The v9 scaffold proves a restricted bridge theorem over list-backed states and well-formed parameters.
However, v9 still relies on proposition-level guards: hasExpectedWidth, hasLnBounds, and activeIndicesWithinWidth.
The v10 goal is to move these conditions into types where possible.

## v10 Non-Goals
v10 should not claim full VF-H2, unrestricted TTP-VF-H2-004, empirical validation, biological validation, biological interpretation, or external validation.

## Proposed Milestones
v10.1 Bounded Coordinate Type
Define BoundedCoord n with val : Nat and bound : val <= n.

v10.2 Finite Width Index Type
Use Fin (3 * d) for valid indices.

v10.3 Typed State
Replace State := List Nat with a typed representation, likely Fin (3 * d) -> BoundedCoord n.

v10.4 Typed Active Set
Replace active : List Nat with active : List (Fin (3 * d)).

v10.5 Typed Fixed Set
Define fixed-set membership over typed active indices.

v10.6 Typed Update Map
Rebuild update map so boundedness is preserved by construction.

v10.7 Typed Ledger
Define ledger as a finite sum over typed coordinates.

v10.8 Typed Fixed-Zero Theorem
Reprove fixed -> ledgerEffect = 0.

v10.9 Typed Nonfixed-Positive Theorem
Reprove nonfixed -> ledgerEffect > 0.

v10.10 Typed Restricted Bridge Theorem
Combine fixed-zero and nonfixed-positive.

## Recommended First v10 Commit
Start Lean v10 bounded coordinate scaffold.
Add only namespace/module setup, BoundedCoord, basic projection lemmas, and no broad theorem claims.

## Stop Rule
Do not port the full v9 theorem in one jump.
Each v10 commit should add one small typed component and pass lake build.
Avoid report loops, alias loops, and tag loops.
