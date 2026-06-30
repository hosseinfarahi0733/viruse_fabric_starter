# Citation Search Query Plan v1

## Status

Scope: draft-citation-search-query-plan-no-new-citations-no-claim-validation

This artifact creates a citation search query plan only. It does not perform source search, does not verify sources, does not add citations, does not add references, does not claim literature support, does not claim validation, and does not claim manuscript readiness.

## Purpose

The purpose of this plan is to define future search queries for verified related-work sources for VF-H2. The queries are grouped by literature bucket and are intended to support only bounded roles:

- background only,
- terminology support only,
- conceptual positioning only,
- methodological framing only.

No query result may be treated as validation evidence.

## Global Search Rules

Future source search must follow these rules:

1. Search one literature bucket at a time.
2. Prefer peer-reviewed surveys, foundational papers, methodological papers, and reputable conference papers.
3. Record exact bibliographic metadata before any source is considered.
4. Record the exact claim supported by each source.
5. Record what the source does not support.
6. Reject sources that force biological, operational, pathogen, receptor, host-range, infectivity, or immune-evasion interpretation.
7. Do not add citations until a separate source-verification artifact approves them.
8. Do not claim VF-H2 validation from literature similarity.

## Planned Query Families

### 1. Graph Dynamical Systems

Search purpose:
Find sources for conceptual positioning of finite graph state updates and discrete graph dynamics.

Planned queries:

- "graph dynamical systems discrete state updates"
- "finite graph dynamical systems local update rules"
- "dynamical systems on graphs discrete networks"
- "network dynamical systems local global update rules"
- "graph-based discrete dynamical systems survey"

Allowed future use:
Conceptual positioning only.

Forbidden future use:
Do not claim VF-H2 validation or formal equivalence.

### 2. Memory in Complex Networks

Search purpose:
Find sources for history-dependent network dynamics and memory effects.

Planned queries:

- "memory effects in complex networks"
- "history dependent dynamics in complex networks"
- "memory dependent network processes"
- "path dependent diffusion networks"
- "network dynamics with memory survey"

Allowed future use:
Conceptual framing for persistent memory.

Forbidden future use:
Do not claim that memory literature proves VF-H2.

### 3. Non-Markovian Propagation Models

Search purpose:
Find sources on non-Markovian spreading or propagation where history affects future state.

Planned queries:

- "non-Markovian spreading processes networks"
- "history dependent spreading processes"
- "non-Markovian diffusion on networks"
- "memory dependent propagation models"
- "temporal network non-Markovian spreading review"

Allowed future use:
Conceptual positioning of history-dependent propagation.

Forbidden future use:
Do not claim real-world contagion or biological relevance.

### 4. Memory-Augmented Automata and Rule-Based Toy Systems

Search purpose:
Find sources on automata or rule-based systems with memory.

Planned queries:

- "cellular automata with memory"
- "memory cellular automata review"
- "automata with history dependent rules"
- "graph cellular automata memory"
- "rule based dynamical systems with memory"

Allowed future use:
Toy-model and rule-system positioning.

Forbidden future use:
Do not claim VF-H2 is equivalent to an existing automaton class without proof.

### 5. Reservoir Computing and Echo State Networks

Search purpose:
Find sources for analogy-level discussion of memory-bearing recurrent systems.

Planned queries:

- "reservoir computing memory capacity"
- "echo state networks memory capacity"
- "recurrent state dynamics memory"
- "fading memory property reservoir computing"
- "reservoir computing survey memory"

Allowed future use:
Analogy-level positioning only.

Forbidden future use:
Do not claim VF-H2 is a reservoir computing model.

### 6. Temporal Networks and Multi-Time Indexing

Search purpose:
Find sources on time-indexed network processes and dynamic graphs.

Planned queries:

- "temporal networks survey"
- "dynamic graphs time varying networks"
- "time varying graph processes"
- "temporal network dynamics review"
- "multilayer temporal networks dynamics"

Allowed future use:
Conceptual framing of time-indexed state changes.

Forbidden future use:
Do not claim empirical validation of the three-time coordinate.

### 7. Abstract Causal Structure

Search purpose:
Find sources for cautious terminology around abstract causal structure and ordered dependencies.

Planned queries:

- "abstract causal structure discrete systems"
- "causal graph dynamics"
- "partial order dynamics discrete systems"
- "causal structure in dynamical systems"
- "causal set theory discrete order overview"

Allowed future use:
Terminology and conceptual caution.

Forbidden future use:
Do not claim VF-H2 is a causal set theory model.

### 8. Null Models and Network Science

Search purpose:
Find sources supporting null models as methodological tools.

Planned queries:

- "null models in network science"
- "network science null models review"
- "null model methodology complex networks"
- "random graph null models network analysis"
- "null models for graph dynamics"

Allowed future use:
Methodological framing for null controls.

Forbidden future use:
Do not claim that a null model proves VF-H2.

### 9. Ablation and Robustness in Computational Modeling

Search purpose:
Find sources on ablation studies, robustness checks, artifact detection, and reproducibility.

Planned queries:

- "ablation studies computational modeling"
- "robustness checks simulation studies"
- "simulation artifact detection computational experiments"
- "reproducibility computational modeling independent implementation"
- "methodological robustness computational experiments"

Allowed future use:
Methodological framing for ablation, robustness, and independent implementation-level replication.

Forbidden future use:
Do not claim external validation.

### 10. Artificial Life and Toy Models

Search purpose:
Find sources supporting toy-model positioning in artificial life or complex systems.

Planned queries:

- "artificial life toy models"
- "complex systems toy models"
- "abstract simulation models artificial life"
- "toy models in complex systems"
- "mechanism oriented toy models computational systems"

Allowed future use:
Toy-model positioning.

Forbidden future use:
Do not claim biological relevance.

## Query Execution Plan

Future execution should proceed in this order:

1. Graph dynamical systems.
2. Memory and non-Markovian network processes.
3. Memory-augmented automata.
4. Temporal networks.
5. Null models and ablation methodology.
6. Artificial life and toy-model positioning.
7. Reservoir computing analogy only if needed.
8. Abstract causal structure only if terminology remains necessary.

## Per-Source Screening Questions

For every future candidate source, answer:

1. Which literature bucket does this source belong to?
2. Is the source peer-reviewed or otherwise academically reliable?
3. What exact sentence or concept in VF-H2 can this source support?
4. What does this source not support?
5. Does the source create biological or operational interpretation risk?
6. Does the source risk implying validation?
7. Is the source being used only for background, terminology, conceptual positioning, or method framing?
8. Should the source be accepted, rejected, or held for review?

## Query Result Acceptance Gate

A query result may move to source verification only if:

- it matches a planned literature bucket,
- it is inspectable,
- it has stable bibliographic metadata,
- it supports a bounded non-validation role,
- it does not create real-bio or operational risk,
- it does not imply theory validation,
- it does not imply manuscript readiness.

## Explicit Non-Claims

This query plan does not claim:

- source search has been performed,
- sources have been verified,
- citations have been added,
- references have been added,
- literature support has been established,
- literature validation has been established,
- theory validation,
- formal proof,
- external validation,
- independent empirical validation,
- biological relevance,
- real-world relevance,
- manuscript readiness,
- submission readiness.

## Safety Boundary

Safe abstract toy model only. No real biological datasets, no real pathogen models, no receptor parameters, no operational targeting, no wet-lab protocol, no infectivity optimization, no immune evasion optimization, and no host range prediction are introduced.

## Next Allowed Action

execute_source_search_for_related_work_candidates_no_citation_insertion_no_claim_validation
