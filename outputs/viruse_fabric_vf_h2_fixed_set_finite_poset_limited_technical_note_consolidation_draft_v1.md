# Strict Lyapunov Improvement for Maps with Characterized Fixed Sets on Finite Posets

Limited Technical Note Draft Skeleton v1

Action:
execute_vf_h2_fixed_set_finite_poset_limited_technical_note_consolidation_draft_no_claim_submission

Scope:
safe abstract finite order-theoretic toy VF-H2 only.

## Status

This is a limited technical note draft skeleton.

This is not a submission-ready manuscript.
This is not a manuscript-readiness claim.
This is not a journal-suitability claim.
This is not an external endorsement claim.
No named mathematician endorsement is recorded or asserted.

This note does not prove:

- original unrestricted TTP-VF-H2-004
- generalized theorem without assumptions
- full Viruse Fabric theory
- empirical validation
- biological validation

## Abstract

This note studies a restricted finite order-theoretic toy setting motivated by VF-H2 ledger dynamics. We prove a fixed-set Lyapunov improvement theorem for maps on finite posets: if every non-fixed point is strictly increased by the map and the functional is strict order-preserving, then the functional strictly increases outside the fixed set and remains unchanged on the fixed set. This formulation supports multi-element fixed sets, unlike top-only formulations. As a corollary, finite product-lattice VF-H2 subset-update models yield positive ledger effect outside the active-coordinate saturated set. We also record an activation/aggregate lift under explicit strictness-preservation and strict-positivity assumptions. Finally, finite counterexamples show the necessity of the main assumptions and clarify that monotonicity of the update map is not required for the one-step theorem.

Boundary:
This note is restricted to a safe abstract finite toy theorem. It is not empirical validation and does not establish the full Viruse Fabric theory.

## 1. Introduction

The VF-H2 proof chain began as a restricted finite coordinatewise toy theorem about positive ledger effect under explicit structural assumptions. Subsequent proof steps extended the model through finite chains, product lattices, active-coordinate subset updates, weighted updates, state-dependent saturated updates, and activation/aggregate lifts.

The purpose of this note is not to introduce a full theory. Instead, the goal is to consolidate the audited proof chain into a small finite-poset Lyapunov theorem.

The central observation is that the essential mechanism is order-theoretic:

- non-fixed states are strictly moved upward by the update map
- a strict order-preserving functional detects this upward movement
- therefore the functional strictly increases outside the fixed set

This formulation naturally handles multi-element fixed sets, which occur in VF-H2 active-coordinate subset updates.

## 2. Preliminaries

Let:

(P, <=)

be a finite poset.

For x,y in P, write:

x < y

when:

x <= y and x != y

Let:

f:P -> P

be a map.

Define the fixed set:

F = Fix(f) = {x in P : f(x)=x}

A map f is strictly progressive outside F when:

x notin F implies x < f(x)

A function:

V:P -> R

is strict order-preserving when:

x < y implies V(x) < V(y)

Precision note:
Because F is defined as Fix(f), the implication:

x in F implies f(x)=x

is definitional, not an additional assumption.

If F is instead specified independently, fixed-set consistency must be assumed separately.

## 3. Main theorem

### Theorem FFP-LYAP-T-VF-H2-001-R

Let (P, <=) be a finite poset and let f:P -> P be a map.

Let:

F = Fix(f)

Assume:

1. strict progressivity outside F:

   x notin F implies x < f(x)

2. strict order-preservation:

   V:P -> R satisfies x < y implies V(x) < V(y)

Then for all x in P:

- if x notin F, then V(f(x)) > V(x)
- if x in F, then V(f(x)) = V(x)

Thus V is a strict one-step Lyapunov function outside the fixed set F.

### Proof

Let x be arbitrary.

Case 1:
x notin F.

By strict progressivity outside F:

x < f(x)

Since V is strict order-preserving:

V(x) < V(f(x))

Therefore:

V(f(x)) > V(x)

Case 2:
x in F.

Since F=Fix(f):

f(x)=x

Therefore:

V(f(x)) = V(x)

This proves the theorem.

### Monotonicity note

The proof does not use monotonicity of f.

Therefore monotonicity of f is not required for the one-step Lyapunov improvement theorem.

Monotonicity may still be useful for stronger structural interpretations, closure-operator analysis, or monotone finite dynamics, but it is not part of the minimal one-step theorem.

## 4. Finite-dynamics consequence

Because P is finite, an orbit:

x, f(x), f(f(x)), ...

cannot contain infinitely many distinct non-fixed states under strict Lyapunov improvement.

Outside F, the value V strictly increases. Therefore no non-fixed state can be revisited.

Thus every trajectory eventually reaches F.

This remains a finite abstract toy-dynamics consequence. It is not empirical validation.

## 5. Product-lattice VF-H2 corollary

Let:

D_{n,d} = {0,1,...,n}^d

with coordinatewise order.

Let S be a nonempty active-coordinate subset of {1,...,d}.

For each active coordinate i in S, let:

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

### Fixed set

The fixed set is:

F = Fix(M_{S,h})
  = {x in D_{n,d} : x_i=n for every i in S}

If all active coordinates equal n, then active coordinates remain fixed by h_i(n)=n and inactive coordinates are unchanged.

Conversely, if some active coordinate i satisfies x_i<n, then h_i(x_i)>x_i, so M_{S,h}(x) differs from x.

Therefore the fixed set is exactly the active-coordinate saturated set.

### Rank functional

Let:

rho(x) = sum_i x_i

If x < y in coordinatewise order, then every coordinate of x is less than or equal to the corresponding coordinate of y, and at least one coordinate is strictly smaller.

