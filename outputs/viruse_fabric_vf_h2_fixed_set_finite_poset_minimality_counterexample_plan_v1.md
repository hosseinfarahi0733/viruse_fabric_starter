# VF-H2 Fixed-Set Finite Poset Minimality / Counterexample Plan v1

Action:
draft_vf_h2_fixed_set_finite_poset_minimality_counterexample_plan_no_claim_validation

Scope:
safe abstract finite order-theoretic toy VF-H2 only.

## Purpose

Plan counterexample checks for the fixed-set finite poset Lyapunov theorem and its activation/aggregate lift.

This is not a proof yet.
This does not prove the unrestricted theorem.
This does not prove a generalized theorem without assumptions.
This does not prove full Viruse Fabric theory.
This does not claim empirical or biological validation.
This does not claim manuscript readiness or submission readiness.

## Prior proved anchor

FFP-LYAP-T-VF-H2-001-R:
fixed-set finite poset Lyapunov improvement theorem.

Statement:
Let (P, <=) be a finite poset, f:P -> P, and F=Fix(f).
If:

1. x notin F implies x < f(x)
2. V is strict order-preserving

then:

- x notin F implies V(f(x)) > V(x)
- x in F implies V(f(x)) = V(x)

## Goal

Test whether the assumptions are necessary by constructing finite counterexamples when each key condition is removed.

The purpose is not to weaken the theorem irresponsibly.
The purpose is to identify which assumptions are mathematically essential.

## Minimality targets

### Target 1: remove strict progressivity outside F

Expected failure:
There may exist x notin F such that x is not below f(x), so V(f(x)) > V(x) need not follow.

Planned counterexample:

P = {a,b}

with a and b incomparable.

Define:

f(a)=b
f(b)=b

Then:

F=Fix(f)={b}

So:

a notin F

but:

a < f(a)

is false because a and b are incomparable.

Choose V(a)=1, V(b)=0.

Since there are no comparable strict pairs, V is vacuously strict order-preserving.

But:

V(f(a)) = V(b)=0 < 1=V(a)

Thus positive Lyapunov improvement fails.

Conclusion:
strict progressivity outside F is necessary.

### Target 2: remove strict order-preservation of V

Expected failure:
Even if x < f(x), V may fail to increase.

Planned counterexample:

P={a,b}

with:

a < b

Define:

f(a)=b
f(b)=b

Then:

F={b}

and for a notin F:

a < f(a)=b

So strict progressivity outside F holds.

Choose:

V(a)=0
V(b)=0

Then V is not strict order-preserving.

For a:

V(f(a)) = V(b)=0
V(a)=0

So:

V(f(a)) > V(a)

fails.

Conclusion:
strict order-preservation of V is necessary.

### Target 3: fixed-set consistency if F is externally specified

In the main theorem, F is defined as Fix(f), so fixed-point consistency is definitional.

If F is instead externally specified, then the condition:

x in F implies f(x)=x

must be assumed.

Planned counterexample for externally specified F:

P={a,b}

with:

a < b

Let:

F={a}

but define:

f(a)=b
f(b)=b

Then a is declared fixed by external F, but f(a) != a.

For x=a in F:

V(f(a)) = V(b) > V(a)

so the zero-change fixed-set conclusion fails.

Conclusion:
if F is not defined as Fix(f), fixed-set consistency is necessary.

### Target 4: remove A strictness preservation in activation lift

Expected failure:
Even if x < f(x), activation A may collapse the strict improvement.

Planned counterexample:

P={a,b}

with:

a < b

Define:

f(a)=b
f(b)=b

F={b}

Let activation domain Y={0}

with only one element.

Define:

A(a)=0
A(b)=0

Then A is monotone but not strictness-preserving.

Let G(0)=0.

For a:

A(a)=A(f(a))

so:

G(A(f(a))) - G(A(a)) = 0

Positive lifted effect fails.

Conclusion:
strictness preservation of A on relevant update pairs is necessary for the lift.

### Target 5: remove G strict positivity in activation lift

Expected failure:
Even if A preserves strictness, G may collapse strict activation-domain improvements.

Planned counterexample:

P={a,b}

with:

a < b

Define:

f(a)=b
f(b)=b

F={b}

Let:

Y={0,1}
0 < 1

Define:

A(a)=0
A(b)=1

So A preserves strictness.

Define:

G(0)=0
G(1)=0

Then G is not strictly positive.

For a:

A(a)<A(f(a))

but:

G(A(f(a))) - G(A(a)) = 0

Positive lifted effect fails.

Conclusion:
strict positivity of G is necessary for the lift.

## Non-minimality target

### Target 6: monotonicity of f is not necessary

The prior audit confirmed monotonicity of f is not required for one-step Lyapunov improvement.

Planned witness:

P={a,b,c}

with order:

a < b
a < c

and b,c incomparable.

Define:

f(a)=b
f(b)=b
f(c)=c

Then:

F={b,c}

For a notin F:

a < f(a)=b

So strict progressivity outside F holds.

But f is not monotone because:

a < c

yet:

f(a)=b

and:

f(c)=c

with b and c incomparable.

Choose strict order-preserving V, for example:

V(a)=0
V(b)=1
V(c)=1

Then:

V(f(a))=V(b)=1 > 0=V(a)

and fixed states have zero change.

Conclusion:
monotonicity of f is not necessary for the one-step theorem.

## Planned output

The execution step should produce:

1. finite counterexample for removing strict progressivity outside F
2. finite counterexample for removing strict order-preservation of V
3. finite counterexample for external F without fixed-set consistency
4. finite counterexample for removing A strictness preservation
5. finite counterexample for removing G strict positivity
6. witness showing monotonicity of f is not necessary

## Boundary

This only plans minimality/counterexample checks for the safe abstract finite poset theorem and its activation/aggregate lift.

It does not prove:

- original unrestricted TTP-VF-H2-004
- generalized ordered-domain theorem without assumptions
- full Viruse Fabric theory
- empirical validation
- biological validation
- manuscript readiness
- submission readiness

## Next allowed action

execute_vf_h2_fixed_set_finite_poset_minimality_counterexample_proof_attempt_no_claim_validation

VF_H2_FIXED_SET_FINITE_POSET_MINIMALITY_COUNTEREXAMPLE_PLAN_CREATED_OK
STRICT_PROGRESSIVITY_COUNTEREXAMPLE_TARGET_DEFINED_OK
STRICT_ORDER_PRESERVING_V_COUNTEREXAMPLE_TARGET_DEFINED_OK
EXTERNAL_FIXED_SET_CONSISTENCY_COUNTEREXAMPLE_TARGET_DEFINED_OK
A_STRICTNESS_PRESERVATION_COUNTEREXAMPLE_TARGET_DEFINED_OK
G_STRICT_POSITIVITY_COUNTEREXAMPLE_TARGET_DEFINED_OK
MONOTONICITY_F_NOT_NECESSARY_WITNESS_TARGET_DEFINED_OK
GENERALIZED_THEOREM_WITHOUT_ASSUMPTIONS_REMAINS_NOT_PROVED_OK
ORIGINAL_UNRESTRICTED_TTP_VF_H2_004_REMAINS_NOT_PROVED_OK
FULL_VIRUSE_FABRIC_THEORY_REMAINS_NOT_PROVED_OK
NEXT_ALLOWED_EXECUTE_VF_H2_FIXED_SET_FINITE_POSET_MINIMALITY_COUNTEREXAMPLE_PROOF_ATTEMPT_OK
