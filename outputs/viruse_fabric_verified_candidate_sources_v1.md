# Verified Candidate Sources v1

## Status

Scope: verify-candidate-sources-no-citation-insertion-no-claim-validation

This artifact verifies candidate-source records only. It does not insert citations, does not add references, does not claim literature support, does not claim validation, and does not claim manuscript readiness.

## Verification Summary

- candidate_source_record_count: 14
- verified_candidate_record_count: 14
- accepted_for_future_related_work_count: 11
- hold_for_review_count: 2
- rejected_for_current_related_work_count: 1
- citation_inserted_count: 0
- reference_added_count: 0
- literature_support_claim_made: False
- literature_validation_claim_made: False

## Boundary

Verified candidate records are not inserted citations. They are not manuscript references. They do not validate VF-H2. They only define which sources may later be used for bounded roles after citation-insertion review.

## Safety Boundary

Safe abstract toy model only. No real biological datasets, no real pathogen models, no receptor parameters, no operational targeting, no wet-lab protocol, no infectivity optimization, no immune evasion optimization, and no host range prediction are introduced.

## Next Allowed Action

draft_citation_insertion_plan_from_verified_sources_no_claim_validation


## Verified Candidate Source Records

### SRC-CAND-GDS-001: Parallel Dynamical Systems over Graphs and Related Topics: A Survey

- verification_decision: verified_accept_for_future_related_work
- source_type: peer_reviewed_survey_article
- authors: Juan A. Aledo; Silvia Martinez; Jose C. Valverde
- venue: Journal of Applied Mathematics
- year: 2015
- volume_issue_pages: 2015, Article ID 594294, 1-14
- doi_or_stable_identifier: 10.1155/2015/594294
- literature_bucket: graph dynamical systems
- claim_supported: Graph-based discrete/parallel dynamical systems can be used as conceptual background for abstract finite graph update systems.
- claim_not_supported: Does not validate VF-H2, does not prove ledger_effect_size, and does not establish formal equivalence.
- allowed_use: conceptual positioning only
- forbidden_use: VF-H2 validation; Viruse Fabric theory validation; formal proof; manuscript readiness
- overextension_risk: low
- include_in_related_work: True
- citation_inserted: False
- reference_added: False

### SRC-CAND-GDS-002: Finite Dynamical Systems: A Mathematical Framework for Computer Simulation

- verification_decision: verified_accept_for_future_related_work
- source_type: conference_chapter
- authors: A. S. Jarrah; R. Laubenbacher
- venue: Mathematical Modeling, Simulation, Visualization and e-Learning
- year: 2008
- volume_issue_pages: pp. 343-358
- doi_or_stable_identifier: 10.1007/978-3-540-74339-2_21
- literature_bucket: graph dynamical systems
- claim_supported: Finite dynamical systems provide a mathematical simulation framework relevant to discrete abstract systems.
- claim_not_supported: Does not validate VF-H2 and does not support any biological or real-world claim.
- allowed_use: background only
- forbidden_use: validation claim; formal proof claim; real-world relevance claim
- overextension_risk: low
- include_in_related_work: True
- citation_inserted: False
- reference_added: False

### SRC-CAND-TEMP-001: Temporal Networks

- verification_decision: verified_accept_for_future_related_work
- source_type: peer_reviewed_review_article
- authors: Petter Holme; Jari Saramäki
- venue: Physics Reports
- year: 2012
- volume_issue_pages: 519(3), 97-125
- doi_or_stable_identifier: 10.1016/j.physrep.2012.03.001
- literature_bucket: temporal networks
- claim_supported: Temporal networks provide conceptual background for time-indexed network structure and dynamics.
- claim_not_supported: Does not empirically validate the VF-H2 three-time coordinate.
- allowed_use: conceptual positioning only
- forbidden_use: three-time coordinate validation; real-world validation; biological interpretation
- overextension_risk: medium
- include_in_related_work: True
- citation_inserted: False
- reference_added: False

### SRC-CAND-MEM-001: The shape of memory in temporal networks

- verification_decision: verified_accept_for_future_related_work
- source_type: peer_reviewed_article
- authors: Oliver E. Williams; Lucas Lacasa; Ana P. Millán; Vito Latora; et al.
- venue: Nature Communications
- year: 2022
- volume_issue_pages: 13, Article 499
- doi_or_stable_identifier: 10.1038/s41467-022-28123-z
- literature_bucket: memory in temporal networks
- claim_supported: Temporal-network memory can be structured and nontrivial, supporting cautious conceptual framing of memory.
- claim_not_supported: Does not validate the persistent memory ledger or ledger_effect_size.
- allowed_use: conceptual positioning only
- forbidden_use: VF-H2 validation; ledger_effect_size validation; real-network generalization
- overextension_risk: medium
- include_in_related_work: True
- citation_inserted: False
- reference_added: False

