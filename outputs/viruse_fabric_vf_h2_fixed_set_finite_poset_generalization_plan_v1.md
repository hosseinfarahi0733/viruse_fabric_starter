# VF-H2 Fixed-Set Finite Poset Generalization Plan v1

Action:
draft_vf_h2_fixed_set_finite_poset_generalization_plan_no_claim_validation

Scope:
safe abstract finite order-theoretic toy VF-H2 only.

## Purpose

Plan a proof attempt compressing the VF-H2 finite coordinatewise toy proof chain into a fixed-set finite poset Lyapunov theorem.

This plan is based on user-provided mathematical review feedback.

No external endorsement is claimed.
No named mathematician endorsement is recorded or asserted.

This is not a proof.
This does not prove the unrestricted theorem.
This does not prove a generalized theorem without assumptions.
This does not prove full Viruse Fabric theory.
This does not claim empirical or biological validation.
This does not claim manuscript readiness or submission readiness.

## Reason for redirect

A non-identity activation/aggregate model plan already exists.

However, the stronger proof-forward step is now fixed-set finite poset generalization, because it compresses the existing coordinatewise toy chain into a cleaner order-theoretic theorem.

The redirect is:

from:
additional model-existence construction

to:
fixed-set finite poset Lyapunov generalization

Reason:

- multi-element fixed sets are needed for active-coordinate subset updates
- top-only finite bounded poset formulation is too narrow
- monotonicity of f is not needed for the minimal one-step improvement theorem
- product-lattice VF-H2 models should become corollaries, not separate endlessly repeated constructions

## Target theorem

FFP-LYAP-T-VF-H2-001-R:
fixed-set finite poset Lyapunov improvement theorem

Planned statement:

Let (P, <=) be a finite poset and let f:P -> P.

Let:

F = Fix(f) = {x in P : f(x)=x}

Assume:

1. strict progressivity outside F:
   if x notin F, then x < f(x)

2. V:P -> R is strict order-preserving:
   if x < y, then V(x) < V(y)

Then for all x in P:

- if x notin F, then V(f(x)) > V(x)
- if x in F, then V(f(x)) = V(x)

Thus V is a strict one-step Lyapunov function outside the fixed set F.

## Precision note

If F is defined as Fix(f), then:

x in F implies f(x)=x

is not an additional assumption.
It is definitional.

If F is instead specified independently, then the fixed-point condition must be stated as an assumption.

For this theorem, F is defined as Fix(f), so the fixed-point condition is not counted as an independent assumption.

## Monotonicity note

Monotonicity of f is not needed for the one-step Lyapunov improvement proof.

The proof uses only:

- x notin F implies x < f(x)
- V strict order-preserving

Monotonicity of f may be useful for stronger order-theoretic dynamics, closure-operator analysis, or structural interpretation, but it is not part of the minimal one-step theorem.

## Planned proof

For x notin F:

By strict progressivity outside F:

x < f(x)

By strict order preservation of V:

V(x) < V(f(x))

Therefore:

V(f(x)) > V(x)

For x in F:

Since F = Fix(f):

f(x)=x

Therefore:

V(f(x)) = V(x)

This proves the one-step Lyapunov improvement statement.

## Product-lattice VF-H2 corollary target

Let:

D_{n,d} = {0,1,...,n}^d

with coordinatewise order.

Let S be a nonempty active-coordinate subset.

Let:

M_{S,h}(x)_i =
- h_i(x_i), if i in S
- x_i, if i notin S

where each active h_i satisfies the VF-H2 saturated update assumptions:

- h_i maps {0,...,n} to {0,...,n}
- h_i is extensive
- h_i(n)=n
- if a<n, then h_i(a)>a

Then:

F = Fix(M_{S,h})
  = {x in D_{n,d} : x_i=n for every i in S}

This fixed set may be multi-element when S is not the full coordinate set.

Let:

rho(x) = sum_i x_i

Then rho is strict order-preserving on the coordinatewise product lattice.

Therefore:

x notin F implies rho(M_{S,h}(x)) > rho(x)

and:

x in F implies rho(M_{S,h}(x)) = rho(x)

This recovers the VF-H2 ledger-effect result:

rho(M_{S,h}(x)) - rho(x)
=
sum over i in S of [h_i(x_i)-x_i]

## Activation/aggregate lift target

Let A map P into an ordered activation domain Y.

Assume A is strictness-preserving on relevant update pairs:

x < f(x) implies A(x) <_Y A(f(x))

Let G map Y into a numeric ordered effect domain.

Assume G is strictly positive on strict activation-domain improvements:

u <_Y v implies G(v)-G(u)>0

Then:

x notin F implies G(A(f(x))) - G(A(x)) > 0

and:

x in F implies G(A(f(x))) - G(A(x)) = 0

This recovers the previously audited AAL-SDSCUF result as a corollary.

## Minimality follow-up plan

A follow-up minimality step should test counterexamples for removing:

1. strict progressivity outside F
2. strict order-preservation of V
3. fixed-set definitional consistency if F is specified independently
4. strictness preservation of A in the lift
5. strict positivity of G in the lift

Monotonicity of f should be classified as not necessary for the one-step theorem.

## Boundary

This only plans a finite poset fixed-set Lyapunov generalization of the safe abstract toy VF-H2 proof chain.

It does not prove:

- original unrestricted TTP-VF-H2-004
- generalized ordered-domain theorem without assumptions
- full Viruse Fabric theory
- empirical validation
- biological validation
- manuscript readiness
- submission readiness

## Next allowed action

execute_vf_h2_fixed_set_finite_poset_generalization_proof_attempt_no_claim_validation

VF_H2_FIXED_SET_FINITE_POSET_GENERALIZATION_PLAN_CREATED_OK
FFP_LYAP_T_VF_H2_001_R_TARGET_DEFINED_NOT_PROVED_OK
FIXED_SET_FORMULATION_SELECTED_OK
MULTI_ELEMENT_FIXED_SET_SUPPORTED_OK
TOP_ONLY_FORMULATION_SUPERSEDED_OK
MONOTONICITY_F_NOT_REQUIRED_FOR_ONE_STEP_IMPROVEMENT_NOTED_OK
PRODUCT_LATTICE_COROLLARY_TARGET_DEFINED_OK
ACTIVATION_AGGREGATE_LIFT_COROLLARY_TARGET_DEFINED_OK
NONIDENTITY_ACTIVATION_AGGREGATE_PLAN_RETAINED_BUT_NOT_EXECUTED_AS_NEXT_STEP_OK
NO_EXTERNAL_ENDORSEMENT_CLAIM_OK
GENERALIZED_THEOREM_WITHOUT_ASSUMPTIONS_REMAINS_NOT_PROVED_OK
ORIGINAL_UNRESTRICTED_TTP_VF_H2_004_REMAINS_NOT_PROVED_OK
FULL_VIRUSE_FABRIC_THEORY_REMAINS_NOT_PROVED_OK
NEXT_ALLOWED_EXECUTE_VF_H2_FIXED_SET_FINITE_POSET_GENERALIZATION_PROOF_ATTEMPT_OK
