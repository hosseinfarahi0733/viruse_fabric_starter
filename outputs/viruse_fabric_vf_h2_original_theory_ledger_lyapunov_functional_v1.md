# VF-H2 Original Theory Ledger Lyapunov Functional v1

Action:
execute_vf_h2_original_theory_ledger_lyapunov_functional_no_claim_validation

Scope:
safe abstract mathematical formalization only.

This is a bridge-building step after:

- P_R-STATEDEF-VF-H2-001-R
- ORD-R-VF-H2-001-R
- RUMAP-VF-H2-001-R
- FSP-R-VF-H2-001-R

This does not reopen the frozen fixed-set finite poset package.
This does not prove full Viruse Fabric theory.
This does not prove original unrestricted TTP-VF-H2-004.
This does not claim empirical validation.
This does not claim biological validation.
This does not claim manuscript readiness.
This does not claim submission readiness.

## Purpose

Define a restricted ledger/Lyapunov functional:

V_R:P_R(n,d)->R

and prove that it is strict order-preserving on:

(P_R(n,d), <=_R)

This resolves the next bridge obligation required for applying:

FFP-LYAP-T-VF-H2-001-R

to the restricted original VF-H2 formalization.

## Prior anchors

### State space

P_R-STATEDEF-VF-H2-001-R proved:

P_R(n,d)=L_n^(T_3 x I_d)

where:

T_3={1,2,3}
I_d={1,2,...,d}
L_n={0,1,...,n}

### Order

ORD-R-VF-H2-001-R proved:

(P_R(n,d), <=_R)

is a finite poset.

The order is coordinatewise:

x <=_R y

iff for every alpha in T_3 x I_d:

x_alpha <= y_alpha

and:

x <_R y

iff:

x <=_R y and x != y

equivalently, all coordinates are nondecreasing and at least one coordinate strictly increases.

### Update map

RUMAP-VF-H2-001-R proved:

f_R:P_R(n,d)->P_R(n,d)

is a well-defined restricted saturated coordinate update map.

### Fixed set and strict progressivity

FSP-R-VF-H2-001-R proved:

Let:

F_R = {x in P_R(n,d) : x_alpha=n for every alpha in A_R}

Then:

Fix(f_R)=F_R

and:

x notin F_R implies x <_R f_R(x)

## Target theorem

LEDGER-LYAP-R-VF-H2-001-R:
restricted ledger/Lyapunov functional theorem

Statement:

Let:

Alpha_R = T_3 x I_d

Define:

V_R(x)=sum_{alpha in Alpha_R} x_alpha

Then:

1. V_R:P_R(n,d)->R is well-defined.
2. V_R is strict order-preserving:
   x <_R y implies V_R(x)<V_R(y)
3. If x notin F_R, then:
   V_R(f_R(x))-V_R(x)>0
4. If x in F_R, then:
   V_R(f_R(x))-V_R(x)=0

## Definition of Alpha_R

Define:

Alpha_R = T_3 x I_d

Since:

|T_3|=3

and:

|I_d|=d

we have:

|Alpha_R|=3d

Thus Alpha_R is finite.

ALPHA_R_DEFINED_OK

## Definition of V_R

Define:

V_R:P_R(n,d)->R

by:

V_R(x)=sum_{alpha in Alpha_R} x_alpha

where:

x_alpha=x_{tau,i}

for alpha=(tau,i).

This is the all-coordinate restricted ledger/Lyapunov functional.

V_R_DEFINED_OK

## Proof of well-definedness

Let x be any element of P_R(n,d).

By definition of P_R(n,d):

x_alpha in L_n={0,1,...,n}

for every alpha in Alpha_R.

Thus every x_alpha is a finite integer.

Since Alpha_R is finite with cardinality 3d, the sum:

sum_{alpha in Alpha_R} x_alpha

is a finite integer.

Every finite integer is a real number.

Therefore:

V_R(x) in R

So:

V_R:P_R(n,d)->R

is well-defined.

V_R_WELL_DEFINEDNESS_PROVED_OK

## Proof of strict order-preservation

Assume:

x <_R y

By the strict order characterization from ORD-R-VF-H2-001-R:

1. for every alpha in Alpha_R:
   x_alpha <= y_alpha

2. there exists beta in Alpha_R such that:
   x_beta < y_beta

For every alpha in Alpha_R:

y_alpha - x_alpha >= 0

For beta:

y_beta - x_beta > 0

Now compute:

V_R(y)-V_R(x)
=
sum_{alpha in Alpha_R} y_alpha
-
sum_{alpha in Alpha_R} x_alpha

Therefore:

V_R(y)-V_R(x)
=
sum_{alpha in Alpha_R} (y_alpha-x_alpha)

