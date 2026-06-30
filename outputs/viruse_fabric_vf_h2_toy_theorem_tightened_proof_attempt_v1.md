# VF-H2 Toy Theorem Tightened Proof Attempt v1

## Status

Scope: execute-vf-h2-toy-theorem-tightened-proof-attempt-no-claim-validation

This artifact executes a tightened proof attempt inside the safe abstract toy model. It proves three tightened toy results and does not prove the gap-sensitive structural witness theorem.

It does not prove the full Viruse Fabric theory, does not validate VF-H2 empirically, does not provide literature validation, does not provide biological validation, does not provide external validation, does not create a complete manuscript, does not claim manuscript readiness, and does not claim submission readiness.

## Source State

The prior audited result remains preserved:

- primary theorem: VF-H2-TOY-THEOREM-002
- theorem scope: conditional_safe_abstract_toy_theorem_only
- conditional toy theorem proved: True

## Tightened Proof Result

Three tightened toy results are proved for tightened toy assumptions:

1. TTP-VF-H2-001: decomposed monotonicity dominance,
2. TTP-VF-H2-002: strict sign without normalized aggregation,
3. TTP-VF-H2-003: separated boundedness.

TTP-VF-H2-004, the structural witness strict positivity theorem, is not proved in this attempt because two known blocking gaps remain.

## Boundary

Safe abstract toy model only. No real biological datasets, no real pathogen models, no receptor parameters, no operational targeting, no wet-lab protocol, no infectivity optimization, no immune evasion optimization, and no host range prediction are introduced.

## Explicit Non-Claims

This proof attempt does not claim:

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

## Proved Tightened Results

### TTP-VF-H2-001: decomposed monotonicity dominance

- statement: If ledger increments are nonnegative, ledger readout is order-preserving, the state component is order-preserving, and activation is monotone in ledger readout, then the memory-ledger trajectory pointwise dominates the no-persistent-memory null trajectory.
- proof: Use induction on finite time. At time zero, the coupled memory-ledger and null trajectories have the same toy state. Assume coordinatewise dominance at time t. Nonnegative ledger increments and order-preserving ledger readout ensure that the memory-ledger readout is not below the null readout. The state component is order-preserving and activation is monotone in ledger readout, so the next memory-ledger state is coordinatewise not below the next null state. Finite induction proves pointwise dominance for all times in the horizon.
- status: proved_for_tightened_toy_assumptions
- scope: safe_abstract_toy_only

### TTP-VF-H2-002: strict sign without normalized aggregation

- statement: If pointwise dominance holds, aggregation weights are nonnegative, and at least one strict witness receives positive aggregation weight, then ledger_effect_size is strictly positive even without normalized weights.
- proof: Pointwise dominance makes every aggregated difference nonnegative. The strict witness contributes one strictly positive difference multiplied by a positive weight. All other weighted terms are nonnegative. Therefore the aggregate is strictly positive. Normalization is not required for the sign; it is needed only when interpreting the value as a bounded normalized average.
- status: proved_for_tightened_toy_assumptions
- scope: safe_abstract_toy_only

### TTP-VF-H2-003: separated boundedness

- statement: If toy states are normalized in [0,1] and aggregation weights are normalized and nonnegative, then positive ledger_effect_size is bounded above by 1.
- proof: Every coordinatewise difference used in ledger_effect_size lies in [0,1] when pointwise dominance holds and toy states are normalized in [0,1]. A normalized nonnegative weighted average of values in [0,1] is also in [0,1]. Therefore positive ledger_effect_size is bounded above by 1.
- status: proved_for_tightened_toy_assumptions
- scope: safe_abstract_toy_only

## Unproved Gap-Sensitive Result

### TTP-VF-H2-004: structural witness strict positivity

- statement: If decomposed monotonicity holds and a reachable non-saturated node-time pair receives positive ledger contribution absent in the null trajectory with strict activation margin and positive aggregation weight, then ledger_effect_size is strictly positive.
- status: not_proved_in_this_attempt
- reason: The structural witness result still depends on fixing a strict activation margin condition and a precise coordinatewise order before it can be proved without circularly assuming the witness.
- blocking_gaps: TGAP-VF-H2-001, TGAP-VF-H2-002

## Tightened Gap Register

### TGAP-VF-H2-001

- severity: medium
- description: The structural witness derivation still requires an explicit strict activation margin condition.
- status_after_attempt: still_blocking_for_structural_witness_theorem
- blocking_for_current_proved_tightened_results: False
- blocking_for_ttp_vf_h2_004: True

### TGAP-VF-H2-002

- severity: medium
- description: The exact partial order for generalized ordered-domain sign theorem must be fixed before the structural witness proof.
- status_after_attempt: reduced_by_restricting_proved_results_to_coordinatewise_order_but_still_blocking_for_generalized_structural_witness
- blocking_for_current_proved_tightened_results: False
- blocking_for_ttp_vf_h2_004: True

## Next Allowed Action

audit_vf_h2_toy_theorem_tightened_proof_attempt_no_claim_validation
