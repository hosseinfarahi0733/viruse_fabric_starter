# VF-H2 Fixed-Set Finite Poset Minimality / Counterexample Proof Attempt Audit v1

Action:
audit_vf_h2_fixed_set_finite_poset_minimality_counterexample_proof_attempt_no_claim_validation

Source commit:
587b78e

Audit result:
passed with finite-counterexample scope clarification

## Confirmed prior anchor

FFP-LYAP-T-VF-H2-001-R remains the proved anchor:

Let (P, <=) be a finite poset, f:P -> P, and F=Fix(f).
If:

1. x notin F implies x < f(x)
2. V is strict order-preserving

then:

- x notin F implies V(f(x)) > V(x)
- x in F implies V(f(x)) = V(x)

## Counterexample audit

### 1. Strict progressivity outside F

Confirmed:
The counterexample with P={a,b} incomparable, f(a)=b, f(b)=b, F={b}, and V(a)=1,V(b)=0 is valid.

Reason:
a notin F, but a < f(a) is false because a and b are incomparable.
V is vacuously strict order-preserving because there are no strict comparable pairs.
The positive improvement conclusion fails:

V(f(a)) = V(b)=0
V(a)=1

So:

V(f(a)) > V(a)

is false.

Conclusion:
strict progressivity outside F is necessary.

### 2. Strict order-preservation of V

Confirmed:
The counterexample with P={a<b}, f(a)=b, f(b)=b, F={b}, and constant V is valid.

Reason:
strict progressivity outside F holds because a < f(a)=b.
But V is not strict order-preserving.
The positive improvement conclusion fails:

V(f(a)) = V(a)

Conclusion:
strict order-preservation of V is necessary.

### 3. External F without fixed-set consistency

Confirmed:
The external-F counterexample is valid only for formulations where F is externally specified rather than defined as Fix(f).

Reason:
If F_ext={a} while f(a)=b, then a is externally labeled fixed even though f(a) != a.
The fixed-state zero-change conclusion fails:

V(f(a)) != V(a)

Conclusion:
If F is defined as Fix(f), fixed-set consistency is definitional.
If F is specified externally, fixed-set consistency is necessary.

### 4. A strictness preservation in activation lift

Confirmed:
The constant-activation counterexample is valid.

Reason:
P={a<b}, f(a)=b, f(b)=b gives a < f(a).
Constant A collapses the strict update pair:

A(a)=A(f(a))

Thus the lifted positive effect can be zero.

Conclusion:
A strictness preservation on relevant update pairs is necessary for the activation lift.

### 5. G strict positivity in aggregate lift

Confirmed:
The constant-G counterexample is valid.

Reason:
A preserves strictness with A(a)=0 and A(b)=1.
But constant G collapses the strict activation improvement:

G(A(f(a))) - G(A(a)) = 0

Conclusion:
G strict positivity on strict activation-domain improvements is necessary for the aggregate lift.

### 6. Monotonicity of f is not necessary

Confirmed:
The witness with P={a,b,c}, order a<b and a<c with b,c incomparable, and f(a)=b, f(b)=b, f(c)=c is valid.

Reason:
F={b,c}.
The only non-fixed point a satisfies:

a < f(a)=b

So strict progressivity outside F holds.

But f is not monotone because:

a < c

while:

f(a)=b
f(c)=c

and b,c are incomparable.

With V(a)=0,V(b)=1,V(c)=1, V is strict order-preserving and the one-step Lyapunov conclusion holds.

Conclusion:
monotonicity of f is not necessary for the one-step fixed-set theorem.

## Minimality conclusion

Confirmed necessary for the base fixed-set theorem:

1. strict progressivity outside F
2. strict order-preservation of V

Confirmed necessary only when F is externally specified:

3. fixed-set consistency

Confirmed necessary for the activation/aggregate lift:

4. A strictness preservation on relevant update pairs
5. G strict positivity on strict activation-domain improvements

Confirmed not necessary for the one-step theorem:

6. monotonicity of f

## Boundary confirmation

This audit confirms only finite counterexample checks for the safe abstract finite poset theorem and its activation/aggregate lift.

It does not prove:

- original unrestricted TTP-VF-H2-004
- generalized ordered-domain theorem without assumptions
- full Viruse Fabric theory
- empirical validation
- biological validation
- manuscript readiness
- submission readiness

## Decision

The fixed-set finite poset proof chain is now strong enough for a limited technical-note consolidation step.

The next step should collect:

- FFP-LYAP-T-VF-H2-001-R
- product-lattice VF-H2 corollary
- activation/aggregate lift corollary
- minimality/counterexample suite
- explicit boundary statements

into a limited technical note skeleton without claiming submission readiness.

## Next allowed action

draft_vf_h2_fixed_set_finite_poset_limited_technical_note_consolidation_plan_no_claim_submission

VF_H2_FIXED_SET_FINITE_POSET_MINIMALITY_COUNTEREXAMPLE_AUDIT_PASSED_OK
STRICT_PROGRESSIVITY_OUTSIDE_F_NECESSARY_CONFIRMED_OK
STRICT_ORDER_PRESERVING_V_NECESSARY_CONFIRMED_OK
EXTERNAL_FIXED_SET_CONSISTENCY_NECESSARY_IF_F_EXTERNAL_CONFIRMED_OK
A_STRICTNESS_PRESERVATION_NECESSARY_FOR_LIFT_CONFIRMED_OK
G_STRICT_POSITIVITY_NECESSARY_FOR_LIFT_CONFIRMED_OK
MONOTONICITY_F_NOT_NECESSARY_FOR_ONE_STEP_THEOREM_CONFIRMED_OK
MINIMALITY_COUNTEREXAMPLE_SUITE_ESTABLISHED_CONFIRMED_OK
GENERALIZED_THEOREM_WITHOUT_ASSUMPTIONS_REMAINS_NOT_PROVED_OK
ORIGINAL_UNRESTRICTED_TTP_VF_H2_004_REMAINS_NOT_PROVED_OK
FULL_VIRUSE_FABRIC_THEORY_REMAINS_NOT_PROVED_OK
NO_MANUSCRIPT_READY_CLAIM_OK
NO_SUBMISSION_READY_CLAIM_OK
NEXT_ALLOWED_DRAFT_VF_H2_FIXED_SET_FINITE_POSET_LIMITED_TECHNICAL_NOTE_CONSOLIDATION_PLAN_OK
