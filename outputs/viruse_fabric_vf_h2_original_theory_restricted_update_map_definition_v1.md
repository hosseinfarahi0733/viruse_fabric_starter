# VF-H2 Original Theory Restricted Update Map Definition v1

Action:
execute_vf_h2_original_theory_restricted_update_map_definition_no_claim_validation

Scope:
safe abstract mathematical formalization only.

This is a bridge-building step after:

- P_R-STATEDEF-VF-H2-001-R
- ORD-R-VF-H2-001-R

This does not reopen the frozen fixed-set finite poset package.
This does not prove full Viruse Fabric theory.
This does not prove original unrestricted TTP-VF-H2-004.
This does not claim empirical validation.
This does not claim biological validation.
This does not claim manuscript readiness.
This does not claim submission readiness.

## Purpose

Define a restricted VF-H2 update map:

f_R:P_R(n,d)->P_R(n,d)

on the finite poset:

(P_R(n,d), <=_R)

This resolves the bridge obligation:

update map formalized as a function P_R -> P_R

This does not yet prove the full bridge theorem.
This does not yet prove original unrestricted VF-H2.
This does not yet prove ledger_effect_size positivity.

## Prior anchors

### State space

P_R-STATEDEF-VF-H2-001-R proved:

P_R(n,d)=L_n^(T_3 x I_d)

where:

T_3={1,2,3}
I_d={1,2,...,d}
L_n={0,1,...,n}

and:

|P_R(n,d)|=(n+1)^(3d)

### Order

ORD-R-VF-H2-001-R proved:

(P_R(n,d), <=_R)

is a finite poset, where:

x <=_R y

iff for every alpha=(tau,i) in T_3 x I_d:

x_alpha <= y_alpha

## Target theorem

RUMAP-VF-H2-001-R:
restricted saturated coordinate update map theorem

Statement:
Given a nonempty active index set A_R subset T_3 x I_d and coordinate update maps h_alpha:L_n->L_n satisfying finite alphabet closure, extensivity, top saturation, and strict progress below top, the map f_R:P_R(n,d)->P_R(n,d) defined by active-coordinate update is well-defined. Moreover, f_R is globally extensive:

x <=_R f_R(x)

for all x in P_R(n,d), and it has local strict progress below top on every active coordinate.

## Active index set

Let:

A_R subset T_3 x I_d

be nonempty.

A_R is a safe abstract active layer-coordinate set.

No empirical, biological, or physical interpretation is assigned.

## Coordinate update functions

For each active coordinate:

alpha in A_R

choose:

h_alpha:L_n -> L_n

satisfying:

1. finite alphabet closure:
   for every a in L_n, h_alpha(a) in L_n

2. extensivity:
   a <= h_alpha(a)

3. top saturation:
   h_alpha(n)=n

4. strict progress below top:
   if a<n, then h_alpha(a)>a

## Definition of f_R

For x in P_R(n,d), define f_R(x) coordinatewise.

For each:

alpha=(tau,i) in T_3 x I_d

define:

f_R(x)_alpha =
- h_alpha(x_alpha), if alpha in A_R
- x_alpha, if alpha notin A_R

where:

x_alpha = x_{tau,i}

Thus f_R updates active coordinates using h_alpha and leaves inactive coordinates unchanged.

## Proof of well-definedness

Let x be any element of P_R(n,d).

We must prove:

f_R(x) in P_R(n,d)

For every coordinate alpha in T_3 x I_d:

Case 1:
alpha in A_R.

Then:

x_alpha in L_n

because x in P_R(n,d).

Since:

h_alpha:L_n -> L_n

we have:

h_alpha(x_alpha) in L_n

Therefore:

f_R(x)_alpha in L_n

Case 2:
alpha notin A_R.

Then:

f_R(x)_alpha = x_alpha

and:

x_alpha in L_n

Therefore:

f_R(x)_alpha in L_n

So every coordinate of f_R(x) belongs to L_n.

Therefore:

f_R(x) in L_n^(T_3 x I_d)=P_R(n,d)

Thus:

f_R:P_R(n,d)->P_R(n,d)

is well-defined.

WELL_DEFINEDNESS_OF_F_R_PROVED_OK

## Inactive-coordinate identity

If:

alpha notin A_R

then by definition:

f_R(x)_alpha=x_alpha

Therefore inactive coordinates are unchanged.

INACTIVE_COORDINATE_IDENTITY_PROVED_OK

## Active-coordinate extensivity

If:

alpha in A_R

then:

f_R(x)_alpha = h_alpha(x_alpha)

By extensivity of h_alpha:

x_alpha <= h_alpha(x_alpha)

Therefore:

x_alpha <= f_R(x)_alpha

ACTIVE_COORDINATE_EXTENSIVITY_PROVED_OK