Therefore:

rho(x) < rho(y)

So rho is strict order-preserving.

### Ledger effect

By the main theorem:

x notin F implies rho(M_{S,h}(x)) > rho(x)

and:

x in F implies rho(M_{S,h}(x)) = rho(x)

Moreover:

rho(M_{S,h}(x)) - rho(x)
=
sum over i in S of [h_i(x_i)-x_i]

Thus the VF-H2 product-lattice ledger-effect result follows as a corollary.

## 6. Activation/aggregate lift

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

If x notin F, then:

x < f(x)

Therefore:

A(x) <_Y A(f(x))

By strict positivity of G:

G(A(f(x))) - G(A(x)) > 0

If x in F, then:

f(x)=x

Therefore:

G(A(f(x))) - G(A(x))
=
G(A(x))-G(A(x))
=
0

Thus the activation/aggregate lift follows under explicit A and G assumptions.

## 7. Minimality and counterexamples

The finite counterexample suite confirms the following.

### Necessary for the base theorem

1. Strict progressivity outside F is necessary.

Without it, a non-fixed point may fail to satisfy x < f(x), and V(f(x)) > V(x) can fail.

2. Strict order-preservation of V is necessary.

Without it, even x < f(x) does not force V(f(x)) > V(x).

### Necessary if F is externally specified

If F is defined as Fix(f), fixed-set consistency is definitional.

If F is externally specified, then:

x in F implies f(x)=x

must be assumed.

Otherwise the fixed-state zero-change conclusion can fail.

### Necessary for the activation/aggregate lift

1. A strictness preservation is necessary.

Without it, A can collapse a strict update pair.

2. G strict positivity is necessary.

Without it, strict activation improvement can be collapsed by G.

### Not necessary for the one-step theorem

Monotonicity of f is not necessary.

There exist finite non-monotone maps satisfying strict progressivity outside F for which the one-step Lyapunov conclusion holds.

## 8. Boundary and limitations

This note proves only a finite fixed-set poset Lyapunov theorem and its restricted VF-H2 toy corollaries.

It does not prove:

- original unrestricted TTP-VF-H2-004
- generalized theorem without assumptions
- full Viruse Fabric theory
- empirical validation
- biological validation
- manuscript readiness
- submission readiness
- external endorsement
- journal suitability

All claims are restricted to the safe abstract finite order-theoretic toy setting.

## 9. Internal artifact inventory

Primary anchors:

1. FFP-LYAP-T-VF-H2-001-R proof attempt
2. FFP-LYAP-T-VF-H2-001-R audit
3. fixed-set finite poset minimality/counterexample proof attempt
4. fixed-set finite poset minimality/counterexample audit

Secondary anchors:

1. SDSCUF proof attempt and audit
2. AAL-SDSCUF proof attempt and audit
3. earlier restricted TTP-VF-H2-004-R proof chain

## Claim boundary table

| Claim | Status |
|---|---|
| Fixed-set finite poset theorem proved in finite abstract setting | allowed |
| Product-lattice VF-H2 corollary follows | allowed |
| Activation/aggregate lift follows under explicit assumptions | allowed |
| Counterexamples establish necessity of selected assumptions | allowed |
| Monotonicity of f is not required for one-step theorem | allowed |
| Full Viruse Fabric theory proved | forbidden |
| Unrestricted TTP-VF-H2-004 proved | forbidden |
| Empirical validation achieved | forbidden |
| Biological validation achieved | forbidden |
| Manuscript ready | forbidden |
| Submission ready | forbidden |
| External mathematician endorsement obtained | forbidden |
| Journal acceptance or suitability established | forbidden |

## Consolidation result

This limited technical note skeleton consolidates:

- the fixed-set finite poset theorem
- the product-lattice VF-H2 corollary
- the activation/aggregate lift corollary
- the minimality/counterexample suite
- explicit limitation boundaries

No new theorem is claimed beyond the audited proof chain.

## Next allowed action

audit_vf_h2_fixed_set_finite_poset_limited_technical_note_consolidation_draft_no_claim_submission

VF_H2_FIXED_SET_FINITE_POSET_LIMITED_TECHNICAL_NOTE_CONSOLIDATION_DRAFT_CREATED_OK
LIMITED_TECHNICAL_NOTE_SKELETON_CREATED_OK
MAIN_THEOREM_INCLUDED_OK
MAIN_THEOREM_PROOF_INCLUDED_OK
PRODUCT_LATTICE_COROLLARY_INCLUDED_OK
ACTIVATION_AGGREGATE_LIFT_INCLUDED_OK
MINIMALITY_COUNTEREXAMPLE_SECTION_INCLUDED_OK
BOUNDARY_LIMITATION_SECTION_INCLUDED_OK
INTERNAL_ARTIFACT_INVENTORY_INCLUDED_OK
CLAIM_BOUNDARY_TABLE_INCLUDED_OK
NO_EXTERNAL_ENDORSEMENT_CLAIM_OK
NO_MANUSCRIPT_READY_CLAIM_OK
NO_SUBMISSION_READY_CLAIM_OK
GENERALIZED_THEOREM_WITHOUT_ASSUMPTIONS_REMAINS_NOT_PROVED_OK
ORIGINAL_UNRESTRICTED_TTP_VF_H2_004_REMAINS_NOT_PROVED_OK
FULL_VIRUSE_FABRIC_THEORY_REMAINS_NOT_PROVED_OK
NEXT_ALLOWED_AUDIT_VF_H2_FIXED_SET_FINITE_POSET_LIMITED_TECHNICAL_NOTE_CONSOLIDATION_DRAFT_OK
