# VF-H2 Coordinate-Subset Update Family Plan v1

Action:
draft_vf_h2_coordinate_subset_update_family_plan_no_claim_validation

Scope:
safe abstract finite coordinatewise toy VF-H2 only.

## Purpose

Plan a proof attempt extending the product-lattice model from all-coordinate updates to nonempty active-coordinate subset updates.

This is not a proof.
This does not prove the unrestricted theorem.
This does not prove a generalized theorem without assumptions.
This does not prove full Viruse Fabric theory.
This does not claim empirical or biological validation.

## Prior proved anchor

PFPL-T-VF-H2-001-R:
proved a parametric finite product-lattice model using all-coordinate saturated increment update.

## Target theorem

CSUF-T-VF-H2-001-R:
coordinate-subset update family theorem

Planned statement:
For every n >= 1, d >= 1, and every nonempty active-coordinate subset S of {1,...,d}, there exists a finite coordinatewise toy model satisfying the combined toy assumptions, with positive ledger effect exactly on states having at least one active unsaturated coordinate.

## Model candidate

Let:

n >= 1
d >= 1
S subset {1,...,d}
S nonempty

Domain:

D_{n,d} = {0,1,...,n}^d

Order:

coordinatewise order

Ledger update:

M_S(x)_i =
- min(x_i + 1, n), if i in S
- x_i, if i not in S

Activation:

A(x) = x

Aggregate:

G(x) = sum_i x_i

Embedding:

E(x) = x

Abstraction:

Q(x) = x

## Expected ledger effect

For x in D_{n,d}:

ledger_effect_size_S(x) = G(A(M_S(x))) - G(A(x))

Since A is identity:

ledger_effect_size_S(x) = G(M_S(x)) - G(x)

For each coordinate i:

if i in S and x_i < n, then M_S(x)_i - x_i = 1
if i in S and x_i = n, then M_S(x)_i - x_i = 0
if i not in S, then M_S(x)_i - x_i = 0

Therefore:

ledger_effect_size_S(x) =
number of active coordinates i in S such that x_i < n.

## Expected witness structure

Strict witness states:

{x in D_{n,d} : exists i in S with x_i < n}

Saturated non-strict states relative to S:

{x in D_{n,d} : for every i in S, x_i = n}

Let m = |S|.

Total state count:

(n+1)^d

Saturated non-strict state count:

(n+1)^(d-m)

Strict witness count:

(n+1)^d - (n+1)^(d-m)

Because S is nonempty, m >= 1.

## Planned proof obligations

1. D_{n,d} is finite and nonempty.
2. The coordinatewise order is a valid finite partial order.
3. M_S maps D_{n,d} into D_{n,d}.
4. M_S is coordinatewise monotone.
5. A is identity, hence monotone and strictness-preserving.
6. G is coordinate-sum, hence preserves strict coordinatewise positive improvement.
7. E is identity, hence injective, order-preserving, and strict-witness-preserving.
8. Q is identity, hence order-reflecting.
9. ledger_effect_size_S(x) equals the number of active unsaturated coordinates.
10. A state is a strict witness iff at least one active coordinate is below n.
11. A state is saturated non-strict iff all active coordinates are at n.
12. The construction includes the all-coordinate PFPL case when S = {1,...,d}.

## Boundary

This only plans a finite coordinatewise toy proof with active-coordinate subsets.

It does not prove:
- unrestricted TTP-VF-H2-004
- generalized theorem without assumptions
- full Viruse Fabric theory
- empirical validation
- biological validation
- manuscript readiness
- submission readiness

## Next allowed action

execute_vf_h2_coordinate_subset_update_family_proof_attempt_no_claim_validation

VF_H2_COORDINATE_SUBSET_UPDATE_FAMILY_PLAN_CREATED_OK
CSUF_T_VF_H2_001_R_TARGET_DEFINED_NOT_PROVED_OK
NONEMPTY_ACTIVE_COORDINATE_SUBSET_S_DEFINED_OK
M_S_COORDINATE_SUBSET_INCREMENT_DEFINED_OK
EXPECTED_LEDGER_EFFECT_ACTIVE_UNSATURATED_COORDINATE_COUNT_OK
EXPECTED_STRICT_WITNESS_COUNT_DEFINED_OK
EXPECTED_SATURATED_NONSTRICT_COUNT_DEFINED_OK
PFPL_ALL_COORDINATE_CASE_INCLUDED_AS_SPECIAL_CASE_OK
GENERALIZED_THEOREM_WITHOUT_ASSUMPTIONS_REMAINS_NOT_PROVED_OK
ORIGINAL_UNRESTRICTED_TTP_VF_H2_004_REMAINS_NOT_PROVED_OK
FULL_VIRUSE_FABRIC_THEORY_REMAINS_NOT_PROVED_OK
NEXT_ALLOWED_EXECUTE_VF_H2_COORDINATE_SUBSET_UPDATE_FAMILY_PROOF_ATTEMPT_OK