Every summand is nonnegative, and at least one summand is strictly positive.

Therefore:

V_R(y)-V_R(x)>0

Thus:

V_R(x)<V_R(y)

So V_R is strict order-preserving.

V_R_STRICT_ORDER_PRESERVING_PROVED_OK

## Update increment positivity outside F_R

Assume:

x notin F_R

By FSP-R-VF-H2-001-R:

x <_R f_R(x)

Since V_R is strict order-preserving:

V_R(x)<V_R(f_R(x))

Therefore:

V_R(f_R(x))-V_R(x)>0

So the restricted Lyapunov increment is positive outside the fixed set.

UPDATE_INCREMENT_POSITIVE_OUTSIDE_F_R_PROVED_OK

## Zero increment on F_R

Assume:

x in F_R

By FSP-R-VF-H2-001-R:

F_R=Fix(f_R)

Therefore:

f_R(x)=x

Then:

V_R(f_R(x))-V_R(x)
=
V_R(x)-V_R(x)
=
0

So the restricted Lyapunov increment is zero on the fixed set.

FIXED_SET_ZERO_INCREMENT_PROVED_OK

## Optional weighted version

The same proof works for:

V_w(x)=sum_{alpha in Alpha_R} w_alpha x_alpha

provided:

w_alpha>0

for every alpha.

This weighted version is not needed for the current restricted bridge.

The unweighted V_R is sufficient.

OPTIONAL_WEIGHTED_VERSION_DEFERRED_OK

## What this resolves

Resolved:

1. Alpha_R is defined.
2. V_R is formally defined.
3. V_R:P_R->R is well-defined.
4. V_R is strict order-preserving.
5. V_R(f_R(x))-V_R(x)>0 is proved for x notin F_R.
6. V_R(f_R(x))-V_R(x)=0 is proved for x in F_R.

## What remains unresolved

Still unresolved:

1. Formal ledger_effect_size_R definition
2. ledger_effect_size_R identity
3. Final restricted bridge theorem
4. Activation/aggregate assumptions, if used
5. Full original unrestricted VF-H2
6. Empirical or biological validation

## Bridge status after this theorem

The restricted formalization now has all base ingredients needed for the finite-poset theorem:

1. finite state space P_R
2. finite poset structure (P_R, <=_R)
3. well-defined update map f_R:P_R->P_R
4. fixed set F_R=Fix(f_R)
5. strict progressivity outside F_R
6. strict order-preserving Lyapunov functional V_R

The remaining step is not another structural assumption.

The remaining step is to define:

ledger_effect_size_R(x)=V_R(f_R(x))-V_R(x)

and state the final restricted bridge theorem.

## Boundary

This step proves only the restricted ledger/Lyapunov functional theorem.

It does not prove:

- full Viruse Fabric theory
- original unrestricted TTP-VF-H2-004
- generalized theorem without assumptions
- empirical validation
- biological validation
- manuscript readiness
- submission readiness

## Result

LEDGER-LYAP-R-VF-H2-001-R proved:
true

The restricted ledger/Lyapunov functional:

V_R(x)=sum_{alpha in T_3 x I_d} x_alpha

is well-defined and strict order-preserving.

It yields:

x notin F_R implies V_R(f_R(x))-V_R(x)>0

and:

x in F_R implies V_R(f_R(x))-V_R(x)=0

## Next allowed action

draft_vf_h2_original_theory_final_restricted_bridge_theorem_plan_no_claim_full_theory

VF_H2_ORIGINAL_THEORY_LEDGER_LYAPUNOV_FUNCTIONAL_EXECUTED_OK
LEDGER_LYAP_R_VF_H2_001_R_PROVED_TRUE_OK
ALPHA_R_DEFINED_OK
V_R_DEFINED_AS_ALL_COORDINATE_SUM_OK
V_R_WELL_DEFINEDNESS_PROVED_OK
V_R_STRICT_ORDER_PRESERVING_PROVED_OK
UPDATE_INCREMENT_POSITIVE_OUTSIDE_F_R_PROVED_OK
FIXED_SET_ZERO_INCREMENT_PROVED_OK
LEDGER_EFFECT_SIZE_R_REMAINS_UNDEFINED_OK
FINAL_RESTRICTED_BRIDGE_THEOREM_REMAINS_UNPROVED_OK
FULL_ORIGINAL_THEORY_REMAINS_NOT_PROVED_OK
ORIGINAL_UNRESTRICTED_TTP_VF_H2_004_REMAINS_NOT_PROVED_OK
NEXT_ALLOWED_DRAFT_VF_H2_ORIGINAL_THEORY_FINAL_RESTRICTED_BRIDGE_THEOREM_PLAN_OK
