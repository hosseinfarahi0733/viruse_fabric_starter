# VF-H2 Structural Witness Gap Resolution Plan v1

## Status

Scope: draft-vf-h2-structural-witness-gap-resolution-plan-no-claim-validation

This artifact creates a structural witness gap resolution plan only. It does not execute the gap resolution, does not prove TTP-VF-H2-004, does not prove a new theorem, does not validate VF-H2 empirically, does not validate the full Viruse Fabric theory, does not create a complete manuscript, does not claim manuscript readiness, and does not claim submission readiness.

## Source State

The tightened proof attempt audit confirmed:

- proved tightened result count: 3
- TTP-VF-H2-001 proved: True
- TTP-VF-H2-002 proved: True
- TTP-VF-H2-003 proved: True
- TTP-VF-H2-004 proved: False
- blocking gap for structural witness theorem count: 2
- unscoped overclaim hit count: 0
- forbidden real bio hit count: 0

## Purpose

The purpose is to resolve the two remaining structural witness blockers without pretending they are already solved. Tiny miracle, the plan is doing planning, not theater.

The two blockers are:

1. TGAP-VF-H2-001: strict activation margin,
2. TGAP-VF-H2-002: coordinatewise order restriction.

## Boundary

Safe abstract toy model only. No real biological datasets, no real pathogen models, no receptor parameters, no operational targeting, no wet-lab protocol, no infectivity optimization, no immune evasion optimization, and no host range prediction are introduced.

## Explicit Non-Claims

This plan does not claim:

- TTP-VF-H2-004 proved,
- structural witness theorem proved,
- a new theorem proved,
- full Viruse Fabric theory proof,
- empirical VF-H2 validation,
- literature validation,
- external validation,
- independent empirical validation,
- biological validation,
- manuscript readiness,
- submission readiness.

## Next Allowed Action

execute_vf_h2_structural_witness_gap_resolution_analysis_no_claim_validation

## Gap Resolution Targets

### TGAP-VF-H2-001: strict activation margin

- problem: The structural witness theorem cannot be proved unless strict ledger contribution creates a strict next-state difference rather than a merely weak nondecrease.
- planned_resolution: Introduce an explicit primitive margin condition: at witness pair (v*,t*), the activation map is strictly increasing with respect to the ledger readout over the relevant interval.
- success_criterion: A strict local ledger readout advantage implies x_L(t*+1,v*) > x_0(t*+1,v*) without assuming the witness conclusion directly.
- risk: medium

### TGAP-VF-H2-002: coordinatewise order restriction

- problem: The generalized ordered-domain claim is too broad for the next proof attempt.
- planned_resolution: Restrict the structural witness theorem to finite real-valued toy states with coordinatewise order and nonnegative aggregation weights.
- success_criterion: The proof no longer depends on an unspecified abstract partial order.
- risk: low

## Primitive Structural Witness Conditions

### SWC-VF-H2-001: finite coordinatewise toy domain

- statement: The toy state space is [0,1]^V over finite V, ordered coordinatewise.
- role: resolves TGAP-VF-H2-002

### SWC-VF-H2-002: matched null coupling

- statement: The memory-ledger and null processes share initial state, finite horizon, graph, and symbolic inputs.
- role: preserves coupling from prior proof

### SWC-VF-H2-003: positive ledger readout advantage

- statement: At a reachable witness pair, the persistent ledger readout is strictly greater than the null ledger readout.
- role: supplies local strict advantage

### SWC-VF-H2-004: strict activation margin

- statement: At the witness pair, the activation map is strictly increasing over the ledger-readout interval induced by SWC-VF-H2-003.
- role: resolves TGAP-VF-H2-001

### SWC-VF-H2-005: non-saturation

- statement: The witness coordinate is not already saturated in a way that erases the strict activation difference.
- role: prevents clipping from destroying strictness

### SWC-VF-H2-006: positive witness aggregation weight

- statement: The witness node-time pair has strictly positive aggregation weight.
- role: turns local strict difference into positive ledger_effect_size

## Planned Lemmas

### SWL-VF-H2-001: strict local activation lemma

- planned_claim: Under SWC-VF-H2-003, SWC-VF-H2-004, and SWC-VF-H2-005, the witness coordinate has strict memory-ledger advantage.
- status: planned_not_proved

### SWL-VF-H2-002: structural witness lemma

- planned_claim: The primitive witness conditions imply the strict witness condition used by the earlier conditional theorem.
- status: planned_not_proved

### SWL-VF-H2-003: positive aggregate witness lemma

- planned_claim: A strict witness coordinate with positive aggregation weight implies ledger_effect_size > 0 under nonnegative weights.
- status: planned_not_proved

## Planned Theorem

### TTP-VF-H2-004-R: resolved structural witness strict positivity theorem

- planned_statement: In the finite coordinatewise toy domain, if decomposed monotonicity holds and SWC-VF-H2-001 through SWC-VF-H2-006 hold, then ledger_effect_size > 0.
- status: planned_not_proved
- claim_boundary: safe_abstract_toy_only
