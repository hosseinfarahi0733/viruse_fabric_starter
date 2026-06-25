# First Raw Result Screening Plan v5.8

## Question
Can Viruse Fabric plan the first raw-result screening step without actually screening results, creating candidate sources, retaining sources, adding citations, populating the evidence matrix, or revising the manuscript?

## Status
Current project status remains:

`research prototype with internal validation`

This artifact is not externally validated, not submission-ready, and not a final paper.

This is a screening plan, not screening execution. The screening plan does not create candidate sources, does not retain sources, does not add citations, does not populate the evidence matrix, and does not revise the manuscript.

## Source Artifacts
| Source artifact | Exists |
|---|---|
| `outputs/first_controlled_live_search_execution_v5_7.md` | True |
| `outputs/first_search_run_artifact_audit_v5_6.md` | True |
| `outputs/first_search_run_artifact_v5_5.md` | True |
| `outputs/first_literature_family_search_plan_v5_4.md` | True |
| `outputs/literature_search_log_empty_v5_2.md` | True |
| `outputs/literature_search_log_template_v5_1.md` | True |
| `outputs/claim_to_citation_readiness_map_v4_9.md` | True |
| `outputs/literature_family_evidence_matrix_v4_8.md` | True |

## Screening Plan Metadata
| Screening plan field | Value |
|---|---|
| `screening_plan_id` | SP-0001 |
| `linked_execution_id` | SE-0001 |
| `linked_shell_id` | SR-0001-SHELL |
| `plan_status` | planned_not_executed |
| `literature_family` | constraint-based causality and dynamical-systems framing |
| `claim_category` | literature-needed: constraints shape possible trajectories |
| `raw_result_count_from_v5_7` | 23 |
| `raw_result_observation_count_from_v5_7` | 5 |
| `screened_result_count` | 0 |
| `candidate_source_count` | 0 |
| `retained_source_count` | 0 |

## Raw Observations to Be Screened Later
- raw_result_observation_01
- raw_result_observation_02
- raw_result_observation_03
- raw_result_observation_04
- raw_result_observation_05

## Screening Fields
| Screening field | v5.8 status |
|---|---|
| `raw_result_observation_id` | planned for later screening execution |
| `raw_result_title` | planned for later screening execution |
| `stable_access_route_present` | planned for later screening execution |
| `metadata_sufficiency` | planned for later screening execution |
| `claim_category_alignment` | planned for later screening execution |
| `conceptual_relevance` | planned for later screening execution |
| `source_type` | planned for later screening execution |
| `primary_or_secondary_status` | planned for later screening execution |
| `inclusion_reason` | planned for later screening execution |
| `exclusion_risk` | planned for later screening execution |
| `candidate_source_recommendation` | planned for later screening execution |
| `review_notes` | planned for later screening execution |

## Planned Screening Rows
| Raw observation id | Screening status | Candidate source status |
|---|---|---|
| raw_result_observation_01 | planned_not_screened | not_created |
| raw_result_observation_02 | planned_not_screened | not_created |
| raw_result_observation_03 | planned_not_screened | not_created |
| raw_result_observation_04 | planned_not_screened | not_created |
| raw_result_observation_05 | planned_not_screened | not_created |

## Inclusion Criteria
- The result must address constraints, causality, dynamical systems, causal structure, or state-space reasoning.
- The result must connect to the selected literature family.
- The result must map to at least one v4.9 claim category.
- The result must have enough metadata for later candidate-source logging.
- The result must be more than a keyword-only match.
- The result must support either background, contrast, formal framing, or boundary clarification.
- The result must be reviewable without inventing bibliographic details.
- The result must be separable from biological, clinical, laboratory, or operational guidance claims.

## Exclusion Criteria
- Exclude results that only share vocabulary without conceptual relevance.
- Exclude results with insufficient metadata for controlled logging.
- Exclude results that would require invented authors, titles, venues, years, or identifiers.
- Exclude results that imply external validation of Viruse Fabric.
- Exclude results that push the project toward biological, clinical, laboratory, or operational guidance.
- Exclude results that cannot be mapped to a claim category.
- Exclude results that are useful only as decorative authority.
- Exclude results that cannot be responsibly reviewed in a later source audit.

