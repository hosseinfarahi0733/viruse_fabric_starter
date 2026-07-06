# VF-H2 / Viruse Fabric — Assumption Register after v17.4.0

## Purpose

This file classifies assumptions after `v17.4.0`.

Progress should be measured by reducing or deriving assumptions, not by increasing theorem count.

## Removed / internalized assumptions

The following assumptions have been removed, internalized, or repaired in the v17 line:

```text
- hTypedUpdate
- hBaseScore
- hUpdatedScore
- hEffectBase
- old strong/collapsing updated-bound assumptions
- old strong/collapsing full proof-spine main route
```

## Active fundamental assumptions

### A1 — Fixedness

```lean
hFixed : fixed
```

Status:

```text
external
```

Meaning:

```text
The proof currently assumes fixedness instead of deriving it from update semantics or a fixed-point/fixed-set model.
```

Scientific risk:

```text
High. If fixedness is not semantically grounded, the proof-spine remains conditional.
```

Next target:

```text
Derive hFixed from an explicit fixed-set/update semantics, or classify it as a domain axiom.
```

---

### A2 — Score-key preserving update condition

```lean
restrictedParamsScoreKeyPreservingUpdateCondition
```

Status:

```text
external
```

Meaning:

```text
The update is assumed to preserve the score-relevant key required by the restricted proof-spine route.
```

Scientific risk:

```text
High. This is currently the most important assumption for the main scientific route.
```

Next target:

```text
Derive the condition from a concrete update model, score model, or domain transition semantics.
```

---

### A3 — Natural base lower bound

```lean
hBaseLowerNatural : thresholdLo ≤ productScore x
```

Status:

```text
external
```

Meaning:

```text
The base score is assumed to be above the lower threshold.
```

Scientific risk:

```text
Medium. This is natural, but its source is not yet modeled.
```

Next target:

```text
Explain whether this comes from data, calibration, domain constraints, or a prior verification layer.
```

---

### A4 — Natural base upper bound

```lean
hBaseUpperNatural : productScore x ≤ thresholdHi
```

Status:

```text
external
```

Meaning:

```text
The base score is assumed to be below the upper threshold.
```

Scientific risk:

```text
Medium. This is natural, but its source is not yet modeled.
```

Next target:

```text
Explain whether this comes from data, calibration, domain constraints, or a prior verification layer.
```

---

### A5 — Threshold well-formedness

```lean
hThreshold : thresholdLo ≤ thresholdHi
```

Status:

```text
structural / low-risk
```

Meaning:

```text
The score window is well-formed.
```

Scientific risk:

```text
Low.
```

Next target:

```text
Keep as a basic well-formedness assumption unless a richer interval type is introduced.
```

## Legacy assumptions

The old route used assumptions with the shape:

```lean
thresholdHi ≤ productScore x
productScore x ≤ thresholdLo
```

or equivalent base-effect forms.

Together with:

```lean
thresholdLo ≤ thresholdHi
```

these collapse the score window.

Therefore, the old route is not suitable as the main scientific route for a non-degenerate interval interpretation.

## Assumption priority

Highest-priority assumption to attack next:

```text
restrictedParamsScoreKeyPreservingUpdateCondition
```

Second priority:

```text
hFixed
```

Third priority:

```text
source of natural base interval assumptions
```
