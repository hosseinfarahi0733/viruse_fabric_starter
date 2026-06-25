# Literature Search Log Template v5.1

## Question
Can Viruse Fabric create a controlled template for future literature search logging without adding sources, adding citations, populating the evidence matrix, or revising the manuscript?

## Status
Current project status remains:

`research prototype with internal validation`

This template is not externally validated, not submission-ready, and not a final paper.

No source is added by this template. No citation is added by this template. The evidence matrix is not populated by this template. The manuscript is not revised by this template. Citation placeholders are not citations.

## Source Artifacts
| Source artifact | Exists |
|---|---|
| `outputs/literature_search_protocol_v4_7.md` | True |
| `outputs/literature_family_evidence_matrix_v4_8.md` | True |
| `outputs/claim_to_citation_readiness_map_v4_9.md` | True |
| `outputs/citation_grounded_manuscript_revision_plan_v5_0.md` | True |
| `outputs/citation_placeholder_plan_v3_9.md` | True |

## Purpose
The v5.1 template defines how future search activity should be recorded before any evidence matrix is populated.

It is a log structure, not a search result. It is a control layer between search protocol and evidence population. That sounds bureaucratic because it is, but bureaucracy is occasionally what keeps a research prototype from turning into a decorative bibliography with delusions of grandeur.

## Search Run Fields
| Search run field | Required | Purpose |
|---|---|---|
| `search_run_id` | yes | record search run id for controlled later audit |
| `search_date` | yes | record search date for controlled later audit |
| `searcher` | yes | record searcher for controlled later audit |
| `literature_family` | yes | record literature family for controlled later audit |
| `claim_category` | yes | record claim category for controlled later audit |
| `search_venue` | yes | record search venue for controlled later audit |
| `query_string` | yes | record query string for controlled later audit |
| `query_rationale` | yes | record query rationale for controlled later audit |
| `inclusion_criteria_used` | yes | record inclusion criteria used for controlled later audit |
| `exclusion_criteria_used` | yes | record exclusion criteria used for controlled later audit |
| `raw_result_count` | yes | record raw result count for controlled later audit |
| `screened_result_count` | yes | record screened result count for controlled later audit |
| `candidate_source_count` | yes | record candidate source count for controlled later audit |
| `retained_source_count` | yes | record retained source count for controlled later audit |
| `deferred_source_count` | yes | record deferred source count for controlled later audit |
| `rejected_source_count` | yes | record rejected source count for controlled later audit |
| `notes` | yes | record notes for controlled later audit |

## Candidate Source Review Fields
| Candidate source review field | Required | Purpose |
|---|---|---|
| `candidate_source_id` | yes | record candidate source id for controlled later audit |
| `source_status` | yes | record source status for controlled later audit |
| `source_role` | yes | record source role for controlled later audit |
| `title_pending` | yes | record title pending for controlled later audit |
| `author_pending` | yes | record author pending for controlled later audit |
| `year_pending` | yes | record year pending for controlled later audit |
| `venue_pending` | yes | record venue pending for controlled later audit |
| `identifier_pending` | yes | record identifier pending for controlled later audit |
| `abstract_screening_notes` | yes | record abstract screening notes for controlled later audit |
| `relevant_passage_notes` | yes | record relevant passage notes for controlled later audit |
| `claim_link` | yes | record claim link for controlled later audit |
| `evidence_strength` | yes | record evidence strength for controlled later audit |
| `boundary_effect` | yes | record boundary effect for controlled later audit |
| `decision` | yes | record decision for controlled later audit |
| `decision_rationale` | yes | record decision rationale for controlled later audit |
| `audit_notes` | yes | record audit notes for controlled later audit |

## Claim Mapping Fields
| Claim mapping field | Required | Purpose |
|---|---|---|
| `claim_id` | yes | record claim id for controlled later audit |
| `claim_text` | yes | record claim text for controlled later audit |
| `readiness_category` | yes | record readiness category for controlled later audit |
| `citation_action` | yes | record citation action for controlled later audit |
| `evidence_need` | yes | record evidence need for controlled later audit |
| `allowed_use_level` | yes | record allowed use level for controlled later audit |
| `validation_boundary` | yes | record validation boundary for controlled later audit |
| `candidate_source_id` | yes | record candidate source id for controlled later audit |
| `source_role` | yes | record source role for controlled later audit |
| `decision` | yes | record decision for controlled later audit |
| `revision_instruction` | yes | record revision instruction for controlled later audit |

## Source Status Values
| Source status value | Meaning |
|---|---|
| `unreviewed` | controlled value for later review and audit |
| `screened` | controlled value for later review and audit |
| `candidate` | controlled value for later review and audit |
| `retained` | controlled value for later review and audit |
| `deferred` | controlled value for later review and audit |
| `rejected` | controlled value for later review and audit |