## Screening Steps
- Confirm the raw observation exists in the v5.7 execution artifact.
- Copy the raw title into the screening worksheet only as a raw observation.
- Check whether metadata are sufficient for later candidate-source logging.
- Check conceptual relevance against the selected literature family.
- Check alignment with the v4.9 claim category.
- Apply inclusion criteria.
- Apply exclusion criteria.
- Assign a non-binding screening recommendation.
- Keep candidate source count at zero.
- Record that actual screening has not yet been executed.

## Screening Recommendation Values
- pending_screening
- possible_candidate_later
- defer_for_metadata_check
- exclude_later_if_keyword_only
- exclude_later_if_boundary_risk

## Screening Gates
- Screening must be planned before execution.
- Raw observations must remain raw observations.
- Screening status must remain planned_not_screened in this milestone.
- Candidate source status must remain not_created.
- Candidate source count must remain zero.
- Retained source count must remain zero.
- Citation added count must remain zero.
- Evidence matrix populated count must remain zero.
- Manuscript revised count must remain zero.
- No source may be treated as retained during this milestone.
- No raw result title may be treated as a citation.
- No raw result may be treated as external validation.

## Boundary Phrases
- research prototype with internal validation
- not externally validated
- not submission-ready
- not a final paper
- not biological guidance
- not clinical guidance
- not laboratory guidance
- not operational guidance
- raw results are not candidate sources
- candidate sources are not retained sources
- retained sources are not citations
- citations are not external validation
- screening plan is not screening execution
- does not create candidate sources
- does not add citations
- does not populate the evidence matrix
- does not revise the manuscript

## Prohibited Behaviors
- Do not screen raw results in this milestone.
- Do not create candidate sources in this milestone.
- Do not retain sources in this milestone.
- Do not add citations in this milestone.
- Do not populate the evidence matrix in this milestone.
- Do not revise the manuscript in this milestone.
- Do not treat raw result titles as evidence.
- Do not treat raw snippets as source audit.
- Do not imply external validation.
- Do not imply submission readiness.
- Do not provide biological, clinical, laboratory, or operational guidance.

## Next Steps
- Execute the first raw-result screening in a later milestone.
- Apply inclusion criteria to each raw observation.
- Apply exclusion criteria to each raw observation.
- Record screening decisions explicitly.
- Create candidate source entries only after screening execution.
- Audit candidate source metadata before retention.
- Retain sources only after candidate audit.
- Populate evidence matrix only after retained-source audit.

## Screening Interpretation
The v5.8 artifact prepares a screening procedure for the raw observations recorded in v5.7.

It does not screen them. It does not say any raw observation is useful. It does not say any raw observation is reliable. It does not say any raw observation should become a candidate source. It only defines how those questions should be asked later.

This matters because the raw result stage is where projects often become sloppy. A search result looks relevant, then someone treats it as a source. A source looks impressive, then someone treats it as support. Support looks convenient, then someone treats it as validation. This is how academic fog machines are built.

## Screening Boundary
Screening will be the first interpretive filter after live search.

The screening step must distinguish vocabulary overlap from conceptual relevance. It must distinguish a pointer from a source record. It must distinguish a possible candidate from a retained source. It must check metadata sufficiency before any candidate entry exists. The point is not to reject everything. The point is to stop the project from accepting things before it knows what they are.

The five raw observations from v5.7 are therefore treated as planned screening targets only. They are not candidate sources. They are not retained sources. They are not citations. They are not evidence matrix rows. They are not manuscript support.

## Candidate Boundary
A candidate source may only be created after screening execution.

A future candidate source entry should include enough metadata to be audited: stable title, author information when available, venue or repository, year or access date when appropriate, access route, claim-category mapping, inclusion rationale, exclusion risks, and proposed source role. Without that metadata, a result cannot responsibly enter the evidence workflow.

This milestone intentionally keeps candidate source count at zero. That is not a weakness. It is a boundary. A workflow that cannot tolerate zero counts before evidence exists is not a workflow; it is wishful thinking with headings.

## Output Counts
Raw result count: 23

Raw result observation count: 5

Screening plan count: 1

Screening execution count: 0

Screened result count: 0

Candidate source count: 0

Retained source count: 0

Source added count: 0

Citation added count: 0

Evidence matrix populated count: 0

Manuscript revised count: 0

## Final Boundary Statement
This artifact plans the first raw-result screening step.

It does not screen raw results, does not create candidate sources, does not retain sources, does not add citations, does not populate the evidence matrix, does not revise the manuscript, does not certify external validation, does not make the manuscript ready for submission, and does not provide biological, clinical, laboratory, or operational guidance.

Current status remains:

`research prototype with internal validation`