### SRC-CAND-NM-001: From networks to optimal higher-order models of complex systems

- verification_decision: verified_accept_for_future_related_work
- source_type: peer_reviewed_perspective_article
- authors: Renaud Lambiotte; Martin Rosvall; Ingo Scholtes
- venue: Nature Physics
- year: 2019
- volume_issue_pages: 15(4), 313-320
- doi_or_stable_identifier: 10.1038/s41567-019-0459-y
- literature_bucket: non-Markovian network processes
- claim_supported: Higher-order models can conceptually frame path/history-dependent network representations.
- claim_not_supported: Does not show VF-H2 is a higher-order network model and does not validate VF-H2.
- allowed_use: conceptual positioning only
- forbidden_use: formal equivalence; validation; external empirical support
- overextension_risk: medium
- include_in_related_work: True
- citation_inserted: False
- reference_added: False

### SRC-CAND-NM-002: Equivalence between non-Markovian and Markovian dynamics in epidemic spreading processes

- verification_decision: verified_reject_for_current_related_work_due_boundary_risk
- source_type: peer_reviewed_article
- authors: Michele Starnini; James P. Gleeson; Marián Boguñá
- venue: Physical Review Letters
- year: 2017
- volume_issue_pages: 118, 128301
- doi_or_stable_identifier: 10.1103/PhysRevLett.118.128301
- literature_bucket: non-Markovian network processes
- claim_supported: Could support abstract non-Markovian process background only.
- claim_not_supported: Cannot be used for VF-H2 because epidemic spreading language creates biological/real-world boundary risk.
- allowed_use: none_in_current_related_work
- forbidden_use: biological framing; epidemic analogy; host/pathogen interpretation; VF-H2 validation
- overextension_risk: high
- include_in_related_work: False
- citation_inserted: False
- reference_added: False

### SRC-CAND-CA-001: Cellular Automata with Memory

- verification_decision: verified_hold_for_bibliographic_review
- source_type: academic_book_candidate
- authors: Ramon Alonso-Sanz
- venue: Old City Publishing / book candidate
- year: 2008
- volume_issue_pages: book metadata requires final catalog verification
- doi_or_stable_identifier: ISBN/metadata_to_verify_before_use
- literature_bucket: memory-augmented automata
- claim_supported: Could support the existence of memory-augmented cellular automata as a concept.
- claim_not_supported: Does not establish VF-H2 as a cellular automaton class.
- allowed_use: hold_only
- forbidden_use: citation insertion before metadata verification; formal equivalence; validation
- overextension_risk: medium
- include_in_related_work: False
- citation_inserted: False
- reference_added: False

### SRC-CAND-CA-002: Designing Complex Dynamics in Cellular Automata with Memory

- verification_decision: verified_accept_for_future_related_work
- source_type: peer_reviewed_article
- authors: Genaro J. Martínez; Andrew Adamatzky; Ramon Alonso-Sanz
- venue: International Journal of Bifurcation and Chaos
- year: 2013
- volume_issue_pages: 23(10), 1330035
- doi_or_stable_identifier: 10.1142/S0218127413300358
- literature_bucket: memory-augmented automata
- claim_supported: Memory can alter dynamics in cellular automata, useful for toy/rule-system positioning.
- claim_not_supported: Does not prove or validate VF-H2 and does not establish formal equivalence.
- allowed_use: conceptual positioning only
- forbidden_use: formal equivalence; VF-H2 validation; theory validation
- overextension_risk: medium
- include_in_related_work: True
- citation_inserted: False
- reference_added: False

### SRC-CAND-RC-001: Echo State Network

- verification_decision: verified_accept_for_future_related_work
- source_type: scholarly_encyclopedia_article
- authors: Herbert Jaeger
- venue: Scholarpedia
- year: 2007
- volume_issue_pages: 2(9), 2330
- doi_or_stable_identifier: 10.4249/scholarpedia.2330
- literature_bucket: reservoir-style memory
- claim_supported: Echo state networks can provide terminology-level background for reservoir/recurrent-state analogy.
- claim_not_supported: Does not imply VF-H2 is an echo state network.
- allowed_use: terminology support only
- forbidden_use: model equivalence; validation; reservoir-computing claim
- overextension_risk: low
- include_in_related_work: True
- citation_inserted: False
- reference_added: False

