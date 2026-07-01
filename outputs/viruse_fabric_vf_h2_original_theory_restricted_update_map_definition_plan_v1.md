# VF-H2 Original Theory Restricted Update Map Definition Plan v1

Action:
draft_vf_h2_original_theory_restricted_update_map_definition_plan_no_claim_validation

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

Plan the definition of a restricted VF-H2 update map:

f_R:P_R(n,d)->P_R(n,d)

on the finite poset:

(P_R(n,d), <=_R)

The goal is to resolve the next bridge blocker from OIMAP-VF-H2-001:

update map not formalized as a function P_R -> P_R

This plan defines the update form and proof obligations.

It does not yet prove the full bridge theorem.
It does not yet prove original unrestricted VF-H2.
It does not yet prove ledger_effect_size positivity.

## Prior anchors

### State space anchor

P_R-STATEDEF-VF-H2-001-R proved:

P_R(n,d)=L_n^(T_3 x I_d)

where:

T_3={1,2,3}
I_d={1,2,...,d}
L_n={0,1,...,n}

and:

|P_R(n,d)|=(n+1)^(3d)

### Order anchor

ORD-R-VF-H2-001-R proved:

(P_R(n,d), <=_R)

is a finite poset, where:

x <=_R y

iff for every tau in T_3 and every i in I_d:

x_{tau,i} <= y_{tau,i}

## Target artifact

RUMAP-VF-H2-001

Restricted VF-H2 update map definition.

Planned target theorem:

RUMAP-VF-H2-001-R:
restricted saturated coordinate update map is well-defined on P_R(n,d).

## Active coordinate set

Let:

A_R subset T_3 x I_d

be a nonempty active index set.

Interpretation:
A_R selects the abstract layer-coordinate positions updated by the restricted VF-H2 step.

No empirical or biological interpretation is assigned.

A_R may later encode:

- active causal coordinates
- active ledger coordinates
- active constraint-progress coordinates
- active three-time positions

but these richer interpretations are not claimed here.

## Coordinate update functions

For each active coordinate alpha=(tau,i) in A_R, choose a function:

h_alpha:L_n -> L_n

satisfying:

1. well-defined finite alphabet map:
   h_alpha(a) in L_n for every a in L_n

2. extensivity:
   a <= h_alpha(a)

3. top saturation:
   h_alpha(n)=n

4. strict progress below top:
   if a<n, then h_alpha(a)>a

These are safe abstract saturated update functions.

## Proposed update map

Define:

f_R:P_R(n,d)->P_R(n,d)

by:

f_R(x)_alpha =
- h_alpha(x_alpha), if alpha in A_R
- x_alpha, if alpha notin A_R

where:

alpha=(tau,i)

and:

x_alpha = x_{tau,i}

Equivalently:

f_R updates active layer-coordinate entries using h_alpha and leaves inactive entries unchanged.

## Planned proof obligations

### 1. Well-definedness

Need prove:

for every x in P_R(n,d), f_R(x) belongs to P_R(n,d).

Proof idea:

For alpha in A_R:
x_alpha in L_n and h_alpha:L_n->L_n, so h_alpha(x_alpha) in L_n.

For alpha notin A_R:
f_R(x)_alpha=x_alpha in L_n.

Therefore every coordinate of f_R(x) lies in L_n.

Thus:

f_R(x) in P_R(n,d)

### 2. Inactive-coordinate identity

Need prove:

if alpha notin A_R, then:

f_R(x)_alpha=x_alpha

This is definitional.

### 3. Active-coordinate extensivity

Need prove:

if alpha in A_R, then:

x_alpha <= f_R(x)_alpha

because:

x_alpha <= h_alpha(x_alpha)

### 4. Global extensivity

Need prove:

x <=_R f_R(x)

for every x in P_R(n,d).

For active coordinates this follows from h_alpha extensivity.
For inactive coordinates this follows from equality.

### 5. Strict local progress below top

Need prove:

if alpha in A_R and x_alpha<n, then:

x_alpha < f_R(x)_alpha

because:

h_alpha(x_alpha)>x_alpha

### 6. Candidate fixed set

The expected fixed set is:

F_R = {x in P_R(n,d) : x_alpha=n for every alpha in A_R}

Expected later theorem:

Fix(f_R)=F_R

This fixed-set characterization may be proved either in the execution step or in the next fixed-set step.

To keep this step focused, the execution should at least record the candidate fixed set.

### 7. Candidate strict progressivity outside F_R

Expected later proof:

if x notin F_R, then x <_R f_R(x)

Reason:
x notin F_R means some active coordinate alpha has x_alpha<n.
Then h_alpha(x_alpha)>x_alpha.
All other coordinates are nondecreasing.
Therefore x <_R f_R(x).

This should be proved in a later fixed-set/strict-progressivity step unless the execution combines basic update properties.

## What this resolves

Expected resolved by execution:

1. f_R is explicitly defined.
2. f_R:P_R->P_R is well-defined.
3. active coordinates update by h_alpha.
4. inactive coordinates remain fixed.
5. x <=_R f_R(x) for every x.
6. local strict progress below top is recorded.

## What remains unresolved

Still unresolved after this planned update-map step:

1. Full fixed set proof:
   Fix(f_R)=F_R

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

This plan only prepares a restricted finite update-map definition.

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

1. formal definition of A_R
2. formal assumptions on h_alpha
3. formal definition of f_R
4. proof that f_R:P_R->P_R is well-defined
5. proof of inactive-coordinate identity
6. proof of active-coordinate extensivity
7. proof of global extensivity x<=_R f_R(x)
8. proof of local strict progress below top
9. candidate fixed set F_R
10. remaining blocker list
11. next action toward fixed-set and strict-progressivity proof

## Next allowed action

execute_vf_h2_original_theory_restricted_update_map_definition_no_claim_validation

VF_H2_ORIGINAL_THEORY_RESTRICTED_UPDATE_MAP_DEFINITION_PLAN_CREATED_OK
RUMAP_VF_H2_001_TARGET_DEFINED_NOT_PROVED_OK
P_R_STATEDEF_ANCHOR_CONFIRMED_OK
ORD_R_ANCHOR_CONFIRMED_OK
ACTIVE_INDEX_SET_A_R_DEFINED_OK
SATURATED_COORDINATE_FUNCTIONS_H_ALPHA_PLANNED_OK
UPDATE_MAP_F_R_PLANNED_OK
WELL_DEFINEDNESS_PROOF_OBLIGATION_DEFINED_OK
GLOBAL_EXTENSIVITY_PROOF_OBLIGATION_DEFINED_OK
LOCAL_STRICT_PROGRESS_BELOW_TOP_PROOF_OBLIGATION_DEFINED_OK
CANDIDATE_FIXED_SET_F_R_DEFINED_OK
STRICT_PROGRESSIVITY_OUTSIDE_F_R_REMAINS_UNPROVED_OK
LEDGER_FUNCTIONAL_REMAINS_UNRESOLVED_OK
LEDGER_EFFECT_IDENTITY_REMAINS_UNRESOLVED_OK
FULL_ORIGINAL_THEORY_REMAINS_NOT_PROVED_OK
ORIGINAL_UNRESTRICTED_TTP_VF_H2_004_REMAINS_NOT_PROVED_OK
NEXT_ALLOWED_EXECUTE_VF_H2_ORIGINAL_THEORY_RESTRICTED_UPDATE_MAP_DEFINITION_OK
