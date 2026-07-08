# C10 - ProductFixedSet Derivation Gap Audit

## Objective

Determine whether the current repository can derive ProductFixedSet p x from existing model, update, ledger, fixed-set, or domain semantics.

## Verdict

C10 is classified as Outcome B: fixed-state derivation gap.

The current repository does not contain a theorem that derives ProductFixedSet p x from concrete product update, ledger, or domain semantics.

No fundamental assumption is discharged by C10.

No scientific tag is justified.

## Exact definition

Lean prints ProductFixedSet p x as:

ProductFixedSet p x =
for every i : ProductIndex p.d,
if i is in p.active,
then (x i).val = p.n.

Therefore, ProductFixedSet p x means:

Every active product-index coordinate of x already has top value p.n.

## Candidate classification

### ProductFixedSet.lean

Classification: DEFINITION / CONSEQUENCE.

It defines ProductFixedSet and proves consequences under an assumed fixedness proof.

It does not derive ProductFixedSet p x.

### ProductFixedSetGeneralization.lean

Classification: TRANSPORTS ProductFixedSet.

It proves transport/iff statements between generalized, typed, and product fixed-set forms.

It does not derive ProductFixedSet p x.

### ProductFixedSetTransport.lean

Classification: TRANSPORTS ProductFixedSet.

It proves a representation equivalence between Typed.TypedFixedSet and ProductFixedSet p x.

This is not a domain derivation.

### ProductNonfixedIncrease.lean

Classification: DERIVES NEGATED-FORM CONSEQUENCE.

The theorem product_exists_active_not_top_of_not_fixed proves that from not ProductFixedSet p x one can obtain an active coordinate whose value is not top.

The local line have hfixed : ProductFixedSet p x occurs only inside a proof by cases on the nonexistence of a non-top active coordinate.

It is not a derivation from update, ledger, or domain semantics.

### ProductRestrictedBridge.lean

Classification: SPLITS on ProductFixedSet.

The dichotomy theorem uses by_cases hfixed : ProductFixedSet p x.

It splits on fixedness but does not derive fixedness.

### ProductUpdate.lean

Classification: ASSUMES ProductFixedSet / DERIVES CONSEQUENCE.

It proves update value preservation under hfixed : ProductFixedSet p x.

It does not derive fixedness.

### ProductFixedZero.lean

Classification: ASSUMES ProductFixedSet / DERIVES CONSEQUENCE.

It proves zero ledger effect under hfixed : ProductFixedSet p x.

It does not derive fixedness.

## Scientific interpretation

C9.1 replaced the arbitrary assumption fixed : Prop and hFixed : fixed with the concrete semantic assumption hFixedSet : ProductFixedSet p x.

However, C9.1 did not discharge fixedness.

C10 confirms that the current codebase still lacks a semantic source for the proposition that every active coordinate of x has value p.n.

Therefore, the fixed-state assumption remains fundamental unless future model assumptions or initialization/domain semantics imply all active coordinates are already top-valued.

## Assumption impact

Reduced assumptions: none.

Clarified assumptions: hFixedSet : ProductFixedSet p x.

Remaining fixed-state proof debt: ProductFixedSet p x.

Equivalent form:

For every i : ProductIndex p.d,
if i is in p.active,
then (x i).val = p.n.

## Recommended next targets

1. Define a meaningful domain or initialization condition that implies all active coordinates are top-valued.
2. Prove ProductFixedSet p x from that domain condition.
3. If no such condition is intended, keep ProductFixedSet p x as an explicit model assumption and do not overclaim.
4. Do not add wrapper theorems of shape hFixedSet : ProductFixedSet p x implies target, unless they discharge another independent assumption.

## Tag policy

No tag is justified for this audit.

Reason: no fundamental assumption was discharged.

Last scientific tag remains v17.4.0.

## Final C10 statement

C10 does not prove fixedness.

C10 records that ProductFixedSet p x is currently a concrete but undischarged fixed-state assumption.
