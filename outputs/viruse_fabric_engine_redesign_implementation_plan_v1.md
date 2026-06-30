# Viruse Fabric Engine Redesign Implementation Plan v1

## Status

This is an implementation plan only.

No code is changed by this artifact.
No engine file is modified by this artifact.
No experiment is executed by this artifact.
No new milestone is created.
No official tag is created.
claim expansion remains forbidden.
implementation allowed now: False

## Source

- Source specification: engine_redesign_specification_v1
- Source specification commit: bacb1aa
- Base master head: bacb1aa
- Last official tag: v9.8.0
- Last official tag commit: 6773907
- v9 loop status: stopped

## Scope

- Implementation goal: Allow a clean safe abstract toy parameter sweep without expanding claims or introducing real biological meaning.
- Primary hypothesis scope: VF-H2 only
- Primary signal scope: ledger_effect_size only
- Reduced core scope: memory-ledger-driven toy dynamics only

## Planned Files to Consider

| Path | Role | Allowed future change | Changed now |
|---|---|---|---|
| viruse_fabric/simulation/viruse_fabric_minimal_safe_toy_simulation_engine.py | candidate engine redesign target | separate fixed default validation from safe sweep profile validation | False |
| viruse_fabric/experiments/ | future safe sweep experiment location | add future safe abstract toy sweep experiment only after implementation branch opens | False |
| viruse_fabric/writing/ | future safe sweep report writer location | add future report writer with artifact-risk and null-control reporting only after implementation branch opens | False |
| outputs/ | artifact output location | this plan may write documentation outputs only | True |

## Implementation Phases

### PHASE-001 - Inspect current engine validation boundary

- Purpose: Identify where fixed v9.1 default-value validation blocks safe abstract toy sweep values.
- Code change allowed in this plan: False
- Future acceptance gate: Document exact validation functions before editing them.

### PHASE-002 - Design SafeToySweepProfile structure

- Purpose: Define bounded safe abstract toy parameter registry without biological semantics.
- Code change allowed in this plan: False
- Future acceptance gate: Every sweep parameter has allowed values, allowed role, and forbidden interpretation.

### PHASE-003 - Separate default config validation from sweep profile validation

- Purpose: Allow declared safe sweep profiles without pretending they are v9.1 default configs.
- Code change allowed in this plan: False
- Future acceptance gate: Default v9.1 config still validates exactly, and safe sweep configs validate through a separate profile.

### PHASE-004 - Add mandatory null-control templates

- Purpose: Make null-control leakage checks first-class and unavoidable.
- Code change allowed in this plan: False
- Future acceptance gate: Identical-variant comparisons produce zero ledger_effect_size delta.

### PHASE-005 - Add artifact-risk reporting

- Purpose: Detect mechanically fixed signal patterns such as constant 3.0 deltas.
- Code change allowed in this plan: False
- Future acceptance gate: Reports include distinct delta count, min, max, mean, standard deviation, and artifact-risk verdict.

### PHASE-006 - Run future safe sweep only after implementation branch

- Purpose: Prevent implementation leakage into the planning artifact.
- Code change allowed in this plan: False
- Future acceptance gate: A separate code branch must be opened before any engine or experiment file changes.

## Future Test Plan

### TEST-001 - Default config regression

- Required result: Original v9.1/v9.2 default safe toy config still validates and runs.

### TEST-002 - Safe sweep profile validation

- Required result: At least node_count, packet_count, and step_count_limit can vary inside declared safe abstract bounds.

### TEST-003 - Forbidden biological semantics check

- Required result: Reports preserve zero real biological dataset, pathogen, receptor, targeting, wet-lab, infectivity, immune evasion, and host range counts.

### TEST-004 - Null-control leakage check

- Required result: All identical-variant controls produce zero ledger_effect_size leakage.

### TEST-005 - Artifact-risk check

- Required result: Constant deltas across sweep cells trigger artifact-risk warning.

### TEST-006 - Claim boundary check

- Required result: No report claims validation, empirical support, real biological applicability, or manuscript readiness.

## Go / No-Go Rules

### Go for future code branch

- Specification is on master.
- Implementation plan is on master.
- No new tag is created for documentation-only planning artifacts.
- Implementation branch is separate from documentation branches.

### No-go conditions

- Any real biological semantics are introduced.
- Any manuscript readiness claim is introduced.
- Any validation claim is introduced.
- Any null-control leakage is accepted as harmless.
- Any constant signal is treated as strong evidence without artifact-risk reporting.
- Any VF-H1, VF-H3, or VF-H4 upgrade is attempted without separate evidence.

## Safety Boundary

Safe abstract toy model only. No validation claim is made. No manuscript readiness claim is made. No readiness approval is recorded. No manuscript file is modified. No citation is added. No external validation is performed. No independent experiment is performed. No real biological datasets, no real pathogen models, no receptor parameters, no operational targeting, no wet-lab protocol, no infectivity optimization, no immune evasion optimization, and no host range prediction are introduced.

## Final Planning Decision

The next allowed step after this plan is a separate code branch for safe engine redesign only after the plan is merged to master.
No implementation is allowed inside this planning artifact.
