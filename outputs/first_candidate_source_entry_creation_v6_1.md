# First Candidate Source Entry Creation v6.1

## Question
Can Viruse Fabric create the first candidate source entries from the v5.9 pass-to-candidate-planning decisions while keeping retained sources, citations, evidence matrix population, and manuscript revision at zero?

## Status
Current project status remains:

`research prototype with internal validation`

This artifact is not externally validated, not submission-ready, and not a final paper.

This milestone does create candidate source entries. It does not retain sources, does not add citations, does not populate the evidence matrix, and does not revise the manuscript.

Candidate source entries are not retained sources. Candidate source entries are not citations. Candidate source entries are not external validation. Retained sources are not citations. Citations are not external validation.

## Source Artifacts
| Source artifact | Exists |
|---|---|
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

## Candidate Entry Creation Metadata
| Creation field | Value |
|---|---|
| `candidate_entry_creation_id` | CEC-0001 |
| `linked_candidate_entry_plan_id` | CEP-0001 |
| `linked_screening_execution_id` | SX-0001 |
| `linked_search_execution_id` | SE-0001 |
| `creation_status` | candidate_entries_created_not_retained |
| `literature_family` | constraint-based causality and dynamical-systems framing |
| `claim_category` | literature-needed: constraints shape possible trajectories |
| `planned_candidate_entry_row_count_from_v6_0` | 5 |
| `candidate_source_count` | 3 |
| `deferred_source_count` | 2 |
| `retained_source_count` | 0 |

## Candidate Source Entries Created
| Candidate id | Raw observation | Title | Authors | Venue or repository | Access route | Status |
|---|---|---|---|---|---|---|
| CAND-0001 | raw_result_observation_02 | Beyond Structural Causal Models: Causal Constraints Models | Tineke Blom; Stephan Bongers; Joris M. Mooij | Proceedings of Machine Learning Research / UAI proceedings; arXiv record also available | https://proceedings.mlr.press/v115/blom20a.html | candidate_created_pending_metadata_audit |
| CAND-0002 | raw_result_observation_03 | Causal screening in dynamical systems | Søren Wengel Mogensen | Proceedings of Machine Learning Research / UAI 2020 | https://proceedings.mlr.press/v124/wengel-mogensen20a.html | candidate_created_pending_metadata_audit |
| CAND-0003 | raw_result_observation_05 | Causal Structure Learning for Dynamical Systems with Theoretical Score Analysis | Nicholas Tagliapietra; Katharina Ensinger; Christoph Zimmer; Osman Mian | arXiv | https://arxiv.org/abs/2512.14361 | candidate_created_pending_metadata_audit |

## Deferred Raw Observations Not Created as Candidate Sources
| Raw observation | Title | Screening decision | Candidate source created | Reason |
|---|---|---|---|---|
| raw_result_observation_01 | Information-theoretic formulation of dynamical systems | defer_for_candidate_entry_planning | no | Deferred in v5.9; not promoted to candidate entry in v6.1. |
| raw_result_observation_04 | Causality and independence in perfectly adapted dynamical systems | defer_for_candidate_entry_planning | no | Deferred in v5.9; not promoted to candidate entry in v6.1. |

## Candidate Entry Fields
| Candidate entry field | v6.1 status |
|---|---|
| `candidate_entry_id` | populated for candidate entries only |
| `source_title` | populated for candidate entries only |
| `author_information` | populated for candidate entries only |
| `venue_or_repository` | populated for candidate entries only |
| `publication_year_or_access_date` | populated for candidate entries only |
| `stable_access_route` | populated for candidate entries only |
| `source_type` | populated for candidate entries only |
| `primary_or_secondary_status` | populated for candidate entries only |
| `linked_raw_result_observation_id` | populated for candidate entries only |
| `linked_screening_decision` | populated for candidate entries only |
| `claim_category_mapping` | populated for candidate entries only |
| `inclusion_rationale` | populated for candidate entries only |
| `exclusion_risk_notes` | populated for candidate entries only |
| `proposed_source_role` | populated for candidate entries only |
| `candidate_entry_status` | populated for candidate entries only |
| `audit_required_before_retention` | populated for candidate entries only |

