# VF-H2 Negative Results

Negative results are part of the scientific contribution because they prevent overclaiming and identify exact missing assumptions.

## N1 — Score preservation is not currently derived

### Question

Can the score-key preserving update condition be derived from current product update/domain semantics?

### Result

No current derivation was found.

### Interpretation

The score preservation condition has been clarified as pointwise score preservation, but it remains a domain/update assumption.

## N2 — Arbitrary fixedness was not derived

### Question

Can the old arbitrary assumption `fixed : Prop` with `hFixed : fixed` be derived from fixed-set or update semantics?

### Result

No current derivation was found.

### Interpretation

The old fixedness layer was too abstract to discharge directly.

## N3 — ProductFixedSet is not currently derived

### Question

After C9.1 specialized fixedness to `ProductFixedSet p x`, can this predicate be derived from existing semantics?

### Result

C10 recorded a fixed-state derivation gap.

### Interpretation

`ProductFixedSet p x` is a clear concrete assumption, but still undischarged.

## N4 — Transport is not derivation

### Question

Do fixed-set transport theorems prove product fixedness?

### Result

No.

### Interpretation

Theorems of shape:

`TypedFixedSet ... ↔ ProductFixedSet p x`

only transfer fixedness between representations. They do not prove fixedness from domain semantics.

## N5 — Dichotomy is not derivation

### Question

Does a bridge theorem using `by_cases hfixed : ProductFixedSet p x` derive fixedness?

### Result

No.

### Interpretation

A dichotomy theorem classifies cases. It does not prove which case the current state satisfies.
