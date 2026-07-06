# VF-H2 / Viruse Fabric — Proof Debt after v17.4.0

## Purpose

This file records formal and scientific proof debt.

A proof debt is not a failure. It is an unpaid invoice from reality, and reality is annoyingly strict about payment.

## D1 — Derive score-key preservation

Current state:

```text
restrictedParamsScoreKeyPreservingUpdateCondition is assumed.
```

Debt:

```text
The condition must be derived from a concrete update model, score model, or domain semantics.
```

Priority:

```text
critical
```

Potential next work:

```text
C8 Score-key semantics
```

---

## D2 — Derive fixedness

Current state:

```lean
hFixed : fixed
```

Debt:

```text
Fixedness is not derived from update semantics.
```

Priority:

```text
critical
```

Potential next work:

```text
C9 hFixed semantics
```

---

## D3 — Explain natural base interval source

Current state:

```lean
thresholdLo ≤ productScore x
productScore x ≤ thresholdHi
```

Debt:

```text
The natural base interval assumptions are not yet connected to calibration, data, domain constraints, or an upstream verification layer.
```

Priority:

```text
high
```

---

## D4 — Separate formal route from scientific route

Current state:

```text
identity-like route exists as a sanity route.
```

Debt:

```text
The project must prevent this route from being presented as the scientific main route.
```

Priority:

```text
high
```

---

## D5 — Legacy route boundary

Current state:

```text
legacy strong/collapsing files still exist.
```

Debt:

```text
They must be marked as legacy boundary routes before refactoring or removal.
```

Priority:

```text
high
```

Potential next work:

```text
C7 Legacy Boundary Marking
```

---

## D6 — Domain semantics

Current state:

```text
formal restricted product state exists, but scientific domain semantics are not yet sufficient.
```

Debt:

```text
The model must explain what the score means, what the update means, and why preservation/fixedness are scientifically justified.
```

Priority:

```text
critical
```

---

## D7 — Validation

Current state:

```text
No empirical validation is claimed.
```

Debt:

```text
If the project wants scientific or applied claims, validation must be designed separately.
```

Priority:

```text
future / outside current formal milestone
```

---

## D8 — Derive pointwise score preservation from domain/update semantics

C8.1 classified the score-key condition as equivalent to pointwise score preservation.

C8.2 did not find a current concrete semantic layer deriving:

```lean
∀ y : p.State, productScore (productUpdate y) = productScore y
```

Debt:

```text
Introduce or identify a concrete update/domain semantics from which pointwise score preservation can be derived.
```

Priority:

```text
critical
```

Current status:

```text
open
```