## Candidate Audit Gates
- Candidate entry must link to a v5.9 raw observation.
- Candidate entry must link to a v5.9 pass-to-candidate-planning decision.
- Candidate entry must include source title.
- Candidate entry must include author information.
- Candidate entry must include venue or repository.
- Candidate entry must include publication year or access date.
- Candidate entry must include stable access route.
- Candidate entry must include source type.
- Candidate entry must include primary or secondary status.
- Candidate entry must include claim-category mapping.
- Candidate entry must include inclusion rationale.
- Candidate entry must include exclusion-risk notes.
- Candidate entry must not be treated as retained source.
- Candidate entry must not be treated as citation.

## Boundary Phrases
- research prototype with internal validation
- not externally validated
- not submission-ready
- not a final paper
- not biological guidance
- not clinical guidance
- not laboratory guidance
- not operational guidance
- candidate source entries are not retained sources
- candidate source entries are not citations
- candidate source entries are not external validation
- retained sources are not citations
- citations are not external validation
- does create candidate source entries
- does not retain sources
- does not add citations
- does not populate the evidence matrix
- does not revise the manuscript

## Prohibited Behaviors
- Do not retain sources in this milestone.
- Do not add citations in this milestone.
- Do not populate the evidence matrix in this milestone.
- Do not revise the manuscript in this milestone.
- Do not treat candidate source entries as retained sources.
- Do not treat candidate source entries as citations.
- Do not treat candidate source entries as external validation.
- Do not treat title-level relevance as sufficient for retention.
- Do not imply submission readiness.
- Do not provide biological, clinical, laboratory, or operational guidance.
- Do not convert deferred raw observations into candidate entries in this milestone.

## Next Steps
- Audit candidate source metadata in a later milestone.
- Check stable access routes before retention.
- Check source type and venue status before retention.
- Check claim-category mapping before retention.
- Check source role before retention.
- Retain sources only after candidate metadata audit.
- Populate the evidence matrix only after retained-source audit.
- Add citations only after retained-source decision.
- Revise manuscript only after citation-grounded integration.

## Candidate Entry Interpretation
The v6.1 artifact creates the first candidate source entries in the Viruse Fabric literature workflow.

This is the first milestone where candidate source count is intentionally nonzero. The count is three because only the three v5.9 pass-to-candidate-planning decisions are promoted into candidate entries. The two deferred raw observations remain outside candidate source creation.

This is progress, but it is still not retention. A candidate entry is an auditable source record. It records metadata, linkage, proposed role, and risk notes. It does not mean that the source is accepted as evidence. It does not mean the source can be cited. It does not mean the manuscript has new support.

## Metadata Integrity Boundary
Each candidate entry includes title, author information, venue or repository, year or access-date information, stable access route, source type, primary or secondary status, linked raw observation id, linked screening decision, claim-category mapping, inclusion rationale, exclusion-risk notes, proposed source role, candidate status, and audit requirement.

Those fields are sufficient for candidate entry creation, not for retention. Retention requires later audit. Source role requires later audit. Citation use requires later retained-source decision. Evidence matrix population requires later retained-source audit.

The candidate layer is a staging layer. It is allowed to be useful. It is not allowed to pretend to be evidence, because apparently even files need moral supervision now.

## Retention Boundary
Retained source count remains zero.

No candidate entry is retained in this milestone. No candidate entry is transferred to the evidence matrix. No candidate entry is used as a citation. No candidate entry changes the manuscript.

A later milestone must audit metadata before retention. The audit should check access route stability, authorship, source type, venue or repository status, claim-category fit, source role, and exclusion risk.

## Output Counts
Candidate entry creation count: 1

Candidate source count: 3

Deferred source count: 2

Retained source count: 0

Source added count: 3

Citation added count: 0

Evidence matrix populated count: 0

Manuscript revised count: 0

## Final Boundary Statement
This artifact creates first candidate source entries.

It does not retain sources, does not add citations, does not populate the evidence matrix, does not revise the manuscript, does not certify external validation, does not make the manuscript ready for submission, and does not provide biological, clinical, laboratory, or operational guidance.

Current status remains:

`research prototype with internal validation`