## Global extensivity

We prove:

x <=_R f_R(x)

for every x in P_R(n,d).

Let alpha be any coordinate in T_3 x I_d.

Case 1:
alpha in A_R.

By active-coordinate extensivity:

x_alpha <= f_R(x)_alpha

Case 2:
alpha notin A_R.

By inactive-coordinate identity:

f_R(x)_alpha=x_alpha

so:

x_alpha <= f_R(x)_alpha

Therefore for every coordinate alpha:

x_alpha <= f_R(x)_alpha

By definition of <=_R:

x <=_R f_R(x)

Thus f_R is globally extensive.

GLOBAL_EXTENSIVITY_OF_F_R_PROVED_OK

## Local strict progress below top

Let:

alpha in A_R

and suppose:

x_alpha < n

Then by strict progress below top for h_alpha:

h_alpha(x_alpha)>x_alpha

Since:

f_R(x)_alpha = h_alpha(x_alpha)

we have:

f_R(x)_alpha > x_alpha

Equivalently:

x_alpha < f_R(x)_alpha

Thus every active coordinate below top strictly progresses under f_R.

LOCAL_STRICT_PROGRESS_BELOW_TOP_PROVED_OK

## Candidate fixed set

Define candidate active-saturation set:

F_R^cand = {x in P_R(n,d) : x_alpha=n for every alpha in A_R}

This is the expected fixed set of f_R.

Expected later theorem:

Fix(f_R)=F_R^cand

This is not fully proved in this step.

However, the definition is recorded for the next bridge obligation.

CANDIDATE_FIXED_SET_RECORDED_OK

## What this resolves

Resolved:

1. A_R is defined as a nonempty active index set.
2. h_alpha assumptions are defined.
3. f_R is formally defined.
4. f_R:P_R->P_R is well-defined.
5. inactive coordinates remain fixed.
6. active coordinates are extensive.
7. global extensivity x<=_R f_R(x) is proved.
8. local strict progress below top is proved.
9. candidate fixed set F_R^cand is recorded.

## What remains unresolved

Still unresolved:

1. Fixed set proof:
   Fix(f_R)=F_R^cand

2. Saturation predicate:
   saturated_R(x)

3. Saturation equivalence:
   saturated_R(x) iff f_R(x)=x

4. Strict progressivity outside F_R:
   x notin F_R implies x <_R f_R(x)

5. Ledger/Lyapunov functional V_R

6. Strict order-preservation of V_R

7. ledger_effect_size identity

8. Activation/aggregate assumptions, if used

## Boundary

This step proves only the restricted finite update-map definition and its basic coordinatewise properties.

It does not prove:

- full Viruse Fabric theory
- original unrestricted TTP-VF-H2-004
- generalized theorem without assumptions
- empirical validation
- biological validation
- manuscript readiness
- submission readiness

## Result

RUMAP-VF-H2-001-R proved:
true

The restricted saturated coordinate update map:

f_R:P_R(n,d)->P_R(n,d)

is well-defined and globally extensive, with local strict progress below top on active coordinates.

## Next allowed action

draft_vf_h2_original_theory_fixed_set_and_strict_progressivity_plan_no_claim_validation

VF_H2_ORIGINAL_THEORY_RESTRICTED_UPDATE_MAP_DEFINITION_EXECUTED_OK
RUMAP_VF_H2_001_R_PROVED_TRUE_OK
A_R_DEFINED_OK
H_ALPHA_ASSUMPTIONS_DEFINED_OK
F_R_DEFINED_OK
WELL_DEFINEDNESS_OF_F_R_PROVED_OK
INACTIVE_COORDINATE_IDENTITY_PROVED_OK
ACTIVE_COORDINATE_EXTENSIVITY_PROVED_OK
GLOBAL_EXTENSIVITY_OF_F_R_PROVED_OK
LOCAL_STRICT_PROGRESS_BELOW_TOP_PROVED_OK
CANDIDATE_FIXED_SET_RECORDED_OK
FIXED_SET_PROOF_REMAINS_UNRESOLVED_OK
STRICT_PROGRESSIVITY_OUTSIDE_F_R_REMAINS_UNRESOLVED_OK
LEDGER_FUNCTIONAL_REMAINS_UNRESOLVED_OK
LEDGER_EFFECT_IDENTITY_REMAINS_UNRESOLVED_OK
FULL_ORIGINAL_THEORY_REMAINS_NOT_PROVED_OK
ORIGINAL_UNRESTRICTED_TTP_VF_H2_004_REMAINS_NOT_PROVED_OK
NEXT_ALLOWED_DRAFT_VF_H2_ORIGINAL_THEORY_FIXED_SET_AND_STRICT_PROGRESSIVITY_PLAN_OK
