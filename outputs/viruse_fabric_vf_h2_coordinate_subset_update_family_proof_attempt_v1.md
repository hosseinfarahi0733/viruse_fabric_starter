# VF-H2 Coordinate-Subset Update Family Proof Attempt v1

Action:
execute_vf_h2_coordinate_subset_update_family_proof_attempt_no_claim_validation

Scope:
safe abstract finite coordinatewise toy VF-H2 only.

## Purpose

Attempt proof of:

CSUF-T-VF-H2-001-R

This proof attempt extends the product-lattice model from all-coordinate updates to nonempty active-coordinate subset updates.

This does not prove the unrestricted theorem.
This does not prove a generalized theorem without assumptions.
This does not prove full Viruse Fabric theory.
This does not claim empirical or biological validation.

## Target theorem

CSUF-T-VF-H2-001-R:
coordinate-subset update family theorem

Statement:
For every n >= 1, d >= 1, and every nonempty active-coordinate subset S of {1,...,d}, there exists a finite coordinatewise toy model satisfying the combined toy assumptions, with positive ledger effect exactly on states having at least one active unsaturated coordinate.

## Model

Let:

n >= 1
d >= 1
S subset {1,...,d}
S nonempty
m = |S|

Domain:

D_{n,d} = {0,1,...,n}^d

Order:

coordinatewise order

For x,y in D_{n,d}:

x <= y iff for every coordinate i, x_i <= y_i.

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

## Proof

### 1. Finite nonempty domain

D_{n,d} has:

(n+1)^d

states.

Since n >= 1 and d >= 1, D_{n,d} is finite and nonempty.

### 2. Coordinatewise order

The relation x <= y iff x_i <= y_i for every coordinate i is reflexive, antisymmetric, and transitive.

Therefore D_{n,d} is a finite coordinatewise partially ordered toy domain.

### 3. Ledger update is closed

For every x in D_{n,d} and every coordinate i:

If i in S:

M_S(x)_i = min(x_i + 1,n)

Since x_i in {0,1,...,n}, min(x_i+1,n) is also in {0,1,...,n}.

If i not in S:

M_S(x)_i = x_i

which is already in {0,1,...,n}.

Therefore M_S(x) is in D_{n,d}.

So M_S maps D_{n,d} into itself.

### 4. Ledger update is monotone

Let x <= y coordinatewise.

For i in S:

x_i <= y_i

so:

x_i + 1 <= y_i + 1

Since z -> min(z,n) is monotone:

min(x_i+1,n) <= min(y_i+1,n)

Thus:

M_S(x)_i <= M_S(y)_i

For i not in S:

M_S(x)_i = x_i <= y_i = M_S(y)_i

Therefore M_S(x) <= M_S(y).

So M_S is coordinatewise monotone.

### 5. Activation monotonicity and strictness preservation

A is identity.

If x <= y, then A(x) <= A(y).

If x < y in coordinatewise order, then at least one coordinate is strictly smaller, and identity preserves that strict coordinate.

Therefore A is monotone and strictness-preserving.

### 6. Aggregate strict positivity

G is the coordinate-sum functional:

G(x) = sum_i x_i

If x <= y and x < y, then each difference y_i - x_i is nonnegative and at least one is positive.

Therefore:

G(y) - G(x) = sum_i (y_i - x_i) > 0

So G preserves strict coordinatewise positive improvement.

### 7. Embedding properties

E is identity.

Therefore E is:
- injective
- order-preserving
- strict-witness-preserving

### 8. Abstraction property

Q is identity.

If Q(x) <= Q(y), then x <= y.

Therefore Q is order-reflecting.

### 9. Ledger effect formula

For any x in D_{n,d}:

ledger_effect_size_S(x) = G(A(M_S(x))) - G(A(x))

Since A is identity:

ledger_effect_size_S(x) = G(M_S(x)) - G(x)

By definition of G:

ledger_effect_size_S(x) = sum_i M_S(x)_i - sum_i x_i

Therefore:

ledger_effect_size_S(x) = sum_i (M_S(x)_i - x_i)

For each coordinate i:

