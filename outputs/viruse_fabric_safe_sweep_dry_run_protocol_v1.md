# Safe Sweep Dry-Run Protocol v1

## Status

Scope: safe-sweep-dry-run-protocol-only-no-engine-or-sweep-execution

dry-run protocol created
dry-run not executed
no dry-run execution
no null-control execution
no observed null-control leak
no engine execution
no sweep execution
The engine is not modified.
engine not modified
The engine is not executed.
engine not executed
A sweep is not executed.
sweep not executed
claim expansion remains forbidden.
No validation claim is made.
No theory validation claim is made.
No manuscript readiness claim is made.
No manuscript submission readiness claim is made.
No external validation claim is made.
No independent experiment claim is made.

## Source Artifacts

- null_control_regression: safe_null_control_template_regression_v1
- null_control_templates: safe_null_control_templates_v1
- harness: safe_sweep_execution_harness_v1
- plan: safe_sweep_execution_plan_v1

## Protocol Phases

### DRY-RUN-PROTOCOL-001 — Artifact preflight
- Purpose: Confirm plan, harness, null-control templates, and null-control regression are all present and passing.
- Allowed now: True
- Executes engine: False
- Executes sweep: False
- Executes null controls: False
- Failure response: stop_before_any_dry_run

### DRY-RUN-PROTOCOL-002 — Dry-run manifest construction
- Purpose: Future dry-run may build a manifest of intended cells and null-control pairings without scoring or interpretation.
- Allowed now: False
- Executes engine: False
- Executes sweep: False
- Executes null controls: False
- Failure response: reject_manifest_if_any_execution_flag_is_true

### DRY-RUN-PROTOCOL-003 — Execution refusal checks
- Purpose: Future dry-run must prove engine, sweep, and null-control execution paths remain disabled.
- Allowed now: False
- Executes engine: False
- Executes sweep: False
- Executes null controls: False
- Failure response: stop_if_refusal_check_fails

### DRY-RUN-PROTOCOL-004 — Safety counter audit
- Purpose: Future dry-run must keep all biological, validation, readiness, citation, and claim counters at zero.
- Allowed now: False
- Executes engine: False
- Executes sweep: False
- Executes null controls: False
- Failure response: block_report_if_any_forbidden_counter_is_nonzero

### DRY-RUN-PROTOCOL-005 — Post dry-run protocol gate
- Purpose: Future dry-run output must be classified as protocol/dry-run metadata only, not evidence.
- Allowed now: False
- Executes engine: False
- Executes sweep: False
- Executes null controls: False
- Failure response: stop_claim_expansion

## Stop Rules

- DRY-RUN-STOP-001: if Any engine execution flag becomes true. => stop_immediately
- DRY-RUN-STOP-002: if Any sweep execution flag becomes true. => stop_immediately
- DRY-RUN-STOP-003: if Any null-control execution flag becomes true. => stop_immediately
- DRY-RUN-STOP-004: if Any biological semantics, pathogen framing, receptor parameter, targeting, wet-lab, infectivity, immune evasion, or host range content appears. => reject_artifact
- DRY-RUN-STOP-005: if Any validation, external validation, independent experiment, manuscript readiness, submission readiness, readiness approval, or citation claim appears. => reject_artifact
- DRY-RUN-STOP-006: if Any future dry-run output is interpreted as evidence rather than protocol metadata. => stop_claim_expansion

## Dry-Run Boundary

- allowed_now: False
- future_dry_run_may_build_manifest: True
- future_dry_run_may_execute_engine: False
- future_dry_run_may_execute_sweep: False
- future_dry_run_may_execute_null_controls: False
- future_dry_run_may_make_evidence_claim: False
- interpretation_boundary: protocol_metadata_only_not_evidence

## Required Safety Markers

- safe-sweep-dry-run-protocol-only-no-engine-or-sweep-execution
- dry-run protocol created
- dry-run not executed
- no dry-run execution
- no null-control execution
- no observed null-control leak
- no engine execution
- no sweep execution
- engine not modified
- engine not executed
- sweep not executed
- claim expansion remains forbidden
- No validation claim is made
- No theory validation claim is made
- No manuscript readiness claim is made
- No manuscript submission readiness claim is made
- No external validation claim is made
- No independent experiment claim is made
- No real biological datasets
- no real pathogen models
- no receptor parameters
- no operational targeting
- no wet-lab protocol
- no infectivity optimization
- no immune evasion optimization
- no host range prediction

## Counters

- Claim expansion count: 0
- Dry-run execution count: 0
- Engine execution count: 0
- Engine modification count: 0
- Experiment execution count: 0
- External validation count: 0
- Immune evasion optimization count: 0
- Independent experiment count: 0
- Manuscript readiness claim count: 0
- Manuscript submission ready count: 0
- New citation added count: 0
- New milestone created count: 0
- Null-control execution count: 0
- Observed null-control leak count: 0
- Official tag created count: 0
- Operational host targeting count: 0
- Phase non-execution consistency check count: 1
- Planned future harness cell count: 64
- Planned future null-control pair count: 256
- Planned future null-control template count: 4
- Protocol phase count: 5
- Protocol stop rule count: 6
- Readiness approval count: 0
- Real biological dataset import count: 0
- Real host range prediction count: 0
- Real pathogen simulation count: 0
- Real receptor parameter count: 0
- Real-world infectivity optimization count: 0
- Safe sweep dry-run protocol artifact count: 1
- Source consistency check count: 1
- Sweep execution count: 0
- Theory validation claim count: 0
- Validation claim count: 0
- Wet-lab protocol count: 0

## Boundary

Safe abstract toy model only. No real biological datasets, no real pathogen models, no receptor parameters, no operational targeting, no wet-lab protocol, no infectivity optimization, no immune evasion optimization, and no host range prediction are introduced.

## Next Allowed Action

run_safe_sweep_dry_run_protocol_regression_without_engine_or_sweep_execution
