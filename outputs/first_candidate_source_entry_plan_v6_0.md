# First Candidate Source Entry Plan v6.0

## Question
Can Viruse Fabric plan the first candidate source entry workflow after screening execution without creating candidate sources, retaining sources, adding citations, populating the evidence matrix, or revising the manuscript?

## Status
Current project status remains:

`research prototype with internal validation`

This artifact is not externally validated, not submission-ready, and not a final paper.

This is a candidate source entry plan. Candidate source entry plan is not candidate source creation. Candidate source planning is not source retention. Candidate sources are not retained sources. Retained sources are not citations. Citations are not external validation.

This artifact does not create candidate sources, does not retain sources, does not add citations, does not populate the evidence matrix, and does not revise the manuscript.

## Source Artifacts
| Source artifact | Exists |
|---|---|
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

## Candidate Entry Plan Metadata
| Plan field | Value |
|---|---|
| `candidate_entry_plan_id` | CEP-0001 |
| `linked_screening_execution_id` | SX-0001 |
| `linked_search_execution_id` | SE-0001 |
| `linked_screening_plan_id` | SP-0001 |
| `plan_status` | planned_not_created |
| `literature_family` | constraint-based causality and dynamical-systems framing |
| `claim_category` | literature-needed: constraints shape possible trajectories |
| `screened_result_count_from_v5_9` | 5 |
| `pass_to_candidate_planning_count_from_v5_9` | 3 |
| `defer_to_candidate_planning_count_from_v5_9` | 2 |
| `candidate_source_count` | 0 |
| `retained_source_count` | 0 |

## Planned Candidate Entry Rows
| Raw observation id | Screening decision | Entry plan status | Candidate source created |
|---|---|---|---|
| raw_result_observation_01 | defer_for_candidate_entry_planning | metadata_check_required_before_candidate_entry | no |
| raw_result_observation_02 | pass_to_candidate_entry_planning | candidate_entry_planning_allowed | no |
| raw_result_observation_03 | pass_to_candidate_entry_planning | candidate_entry_planning_allowed | no |
| raw_result_observation_04 | defer_for_candidate_entry_planning | metadata_check_required_before_candidate_entry | no |
| raw_result_observation_05 | pass_to_candidate_entry_planning | candidate_entry_planning_allowed | no |

## Required Candidate Metadata Fields
| Candidate metadata field | v6.0 status |
|---|---|
| `candidate_entry_id` | required later, not populated here |
| `source_title` | required later, not populated here |
| `author_information` | required later, not populated here |
| `venue_or_repository` | required later, not populated here |
| `publication_year_or_access_date` | required later, not populated here |
| `stable_access_route` | required later, not populated here |
| `source_type` | required later, not populated here |
| `primary_or_secondary_status` | required later, not populated here |
| `linked_raw_result_observation_id` | required later, not populated here |
| `linked_screening_decision` | required later, not populated here |
| `claim_category_mapping` | required later, not populated here |
| `inclusion_rationale` | required later, not populated here |
| `exclusion_risk_notes` | required later, not populated here |
| `proposed_source_role` | required later, not populated here |
| `candidate_entry_status` | required later, not populated here |
| `audit_required_before_retention` | required later, not populated here |

## Candidate Status Values
- planned_not_created
- metadata_required
- candidate_entry_allowed_later
- deferred_until_metadata_check
- blocked_until_source_audit

## Proposed Source Role Values
- background_context
- formal_framing
- contrast_source
- boundary_clarification
- future_validation_context
- do_not_use_for_external_validation_claims

## Entry Creation Gates
- Candidate entry creation must be separate from screening execution.
- Candidate entry creation must use stable metadata.
- Candidate entry creation must link back to raw observation id.
- Candidate entry creation must link back to screening decision.
- Candidate entry creation must map to a claim category.
- Candidate entry creation must include inclusion rationale.
- Candidate entry creation must include exclusion-risk notes.
- Candidate entry creation must assign proposed source role.
- Candidate entry creation must not retain sources.
- Candidate entry creation must not add citations.
- Candidate entry creation must not populate the evidence matrix.
- Candidate entry creation must not revise the manuscript.

