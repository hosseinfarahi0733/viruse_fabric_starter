# Viruse Fabric Project Checkpoint — v8.1 In Progress

## Current Repository State

Current branch:

`v8-1-first-submission-readiness-criteria-plan`

Current working assumption:

- `v8.0.0` is officially closed on `master`.
- `v8.1` branch has been created.
- v8.1 is not closed.
- v8.1 goal is planning submission readiness criteria only.
- v8.1 must not execute readiness audit.
- v8.1 must not mark the manuscript as submission-ready.

Current official project status:

`research prototype with internal validation`

## Latest Closed Milestone

Latest fully closed milestone:

`v8.0.0 — First Full Manuscript Revision Package Audit`

Closed commit:

`b41eb09`

Tag:

`v8.0.0`

v8.0 confirmed:

- Experiment 80 passed
- Errors: 0
- Warnings: 2
- Missing required report phrases: 0
- Working tree clean on master
- Tag v8.0.0 on HEAD
- Note added to `notes/theory_log.md`
- Anti-paste check clean

## Current Milestone In Progress

Current milestone:

`v8.1 — First Submission Readiness Criteria Plan`

Current branch:

`v8-1-first-submission-readiness-criteria-plan`

Purpose:

Plan submission readiness criteria from the audited manuscript package produced through v7.9 and audited in v8.0.

Important boundary:

v8.1 is criteria planning only.

It does not execute submission readiness audit.

It does not make the manuscript submission-ready.

It does not add new citations.

It does not claim external validation.

It does not produce a final paper.

## v8.1 Target Counts

Expected v8.1 target counts:

- Submission readiness criteria plan count: 1
- Audited package revision count: 2
- Planned readiness criterion count: 2
- Submission readiness audit execution count: 0
- Manuscript submission ready count: 0
- Full manuscript rewrite count: 1
- New citation added count: 0
- Conditional hold count: 1
- Overclaim count: 0
- Invented citation-like pattern count: 0

Machine-checkable v8.1 target keys:

- submission_readiness_criteria_plan_count: 1
- audited_package_revision_count: 2
- planned_readiness_criterion_count: 2
- submission_readiness_audit_execution_count: 0
- manuscript_submission_ready_count: 0
- full_manuscript_rewrite_count: 1
- new_citation_added_count: 0
- conditional_hold_count: 1
- overclaim_count: 0
- invented_citation_like_pattern_count: 0

## v8.1 Planned Readiness Rows

Expected planned readiness criteria:

### SRCP-ROW-0001

Linked chain:

`SRCP-ROW-0001 -> FMRPA-ROW-0001 -> FMRPE-ROW-0001 -> FMRPP-ROW-0001 -> BRCA-ROW-0001 -> CGRX-0001 -> CIT-REC-0001 -> CAND-0001`

Purpose:

Check conceptual-framing boundedness.

Boundary:

Conceptual adjacency must not become proof, extension, acceptance, external validation, final paper status, or submission readiness.

### SRCP-ROW-0002

Linked chain:

`SRCP-ROW-0002 -> FMRPA-ROW-0002 -> FMRPE-ROW-0002 -> FMRPP-ROW-0002 -> BRCA-ROW-0002 -> CGRX-0002 -> CIT-REC-0002 -> CAND-0002`

Purpose:

Check methodological-context boundedness.

Boundary:

Methodological background must not become biological prediction, clinical relevance, laboratory guidance, operational causal screening, final paper status, or submission readiness.

## Closed Milestone Chain From v7.6 to v8.0

### v7.6.0 — First Citation-Grounded Manuscript Claim Revision Execution

Closed commit:

`3d900c4`

Main artifact:

`outputs/first_citation_grounded_manuscript_claim_revision_execution_v7_6.md`

Main result:

- Citation-grounded claim revision execution count: 1
- Planned claim revision count: 2
- Executed claim revision count: 2
- Bounded revised claim record count: 2
- Manuscript revised count: 1
- Full manuscript rewrite count: 0
- New citation added count: 0
- Conditional hold count: 1
- Overclaim count: 0

Rows:

- CGRX-0001 executes CGRP-0001
- CGRX-0002 executes CGRP-0002

Boundary:

Controlled claim revision record only. No full manuscript rewrite.

### v7.7.0 — First Bounded Revised Claim Audit

Closed commit:

`4f68348`

Main artifact:

`outputs/first_bounded_revised_claim_audit_v7_7.md`

Main result:

- Bounded revised claim audit count: 1
- Bounded revised claim record count: 2
- Bounded revised claim audited count: 2
- Revised claim audit pass count: 2
- Revised claim audit conditional count: 0
- Revised claim audit fail count: 0
- Full manuscript rewrite count: 0
- New citation added count: 0
- Conditional hold count: 1
- Overclaim count: 0

Rows:

- BRCA-ROW-0001 audits CGRX-0001
- BRCA-ROW-0002 audits CGRX-0002

Boundary:

Audits bounded revised claim records only. No full manuscript rewrite.

### v7.8.0 — First Full Manuscript Revision Package Plan

Closed commit:

`55d5596`

Main artifact:

`outputs/first_full_manuscript_revision_package_plan_v7_8.md`

Main result:

- Full manuscript revision package plan count: 1
- Audited bounded revised claim record count: 2
- Planned package revision count: 2
- Full manuscript revision package execution count: 0
- Full manuscript rewrite count: 0
- New citation added count: 0
- Conditional hold count: 1
- Overclaim count: 0

Rows:

- FMRPP-ROW-0001 plans from BRCA-ROW-0001
- FMRPP-ROW-0002 plans from BRCA-ROW-0002

