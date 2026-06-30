# Viruse Fabric Engine Redesign Specification v1

## Status

This is an engine redesign specification, not an implementation.

No code change is requested by this document.
claim expansion remains forbidden.
No new milestone is created.
No official tag is created.

## Source State

- Base master head: f356e2f
- Last official tag: v9.8.0
- Last official tag commit: 6773907
- Technical note commit: f356e2f
- v9 loop status: stopped

## Reason for Redesign

v9.7 produced a narrow safe toy signal:

- Primary hypothesis: VF-H2
- Primary signal: ledger_effect_size
- Reduced core: memory-ledger-driven toy dynamics
- Positive signal replicate count: 6
- Mean signal delta: 3.0
- Robustness verdict: robust_in_this_safe_toy_replicate_grid

v9.8 then found a boundary:

- Candidate parameter count: 6
- Blocked candidate count: 4
- Accepted candidate count: 2
- Parameter sweep boundary verdict: parameter_sweep_partially_blocked_by_engine_spec_boundary

v9.8 null controls were clean:

- Null-control count: 4
- Null-control leak count: 0
- Null-control verdict: no_null_control_leak_detected

Decision:

- Decision: stop_claim_expansion_and_redesign_engine_before_more_toy_evidence
- Next allowed action: engine_redesign_or_limited_technical_note
- Loop guard verdict: stop_v9_loop

## Redesign Goal

Allow a clean safe abstract toy parameter sweep without expanding claims or introducing real biological meaning.

The redesigned engine must support clean safe abstract toy parameter sweeps while preserving safety boundaries and avoiding claim expansion.

## Safe Parameter Registry

| Parameter | Allowed role | Must not mean | Proposed values | Requires engine support |
|---|---|---|---|---|
| node_count | abstract toy graph size only | host count, cell count, organism count, population count, or biological entity count | [12, 16, 20, 24] | True |
| packet_count | abstract toy packet volume only | viral load, dose, infection count, particle count, or biological exposure | [24, 32, 40, 48] | True |
| step_count_limit | abstract discrete iteration count only | incubation time, replication cycle, disease progression time, or biological time | [2, 3, 4, 5] | True |
| graph_seed | abstract randomization seed only | environment, lineage, strain, host type, or empirical scenario | [101, 111, 121, 131] | False |
| packet_seed | abstract packet initialization seed only | exposure route, sample source, patient group, or biological sampling | [202, 212, 222, 232] | False |
| transition_seed | abstract transition randomization seed only | mutation process, transmission process, replication mechanism, or biological pathway | [303, 313, 323, 333] | False |
| symbolic_drift_seed | abstract symbolic drift randomization seed only | immune evasion, antigenic drift, host adaptation, or biological mutation | [404, 414, 424, 434] | False |

## Required Engine Changes

### ENG-REDESIGN-001

- Change: Separate safe envelope validation from fixed v9.1 default-value validation.
- Reason: v9.8 showed that some candidate parameter mutations are blocked by fixed toy-value constraints.
- Acceptance criterion: The engine can validate a declared safe sweep profile without treating every deviation from v9.1 defaults as invalid.

### ENG-REDESIGN-002

- Change: Introduce an explicit SafeToySweepProfile object or equivalent configuration layer.
- Reason: Parameter sweep must be intentional, bounded, and auditable rather than ad hoc mutation of ToyEngineConfig.
- Acceptance criterion: Every varied parameter is listed with allowed values, safe abstract role, and forbidden biological interpretation.

### ENG-REDESIGN-003

- Change: Add null-control templates as first-class experiment checks.
- Reason: v9.8 null controls were clean and must remain mandatory for future sweeps.
- Acceptance criterion: Identical-variant comparisons produce zero ledger_effect_size delta across declared null controls.

### ENG-REDESIGN-004

- Change: Add artifact-risk reporting for constant signals.
- Reason: v9.7 produced a repeated 3.0 signal; a redesign must distinguish robust signal from mechanically fixed artifact.
- Acceptance criterion: Reports include distinct delta count, min, max, mean, standard deviation, and artifact-risk verdict.

### ENG-REDESIGN-005

- Change: Keep real biological semantics explicitly prohibited in engine metadata and reports.
- Reason: The project must remain safe abstract toy only.
- Acceptance criterion: Reports preserve zero counts for real biological datasets, real pathogen simulation, receptor parameters, targeting, wet-lab protocol, infectivity optimization, immune evasion optimization, and host range prediction.

## Future Experiment Acceptance Criteria

- minimum_clean_sweep_requirement: At least three safe abstract parameters can vary without violating the safe sweep profile.
- null_control_requirement: All null controls must have zero ledger_effect_size leakage.
- positive_signal_requirement: VF-H2 signal must remain positive in at least 80 percent of valid safe sweep cells.
- artifact_risk_requirement: If all valid sweep cells produce identical signal deltas, the result must be flagged as artifact-risk moderate_to_high or worse.
- falsification_requirement: If positive signal rate falls below 50 percent or null-control leakage is nonzero, claim expansion must stop.

## Forbidden Directions

- Do not add real biological datasets.
- Do not add real pathogen models.
- Do not add receptor parameters.
- Do not add operational host targeting.
- Do not add wet-lab protocol.
- Do not optimize infectivity.
- Do not optimize immune evasion.
- Do not predict host range.
- Do not claim empirical validation.
- Do not claim full theory validation.
- Do not claim manuscript readiness.
- Do not upgrade VF-H1, VF-H3, or VF-H4 without separate mechanism-specific evidence.

## Implementation Boundary

- Implementation allowed now: False
- Allowed next action: write implementation plan only after this specification is reviewed

No code should be changed until the implementation plan is written from this specification.

## Safety Boundary

Safe abstract toy model only. No validation claim is made. No manuscript readiness claim is made. No readiness approval is recorded. No manuscript file is modified. No citation is added. No external validation is performed. No independent experiment is performed. No real biological datasets, no real pathogen models, no receptor parameters, no operational targeting, no wet-lab protocol, no infectivity optimization, no immune evasion optimization, and no host range prediction are introduced.

## Final Redesign Decision

The next step is not implementation. The next step is an implementation plan derived from this specification.
