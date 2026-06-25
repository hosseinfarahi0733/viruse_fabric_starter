# First Retained Source Decision Plan v6.3

## Question
Can Viruse Fabric plan the first retained source decision after candidate metadata audit while keeping retention execution, retained sources, citations, evidence matrix population, and manuscript revision at zero?

## Status
Current project status remains:

`research prototype with internal validation`

This artifact is not externally validated, not submission-ready, and not a final paper.

This milestone does plan retained source decisions. It does not execute retention decisions, does not create retained sources, does not add citations, does not populate the evidence matrix, and does not revise the manuscript.

Retained source decision plan is not retained source creation. Retention planning is not retention execution. Metadata pass is not source retention. Conditional metadata pass is not source retention. Candidate source entries are not retained sources. Retained sources are not citations. Citations are not external validation.

## Source Artifacts
| Source artifact | Exists |
|---|---|
| `outputs/candidate_source_metadata_audit_v6_2.md` | True |
| `outputs/first_candidate_source_entry_creation_v6_1.md` | True |
| `outputs/first_candidate_source_entry_plan_v6_0.md` | True |
| `outputs/first_raw_result_screening_execution_v5_9.md` | True |
| `outputs/first_raw_result_screening_plan_v5_8.md` | True |
| `outputs/first_controlled_live_search_execution_v5_7.md` | True |
| `outputs/first_search_run_artifact_audit_v5_6.md` | True |
| `outputs/first_search_run_artifact_v5_5.md` | True |
| `outputs/first_literature_family_search_plan_v5_4.md` | True |
| `outputs/literature_search_log_empty_v5_2.md` | True |
| `outputs/literature_search_log_template_v5_1.md` | True |
| `outputs/claim_to_citation_readiness_map_v4_9.md` | True |
| `outputs/literature_family_evidence_matrix_v4_8.md` | True |

## Retained Source Decision Plan Metadata
| Retained source decision plan field | Value |
|---|---|
| `retained_source_decision_plan_id` | RDP-0001 |
| `linked_candidate_metadata_audit_id` | CMA-0001 |
| `linked_candidate_entry_creation_id` | CEC-0001 |
| `linked_candidate_entry_plan_id` | CEP-0001 |
| `plan_status` | retention_decision_planned_not_executed |
| `literature_family` | constraint-based causality and dynamical-systems framing |
| `candidate_source_count_from_v6_2` | 3 |
| `metadata_audit_pass_count_from_v6_2` | 2 |
| `metadata_audit_conditional_pass_count_from_v6_2` | 1 |
| `planned_retention_candidate_count` | 2 |
| `conditional_hold_count` | 1 |
| `retention_decision_execution_count` | 0 |
| `retained_source_count` | 0 |

## Planned Retention Decision Rows
| Candidate id | Metadata audit decision | Retention plan status | Planned action | Retained source created | Reason |
|---|---|---|---|---|---|
| CAND-0001 | metadata_pass_not_retained | eligible_for_retention_decision_later | evaluate_for_retention_in_future_milestone | no | Metadata passed candidate audit, so it can enter a later retention decision. |
| CAND-0002 | metadata_pass_not_retained | eligible_for_retention_decision_later | evaluate_for_retention_in_future_milestone | no | Metadata passed candidate audit, so it can enter a later retention decision. |
| CAND-0003 | metadata_conditional_pass_not_retained | hold_for_update_before_retention_decision | check_updated_metadata_before_retention_decision | no | Conditional metadata pass requires update handling before retention decision. |

## Retention Criteria
- Candidate must have passed metadata audit or have an explicit conditional update path.
- Candidate must have stable title metadata.
- Candidate must have stable author metadata.
- Candidate must have identifiable venue or repository metadata.
- Candidate must have year or access-date metadata that can be recorded without invention.
- Candidate must have a stable access route.
- Candidate source type must be classified.
- Candidate primary or secondary status must be explicit.
- Candidate must link back to raw observation and screening decision.
- Candidate must map to a specific claim category.
- Candidate must have inclusion rationale.
- Candidate must have exclusion-risk notes.
- Candidate must have a bounded proposed source role.
- Candidate must remain outside citation use until retention is explicitly executed.

## Retention Decision Values
- planned_for_future_retention_decision
- hold_for_metadata_update_before_retention
- not_ready_for_retention_decision
- retention_decision_not_executed

## Retention Plan Gates
- Retention planning must be separate from retention execution.
- Retention planning must not create retained sources.
- Retention planning must not add citations.
- Retention planning must not populate the evidence matrix.
- Retention planning must not revise the manuscript.
- Only metadata-pass candidates may be planned for immediate future retention decision.
- Conditional metadata-pass candidates must remain on hold until update handling.
- Every planned retention candidate must preserve candidate source status.
- Every future retention decision must be auditable.
- Every future retention decision must remain separate from citation integration.
- Retained-source decision must not imply external validation.
- Retained-source decision must not imply submission readiness.

