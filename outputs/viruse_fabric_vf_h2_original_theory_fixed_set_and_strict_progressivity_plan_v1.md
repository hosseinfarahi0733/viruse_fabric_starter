# VF-H2 Original Theory Fixed Set and Strict Progressivity Plan v1

Action:
draft_vf_h2_original_theory_fixed_set_and_strict_progressivity_plan_no_claim_validation

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

Plan the proof that the restricted update map f_R has the expected fixed set and satisfies strict progressivity outside that fixed set.

This addresses the next bridge obligations:

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

## Target artifact

FSP-R-VF-H2-001

Restricted fixed set and strict progressivity theorem.

Planned target theorem:

FSP-R-VF-H2-001-R

Statement:

Let:

F_R = {x in P_R(n,d) : x_alpha=n for every alpha in A_R}

Then:

1. Fix(f_R)=F_R
2. saturated_R(x) iff x in F_R
3. x notin F_R implies x <_R f_R(x)

## Definition of saturation

Define:

saturated_R(x)

iff:

for every alpha in A_R:

x_alpha=n

Thus:

F_R = {x in P_R(n,d) : saturated_R(x)}

## Planned proof: F_R subset Fix(f_R)

Assume:

x in F_R

Then for every active alpha in A_R:

x_alpha=n

By top saturation:

h_alpha(n)=n

Therefore for active alpha:

f_R(x)_alpha=h_alpha(x_alpha)=h_alpha(n)=n=x_alpha

For inactive alpha notin A_R:

f_R(x)_alpha=x_alpha

Therefore every coordinate of f_R(x) equals the corresponding coordinate of x.

Thus:

f_R(x)=x

So:

x in Fix(f_R)

Hence:

F_R subset Fix(f_R)

## Planned proof: Fix(f_R) subset F_R

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

f_R(x)_alpha=h_alpha(x_alpha)>x_alpha

Therefore:

f_R(x)_alpha != x_alpha

So:

f_R(x) != x

contradicting:

x in Fix(f_R)

Therefore no active coordinate is below n.

Thus for every alpha in A_R:

x_alpha=n

So:

x in F_R

Hence:

Fix(f_R) subset F_R

## Planned fixed set conclusion

Since both inclusions hold:

Fix(f_R)=F_R

## Planned saturation equivalence

By definition:

saturated_R(x)

iff every active alpha satisfies x_alpha=n

iff x in F_R

Since:

F_R=Fix(f_R)

we get:

saturated_R(x) iff f_R(x)=x

## Planned proof: strict progressivity outside F_R

Assume:

x notin F_R

Then there exists alpha in A_R such that:

x_alpha<n

By strict progress below top:

h_alpha(x_alpha)>x_alpha

Since alpha is active:

f_R(x)_alpha=h_alpha(x_alpha)>x_alpha

So at least one coordinate strictly increases.

From RUMAP-VF-H2-001-R, global extensivity gives:

x <=_R f_R(x)

Since at least one coordinate is strictly increased:

x != f_R(x)

Therefore:

x <_R f_R(x)

Thus:

x notin F_R implies x <_R f_R(x)

## What this resolves

Expected resolved by execution:

1. F_R is formally defined.
2. saturated_R(x) is formally defined.
3. F_R subset Fix(f_R) is proved.
4. Fix(f_R) subset F_R is proved.
5. Fix(f_R)=F_R is proved.
6. saturated_R(x) iff f_R(x)=x is proved.
7. strict progressivity outside F_R is proved:
   x notin F_R implies x <_R f_R(x)

## What remains unresolved

Still unresolved after this planned step:

1. Ledger/Lyapunov functional V_R
2. Strict order-preservation of V_R
3. ledger_effect_size identity
4. Activation/aggregate assumptions, if used
5. Final restricted bridge theorem application

## Candidate next step

After execution, the natural next bridge obligation is defining a ledger/Lyapunov functional:

V_R:P_R(n,d)->R

Candidate:

V_R(x)=sum over all alpha in T_3 x I_d of x_alpha

or possibly:

V_R^A(x)=sum over alpha in A_R of x_alpha

Need decide whether ledger should count:

- all coordinates
- active coordinates only
- selected layer coordinates
- activation/aggregate projection

This choice should be handled in the next plan.

## Boundary

This plan only prepares fixed-set and strict-progressivity proofs for the restricted finite formalization.

It does not prove:

- full Viruse Fabric theory
- original unrestricted TTP-VF-H2-004
- generalized theorem without assumptions
- empirical validation
- biological validation
- manuscript readiness
- submission readiness

## Planned execution step

The execution step should produce:

1. definition of F_R
2. definition of saturated_R(x)
3. proof that F_R subset Fix(f_R)
4. proof that Fix(f_R) subset F_R
5. conclusion Fix(f_R)=F_R
6. proof saturated_R(x) iff f_R(x)=x
7. proof strict progressivity outside F_R
8. remaining blocker list
9. next action toward ledger/Lyapunov functional definition

## Next allowed action

execute_vf_h2_original_theory_fixed_set_and_strict_progressivity_no_claim_validation

VF_H2_ORIGINAL_THEORY_FIXED_SET_AND_STRICT_PROGRESSIVITY_PLAN_CREATED_OK
FSP_R_VF_H2_001_TARGET_DEFINED_NOT_PROVED_OK
P_R_STATEDEF_ANCHOR_CONFIRMED_OK
ORD_R_ANCHOR_CONFIRMED_OK
RUMAP_ANCHOR_CONFIRMED_OK
F_R_DEFINED_AS_ACTIVE_SATURATION_SET_OK
SATURATED_R_PREDICATE_PLANNED_OK
FIX_F_R_EQUAL_F_R_PROOF_OBLIGATIONS_DEFINED_OK
STRICT_PROGRESSIVITY_OUTSIDE_F_R_PROOF_OBLIGATION_DEFINED_OK
LEDGER_FUNCTIONAL_REMAINS_UNRESOLVED_OK
LEDGER_EFFECT_IDENTITY_REMAINS_UNRESOLVED_OK
FINAL_BRIDGE_THEOREM_REMAINS_UNPROVED_OK
FULL_ORIGINAL_THEORY_REMAINS_NOT_PROVED_OK
ORIGINAL_UNRESTRICTED_TTP_VF_H2_004_REMAINS_NOT_PROVED_OK
NEXT_ALLOWED_EXECUTE_VF_H2_ORIGINAL_THEORY_FIXED_SET_AND_STRICT_PROGRESSIVITY_OK
