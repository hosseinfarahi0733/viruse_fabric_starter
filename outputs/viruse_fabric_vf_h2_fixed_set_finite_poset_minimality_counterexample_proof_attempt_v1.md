# VF-H2 Fixed-Set Finite Poset Minimality / Counterexample Proof Attempt v1

Action:
execute_vf_h2_fixed_set_finite_poset_minimality_counterexample_proof_attempt_no_claim_validation

Scope:
safe abstract finite order-theoretic toy VF-H2 only.

## Purpose

Execute counterexample checks for the fixed-set finite poset Lyapunov theorem and its activation/aggregate lift.

This proof attempt tests which assumptions are necessary and which assumptions are not required.

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

## Result summary

The counterexample suite establishes:

1. strict progressivity outside F is necessary
2. strict order-preservation of V is necessary
3. fixed-set consistency is necessary if F is externally specified rather than defined as Fix(f)
4. A strictness preservation is necessary for the activation lift
5. G strict positivity is necessary for the aggregate lift
6. monotonicity of f is not necessary for the one-step theorem

## Counterexample 1: removing strict progressivity outside F

Goal:
Show that without:

x notin F implies x < f(x)

the conclusion:

V(f(x)) > V(x)

can fail.

Let:

P = {a,b}

with a and b incomparable.

Define:

f(a)=b
f(b)=b

Then:

F=Fix(f)={b}

Thus:

a notin F

But:

a < f(a)

is false, because a and b are incomparable.

Now define:

V(a)=1
V(b)=0

Since P has no strict comparable pairs, V is vacuously strict order-preserving.

However:

V(f(a)) = V(b) = 0

and:

V(a)=1

Therefore:

V(f(a)) > V(a)

is false.

Indeed:

0 > 1

is false.

Conclusion:
strict progressivity outside F is necessary for the fixed-set finite poset Lyapunov theorem.

STRICT_PROGRESSIVITY_OUTSIDE_F_NECESSARY_COUNTEREXAMPLE_OK

## Counterexample 2: removing strict order-preservation of V

Goal:
Show that without strict order-preservation of V, strict progressivity of f does not imply Lyapunov improvement.

Let:

P={a,b}

with:

a < b

Define:

f(a)=b
f(b)=b

Then:

F=Fix(f)={b}

For the only non-fixed point a:

a < f(a)=b

So strict progressivity outside F holds.

Now define V as constant:

V(a)=0
V(b)=0

Then V is not strict order-preserving, because:

a < b

but:

V(a)=V(b)

For a:

V(f(a)) = V(b)=0

and:

V(a)=0

Therefore:

V(f(a)) > V(a)

is false.

Conclusion:
strict order-preservation of V is necessary.

STRICT_ORDER_PRESERVING_V_NECESSARY_COUNTEREXAMPLE_OK

## Counterexample 3: external F without fixed-set consistency

In the main theorem:

F = Fix(f)

Therefore:

x in F implies f(x)=x

is definitional.

This counterexample applies only if F is externally specified instead of defined as Fix(f).

Goal:
Show that if F is externally declared but not consistent with f, then the fixed-state zero-change conclusion can fail.

Let:

P={a,b}

with:

a < b

Externally declare:

F_ext={a}

Define:

f(a)=b
f(b)=b

Then:

a in F_ext

but:

f(a) != a

Choose strict order-preserving V:

V(a)=0
V(b)=1

For x=a in F_ext:

V(f(a)) = V(b)=1

but:

V(a)=0

Therefore:

V(f(a)) = V(a)

is false.

Conclusion:
if F is specified independently rather than defined as Fix(f), fixed-set consistency must be assumed.

EXTERNAL_FIXED_SET_CONSISTENCY_NECESSARY_COUNTEREXAMPLE_OK

## Counterexample 4: removing A strictness preservation in the activation lift

Goal:
Show that without A strictness preservation on relevant update pairs, the lifted positive effect can collapse.

Let:

P={a,b}

with:

a < b

Define:

f(a)=b
f(b)=b

Then:

F=Fix(f)={b}

For a notin F:

a < f(a)=b

Let activation domain:

Y={0}

with the only possible order.

Define constant activation:

A(a)=0
A(b)=0

Then A is monotone but not strictness-preserving, since:

a < f(a)

but:

A(a)=A(f(a))

Let:

G(0)=0

For a:

G(A(f(a))) - G(A(a))
=
G(0)-G(0)
=
0

The desired lifted positivity:

G(A(f(a))) - G(A(a)) > 0

fails.

Conclusion:
A strictness preservation on relevant update pairs is necessary for the activation lift.

