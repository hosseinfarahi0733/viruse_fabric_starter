# VF-H2 Toy Theorem Assumption Tightening Analysis v1

## Status

Scope: execute-vf-h2-toy-theorem-assumption-tightening-analysis-no-claim-validation

This artifact executes assumption tightening analysis. It does not prove a new theorem, does not replace the audited conditional toy theorem, does not validate VF-H2 empirically, does not validate the full Viruse Fabric theory, does not create a complete manuscript, does not claim manuscript readiness, and does not claim submission readiness.

## Source State

The existing audited result remains:

- primary theorem: VF-H2-TOY-THEOREM-002
- theorem scope: conditional_safe_abstract_toy_theorem_only
- conditional toy theorem proved: True
- full Viruse Fabric theory proved: False
- VF-H2 empirically validated: False

## Analysis Result

The analysis identifies several assumption-tightening candidates:

1. Global ledger monotonicity can be decomposed.
2. Transition monotonicity can be decomposed.
3. Aggregation normalization can be separated from sign positivity.
4. The [0,1] state assumption can be separated into sign and boundedness roles.
5. The strict witness condition can be partially reduced to primitive finite-time structural conditions, but not fully proved in this artifact.

No new theorem is proved by this analysis.

## Boundary

Safe abstract toy model only. No real biological datasets, no real pathogen models, no receptor parameters, no operational targeting, no wet-lab protocol, no infectivity optimization, no immune evasion optimization, and no host range prediction are introduced.

## Explicit Non-Claims

This analysis does not claim:

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

draft_vf_h2_toy_theorem_tightened_proof_plan_no_claim_validation


## Primitive Condition Map

### PRIM-VF-H2-001

- replaces_or_supports: A5 ledger monotonicity
- primitive_condition: ledger increments are nonnegative under the selected order
- analysis_result: sufficient_candidate

### PRIM-VF-H2-002

- replaces_or_supports: A5 ledger monotonicity
- primitive_condition: ledger readout map is order-preserving
- analysis_result: sufficient_candidate

### PRIM-VF-H2-003

- replaces_or_supports: A6 transition monotonicity
- primitive_condition: state component of transition is order-preserving
- analysis_result: sufficient_candidate

### PRIM-VF-H2-004

- replaces_or_supports: A6 transition monotonicity
- primitive_condition: activation map is monotone in ledger readout
- analysis_result: sufficient_candidate

### PRIM-VF-H2-005

- replaces_or_supports: A8 strict witness
- primitive_condition: there exists a reachable node-time pair receiving positive ledger increment
- analysis_result: partial_candidate

### PRIM-VF-H2-006

- replaces_or_supports: A8 strict witness
- primitive_condition: the witness node-time pair is not saturated in the memory-ledger trajectory
- analysis_result: partial_candidate

### PRIM-VF-H2-007

- replaces_or_supports: A8 strict witness
- primitive_condition: the null trajectory lacks the same positive ledger contribution at the witness pair
- analysis_result: partial_candidate

### PRIM-VF-H2-008

- replaces_or_supports: A8 strict witness
- primitive_condition: the activation map is strictly increasing at the witness margin
- analysis_result: partial_candidate

### PRIM-VF-H2-009

- replaces_or_supports: A7 positive aggregation
- primitive_condition: aggregation weights are nonnegative
- analysis_result: sufficient_for_sign

### PRIM-VF-H2-010

- replaces_or_supports: A7 positive aggregation
- primitive_condition: the witness node-time pair has positive aggregation weight
- analysis_result: sufficient_for_strict_sign

### PRIM-VF-H2-011

- replaces_or_supports: state range [0,1]
- primitive_condition: ordered cone or partially ordered bounded domain exists for sign proof
- analysis_result: sufficient_for_sign_candidate

### PRIM-VF-H2-012

- replaces_or_supports: state range [0,1]
- primitive_condition: bounded normalized range is retained only for upper-bound theorem
- analysis_result: sufficient_for_boundedness

## Tightening Findings

### FIND-TIGHTEN-001: A5 ledger monotonicity

- finding: Global ledger monotonicity can be decomposed into nonnegative ledger increments plus an order-preserving ledger readout map.
- status: tightened_candidate
- new_theorem_proved: False

### FIND-TIGHTEN-002: A6 transition monotonicity

- finding: Transition monotonicity can be decomposed into state-order preservation and monotonicity of the activation map in ledger readout.
- status: tightened_candidate
- new_theorem_proved: False

### FIND-TIGHTEN-003: A8 strict witness

- finding: The strict witness condition is partially reducible to reachability, positive ledger increment, non-saturation, null absence, strict activation margin, and positive aggregation weight.
- status: partial_derivation_candidate
- new_theorem_proved: False

### FIND-TIGHTEN-004: A7 positive aggregation

- finding: Normalization is not required for sign or strict positivity; nonnegative weights and one positive witness weight are sufficient. Normalization is only needed for the upper-bound statement.
- status: tightened_candidate
- new_theorem_proved: False

### FIND-TIGHTEN-005: state range [0,1]

- finding: The sign theorem can be separated from boundedness. Ordered-domain conditions are enough for sign, while [0,1] normalization is needed for 0 <= ledger_effect_size <= 1.
- status: tightened_candidate
- new_theorem_proved: False

## Tightened Theorem Candidates

### TTC-VF-H2-001: decomposed monotonicity nonnegative theorem

- candidate_statement: If ledger increments are nonnegative, ledger readout is order-preserving, and activation is monotone in state and ledger readout, then the ledger trajectory dominates the no-persistent-memory null trajectory.
- status: candidate_not_proved
- depends_on:
  - PRIM-VF-H2-001
  - PRIM-VF-H2-002
  - PRIM-VF-H2-003
  - PRIM-VF-H2-004

### TTC-VF-H2-002: structural witness strict positivity theorem

- candidate_statement: If the decomposed monotonicity conditions hold and a reachable non-saturated node-time pair receives a positive ledger contribution absent in the null trajectory with strict activation margin and positive aggregation weight, then ledger_effect_size > 0.
- status: candidate_not_proved
- depends_on:
  - TTC-VF-H2-001
  - PRIM-VF-H2-005
  - PRIM-VF-H2-006
  - PRIM-VF-H2-007
  - PRIM-VF-H2-008
  - PRIM-VF-H2-010

### TTC-VF-H2-003: sign theorem without normalized aggregation

- candidate_statement: If aggregation weights are nonnegative and at least one strict witness receives positive weight, then strict positivity holds even without normalized weights.
- status: candidate_not_proved
- depends_on:
  - PRIM-VF-H2-009
  - PRIM-VF-H2-010

### TTC-VF-H2-004: separated boundedness theorem

- candidate_statement: If the state domain is normalized to [0,1] and aggregation weights are normalized, then the already-positive effect size is bounded above by 1.
- status: candidate_not_proved
- depends_on:
  - PRIM-VF-H2-012

## Tightening Gap Register

### TGAP-VF-H2-001

- severity: medium
- description: The structural witness derivation still requires an explicit strict activation margin condition.
- blocking_for_current_conditional_theorem: False
- blocking_for_tightened_theorem: True

### TGAP-VF-H2-002

- severity: medium
- description: The exact partial order for a generalized ordered-domain sign theorem must be fixed before proof.
- blocking_for_current_conditional_theorem: False
- blocking_for_tightened_theorem: True

### TGAP-VF-H2-003

- severity: low
- description: The relationship between unnormalized aggregation and boundedness needs a separate theorem split.
- blocking_for_current_conditional_theorem: False
- blocking_for_tightened_theorem: False