## Boundary Phrases
- research prototype with internal validation
- not externally validated
- not submission-ready
- not a final paper
- not biological guidance
- not clinical guidance
- not laboratory guidance
- not operational guidance
- retained source decision plan is not retained source creation
- retention planning is not retention execution
- metadata pass is not source retention
- conditional metadata pass is not source retention
- candidate source entries are not retained sources
- retained sources are not citations
- citations are not external validation
- does plan retained source decisions
- does not create retained sources
- does not add citations
- does not populate the evidence matrix
- does not revise the manuscript

## Prohibited Behaviors
- Do not create retained sources in this milestone.
- Do not add citations in this milestone.
- Do not populate the evidence matrix in this milestone.
- Do not revise the manuscript in this milestone.
- Do not treat metadata pass as retention.
- Do not treat retention planning as retention execution.
- Do not treat planned retention candidates as retained sources.
- Do not treat retained-source planning as citation readiness.
- Do not imply external validation.
- Do not imply submission readiness.
- Do not provide biological, clinical, laboratory, or operational guidance.

## Next Steps
- Execute first retained source decision in a later milestone.
- Evaluate metadata-pass candidates for retention separately.
- Keep conditional metadata-pass candidate on hold until update handling.
- Create retained sources only after explicit retention decision.
- Audit retained source roles after retention decision.
- Populate evidence matrix only after retained-source audit.
- Add citations only after retained-source decision.
- Revise manuscript only after citation-grounded integration.

## Retention Plan Interpretation
The v6.3 artifact creates the first retained-source decision plan after the v6.2 metadata audit.

Two candidate sources are planned for future retention decision because they received metadata pass decisions in v6.2. One candidate source is placed on conditional hold because it received a conditional metadata pass and needs update handling before any retention decision.

This is planning only. No source becomes retained here. No source becomes citation-ready here. No source enters the evidence matrix here. No manuscript claim is revised here.

## Planning Boundary
The plan defines eligibility for a later decision, not the decision itself.

A metadata-pass candidate can be planned for future retention decision, but that future decision still needs explicit execution. A conditional metadata-pass candidate cannot be silently promoted. It must remain on hold until its metadata uncertainty is handled.

This boundary prevents a familiar little disaster: calling something "planned" and then treating it as "done" because a table looks official. Tables are very convincing liars when humans are tired.

## Retention Boundary
Retained source count remains zero.

This milestone does not create retained source records. It only identifies which candidate records may be evaluated in a later retained-source decision milestone. The retained-source layer remains empty.

A retained source, when eventually created, will still not be a citation by itself. Citation integration requires a separate action. Evidence matrix population requires a separate action. Manuscript revision requires a separate action.

## Evidence Boundary
Citation added count remains zero.

Evidence matrix populated count remains zero.

Manuscript revised count remains zero.

The project therefore keeps the distinction between candidate metadata, retention planning, retention execution, citation integration, evidence matrix population, and manuscript revision.

## Retention Decision Consequence Boundary
The retained-source decision plan creates no retained-source record.

It only describes which candidate entries are eligible for a later retained-source decision and which candidate entry must remain on hold. The two metadata-pass candidates are not retained here; they are only scheduled for future evaluation. The conditional candidate is not rejected here; it is held until update handling can resolve its metadata uncertainty.

This means the retained-source layer remains empty. The evidence matrix remains empty with respect to these candidates. The manuscript receives no new support. No citation is added. No external validation is implied.

A future retention decision must still ask whether a candidate source has an appropriate source role, a bounded claim mapping, a stable access route, and acceptable exclusion-risk notes. If that future decision passes, only then can a retained-source record be created.

## Plan Failure Modes Prevented
This artifact prevents several premature transitions.

It prevents metadata pass from becoming automatic retention. It prevents conditional metadata pass from being quietly upgraded into acceptance. It prevents planned retention from being treated as completed retention. It prevents a future citation workflow from inheriting sources that were never explicitly retained.

The artifact also prevents manuscript drift. A source can appear relevant, have metadata, pass audit, and enter a retention plan while still providing zero manuscript support. That is not inefficiency; it is the point of staged scientific bookkeeping. The alternative is a bibliography wearing a fake mustache and calling itself evidence.

## Output Counts
Retained source decision plan count: 1

Candidate source count: 3

Metadata audit pass count: 2

Metadata audit conditional pass count: 1

Planned retention candidate count: 2

Conditional hold count: 1

Retention decision execution count: 0

Retained source count: 0

Citation added count: 0

Evidence matrix populated count: 0

Manuscript revised count: 0

## Final Boundary Statement
This artifact plans first retained source decisions.

It does not execute retention decisions, does not create retained sources, does not add citations, does not populate the evidence matrix, does not revise the manuscript, does not certify external validation, does not make the manuscript ready for submission, and does not provide biological, clinical, laboratory, or operational guidance.

Current status remains:

`research prototype with internal validation`
