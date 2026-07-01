# VF-H2 Original Theory Restricted Finite State Definition v1

Action:
execute_vf_h2_original_theory_restricted_finite_state_definition_no_claim_validation

Scope:
safe abstract mathematical formalization only.

This is a bridge-building step after OIMAP-VF-H2-001.

This does not reopen the frozen fixed-set finite poset package.
This does not prove full Viruse Fabric theory.
This does not prove original unrestricted TTP-VF-H2-004.
This does not claim empirical validation.
This does not claim biological validation.
This does not claim manuscript readiness.
This does not claim submission readiness.

## Purpose

Define a restricted finite VF-H2 state space P_R suitable for possible instantiation into:

FFP-LYAP-T-VF-H2-001-R

This resolves only the first bridge obligation:

finite restricted state abstraction P_R

It does not yet define:

- order relation
- update map
- fixed set
- strict progressivity
- ledger/Lyapunov functional
- ledger_effect_size identity

## Target result

P_R-STATEDEF-VF-H2-001-R:
restricted finite VF-H2 state-space definition

## Parameters

Let:

n >= 1

and:

d >= 1

be fixed positive integers.

Define the abstract three-time layer set:

T_3 = {1,2,3}

Define the finite coordinate index set:

I_d = {1,2,...,d}

Define the finite level alphabet:

L_n = {0,1,...,n}

All symbols are safe abstract mathematical objects.

No biological, empirical, or physical interpretation is assigned.

## Definition of restricted state space

Define:

P_R(n,d) = L_n^(T_3 x I_d)

Equivalently:

P_R(n,d) = {x : T_3 x I_d -> L_n}

An element x in P_R(n,d) is a finite array:

x = (x_{tau,i})

where:

tau in T_3
i in I_d
x_{tau,i} in L_n

Interpretation:
x_{tau,i} is an abstract finite coordinate value at layer tau and coordinate i.

This state space can later support abstract interpretations such as:

- causal-level coordinates
- ledger-level coordinates
- constraint-progress coordinates
- activation-ready coordinates

but those interpretations are not validated or proved in this step.

## Finiteness proof

Since:

|T_3| = 3

and:

|I_d| = d

the product index set has size:

|T_3 x I_d| = 3d

Since:

|L_n| = n+1

the number of functions from T_3 x I_d into L_n is:

|L_n|^(|T_3 x I_d|)

Therefore:

|P_R(n,d)|
=
(n+1)^(3d)

Because n and d are finite positive integers, (n+1)^(3d) is finite.

Thus:

P_R(n,d)

is finite.

## Carrier obligation result

The finite-carrier obligation from OIMAP-VF-H2-001 is resolved for the restricted finite bridge route.

Resolved:

1. P_R is explicitly defined.
2. P_R is finite.
3. P_R has cardinality (n+1)^(3d).
4. P_R supports three abstract layers.
5. P_R is compatible with later coordinatewise order definition.

## Optional channel extension

If later needed, define:

C_k = {1,2,...,k}

and:

P_R(n,d,k) = L_n^(T_3 x I_d x C_k)

with cardinality:

|P_R(n,d,k)| = (n+1)^(3dk)

However, this channel extension is deferred.

Reason:
The minimal bridge route should first use P_R(n,d) unless a later update-map or ledger-functional definition requires additional channels.

## What this does not resolve

Still unresolved:

1. Order relation <=_R on P_R
2. Proof that <=_R is a partial order
3. Update map f_VF:P_R->P_R
4. Fixed set F_R=Fix(f_VF)
5. Saturation predicate saturated_VF(x)
6. Equivalence saturated_VF(x) iff f_VF(x)=x
7. Strict progressivity outside F_R
8. Ledger/Lyapunov functional V_VF
9. Strict order-preservation of V_VF
10. ledger_effect_size identity
11. Activation/aggregate layer assumptions, if used

## Candidate next definition

The natural next step is to define a coordinatewise order on P_R(n,d):

x <=_R y

iff for every tau in T_3 and every i in I_d:

x_{tau,i} <= y_{tau,i}

Expected later proof obligations:

1. reflexivity
2. antisymmetry
3. transitivity

This next proof should establish that:

(P_R(n,d), <=_R)

is a finite poset.

## Boundary

This step proves only a restricted finite state-space definition.

It does not prove:

- full Viruse Fabric theory
- original unrestricted TTP-VF-H2-004
- generalized theorem without assumptions
- empirical validation
- biological validation
- manuscript readiness
- submission readiness

## Result

P_R-STATEDEF-VF-H2-001-R proved:
true

Restricted finite VF-H2 state space:

P_R(n,d)=L_n^(T_3 x I_d)

is finite with cardinality:

(n+1)^(3d)

## Next allowed action

draft_vf_h2_original_theory_coordinatewise_order_definition_plan_no_claim_validation

VF_H2_ORIGINAL_THEORY_RESTRICTED_FINITE_STATE_DEFINITION_EXECUTED_OK
P_R_STATEDEF_VF_H2_001_R_PROVED_TRUE_OK
T3_DEFINED_OK
I_D_DEFINED_OK
L_N_DEFINED_OK
P_R_N_D_DEFINED_AS_L_N_POWER_T3_CROSS_I_D_OK
P_R_FINITE_PROVED_OK
P_R_CARDINALITY_PROVED_OK
FINITE_CARRIER_OBLIGATION_RESOLVED_FOR_RESTRICTED_BRIDGE_OK
OPTIONAL_CHANNEL_EXTENSION_DEFERRED_OK
ORDER_RELATION_REMAINS_UNRESOLVED_OK
UPDATE_MAP_REMAINS_UNRESOLVED_OK
STRICT_PROGRESSIVITY_REMAINS_UNRESOLVED_OK
LEDGER_FUNCTIONAL_REMAINS_UNRESOLVED_OK
LEDGER_EFFECT_IDENTITY_REMAINS_UNRESOLVED_OK
FULL_ORIGINAL_THEORY_REMAINS_NOT_PROVED_OK
ORIGINAL_UNRESTRICTED_TTP_VF_H2_004_REMAINS_NOT_PROVED_OK
NEXT_ALLOWED_DRAFT_VF_H2_ORIGINAL_THEORY_COORDINATEWISE_ORDER_DEFINITION_PLAN_OK
