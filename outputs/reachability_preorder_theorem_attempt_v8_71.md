# Reachability Preorder Theorem Attempt v8.71

## Purpose

Execute a limited theorem-level proof showing that the reachability relation induced by finite R-paths is reflexive and transitive, while keeping proof assistant verification, completed formalization, completed definitions, framework-level proof, proof gap resolution, external validation, citation addition, and manuscript submission readiness counts at zero.

## Source artifact

- Source artifact: `outputs/limited_theorem_pair_boundary_audit_v8_70.md`
- Source artifact count: 1
- Missing source artifact count: 0

## Theorem proof row

| Theorem ID | Theorem name | Depends on | Formal context | Statement | Proof steps | Proof status | Boundary status |
|---|---|---|---|---|---|---|---|
| PKT-003 | Finite R-path reachability preorder theorem | LMP-003 singleton path admissibility; LMP-002 endpoint-compatible concatenation closure; PKT-001 finite R-path kernel closure theorem; PKT-002 finite R-path concatenation identity theorem | Let S be a nonempty state space and let R be a binary relation on S. Define Reach_R(a,b) to hold exactly when there exists a finite R-path p = (s_0, ..., s_n) with s_0 = a and s_n = b. | The relation Reach_R is reflexive and transitive on S; therefore Reach_R is a preorder on S. | 1) Reflexivity: fix any state a in S. 2) By LMP-003, the singleton sequence (a) is a finite R-path. 3) The singleton path starts at a and ends at a, so Reach_R(a,a) holds. 4) Because a was arbitrary, Reach_R is reflexive on S. 5) Transitivity: assume Reach_R(a,b) and Reach_R(b,c). 6) Then there exists a finite R-path p from a to b and a finite R-path q from b to c. 7) The final state of p equals b and the initial state of q equals b, so p and q are endpoint-compatible. 8) By LMP-002, the concatenation of p and q is a finite R-path. 9) That concatenated path starts at a and ends at c, so Reach_R(a,c) holds. 10) Therefore Reach_R is transitive. 11) Since Reach_R is both reflexive and transitive, Reach_R is a preorder on S. | manual limited theorem proof executed for finite R-path reachability preorder | not machine-checked; not framework-level proof; not completed formalization |

## Counts

- Reachability preorder theorem attempt count: 1
- Theorem attempt count: 1
- Theorem statement count: 1
- Theorem proof execution count: 1
- New theorem proven count: 1
- Carried cumulative limited theorem proven count: 2
- Cumulative limited theorem proven count: 3
- Reachability relation definition count: 1
- Preorder property count: 2
- Lemma dependency count: 4
- Proof assistant verification count: 0
- Formalization complete count: 0
- Completed formal definition count: 0
- Definition completion execution count: 0
- Full framework formal proof count: 0
- Formal mathematical proof count: 0
- Formal proof execution count: 0
- Proof execution count: 1
- Proof gap resolution count: 0
- Manuscript submission ready count: 0
- Readiness approval count: 0
- External validation count: 0
- Independent experiment count: 0
- New citation added count: 0

## Carried v8.70 signals

- Carried limited theorem pair boundary audit count: 1
- Carried audited limited theorem count: 2
- Carried new theorem proven count: 0
- Carried proof execution count: 0
- Carried proof assistant verification count: 0
- Carried formalization complete count: 0
- Carried completed formal definition count: 0
- Carried definition completion execution count: 0
- Carried full framework formal proof count: 0
- Carried proof gap resolution count: 0
- Carried external validation count: 0
- Carried new citation added count: 0

## Boundary interpretation

The v8.71 artifact proves one additional limited theorem about the reachability relation induced by finite R-paths. It does not provide proof assistant verification, does not complete formalization, does not complete all formal definitions, does not establish a framework-level proof, does not resolve project-wide proof gaps, does not add citations, does not provide external validation, and does not make the manuscript submission-ready.

## Critical reviewer note

PKT-003 is important because it turns finite R-path existence into a preorder relation. It remains a local path-kernel theorem, not a complete theory result.

## Warnings

- One additional limited finite R-path theorem is manually proven, while proof assistant verification remains absent.
- The theorem is about the reachability relation induced by finite R-paths only.
- This is not a framework-level proof.
- External validation and manuscript submission readiness remain absent.

## Safe claim

The project has executed one additional limited manual theorem proof showing that finite R-path reachability is a preorder, bringing the cumulative limited theorem count to three while keeping proof assistant verification, completed formalization, completed definitions, framework-level proof, proof gap resolution, citation additions, external validation, and manuscript submission readiness at zero.

## Next step discipline

- Do not call this proof assistant verification.
- Do not call this completed formalization.
- Do not call this completed formal definitions.
- Do not call this framework-level proof.
- Do not call this proof gap resolution.
- Do not call this external validation.
- Do not call this manuscript submission readiness.