## Source Role Values
| Source role value | Meaning |
|---|---|
| `background` | controlled value for later review and audit |
| `terminology` | controlled value for later review and audit |
| `comparison` | controlled value for later review and audit |
| `contrast` | controlled value for later review and audit |
| `method_context` | controlled value for later review and audit |
| `boundary_context` | controlled value for later review and audit |

## Decision Values
| Decision value | Meaning |
|---|---|
| `retain_for_later_mapping` | controlled value for later review and audit |
| `defer_pending_full_read` | controlled value for later review and audit |
| `reject_as_irrelevant` | controlled value for later review and audit |
| `reject_as_overclaim_risk` | controlled value for later review and audit |
| `reject_as_insufficient_support` | controlled value for later review and audit |

## Empty Search Run Template
| Field | Value |
|---|---|
| `search_run_id` | `SEARCH_RUN_ID_PENDING` |
| `search_date` | `DATE_PENDING` |
| `literature_family` | `FAMILY_PENDING` |
| `claim_category` | `CLAIM_CATEGORY_PENDING` |
| `search_venue` | `VENUE_PENDING` |
| `query_string` | `QUERY_STRING_PENDING` |
| `raw_result_count` | `COUNT_PENDING` |
| `candidate_source_count` | `COUNT_PENDING` |
| `retained_source_count` | `0` |
| `notes` | `NOTES_PENDING` |

## Empty Candidate Source Template
| Field | Value |
|---|---|
| `candidate_source_id` | `SOURCE_ID_PENDING` |
| `source_status` | `unreviewed` |
| `source_role` | `ROLE_PENDING` |
| `title_pending` | `TITLE_PENDING` |
| `author_pending` | `AUTHOR_PENDING` |
| `year_pending` | `YEAR_PENDING` |
| `identifier_pending` | `IDENTIFIER_PENDING` |
| `claim_link` | `CLAIM_ID_PENDING` |
| `decision` | `DECISION_PENDING` |
| `decision_rationale` | `RATIONALE_PENDING` |

## Audit Rules
- Every search run must record the exact query string.
- Every candidate source must be linked to a literature family.
- Every candidate source must be linked to at least one claim category before manuscript use.
- Every retained source must have a source role.
- Every retained source must have a decision rationale.
- No source can be cited before relevant passages are reviewed.
- No source can be used to imply external validation.
- No citation placeholder can be converted into a citation.
- No source can be inserted directly into the manuscript from this log template.
- A populated search log must be audited before evidence matrix population.

## Boundary Phrases
- research prototype with internal validation
- not externally validated
- not submission-ready
- not a final paper
- not biological guidance
- not clinical guidance
- not laboratory guidance
- not operational guidance
- citation placeholders are not citations
- no source is added by this template
- no citation is added by this template
- the evidence matrix is not populated by this template
- the manuscript is not revised by this template

## Prohibited Behaviors
- Do not add invented sources.
- Do not add invented citations.
- Do not record fake author names.
- Do not record fake identifiers.
- Do not cite unread sources.
- Do not treat search results as retained evidence.
- Do not treat a candidate source as a validated source.
- Do not use sources as decorative authority.
- Do not imply external validation from literature context.
- Do not use this template as a submission-ready bibliography.

## Next Steps
- Create a real search log file from this template.
- Run searches family by family.
- Record each query string exactly.
- Screen results using inclusion and exclusion criteria.
- Record candidate sources without citing them yet.
- Audit candidate source decisions.
- Populate the evidence matrix only after candidate audit.
- Prepare citation-grounded manuscript notes only after retained sources are mapped.

## Template Use Logic
The search log should be created before live literature search begins.

Each search run should record the exact query string, venue, family, claim category, and screening outcome. Each candidate source should remain a candidate until it is read and mapped. Retained sources should move into the evidence matrix only after audit.

This template prevents a common failure mode: finding a source, liking its title, and then letting the manuscript pretend the source already supports the claim. The human brain is very talented at mistaking familiarity for evidence, which is charming in a campfire story and useless in a manuscript.

## Relationship to Evidence Matrix
The evidence matrix remains empty until real candidate sources pass review.

The log records search activity. The matrix records evidence decisions. The manuscript uses neither directly until the relevant source role, claim link, decision value, and boundary effect are clear.

This separation matters because a search hit is not evidence. A candidate source is not a retained source. A retained source is not automatically a citation. A citation is not external validation. The project writes these distinctions repeatedly because apparently one sentence was not enough for civilization.

## Output Counts
Source added count: 0

Citation added count: 0

Populated source count: 0

Evidence matrix populated count: 0

Manuscript revised count: 0

## Final Boundary Statement
This template prepares future literature search logging.

It does not add sources, does not add citations, does not populate the evidence matrix, does not revise the manuscript, does not certify external validation, does not make the manuscript ready for submission, and does not provide biological, clinical, laboratory, or operational guidance.

Current status remains:

`research prototype with internal validation`
