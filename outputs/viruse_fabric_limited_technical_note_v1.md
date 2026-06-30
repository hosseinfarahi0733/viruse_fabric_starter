# VF-H2 as a Memory-Ledger-Driven Abstract Propagation Toy Model: Formal Core and Bounded Internal Results

## Status Boundary

This is a limited technical note draft. It is not a complete manuscript, not a submission-ready paper, not a formal proof, not theory validation, not external validation, not independent empirical validation, and not biological validation.

The note reports only safe abstract toy-model results. No real biological datasets, no real pathogen models, no receptor parameters, no operational targeting, no wet-lab protocol, no infectivity optimization, no immune evasion optimization, and no host range prediction are introduced.

## Abstract

VF-H2 is a bounded safe abstract toy hypothesis about memory-ledger-driven propagation over a finite graph-like state space. The hypothesis asks whether persistent ledger memory produces a positive toy signal, `ledger_effect_size`, relative to no-persistent-memory null controls.

This note defines the mathematical core of VF-H2 using a finite abstract graph, a three-time coordinate, abstract packets, a persistent memory ledger, causal mass, a memory-ledger transition rule, a no-persistent-memory null control, and the primary toy signal `ledger_effect_size`.

The current bounded result is strong internal safe toy support for VF-H2. The evidence chain includes a limited safe toy simulation, a preregistered larger safe toy robustness check, artifact-resistance and ablation checks, and an independent implementation-level replication. These results support only the bounded claim that, within the current safe abstract toy framework, persistent memory-ledger structure is associated with a positive and robust `ledger_effect_size` relative to no-persistent-memory null controls.

The note does not claim that VF-H2 is proved, does not validate the full Viruse Fabric theory, and does not establish biological, empirical, external, or real-world validity.

## 1. Introduction

Persistent memory can alter the behavior of abstract propagation systems. VF-H2 studies this question in a deliberately safe toy setting: when a propagation process is given access to persistent ledger memory, does it produce a positive effect relative to a null control that lacks persistent memory?

The purpose of VF-H2 is narrow. It does not model pathogens, receptors, hosts, cells, organisms, infectivity, immune evasion, or host range. The model is only an abstract graph-based propagation toy used to study whether memory-ledger persistence can create a measurable difference under controlled toy conditions.

The central toy question is:

Can a persistent memory ledger produce a positive and robust `ledger_effect_size` relative to a no-persistent-memory null control?

## 2. Mathematical Core

Let

\[
G=(V,E)
\]

be a finite directed or undirected abstract graph. The node set \(V\) is finite, and \(E\subseteq V\times V\) is an abstract adjacency relation.

A propagation state is indexed by a three-time coordinate

\[
\tau=(t_1,t_2,t_3),
\]

where \(t_1\) represents local update time, \(t_2\) represents ledger accumulation time, and \(t_3\) represents projection or observation time.

Let \(P_\tau\) be a finite multiset of abstract packets at time \(\tau\). Each packet \(p\in P_\tau\) has an abstract location

\[
\ell_\tau(p)\in V.
\]

The node state is

\[
x_\tau(v)\in \mathcal{X}
\]

for each node \(v\in V\).

The persistent memory ledger is

\[
L_\tau:V\rightarrow \mathbb{N}_0,
\]

where \(L_\tau(v)\) records accumulated abstract visits or activations at node \(v\). A simple ledger update is

\[
L_{\tau+1}(v)=L_\tau(v)+A_\tau(v),
\]

where

\[
A_\tau(v)=\#\{p\in P_\tau:\ell_\tau(p)=v\}.
\]

Causal mass is defined as a nonnegative abstract functional

\[
M_\tau(v)=\Phi(L_\tau(v),x_\tau(v),A_\tau(v),\tau).
\]

In the simplest toy case, \(M_\tau(v)=L_\tau(v)\). Causal mass remains an abstract quantity and does not represent biological mass, viral load, real-world transmission, or infectivity.

A memory-ledger transition has the form

\[
x_{\tau+1}(v)=T(x_\tau(v),N_\tau(v),L_\tau(v),M_\tau(v),\eta_\tau),
\]

where \(N_\tau(v)\) is an abstract neighborhood context and \(\eta_\tau\) is a safe symbolic gate or perturbation term.

The no-persistent-memory null control replaces \(L_\tau\) with an ephemeral ledger \(\tilde{L}_\tau\), reset within each local update window. The null condition is intended to preserve limited same-step structure while removing persistent ledger memory.

