# VF-H2 Original Theory Fixed Set and Strict Progressivity v1

Action:
execute_vf_h2_original_theory_fixed_set_and_strict_progressivity_no_claim_validation

Scope:
safe abstract mathematical formalization only.

This is a bridge-building step after:

- P_R-STATEDEF-VF-H2-001-R
- ORD-R-VF-H2-001-R
- RUMAP-VF-H2-001-R

This does not reopen the frozen fixed-set finite poset package.
This does not prove full Viruse Fabric theory.
This does not prove original unrestricted TTP-VF-H2-004.
This does not claim empirical validation.
This does not claim biological validation.
This does not claim manuscript readiness.
This does not claim submission readiness.

## Purpose

Prove that the restricted update map f_R has the expected fixed set and satisfies strict progressivity outside that fixed set.

This resolves the bridge obligations:

1. fixed set characterization
2. saturation equivalence
3. strict progressivity outside the fixed set

These obligations are necessary before applying:

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

is a finite poset with coordinatewise order.

### Update map

RUMAP-VF-H2-001-R proved:

Given a nonempty active index set:

A_R subset T_3 x I_d

and active coordinate update maps:

h_alpha:L_n->L_n

satisfying:

- finite alphabet closure
- extensivity
- top saturation h_alpha(n)=n
- strict progress below top

the update map:

f_R:P_R(n,d)->P_R(n,d)

defined by:

f_R(x)_alpha =
- h_alpha(x_alpha), if alpha in A_R
- x_alpha, if alpha notin A_R

is well-defined and globally extensive:

x <=_R f_R(x)

for every x.

It also has local strict progress below top on active coordinates.

## Target theorem

FSP-R-VF-H2-001-R:
restricted fixed set and strict progressivity theorem

Statement:

Let:

F_R = {x in P_R(n,d) : x_alpha=n for every alpha in A_R}

Then:

1. Fix(f_R)=F_R
2. saturated_R(x) iff x in F_R
3. saturated_R(x) iff f_R(x)=x
4. x notin F_R implies x <_R f_R(x)

## Definition of saturation

Define:

saturated_R(x)

iff:

for every alpha in A_R:

x_alpha=n

Thus:

F_R = {x in P_R(n,d) : saturated_R(x)}

Equivalently:

F_R = {x in P_R(n,d) : x_alpha=n for every alpha in A_R}

## Proof: F_R subset Fix(f_R)

Assume:

x in F_R

Then for every active alpha in A_R:

x_alpha=n

By top saturation:

h_alpha(n)=n

Therefore for every active alpha:

f_R(x)_alpha
=
h_alpha(x_alpha)
=
h_alpha(n)
=
n
=
x_alpha

For inactive alpha notin A_R:

f_R(x)_alpha=x_alpha

by definition of f_R.

Therefore every coordinate of f_R(x) equals the corresponding coordinate of x.

Thus:

f_R(x)=x

So:

x in Fix(f_R)

Hence:

F_R subset Fix(f_R)

F_R_SUBSET_FIX_F_R_PROVED_OK

## Proof: Fix(f_R) subset F_R

Assume:

x in Fix(f_R)

Then:

f_R(x)=x

Suppose for contradiction that:

x notin F_R

Then there exists alpha in A_R such that:

x_alpha<n

By strict progress below top:

h_alpha(x_alpha)>x_alpha

Since alpha is active:

f_R(x)_alpha
=
h_alpha(x_alpha)
>
x_alpha

Therefore:

f_R(x)_alpha != x_alpha

So:

f_R(x) != x

This contradicts:

x in Fix(f_R)

Therefore no active coordinate is below n.

Thus for every alpha in A_R:

x_alpha=n

So:

x in F_R

Hence:

Fix(f_R) subset F_R

FIX_F_R_SUBSET_F_R_PROVED_OK

## Fixed set conclusion

Since:

F_R subset Fix(f_R)

and:

Fix(f_R) subset F_R

we conclude:

Fix(f_R)=F_R

FIX_F_R_EQUALS_F_R_PROVED_OK

## Saturation equivalence

By definition:

saturated_R(x)

iff:

for every alpha in A_R, x_alpha=n

This is equivalent to:

x in F_R

Since:

F_R=Fix(f_R)