A_STRICTNESS_PRESERVATION_NECESSARY_COUNTEREXAMPLE_OK

## Counterexample 5: removing G strict positivity in the aggregate lift

Goal:
Show that without strict positivity of G, activation-domain strictness may not produce positive aggregate effect.

Let:

P={a,b}

with:

a < b

Define:

f(a)=b
f(b)=b

Then:

F=Fix(f)={b}

For a notin F:

a < f(a)=b

Let activation domain:

Y={0,1}

with:

0 < 1

Define:

A(a)=0
A(b)=1

Then A is strictness-preserving on the relevant update pair:

a < f(a)

implies:

A(a)=0 < 1=A(f(a))

Now define constant aggregate:

G(0)=0
G(1)=0

Then G is not strictly positive on strict activation-domain improvements.

For a:

G(A(f(a))) - G(A(a))
=
G(1)-G(0)
=
0-0
=
0

The desired positive lifted effect fails.

Conclusion:
G strict positivity is necessary for the aggregate lift.

G_STRICT_POSITIVITY_NECESSARY_COUNTEREXAMPLE_OK

## Witness 6: monotonicity of f is not necessary

Goal:
Show that the one-step Lyapunov theorem can hold even when f is not monotone.

Let:

P={a,b,c}

with order relations:

a < b
a < c

and b,c incomparable.

Define:

f(a)=b
f(b)=b
f(c)=c

Then:

F=Fix(f)={b,c}

The only non-fixed point is a.

For a:

a < f(a)=b

So strict progressivity outside F holds.

Now check monotonicity of f.

Since:

a < c

monotonicity would require:

f(a) <= f(c)

But:

f(a)=b
f(c)=c

and b,c are incomparable.

Therefore f is not monotone.

Define:

V(a)=0
V(b)=1
V(c)=1

V is strict order-preserving because the only strict order relations are:

a < b
a < c

and both give:

0 < 1

For the only non-fixed point a:

V(f(a)) = V(b)=1

and:

V(a)=0

Thus:

V(f(a)) > V(a)

For fixed points b and c:

f(b)=b
f(c)=c

so:

V(f(b))=V(b)
V(f(c))=V(c)

Conclusion:
monotonicity of f is not necessary for the one-step fixed-set Lyapunov theorem.

MONOTONICITY_F_NOT_NECESSARY_WITNESS_OK

## Overall result

The minimality/counterexample suite is established.

Confirmed necessary for the base theorem:

1. strict progressivity outside F
2. strict order-preservation of V

Confirmed necessary only if F is externally specified:

3. fixed-set consistency

Confirmed necessary for the activation/aggregate lift:

4. A strictness preservation on relevant update pairs
5. G strict positivity on strict activation-domain improvements

Confirmed not necessary for the one-step theorem:

6. monotonicity of f

## Boundary

This establishes only finite counterexample checks for the safe abstract finite poset theorem and its activation/aggregate lift.

It does not prove:

- original unrestricted TTP-VF-H2-004
- generalized ordered-domain theorem without assumptions
- full Viruse Fabric theory
- empirical validation
- biological validation
- manuscript readiness
- submission readiness

## Next allowed action

audit_vf_h2_fixed_set_finite_poset_minimality_counterexample_proof_attempt_no_claim_validation

VF_H2_FIXED_SET_FINITE_POSET_MINIMALITY_COUNTEREXAMPLE_PROOF_ATTEMPT_EXECUTED_OK
STRICT_PROGRESSIVITY_OUTSIDE_F_NECESSARY_COUNTEREXAMPLE_OK
STRICT_ORDER_PRESERVING_V_NECESSARY_COUNTEREXAMPLE_OK
EXTERNAL_FIXED_SET_CONSISTENCY_NECESSARY_COUNTEREXAMPLE_OK
A_STRICTNESS_PRESERVATION_NECESSARY_COUNTEREXAMPLE_OK
G_STRICT_POSITIVITY_NECESSARY_COUNTEREXAMPLE_OK
MONOTONICITY_F_NOT_NECESSARY_WITNESS_OK
MINIMALITY_COUNTEREXAMPLE_SUITE_ESTABLISHED_OK
GENERALIZED_THEOREM_WITHOUT_ASSUMPTIONS_REMAINS_NOT_PROVED_OK
ORIGINAL_UNRESTRICTED_TTP_VF_H2_004_REMAINS_NOT_PROVED_OK
FULL_VIRUSE_FABRIC_THEORY_REMAINS_NOT_PROVED_OK
NEXT_ALLOWED_AUDIT_VF_H2_FIXED_SET_FINITE_POSET_MINIMALITY_COUNTEREXAMPLE_PROOF_ATTEMPT_OK