Boundary:

Package plan only. No package execution.

### v7.9.0 — First Full Manuscript Revision Package Execution

Closed commit:

`da08a71`

Main artifact:

`outputs/first_full_manuscript_revision_package_execution_v7_9.md`

Main result:

- Full manuscript revision package execution count: 1
- Planned package revision count: 2
- Executed package revision count: 2
- Full manuscript revision package count: 1
- Full manuscript rewrite count: 1
- New citation added count: 0
- Conditional hold count: 1
- Overclaim count: 0

Rows:

- FMRPE-ROW-0001 executes FMRPP-ROW-0001
- FMRPE-ROW-0002 executes FMRPP-ROW-0002

Boundary:

Creates one controlled manuscript rewrite artifact, but not a final paper and not submission-ready.

### v8.0.0 — First Full Manuscript Revision Package Audit

Closed commit:

`b41eb09`

Main artifact:

`outputs/first_full_manuscript_revision_package_audit_v8_0.md`

Main result:

- Full manuscript revision package audit count: 1
- Executed package revision count: 2
- Executed package revision audited count: 2
- Package audit pass count: 2
- Package audit conditional count: 0
- Package audit fail count: 0
- Full manuscript rewrite count: 1
- New citation added count: 0
- Conditional hold count: 1
- Overclaim count: 0

Rows:

- FMRPA-ROW-0001 audits FMRPE-ROW-0001
- FMRPA-ROW-0002 audits FMRPE-ROW-0002

Boundary:

Audits the controlled full manuscript revision package. Still not submission-ready.

## Main Evidence and Citation Chain

### CAND-0001

Title:

`Beyond Structural Causal Models: Causal Constraints Models`

Citation key:

`pmlr-v115-blom20a`

Current chain:

`CAND-0001 -> RET-0001 -> EMR-0001 -> CIT-REC-0001 -> MCM-0001 -> MCMA-ROW-0001 -> CGRP-0001 -> CGRX-0001 -> BRCA-ROW-0001 -> FMRPP-ROW-0001 -> FMRPE-ROW-0001 -> FMRPA-ROW-0001 -> planned SRCP-ROW-0001`

Role:

Bounded conceptual or formal-framing context.

Must not be used as:

- proof
- external validation
- accepted theory
- biological validation
- clinical validation
- submission readiness

### CAND-0002

Title:

`Causal screening in dynamical systems`

Citation key:

`pmlr-v124-wengel-mogensen20a`

Current chain:

`CAND-0002 -> RET-0002 -> EMR-0002 -> CIT-REC-0002 -> MCM-0002 -> MCMA-ROW-0002 -> CGRP-0002 -> CGRX-0002 -> BRCA-ROW-0002 -> FMRPP-ROW-0002 -> FMRPE-ROW-0002 -> FMRPA-ROW-0002 -> planned SRCP-ROW-0002`

Role:

Bounded methodological-context background.

Must not be used as:

- biological prediction
- clinical relevance
- laboratory guidance
- operational causal screening
- external validation
- submission readiness

### CAND-0003

Title:

`Causal Structure Learning for Dynamical Systems with Theoretical Score Analysis`

Status:

`hold_for_update_before_retention_decision`

Current boundary:

CAND-0003 remains outside:

- retained source records
- evidence matrix rows
- citation records
- manuscript citation markers
- claim revision rows
- bounded revised claim audit rows
- package plan rows
- package execution rows
- package audit rows
- readiness criteria rows

It remains conditional hold.

## Current Allowed Claim

Viruse Fabric is a research prototype with internal validation that now includes retained sources, audited evidence rows, verified and audited citation records, manuscript citation insertion planning and execution, audited manuscript citation markers, citation-grounded manuscript claim revision planning and execution, audited bounded revised claim records, a full manuscript revision package plan, a controlled full manuscript revision package execution artifact, and an audit of that controlled manuscript package.

After v8.1 closes, the allowed claim may add:

`first submission readiness criteria planned`

but only if v8.1 passes.

## Still Disallowed

The project must not claim:

- proven theory
- external validation
- biological prediction
- clinical relevance
- laboratory guidance
- operational readiness
- submission-ready manuscript
- accepted scientific theory
- final paper
- peer-reviewed manuscript
- acceptance by any venue
- real-world biological prediction
- clinical or laboratory applicability

## Theoretical Core

Persian:

`علیت زنجیره نیست؛ هندسه‌ی قیود است.`

English:

`Causality is not a chain; it is a geometry of constraints.`

Working formulation:

Apparent purpose emerges when constraint geometry, attractor concentration, path compatibility, and observer projection align.

Persian explanation:

`چیزی قصد ندارد؛ اما قیود مسیرها را طوری شکل می‌دهند که برای مشاهده‌گر هدفمند دیده می‌شوند.`

## Immediate Next Steps

1. Continue v8.1 only as readiness criteria planning.
2. Run quick generator test for v8.1.
3. Create official Experiment 81 only after quick run passes.
4. Keep readiness audit execution count at zero.
5. Keep manuscript submission ready count at zero.
6. Keep new citation added count at zero.
7. Keep CAND-0003 on conditional hold.
8. Do not tag or merge v8.1 until:
   - builder passes
   - official experiment passes
   - main commit exists
   - note commit exists
   - anti-paste check is clean
   - tag exists
   - ff-only merge to master succeeds
   - final master test passes

## Checkpoint Boundary

This checkpoint is documentation only.

It does not close v8.1.

It does not execute readiness audit.

It does not make the manuscript submission-ready.

It does not add citations.

It does not change project scientific status.

Current status remains:

`research prototype with internal validation`

