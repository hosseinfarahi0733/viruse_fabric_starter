# VF-H2 / Viruse Fabric — Negative Results after v17.4.0

## Purpose

This file records failed, collapsed, or non-main routes.

Negative results are part of the scientific value of the project.

## N1 — Old strong bridge route collapses the score window

Old assumption shape:

```lean
hThreshold : thresholdLo ≤ thresholdHi
hBaseLower : thresholdHi ≤ productScore x
hBaseUpper : productScore x ≤ thresholdLo
```

Result:

```text
thresholdLo = thresholdHi
thresholdHi = productScore x
productScore x = thresholdLo
```

Interpretation:

```text
The old route forces a degenerate score window.
```

Consequence:

```text
It cannot be the main route for a natural non-degenerate interval interpretation.
```

## N2 — Strict interval is impossible under old strong assumptions

Old route implication:

```text
thresholdLo < thresholdHi → False
```

Interpretation:

```text
The old route is incompatible with a strict score window.
```

## N3 — Identity-like update is not a scientific main route

The identity-like route is useful as a sanity route.

But it does not explain realistic domain update behavior.

Consequence:

```text
Do not present identity-like update as the scientific main route.
```

## N4 — Wrapper theorems do not count as scientific progress

A theorem that only repackages the same assumptions without reducing, deriving, or classifying them does not count as a scientific milestone.

Consequence:

```text
No new scientific tag for wrapper-only work.
```

---

## N5 — C8.2 did not derive pointwise score preservation from domain/update semantics

After C8.1, the score-key condition is classified as equivalent to:

```lean
∀ y : p.State, productScore (productUpdate y) = productScore y
```

C8.2 audited the current product-side update/score surfaces and did not find a concrete domain/update semantic layer that derives this pointwise score preservation.

Interpretation:

```text
Pointwise score preservation remains a fundamental domain/update assumption.
```

Consequence:

```text
C8.2 is a negative/classification result, not a new scientific proof milestone.
```

Forbidden claim:

```text
Do not claim that score preservation has been derived from domain dynamics.
```