we have:

x in F_R

iff:

f_R(x)=x

Therefore:

saturated_R(x) iff f_R(x)=x

SATURATION_EQUIVALENCE_PROVED_OK

## Proof: strict progressivity outside F_R

Assume:

x notin F_R

Then there exists alpha in A_R such that:

x_alpha<n

By strict progress below top:

h_alpha(x_alpha)>x_alpha

Since alpha is active:

f_R(x)_alpha=h_alpha(x_alpha)>x_alpha

Thus at least one coordinate strictly increases.

From RUMAP-VF-H2-001-R, global extensivity gives:

x <=_R f_R(x)

Since at least one coordinate strictly increases:

x != f_R(x)

Therefore, by definition of strict coordinatewise order:

x <_R f_R(x)

Thus:

x notin F_R implies x <_R f_R(x)

STRICT_PROGRESSIVITY_OUTSIDE_F_R_PROVED_OK

## What this resolves

Resolved:

1. F_R is formally defined.
2. saturated_R(x) is formally defined.
3. F_R subset Fix(f_R) is proved.
4. Fix(f_R) subset F_R is proved.
5. Fix(f_R)=F_R is proved.
6. saturated_R(x) iff f_R(x)=x is proved.
7. strict progressivity outside F_R is proved:
   x notin F_R implies x <_R f_R(x)

## What remains unresolved

Still unresolved:

1. Ledger/Lyapunov functional V_R
2. Strict order-preservation of V_R
3. ledger_effect_size identity
4. Activation/aggregate assumptions, if used
5. Final restricted bridge theorem application

## Bridge status after this theorem

The restricted formalization now has:

1. finite state space P_R
2. finite poset structure (P_R, <=_R)
3. well-defined update map f_R:P_R->P_R
4. fixed set F_R=Fix(f_R)
5. strict progressivity outside F_R

The remaining base-theorem obligation is:

define V_R:P_R->R and prove V_R is strict order-preserving.

After that, the fixed-set finite poset theorem can be applied to obtain restricted ledger positivity, provided ledger_effect_size is identified with the Lyapunov increment.

## Boundary

This step proves only fixed-set characterization and strict progressivity for the restricted finite formalization.

It does not prove:

- full Viruse Fabric theory
- original unrestricted TTP-VF-H2-004
- generalized theorem without assumptions
- empirical validation
- biological validation
- manuscript readiness
- submission readiness

## Result

FSP-R-VF-H2-001-R proved:
true

The restricted update map f_R has fixed set:

F_R = {x in P_R(n,d) : x_alpha=n for every alpha in A_R}

and satisfies:

x notin F_R implies x <_R f_R(x)

## Next allowed action

draft_vf_h2_original_theory_ledger_lyapunov_functional_plan_no_claim_validation

VF_H2_ORIGINAL_THEORY_FIXED_SET_AND_STRICT_PROGRESSIVITY_EXECUTED_OK
FSP_R_VF_H2_001_R_PROVED_TRUE_OK
F_R_DEFINED_OK
SATURATED_R_DEFINED_OK
F_R_SUBSET_FIX_F_R_PROVED_OK
FIX_F_R_SUBSET_F_R_PROVED_OK
FIX_F_R_EQUALS_F_R_PROVED_OK
SATURATION_EQUIVALENCE_PROVED_OK
STRICT_PROGRESSIVITY_OUTSIDE_F_R_PROVED_OK
FINITE_POSET_UPDATE_FIXED_SET_PROGRESSIVITY_READY_FOR_LEDGER_FUNCTIONAL_OK
LEDGER_FUNCTIONAL_REMAINS_UNRESOLVED_OK
LEDGER_EFFECT_IDENTITY_REMAINS_UNRESOLVED_OK
FINAL_RESTRICTED_BRIDGE_THEOREM_REMAINS_UNPROVED_OK
FULL_ORIGINAL_THEORY_REMAINS_NOT_PROVED_OK
ORIGINAL_UNRESTRICTED_TTP_VF_H2_004_REMAINS_NOT_PROVED_OK
NEXT_ALLOWED_DRAFT_VF_H2_ORIGINAL_THEORY_LEDGER_LYAPUNOV_FUNCTIONAL_PLAN_OK
