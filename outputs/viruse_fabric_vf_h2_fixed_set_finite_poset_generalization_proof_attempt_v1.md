# VF-H2 Fixed-Set Finite Poset Generalization Proof Attempt v1

Action:
execute_vf_h2_fixed_set_finite_poset_generalization_proof_attempt_no_claim_validation

Scope:
safe abstract finite order-theoretic toy VF-H2 only.

## Purpose

Execute the proof attempt compressing the VF-H2 finite coordinatewise toy proof chain into a fixed-set finite poset Lyapunov theorem.

This proof does not use or claim external endorsement.
No named mathematician endorsement is claimed.

This does not prove the unrestricted theorem.
This does not prove a generalized theorem without assumptions.
This does not prove full Viruse Fabric theory.
This does not claim empirical or biological validation.
This does not claim manuscript readiness or submission readiness.

## Target theorem

FFP-LYAP-T-VF-H2-001-R:
fixed-set finite poset Lyapunov improvement theorem

## Statement

Let:

(P, <=)

be a finite poset and let:

f:P -> P

be a map.

Let:

F = Fix(f) = {x in P : f(x)=x}

Assume:

1. strict progressivity outside F:

if x notin F, then x < f(x)

2. strict order-preserving Lyapunov functional:

V:P -> R

such that:

if x < y, then V(x) < V(y)

Then for all x in P:

- if x notin F, then V(f(x)) > V(x)
- if x in F, then V(f(x)) = V(x)

Thus V is a strict one-step Lyapunov function outside the fixed set F.

## Precision note

Because F is defined as Fix(f), the statement:

x in F implies f(x)=x

is definitional, not an additional assumption.

If F were specified independently, then fixed-point consistency would need to be assumed separately.

## Proof

Let x be an arbitrary element of P.

### Case 1: x notin F

By strict progressivity outside F:

x < f(x)

Since V is strict order-preserving:

x < f(x) implies V(x) < V(f(x))

Therefore:

V(f(x)) > V(x)

So every non-fixed state has strict positive Lyapunov improvement.

### Case 2: x in F

Since:

F = Fix(f)

we have:

f(x)=x

Therefore:

V(f(x)) = V(x)

So every fixed state has zero Lyapunov change.

This proves the theorem.

## Finite-dynamics consequence

Because P is finite, an orbit:

x, f(x), f(f(x)), ...

cannot contain infinitely many distinct states.

For every non-fixed state, V strictly increases after one step.

Therefore a trajectory cannot revisit a non-fixed state.

Hence every trajectory eventually reaches F.

This convergence consequence still does not require monotonicity of f.

## Monotonicity note

Monotonicity of f is not used in the proof.

The proof uses only:

- strict progressivity outside F
- strict order-preservation of V
- the definition F=Fix(f)

Therefore monotonicity of f is not required for the minimal one-step Lyapunov theorem.

Monotonicity may still be useful for stronger order-theoretic dynamics, closure-operator interpretation, or structural analysis, but it is not part of this minimal one-step result.

## Product-lattice VF-H2 corollary

Let:

D_{n,d} = {0,1,...,n}^d

with coordinatewise order.

Let S be a nonempty active-coordinate subset of {1,...,d}.

For every active coordinate i in S, let:

h_i : {0,1,...,n} -> {0,1,...,n}

satisfy:

1. h_i maps the coordinate domain into itself
2. h_i is extensive: a <= h_i(a)
3. h_i(n)=n
4. if a<n, then h_i(a)>a

Define:

M_{S,h}(x)_i =
- h_i(x_i), if i in S
- x_i, if i notin S

Let:

rho(x) = sum_i x_i

### Fixed set

The fixed set is:

F = Fix(M_{S,h})
  = {x in D_{n,d} : x_i=n for every i in S}

Proof:

If x_i=n for every active i in S, then h_i(x_i)=h_i(n)=n=x_i for active coordinates, and inactive coordinates are unchanged. Hence M_{S,h}(x)=x.

Conversely, if there exists active i in S with x_i<n, then h_i(x_i)>x_i, so M_{S,h}(x) differs from x. Hence x is not fixed.

Therefore:

F = {x : x_i=n for every i in S}

This fixed set may be multi-element when S is not the full coordinate set.

