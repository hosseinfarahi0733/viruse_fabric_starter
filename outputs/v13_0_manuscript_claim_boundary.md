# VF-H2 v13.0.0 — Manuscript Claim Boundary

## Purpose

This milestone records a manuscript-safe claim boundary and contribution
statement for the current Lean formalization. It is not a new theorem milestone.
Its purpose is to prevent overclaiming when the v12 generalization layer is
described in an abstract, introduction, related-work section, or conclusion.

## Recommended title

**A Lean-Checked Transport Layer for Representation Consistency in a Restricted VF-H2 Scaffold**

## Recommended short title

**Lean-Checked Transport for a Restricted VF-H2 Scaffold**

## Core contribution statement

The contribution is a Lean-machine-checked representation-transport layer, not a
full VF-H2 proof. It establishes that the current restricted scaffold preserves
selected structures and operations when moving between product-structured and
typed representations, and it records these results in a generalized transport
certificate.

## Allowed claims

- Lean-machine-checked transport layer for a restricted VF-H2 scaffold.
- Generalized active-set membership transport.
- Generalized pointwise predicate transport.
- Generalized fixed-set transport.
- Generalized active-update transport.
- Generic effect-transport theorem under explicit hypotheses.
- Generic bridge-target transport for conjunction-shaped bridge targets.
- Clean generalized transport certificate at `v12.7.2`.
- Manuscript-safe theorem inventory at `v12.9.0`.

## Forbidden claims

- Full VF-H2 theory proven.
- Unrestricted VF-H2 theorem proven.
- Complete causal theory validated.
- Biological validation.
- Empirical validation.
- Clinical or real-world validation.
- Manuscript-ready full theory.
- Clean theorem-bearing status for `v12.7.0` or `v12.7.1`.

## Tag boundary

| Tag | Status | Claim policy |
|---|---|---|
| `v12.7.0` | build-failing, non-release-bearing | do not cite as theorem milestone |
| `v12.7.1` | build-failing, non-release-bearing | do not cite as theorem milestone |
| `v12.7.2` | clean release-bearing generalized certificate | cite as certificate milestone |
| `v12.8.0` | release-correction audit | cite as audit milestone |
| `v12.9.0` | manuscript-safe theorem inventory | cite as inventory milestone |

## Theorem-to-claim mapping

| Claim ID | Safe wording | Formal support | Scope boundary |
|---|---|---|---|
| C1 | generalized active-set membership transport | `VFH2.ProductActiveSetGeneralization.mem_map_flatten_iff_unflatten_mem`<br>`VFH2.ProductActiveSetGeneralization.restricted_mem_typed_active_iff_unflatten_mem` | arbitrary ProductIndex active lists plus restricted-parameter instance |
| C2 | generalized pointwise predicate transport | `VFH2.ProductPointwiseTransportGeneralization.forall_width_iff_forall_product`<br>`VFH2.ProductPointwiseTransportGeneralization.forall_width_mem_map_iff_forall_product_mem` | pointwise predicates and active-list restricted predicate transport |
| C3 | generalized fixed-set transport | `VFH2.ProductFixedSetGeneralization.generalized_fixedSet_transport`<br>`VFH2.ProductFixedSetGeneralization.restricted_fixedSet_transport_from_general` | fixed-set condition used by current ProductTypedState scaffold |
| C4 | generalized active-update transport | `VFH2.ProductUpdateGeneralization.productToTyped_generalizedProductUpdateState_eq_generalizedTypedUpdateState`<br>`VFH2.ProductUpdateGeneralization.restricted_update_transport_from_general` | active-update operation setting active coordinates to top in the current scaffold |
| C5 | generic effect-transport theorem | `VFH2.ProductEffectTransportGeneralization.genericEffect_transport`<br>`VFH2.ProductEffectTransportGeneralization.restricted_ledgerEffect_transport_instance` | generic effect pattern and restricted ledger-effect instance |
| C6 | generic bridge-target transport theorem | `VFH2.ProductBridgeGeneralization.genericBridgeTarget_transport`<br>`VFH2.ProductBridgeGeneralization.restricted_bridgeTarget_transport_instance` | generic conjunction-shaped bridge targets and restricted bridge target instance |
| C7 | generalized transport ladder certificate | `VFH2.ProductGeneralizedTransportCertificate.generalizedTransportLadder_certificate`<br>`VFH2.ProductGeneralizedTransportCertificate.restrictedTransportInstance_certificate` | certificate collecting v12 generalized transport layers; clean build at v12.7.2 |

## One-paragraph manuscript contribution

This work contributes a Lean-machine-checked representation-transport layer for
a restricted VF-H2 computational scaffold. The formal development proves
generalized transport results for active-set membership, pointwise predicates,
fixed-set conditions, active-update operations, generic update-effect
expressions, and conjunction-shaped bridge targets between product-structured
and typed representations. These results are collected in a clean generalized
transport ladder certificate at `v12.7.2`, with subsequent audit and inventory
milestones clarifying the theorem surface and release boundary. The contribution
is a formal representation-consistency scaffold; it does not claim the full
VF-H2 theory, unrestricted correctness, empirical validation, or biological
validation.

## Compact claim boundary for paper footnote

The formal claims in this paper are limited to the Lean-checked restricted
scaffold and its generalized transport layer. They should not be read as a proof
of the full VF-H2 theory, unrestricted dynamics, or empirical/biological
validity.

