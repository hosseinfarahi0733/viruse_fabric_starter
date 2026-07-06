# VF-H2 v17.4 — Full Natural Proof-Spine Audit

## Purpose
This stage proves the full restricted proof-spine target from natural base interval assumptions.

## Main repair
The full restricted proof-spine target no longer needs the strong/collapsing assumptions:

```lean
thresholdHi ≤ productScore x
productScore x ≤ thresholdLo
```

Instead, the route uses the natural base interval:

```lean
thresholdLo ≤ productScore x
productScore x ≤ thresholdHi
```

## Proven routes
- score-key preserving update condition → full natural restricted proof-spine target
- identity-like update → full natural restricted proof-spine target

## Important scope boundary
This stage repairs the formal restricted proof-spine route.
It does not derive hFixed.
It does not derive the score-key condition from domain semantics.
It does not prove unrestricted VF-H2.
It does not provide empirical or scientific validation.

## Allowed claim
v17.4 proves the full restricted proof-spine target from natural base interval assumptions under fixedness and score-preserving policy routes.

## Forbidden claim
This is not a proof of full VF-H2, not a derivation of fixedness, and not a domain-scientific validation.
