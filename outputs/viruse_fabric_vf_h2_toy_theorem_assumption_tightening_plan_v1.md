# VF-H2 Toy Theorem Assumption Tightening Plan v1

## Status

Scope: draft-vf-h2-toy-theorem-assumption-tightening-plan-no-claim-validation

This artifact creates an assumption tightening plan only. It does not execute assumption tightening, does not prove a new theorem, does not strengthen the existing theorem, does not validate VF-H2, does not validate the full Viruse Fabric theory, does not create a complete manuscript, does not claim manuscript readiness, and does not claim submission readiness.

## Source State

The audited proof attempt established a conditional safe abstract toy theorem only:

- primary theorem: VF-H2-TOY-THEOREM-002
- theorem scope: conditional_safe_abstract_toy_theorem_only
- proved theorem count: 3
- proved lemma count: 5
- blocking proof gap count: 0
- non-blocking proof gap count: 3

The next scientific goal is not more presentation polish. The next goal is to reduce unnecessary proof assumptions and identify whether the strict witness condition can be derived from simpler primitive conditions.

## Purpose

The purpose of this plan is to move from a conditional toy theorem with strong assumptions toward a sharper and less assumption-heavy toy theorem.

The plan focuses on:

- decomposing monotonicity assumptions,
- separating sign arguments from boundedness arguments,
- weakening normalized aggregation where possible,
- deriving or partially deriving the witness condition,
- creating a gap register if a witness derivation cannot be completed.

## Boundary

Safe abstract toy model only. No real biological datasets, no real pathogen models, no receptor parameters, no operational targeting, no wet-lab protocol, no infectivity optimization, no immune evasion optimization, and no host range prediction are introduced.

## Explicit Non-Claims

This plan does not claim:

- a new theorem proved,
- full Viruse Fabric theory proof,
- empirical VF-H2 validation,
- literature validation,
- external validation,
- independent empirical validation,
- biological validation,
- real-world relevance,
- operational usefulness,
- manuscript readiness,
- submission readiness.

## Next Allowed Action

execute_vf_h2_toy_theorem_assumption_tightening_analysis_no_claim_validation


## Tightening Targets

### TIGHTEN-VF-H2-001: A5 ledger monotonicity

- current_form: Persistent ledger contribution is nonnegative under the chosen partial order.
- tightening_goal: Replace global ledger monotonicity with local sufficient conditions on the ledger update map.
- planned_analysis: Check whether ledger monotonicity follows from nonnegative ledger increments plus an order-preserving ledger readout.
- risk: medium

### TIGHTEN-VF-H2-002: A6 transition monotonicity

- current_form: Increasing ledger contribution cannot decrease the next toy state.
- tightening_goal: Separate monotonicity in state from monotonicity in ledger contribution.
- planned_analysis: Decompose F into state update, ledger readout, and activation map; identify which component needs monotonicity.
- risk: medium

### TIGHTEN-VF-H2-003: A8 strict witness

- current_form: There exists at least one node-time pair with strict ledger advantage and positive aggregation weight.
- tightening_goal: Derive a witness from primitive finite-time structural conditions rather than assuming it directly.
- planned_analysis: Search for sufficient conditions: reachable node, positive ledger increment, active edge/path, positive threshold margin, and positive aggregation weight.
- risk: high

### TIGHTEN-VF-H2-004: A7 positive aggregation

- current_form: Aggregation weights are nonnegative and normalized.
- tightening_goal: Allow unnormalized positive weights while preserving sign of ledger_effect_size.
- planned_analysis: Show strict positivity only requires at least one positive witness weight and no negative weights; normalization is only needed for boundedness.
- risk: low

### TIGHTEN-VF-H2-005: state range [0,1]

- current_form: x_t(v) in [0,1].
- tightening_goal: Separate sign proof from boundedness proof.
- planned_analysis: Check if nonnegative or positive ledger_effect_size works over any ordered cone, while boundedness needs [0,1].
- risk: medium

## Dependency Map

### L1 coupled null construction

- depends_on:
  - A2 matched initial state
  - A3 matched symbolic inputs
  - A4 null ledger removal

### L2 pointwise dominance

- depends_on:
  - A1 finite bounded toy state
  - A2 matched initial state
  - A3 matched symbolic inputs
  - A5 ledger monotonicity
  - A6 transition monotonicity

### L3 nonnegative aggregate effect

- depends_on:
  - L2 pointwise dominance
  - A7 positive aggregation

### L4 strict witness positivity

- depends_on:
  - L2 pointwise dominance
  - A7 positive aggregation
  - A8 strict witness

### L5 bounded normalized signal

- depends_on:
  - A1 finite bounded toy state
  - A7 normalized positive aggregation

### VF-H2-TOY-THEOREM-002

- depends_on:
  - L1
  - L2
  - L3
  - L4
  - A8 strict witness

## Planned Outputs

- OUT-TIGHTEN-001: primitive condition map — Map each strong assumption to weaker primitive conditions.
- OUT-TIGHTEN-002: tightened theorem candidates — Draft theorem variants with weaker assumptions.
- OUT-TIGHTEN-003: witness derivation attempt — Attempt to derive A8 from finite-time structural conditions.
- OUT-TIGHTEN-004: assumption dependency graph — Record which lemma depends on which assumption.
- OUT-TIGHTEN-005: gap register if tightening fails — Record unresolved assumption gaps honestly.

## Non-Claims

- No new theorem is proved by this plan.
- No full Viruse Fabric theory proof is claimed.
- No empirical validation is claimed.
- No literature validation is claimed.
- No biological validation is claimed.
- No external validation is claimed.
- No manuscript readiness is claimed.
- No submission readiness is claimed.