### Strict progressivity outside F

If x notin F, then there exists i in S such that x_i<n.

By strict progressivity below top:

h_i(x_i)>x_i

For active coordinates, extensiveness gives x_j <= h_j(x_j).

For inactive coordinates, M_{S,h}(x)_j=x_j.

Therefore:

x < M_{S,h}(x)

### Rank functional

rho is strict order-preserving on the coordinatewise product lattice:

if x<y, then x_i<=y_i for every coordinate and at least one coordinate is strictly smaller.

Therefore:

rho(x) = sum_i x_i < sum_i y_i = rho(y)

### Ledger effect

By the fixed-set theorem:

x notin F implies rho(M_{S,h}(x)) > rho(x)

and:

x in F implies rho(M_{S,h}(x)) = rho(x)

Moreover:

rho(M_{S,h}(x)) - rho(x)
=
sum over i in S of [h_i(x_i)-x_i]

Thus the VF-H2 finite coordinatewise ledger-effect result follows as a corollary.

## Activation/aggregate lift corollary

Let A map P into an ordered activation domain Y.

Assume A is strictness-preserving on relevant update pairs:

x < f(x) implies A(x) <_Y A(f(x))

Let G map Y into a numeric ordered effect domain.

Assume G is strictly positive on strict activation-domain improvements:

u <_Y v implies G(v)-G(u)>0

Define:

ledger_effect_size_{A,G}(x)
=
G(A(f(x))) - G(A(x))

If x notin F, then by the fixed-set theorem:

x < f(x)

By strictness preservation of A:

A(x) <_Y A(f(x))

By strict positivity of G:

G(A(f(x))) - G(A(x)) > 0

Therefore:

x notin F implies ledger_effect_size_{A,G}(x)>0

If x in F, then f(x)=x, so:

ledger_effect_size_{A,G}(x)
=
G(A(x))-G(A(x))
=
0

Thus the activation/aggregate lift follows as a corollary.

## Result

FFP-LYAP-T-VF-H2-001-R proved:
true

The proof establishes:

- fixed-set finite poset Lyapunov improvement
- multi-element fixed sets are supported
- top-only formulation is not required
- monotonicity of f is not required for one-step improvement
- product-lattice VF-H2 ledger effect follows as a corollary
- activation/aggregate lift follows under explicit A and G assumptions

## Boundary

This proves only a finite poset fixed-set Lyapunov theorem within the safe abstract toy VF-H2 proof chain.

It does not prove:

- original unrestricted TTP-VF-H2-004
- generalized ordered-domain theorem without assumptions
- full Viruse Fabric theory
- empirical validation
- biological validation
- manuscript readiness
- submission readiness

## Next allowed action

audit_vf_h2_fixed_set_finite_poset_generalization_proof_attempt_no_claim_validation

VF_H2_FIXED_SET_FINITE_POSET_GENERALIZATION_PROOF_ATTEMPT_EXECUTED_OK
FFP_LYAP_T_VF_H2_001_R_PROVED_TRUE_OK
FIXED_SET_FINITE_POSET_LYAPUNOV_THEOREM_PROVED_OK
MULTI_ELEMENT_FIXED_SET_SUPPORTED_CONFIRMED_OK
TOP_ONLY_FORMULATION_NOT_REQUIRED_CONFIRMED_OK
MONOTONICITY_F_NOT_REQUIRED_FOR_ONE_STEP_IMPROVEMENT_CONFIRMED_OK
PRODUCT_LATTICE_VF_H2_COROLLARY_PROVED_OK
ACTIVATION_AGGREGATE_LIFT_COROLLARY_PROVED_UNDER_EXPLICIT_ASSUMPTIONS_OK
NO_EXTERNAL_ENDORSEMENT_CLAIM_OK
GENERALIZED_THEOREM_WITHOUT_ASSUMPTIONS_REMAINS_NOT_PROVED_OK
ORIGINAL_UNRESTRICTED_TTP_VF_H2_004_REMAINS_NOT_PROVED_OK
FULL_VIRUSE_FABRIC_THEORY_REMAINS_NOT_PROVED_OK
NEXT_ALLOWED_AUDIT_VF_H2_FIXED_SET_FINITE_POSET_GENERALIZATION_PROOF_ATTEMPT_OK
