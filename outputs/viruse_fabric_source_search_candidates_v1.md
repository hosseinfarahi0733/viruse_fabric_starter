# Source Search Candidates v1

## Status

Scope: execute-source-search-for-related-work-candidates-no-citation-insertion-no-claim-validation

This artifact records source-search candidates only. It does not verify sources, does not insert citations, does not add references, does not claim literature support, does not claim validation, and does not claim manuscript readiness.

## Candidate Summary

- source_search_performed: True
- candidate_source_count: 14
- pending_verification_count: 13
- hold_for_review_count: 1
- sources_verified: 0
- citations_added: 0
- references_added: 0
- literature_support_claim_made: False
- literature_validation_claim_made: False

## Candidate Buckets Covered

- graph dynamical systems
- temporal networks
- memory in temporal networks
- non-Markovian network processes
- memory-augmented automata
- reservoir-style memory
- null models and network science
- ablation robustness reproducibility
- artificial life and toy models

## Boundary

These candidates may only be used for future source verification. They are not citations in the technical note. They are not references in the manuscript. They do not validate VF-H2.

## Safety Boundary

Safe abstract toy model only. No real biological datasets, no real pathogen models, no receptor parameters, no operational targeting, no wet-lab protocol, no infectivity optimization, no immune evasion optimization, and no host range prediction are introduced.

## Next Allowed Action

verify_candidate_sources_no_citation_insertion_no_claim_validation


## Candidate Sources

### SRC-CAND-GDS-001: Parallel Dynamical Systems over Graphs and Related Topics

- bucket: graph dynamical systems
- candidate_source_type: peer-reviewed article candidate
- candidate_role: conceptual positioning only
- verification_status: not_verified
- include_in_related_work: pending_verification
- citation_inserted: False
- reference_added: False
- allowed_future_use: Frame VF-H2 as an abstract graph-based discrete dynamical system.
- forbidden_future_use: Do not use as VF-H2 validation, formal equivalence, or proof.
- risk: low_if_used_for_graph_dynamics_positioning_only

### SRC-CAND-GDS-002: Finite Dynamical Systems: A Mathematical Framework for Computer Simulation

- bucket: graph dynamical systems
- candidate_source_type: academic book chapter candidate
- candidate_role: conceptual positioning only
- verification_status: not_verified
- include_in_related_work: pending_verification
- citation_inserted: False
- reference_added: False
- allowed_future_use: Support terminology around finite dynamical systems.
- forbidden_future_use: Do not use as evidence that VF-H2 is validated.
- risk: low_if_used_for_background_only

### SRC-CAND-TEMP-001: Temporal Networks

- bucket: temporal networks
- candidate_source_type: review article candidate
- candidate_role: conceptual positioning only
- verification_status: not_verified
- include_in_related_work: pending_verification
- citation_inserted: False
- reference_added: False
- allowed_future_use: Frame the three-time coordinate cautiously near temporal-network concepts.
- forbidden_future_use: Do not claim empirical validation of VF-H2 or the three-time coordinate.
- risk: medium_due_possible_real_world_examples_use_abstractly_only

### SRC-CAND-MEM-001: The shape of memory in temporal networks

- bucket: memory in temporal networks
- candidate_source_type: peer-reviewed article candidate
- candidate_role: conceptual positioning only
- verification_status: not_verified
- include_in_related_work: pending_verification
- citation_inserted: False
- reference_added: False
- allowed_future_use: Support the need to treat memory structure carefully.
- forbidden_future_use: Do not use as validation of ledger_effect_size or VF-H2.
- risk: medium_due_real_network_examples_do_not_generalize

### SRC-CAND-NM-001: From networks to optimal higher-order models of complex systems

- bucket: non-Markovian network processes
- candidate_source_type: peer-reviewed article candidate
- candidate_role: conceptual positioning only
- verification_status: not_verified
- include_in_related_work: pending_verification
- citation_inserted: False
- reference_added: False
- allowed_future_use: Frame history/path dependence without claiming equivalence.
- forbidden_future_use: Do not claim VF-H2 is a higher-order network model unless formally shown.
- risk: medium_due_possible_empirical_network_context

### SRC-CAND-NM-002: Equivalence between Non-Markovian and Markovian Dynamics in Epidemic Spreading Processes