- if i in S and x_i < n, then M_S(x)_i - x_i = 1
- if i in S and x_i = n, then M_S(x)_i - x_i = 0
- if i not in S, then M_S(x)_i - x_i = 0

Therefore:

ledger_effect_size_S(x) =
the number of active coordinates i in S such that x_i < n.

### 10. Strict witness states

If there exists i in S such that x_i < n, then:

ledger_effect_size_S(x) >= 1

Therefore:

ledger_effect_size_S(x) > 0

So x is a strict witness.

Conversely, if every active coordinate i in S satisfies x_i = n, then each active-coordinate increment is saturated and each inactive coordinate is unchanged.

Therefore:

ledger_effect_size_S(x) = 0

So x is not a strict witness.

Thus:

x is a strict witness iff at least one active coordinate is below n.

### 11. Saturated non-strict states

A state x is saturated non-strict relative to S iff:

for every i in S, x_i = n.

The inactive coordinates outside S are arbitrary.

There are:

(n+1)^(d-m)

such states.

### 12. Strict witness count

Total state count:

(n+1)^d

Saturated non-strict state count:

(n+1)^(d-m)

Therefore strict witness count:

(n+1)^d - (n+1)^(d-m)

Since S is nonempty, m >= 1.

### 13. PFPL special case

If S = {1,...,d}, then m=d.

The saturated non-strict count becomes:

(n+1)^(d-d) = (n+1)^0 = 1

The strict witness count becomes:

(n+1)^d - 1

This recovers the prior all-coordinate PFPL construction as a special case.

## Result

CSUF-T-VF-H2-001-R proved:
true

For every n >= 1, d >= 1, and every nonempty active-coordinate subset S of {1,...,d}, the coordinate-subset update model satisfies the finite coordinatewise toy construction.

The model has:

- total state count: (n+1)^d
- ledger_effect_size_S(x): number of active coordinates below n
- strict witness states: states with at least one active coordinate below n
- saturated non-strict states: states with all active coordinates equal to n
- saturated non-strict count: (n+1)^(d-|S|)
- strict witness count: (n+1)^d - (n+1)^(d-|S|)

## Boundary

This proves only a finite coordinatewise toy theorem with active-coordinate subset updates.

It does not prove:
- unrestricted TTP-VF-H2-004
- generalized theorem without assumptions
- full Viruse Fabric theory
- empirical validation
- biological validation
- manuscript readiness
- submission readiness

## Next allowed action

audit_vf_h2_coordinate_subset_update_family_proof_attempt_no_claim_validation

VF_H2_COORDINATE_SUBSET_UPDATE_FAMILY_PROOF_ATTEMPT_EXECUTED_OK
CSUF_T_VF_H2_001_R_PROVED_TRUE_OK
FOR_EVERY_NONEMPTY_ACTIVE_COORDINATE_SUBSET_S_MODEL_EXISTS_OK
LEDGER_EFFECT_EQUALS_ACTIVE_UNSATURATED_COORDINATE_COUNT_OK
STRICT_WITNESS_IFF_ACTIVE_UNSATURATED_COORDINATE_EXISTS_OK
SATURATED_NONSTRICT_IFF_ALL_ACTIVE_COORDINATES_AT_N_OK
SATURATED_NONSTRICT_COUNT_N_PLUS_1_POWER_D_MINUS_ABS_S_CONFIRMED_OK
STRICT_WITNESS_COUNT_TOTAL_MINUS_SATURATED_CONFIRMED_OK
PFPL_ALL_COORDINATE_CASE_RECOVERED_AS_SPECIAL_CASE_OK
GENERALIZED_THEOREM_WITHOUT_ASSUMPTIONS_REMAINS_NOT_PROVED_OK
ORIGINAL_UNRESTRICTED_TTP_VF_H2_004_REMAINS_NOT_PROVED_OK
FULL_VIRUSE_FABRIC_THEORY_REMAINS_NOT_PROVED_OK
NEXT_ALLOWED_AUDIT_VF_H2_COORDINATE_SUBSET_UPDATE_FAMILY_PROOF_ATTEMPT_OK