### SRC-CAND-RC-002: Memory Capacity of Input-Driven Echo State Networks at the Edge of Chaos

- verification_decision: verified_accept_for_future_related_work
- source_type: conference_chapter
- authors: Peter Barančok; Igor Farkaš
- venue: Artificial Neural Networks and Machine Learning - ICANN 2014
- year: 2014
- volume_issue_pages: LNCS 8681, 41-48
- doi_or_stable_identifier: 10.1007/978-3-319-11179-7_6
- literature_bucket: reservoir-style memory
- claim_supported: Can support terminology around memory capacity in echo state networks.
- claim_not_supported: Does not imply VF-H2 has reservoir-computing memory capacity.
- allowed_use: terminology support only
- forbidden_use: VF-H2 reservoir claim; validation; formal proof
- overextension_risk: low
- include_in_related_work: True
- citation_inserted: False
- reference_added: False

### SRC-CAND-NULL-001: Null models in network neuroscience

- verification_decision: verified_accept_for_future_related_work
- source_type: peer_reviewed_review_article
- authors: František Váša; Bratislav Mišić
- venue: Nature Reviews Neuroscience
- year: 2022
- volume_issue_pages: 23(8), 493-504
- doi_or_stable_identifier: 10.1038/s41583-022-00601-9
- literature_bucket: null models and network science
- claim_supported: Can support methodological framing of null models as benchmarking tools in network contexts.
- claim_not_supported: Does not prove VF-H2 and does not validate the no-persistent-memory null control.
- allowed_use: methodological framing only
- forbidden_use: proof claim; validation claim; neuroscience analogy overextension
- overextension_risk: medium
- include_in_related_work: True
- citation_inserted: False
- reference_added: False

### SRC-CAND-ROB-001: Moving towards reproducible machine learning

- verification_decision: verified_accept_for_future_related_work
- source_type: editorial
- authors: Nature Computational Science Editorial Board
- venue: Nature Computational Science
- year: 2021
- volume_issue_pages: 1, 629-630
- doi_or_stable_identifier: 10.1038/s43588-021-00152-6
- literature_bucket: ablation robustness reproducibility
- claim_supported: Can support general reproducibility-reporting motivation in computational work.
- claim_not_supported: Does not validate VF-H2 or establish empirical replication.
- allowed_use: methodological framing only
- forbidden_use: validation; external replication; manuscript readiness
- overextension_risk: medium
- include_in_related_work: True
- citation_inserted: False
- reference_added: False

### SRC-CAND-ROB-002: A Protocol for Structured Robustness Reproductions and Replicability Assessments

- verification_decision: verified_accept_for_future_related_work_with_domain_caution
- source_type: peer_reviewed_article
- authors: J. Ankel-Peters; et al.
- venue: Q Open
- year: 2025
- volume_issue_pages: article metadata to finalize before citation insertion
- doi_or_stable_identifier: 10.1093/qopen/qoaf004
- literature_bucket: ablation robustness reproducibility
- claim_supported: Can support general structured robustness/replicability discussion with domain caution.
- claim_not_supported: Does not validate VF-H2 and does not establish independent empirical validation.
- allowed_use: methodological framing only
- forbidden_use: external validation; field-equivalence; empirical support claim
- overextension_risk: medium_high_due_economics_domain_transfer
- include_in_related_work: True
- citation_inserted: False
- reference_added: False

### SRC-CAND-ALIFE-001: Complex Systems and Artificial Life: A Decade's Overview

- verification_decision: verified_hold_for_scope_review
- source_type: conference_paper
- authors: Thomas McAtee; Claudia Szabo
- venue: ALIFE 2019: The 2019 Conference on Artificial Life
- year: 2019
- volume_issue_pages: pp. 263-270
- doi_or_stable_identifier: 10.1162/isal_a_00172
- literature_bucket: artificial life and toy models
- claim_supported: Could support broad artificial-life positioning if scope remains useful.
- claim_not_supported: Does not validate VF-H2, biological relevance, or real-world relevance.
- allowed_use: hold_only_pending_scope_review
- forbidden_use: biological relevance; real-world relevance; validation
- overextension_risk: medium_due_low_citation_and_broad_scope
- include_in_related_work: False
- citation_inserted: False
- reference_added: False
