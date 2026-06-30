# VF-H2 Mathematical Core Formalization v1

## 1. Scope

This document formalizes the mathematical core of VF-H2 as a safe abstract toy model. It does not provide a formal proof, theory validation, external validation, biological validation, manuscript readiness, or submission readiness.

VF-H2 is formalized as a memory-ledger-driven abstract propagation model over a finite graph-like state space. The goal is to define the objects used in the toy framework clearly enough that future tests, proofs, or technical notes can refer to a stable mathematical core.

## 2. Finite Abstract Space

Let

\[
G = (V, E)
\]

be a finite directed or undirected abstract graph, where \(V\) is a finite set of nodes and \(E \subseteq V \times V\) is an abstract adjacency relation.

No node represents a biological host, receptor, cell, organism, pathogen, or real-world target. The graph is only an abstract state space.

## 3. Three-Time Coordinate

A propagation state is indexed by a three-time coordinate

\[
\tau = (t_1, t_2, t_3) \in \mathbb{T}_1 \times \mathbb{T}_2 \times \mathbb{T}_3.
\]

For the current toy implementation, this can be reduced to a discrete execution index \(k\), but the formal model keeps the three-time structure explicit:

- \(t_1\): local update time,
- \(t_2\): ledger accumulation time,
- \(t_3\): projection or observation time.

The reduced toy case uses a mapping

\[
k \mapsto \tau_k = (t_{1,k}, t_{2,k}, t_{3,k}).
\]

## 4. Abstract Packets and State

Let \(P_\tau\) be a finite multiset of abstract packets at time \(\tau\). Each packet \(p \in P_\tau\) has an abstract location

\[
\ell_\tau(p) \in V.
\]

The node state is represented by

\[
x_\tau(v) \in \mathcal{X}
\]

for each \(v \in V\), where \(\mathcal{X}\) is an abstract state set.

Packets are symbolic update carriers only. They do not encode biological, epidemiological, molecular, receptor, infectivity, immune-evasion, or host-range information.

## 5. Persistent Memory Ledger

The persistent memory ledger is a function

\[
L_\tau: V \rightarrow \mathbb{N}_0
\]

where \(L_\tau(v)\) records the accumulated abstract visit or activation count of node \(v\) up to the ledger-time component of \(\tau\).

A simple ledger update is

\[
L_{\tau + 1}(v) = L_\tau(v) + A_\tau(v),
\]

where

\[
A_\tau(v) = \#\{p \in P_\tau : \ell_\tau(p) = v\}.
\]

The key VF-H2 mechanism is persistence: \(L_\tau\) is not reset at every local update step. This distinguishes the persistent memory ledger condition from no-persistent-memory null controls.

## 6. Causal Mass

Define causal mass as a nonnegative abstract functional

\[
M_\tau(v) = \Phi(L_\tau(v), x_\tau(v), A_\tau(v), \tau),
\]

where \(\Phi\) is a bounded toy-model functional. In the simplest ledger-only case,

\[
M_\tau(v) = L_\tau(v).
\]

In richer variants, causal mass may include state, local activation, and projection factors. In the current safe toy model, causal mass remains abstract and does not represent biological mass, viral load, infectivity, or real-world transmission.

## 7. Transition Rule

A memory-ledger transition has the form

\[
x_{\tau+1}(v) = T(x_\tau(v), N_\tau(v), L_\tau(v), M_\tau(v), \eta_\tau),
\]

where:

- \(N_\tau(v)\) is an abstract neighborhood context,
- \(L_\tau(v)\) is persistent ledger memory,
- \(M_\tau(v)\) is causal mass,
- \(\eta_\tau\) is a safe abstract symbolic gate or perturbation term.

The defining feature of VF-H2 is that persistent memory \(L_\tau\) can affect transition outcomes.

## 8. Null Control

The no-persistent-memory null condition replaces \(L_\tau\) with an ephemeral ledger

\[
\tilde{L}_\tau(v),
\]

where \(\tilde{L}_\tau\) is reset within each local update window. Thus,

\[
\tilde{L}_{\tau+1}(v)
\]

does not preserve cross-step memory in the same way as \(L_\tau(v)\).

The null transition has the form

\[
\tilde{x}_{\tau+1}(v) = T_0(\tilde{x}_\tau(v), N_\tau(v), \tilde{L}_\tau(v), \tilde{\eta}_\tau).
\]

The null control is designed to test whether persistent memory, not merely same-step duplicate structure, contributes to the observed toy signal.

## 9. Toy Score

Let

\[
S_{\mathrm{ledger}}
\]

be the normalized score produced by the persistent memory-ledger condition, and let

\[
S_{\mathrm{null}}
\]

be the normalized score produced by the no-persistent-memory null control.

The primary toy signal is

\[
\Delta_{\mathrm{ledger}} = S_{\mathrm{ledger}} - S_{\mathrm{null}}.
\]

In the implementation artifacts, this signal is named:

\[
\texttt{ledger\_effect\_size}.
\]

## 10. VF-H2 Hypothesis

VF-H2 is the bounded toy hypothesis:

\[
H_{VF-H2}: \Delta_{\mathrm{ledger}} > 0
\]

under a preregistered safe abstract toy protocol and under specified artifact-resistance and replication checks.

A statistical or batch form is:

\[
\Pr(\Delta_{\mathrm{ledger}} > 0) \geq \theta
\]

for a preregistered threshold \(\theta\), such as \(\theta = 0.8\), with zero null-control leaks under the defined toy procedure.

## 11. Supported Current Bounded Claim

The current evidence chain supports only the following bounded claim:

Within the current safe abstract toy framework, persistent memory-ledger structure is associated with a positive and robust `ledger_effect_size` relative to no-persistent-memory null controls. This support includes preregistered robustness, artifact-resistance checks, ablation checks, and independent implementation-level replication.

## 12. What This Does Not Prove

This formalization does not prove VF-H2. It does not validate the full Viruse Fabric theory. It does not establish real-world relevance, biological relevance, external validation, independent empirical validation, or manuscript readiness.

## 13. Safety Boundary

This formalization introduces no real biological datasets, no real pathogen models, no receptor parameters, no operational targeting, no wet-lab protocol, no infectivity optimization, no immune evasion optimization, and no host range prediction.

## 14. Next Mathematical Work

Future mathematical work may attempt to prove conditional statements of the following form:

If a finite abstract propagation system satisfies ledger persistence, bounded symbolic gating, nondegenerate packet recurrence, and null-control separation, then the expected ledger effect is positive under specified toy conditions.

Such a theorem has not yet been proved in the current artifact.
