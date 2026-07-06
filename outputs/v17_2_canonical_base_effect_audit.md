# VF-H2 v17.2 / Stage B — Canonical BaseEffect Audit

## Purpose

This stage removes the external base-effect equality assumption:

```lean
hEffectBase : baseEffect = productScore x
```

from the canonical restricted proof-spine route.

## Method

The route specializes:

```lean
baseEffect := productScore x
```

and discharges the previous equality by:

```lean
rfl
```

## Real assumption reduction

Removed from the exported route:

```text
hEffectBase
baseEffect as an external Int parameter
```

Remaining assumptions are explicit:

```text
hCondition      : score-key preserving condition
or
hIdentityLike   : identity-like update

hFixed          : fixed
hBaseLower      : thresholdHi ≤ productScore x
hBaseUpper      : productScore x ≤ thresholdLo
hThreshold      : thresholdLo ≤ thresholdHi
```

## Scientific status

This is an architectural assumption reduction, not a full scientific derivation.

It does not derive:

```text
fixed
bridge inequalities
score-key condition
domain semantics
physical or biological validity
```

## Allowed claim

The canonical restricted route no longer exposes `hEffectBase`; baseEffect is specialized to `productScore x`.

## Forbidden claim

This does not prove full VF-H2 and does not discharge bridge, fixedness, or domain-policy assumptions.