The primary toy metric is

\[
\Delta_{\mathrm{ledger}} = S_{\mathrm{ledger}} - S_{\mathrm{null}},
\]

where \(S_{\mathrm{ledger}}\) is the normalized score under the persistent memory-ledger condition and \(S_{\mathrm{null}}\) is the normalized score under the no-persistent-memory null control.

In the implementation artifacts, this quantity is named `ledger_effect_size`.

## 3. VF-H2 Hypothesis

VF-H2 is the bounded toy hypothesis:

\[
H_{VF-H2}: \Delta_{\mathrm{ledger}}>0
\]

under a specified safe abstract toy protocol.

A batch form is:

\[
\Pr(\Delta_{\mathrm{ledger}}>0)\geq \theta,
\]

with a preregistered threshold such as \(\theta=0.8\), and with zero null-control leaks under the defined toy procedure.

This hypothesis is restricted to the toy framework. It is not a claim about real biological systems or external empirical systems.

## 4. Methods

The evidence chain contains four bounded safe toy stages.

First, a limited safe toy simulation evaluated VF-H2 under a small initial replicate set.

Second, a preregistered larger safe toy robustness check evaluated 64 planned toy replicates using `ledger_effect_size` as the primary signal.

Third, artifact-resistance and ablation tests checked whether the observed signal persisted under specific stress tests, including removal or weakening of memory structure, shuffled or randomized variants, strengthened null controls, seed permutation, score-component checks, constant-effect guards, subgroup consistency checks, null-leak guards, and effect-size distribution checks.

Fourth, an independent safe toy implementation replication rewrote packet generation, memory-ledger dynamics, null control, and metric calculation without importing the earlier robustness or artifact-resistance experiment modules.

All stages remained inside the safe abstract toy boundary.

## 5. Results

The limited safe toy simulation produced positive `ledger_effect_size` in 8 out of 8 toy replicates.

The preregistered larger safe toy robustness check produced positive `ledger_effect_size` in all 64 planned toy replicates. The mean `ledger_effect_size` was 2.4299456776344797, the minimum was 1.375, the maximum was 3.2041666666666666, and the null-control leak count was 0.

The artifact-resistance and ablation stage passed all six planned ablation tests and all four planned artifact-resistance checks. This supported the bounded interpretation that the positive toy signal was not merely a constant-effect artifact, a null-control leak, or an artifact of a single tested implementation assumption.

The independent safe toy implementation replication produced positive `ledger_effect_size` in all 64 independently implemented toy replicates. The positive effect rate was 1.0, the mean `ledger_effect_size` was 2.4857931685405643, the minimum was 1.3888888888888888, the maximum was 2.8851851851851853, and the null-control leak count was 0. The artifact-risk status was low because effect sizes varied across the independent grid.

## 6. Bounded Interpretation

The current evidence chain supports the bounded claim that VF-H2 has strong internal safe toy support with artifact-resistance and independent implementation-level replication.

More specifically, within the current safe abstract toy framework, persistent memory-ledger structure is associated with a positive and robust `ledger_effect_size` relative to no-persistent-memory null controls.

This interpretation is deliberately limited. It does not prove VF-H2. It does not validate the full Viruse Fabric theory. It does not establish external validation, independent empirical validation, real-world relevance, biological relevance, or manuscript readiness.

## 7. Limitations

The current results are internal to safe abstract toy models. They are not empirical validation.

The independent replication is independent at the implementation level, but it is still internal to a toy framework.

No theorem has been proved. No formal proof is claimed.

No real-world dataset is used. No biological interpretation is established.

No citations are added as validation evidence in this draft.

The results do not justify operational use, real-world targeting, or biological extrapolation.

## 8. Next Work

The next defensible work includes:

- auditing the limited technical note for overclaiming,
- refining the mathematical definitions,
- designing proof targets without claiming proof,
- mapping related literature without using citations as validation,
- designing topology, noise, and sensitivity extensions,
- preparing a guarded technical note draft only within the current boundaries.

## 9. Safety Boundary

Safe abstract toy model only. No real biological datasets, no real pathogen models, no receptor parameters, no operational targeting, no wet-lab protocol, no infectivity optimization, no immune evasion optimization, and no host range prediction are introduced.

## 10. Non-Claims

This limited technical note draft does not claim:

- theory validation,
- formal proof,
- external validation,
- independent empirical validation,
- biological validity,
- manuscript readiness,
- submission readiness,
- real-world applicability,
- operational usefulness.