## Metadata Audit Requirements
- Check whether source title is stable.
- Check whether author information is available.
- Check whether venue or repository is identifiable.
- Check whether year or access date can be recorded without invention.
- Check whether access route is stable enough for later review.
- Check whether the source type can be classified.
- Check whether primary or secondary status can be determined.
- Check whether claim-category mapping is justified.
- Check whether inclusion rationale is explicit.
- Check whether exclusion-risk notes are explicit.
- Check whether proposed source role is bounded.
- Check whether source should remain outside retention until audited.

## Boundary Phrases
- research prototype with internal validation
- not externally validated
- not submission-ready
- not a final paper
- not biological guidance
- not clinical guidance
- not laboratory guidance
- not operational guidance
- candidate source entry plan is not candidate source creation
- candidate source planning is not source retention
- candidate sources are not retained sources
- retained sources are not citations
- citations are not external validation
- does not create candidate sources
- does not retain sources
- does not add citations
- does not populate the evidence matrix
- does not revise the manuscript

## Prohibited Behaviors
- Do not create candidate sources in this milestone.
- Do not retain sources in this milestone.
- Do not add citations in this milestone.
- Do not populate the evidence matrix in this milestone.
- Do not revise the manuscript in this milestone.
- Do not treat screening decisions as source entries.
- Do not treat candidate-entry planning as retention.
- Do not treat planned metadata fields as real metadata.
- Do not imply external validation.
- Do not imply submission readiness.
- Do not provide biological, clinical, laboratory, or operational guidance.

## Next Steps
- Create first candidate source entries in a later milestone.
- Populate candidate metadata only from real source records.
- Keep candidate entries separate from retained sources.
- Audit candidate metadata before retention.
- Retain sources only after candidate audit.
- Populate the evidence matrix only after retained-source audit.
- Add citations only after retained-source decision.
- Revise manuscript only after citation-grounded integration.

## Candidate Entry Interpretation
The v6.0 artifact plans the first candidate source entry workflow after the v5.9 screening execution.

The v5.9 screening execution produced three pass-to-candidate-planning decisions and two defer-to-candidate-planning decisions. That is not the same as creating candidate sources. The current artifact only defines what must be collected before candidate entries can exist.

This distinction matters because a screened raw observation still has no stable source record inside the project. It may have a title. It may look relevant. It may deserve metadata work. But it is not yet a candidate source. A project that treats screened titles as sources is not doing literature grounding; it is arranging words into a confidence costume.

## Metadata Boundary
Candidate entry creation requires real metadata.

A future candidate entry must identify a stable title, authorship information, venue or repository, year or access date when appropriate, access route, source type, primary or secondary status, linked raw observation id, linked screening decision, claim-category mapping, inclusion rationale, exclusion-risk notes, proposed source role, candidate status, and audit requirement.

None of those fields are populated in this milestone. They are only defined as required fields. This prevents a plan from masquerading as a database. Plans love doing that when nobody is watching. Very bureaucratic of them.

## Retention Boundary
Candidate source planning is not retention.

A candidate source, once created later, will still require audit before retention. Retention will require a separate decision. Only retained and audited sources may later enter the evidence matrix. Only after evidence matrix population should citation-grounded manuscript revision be considered.

The workflow therefore remains deliberately staged: screening decision, candidate entry plan, candidate entry creation, candidate metadata audit, retention decision, evidence matrix transfer, citation integration, manuscript revision. It is slow because each boundary prevents a different kind of nonsense.

## Output Counts
Candidate entry plan count: 1

Planned candidate entry row count: 5

Pass to candidate planning count: 3

Defer to candidate planning count: 2

Candidate source count: 0

Retained source count: 0

Source added count: 0

Citation added count: 0

Evidence matrix populated count: 0

Manuscript revised count: 0

## Final Boundary Statement
This artifact plans first candidate source entry.

It does not create candidate sources, does not retain sources, does not add citations, does not populate the evidence matrix, does not revise the manuscript, does not certify external validation, does not make the manuscript ready for submission, and does not provide biological, clinical, laboratory, or operational guidance.

Current status remains:

`research prototype with internal validation`