- bucket: non-Markovian network processes
- candidate_source_type: peer-reviewed article candidate
- candidate_role: background only
- verification_status: not_verified_high_boundary_risk
- include_in_related_work: hold_for_review
- citation_inserted: False
- reference_added: False
- allowed_future_use: Use only for abstract non-Markovian process context if verified and carefully bounded.
- forbidden_future_use: Do not use for biological, epidemiological, pathogen, or real-world claims.
- risk: high_due_epidemic_spreading_language

### SRC-CAND-CA-001: Cellular Automata with Memory

- bucket: memory-augmented automata
- candidate_source_type: academic book or reference entry candidate
- candidate_role: conceptual positioning only
- verification_status: not_verified
- include_in_related_work: pending_verification
- citation_inserted: False
- reference_added: False
- allowed_future_use: Frame VF-H2 near memory-augmented rule-based toy systems.
- forbidden_future_use: Do not claim VF-H2 is a cellular automaton class.
- risk: low_if_used_as_toy_model_positioning_only

### SRC-CAND-CA-002: Designing Complex Dynamics in Cellular Automata with Memory

- bucket: memory-augmented automata
- candidate_source_type: preprint or conference-style candidate
- candidate_role: conceptual positioning only
- verification_status: not_verified
- include_in_related_work: pending_verification
- citation_inserted: False
- reference_added: False
- allowed_future_use: Use cautiously for toy/rule-based memory discussion.
- forbidden_future_use: Do not treat as settled validation or formal equivalence.
- risk: medium_due_preprint_status_check_needed

### SRC-CAND-RC-001: Echo State Network

- bucket: reservoir-style memory
- candidate_source_type: scholarly encyclopedia article candidate
- candidate_role: terminology support only
- verification_status: not_verified
- include_in_related_work: pending_verification
- citation_inserted: False
- reference_added: False
- allowed_future_use: Use only as analogy for memory-bearing recurrent state.
- forbidden_future_use: Do not claim VF-H2 is an echo state network or reservoir model.
- risk: low_if_used_as_analogy_only

### SRC-CAND-RC-002: Memory Capacity of Input-Driven Echo State Networks at the Edge of Chaos

- bucket: reservoir-style memory
- candidate_source_type: conference or book chapter candidate
- candidate_role: terminology support only
- verification_status: not_verified
- include_in_related_work: pending_verification
- citation_inserted: False
- reference_added: False
- allowed_future_use: Use only for memory-capacity vocabulary if verified.
- forbidden_future_use: Do not claim VF-H2 has reservoir-computing memory capacity.
- risk: low_if_used_for_terminology_only

### SRC-CAND-NULL-001: Null models in network neuroscience

- bucket: null models and network science
- candidate_source_type: peer-reviewed review article candidate
- candidate_role: methodological framing only
- verification_status: not_verified
- include_in_related_work: pending_verification
- citation_inserted: False
- reference_added: False
- allowed_future_use: Frame why VF-H2 uses no-persistent-memory null controls.
- forbidden_future_use: Do not claim null models prove VF-H2.
- risk: medium_due_domain_specificity_network_neuroscience

### SRC-CAND-ROB-001: Moving towards reproducible machine learning

- bucket: ablation robustness reproducibility
- candidate_source_type: peer-reviewed commentary or perspective candidate
- candidate_role: methodological framing only
- verification_status: not_verified
- include_in_related_work: pending_verification
- citation_inserted: False
- reference_added: False
- allowed_future_use: Frame ablation and reproducibility norms cautiously.
- forbidden_future_use: Do not claim VF-H2 is validated because it passed ablations.
- risk: medium_due_machine_learning_domain_not_exact_match

### SRC-CAND-ROB-002: A protocol for structured robustness reproductions and replicability discussions

- bucket: ablation robustness reproducibility
- candidate_source_type: peer-reviewed article candidate
- candidate_role: methodological framing only
- verification_status: not_verified
- include_in_related_work: pending_verification
- citation_inserted: False
- reference_added: False
- allowed_future_use: Use only for general robustness/reproducibility framing if verified.
- forbidden_future_use: Do not claim independent empirical validation.
- risk: medium_due_field_transfer_check_needed

### SRC-CAND-ALIFE-001: Complex Systems and Artificial Life: A Decade's Overview

- bucket: artificial life and toy models
- candidate_source_type: conference paper or review-style candidate
- candidate_role: background only
- verification_status: not_verified
- include_in_related_work: pending_verification
- citation_inserted: False
- reference_added: False
- allowed_future_use: Frame VF-H2 as abstract toy-model work.
- forbidden_future_use: Do not claim biological or real-world relevance.
- risk: medium_due_low_citation_and_scope_check_needed
