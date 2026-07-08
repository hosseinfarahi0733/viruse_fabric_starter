# VF-H2 Assumptions

## A1 — Score Preservation

### Formal shape

Pointwise score preservation:

`∀ y : p.State, productScore (productUpdate y) = productScore y`

or its project-specific score-key preserving policy form.

### Status

Remaining assumption.

### Current evidence

C8.1 classified the score-key condition as pointwise score preservation.

C8.2 recorded that this preservation is not currently derived from product update/domain semantics.

### Where it is used

It is required by the score-preserving route into the restricted proof-spine target.

### Scientific risk

High.

If score preservation is not justified by update semantics or domain constraints, the main theorem remains conditional on a strong policy assumption.

## A2 — Fixed-state evidence

### Formal shape

`hFixedSet : ProductFixedSet p x`

Equivalent meaning:

For every active product-index coordinate `i`, if `i ∈ p.active`, then `(x i).val = p.n`.

### Status

Remaining assumption.

### Current evidence

C9 recorded that arbitrary `hFixed` was not derived.

C9.1 specialized the arbitrary fixedness proposition to the concrete semantic predicate `ProductFixedSet p x`.

C10 recorded that the current repository does not derive `ProductFixedSet p x` from existing product update, ledger, or domain semantics.

### Where it is used

It is required by the fixedness route into the restricted proof-spine target and by fixed-zero/update-preservation consequences.

### Scientific risk

High.

Without a domain or initialization condition implying `ProductFixedSet p x`, the main theorem remains conditional.

## A3 — Natural base lower bound

### Formal shape

`thresholdLo ≤ productScore x`

### Status

Remaining assumption.

### Where it is used

It is required by the natural-base interval route into the restricted proof-spine target.

### Scientific risk

Medium.

This may be derivable from score construction, initialization constraints, or threshold definitions, but that is not yet established.

## A4 — Natural base upper bound

### Formal shape

`productScore x ≤ thresholdHi`

### Status

Remaining assumption.

### Where it is used

It is required by the natural-base interval route into the restricted proof-spine target.

### Scientific risk

Medium.

This may be derivable from score construction, initialization constraints, or threshold definitions, but that is not yet established.
