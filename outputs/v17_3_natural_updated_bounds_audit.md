# VF-H2 v17.3 / Stage C4 — Natural Updated Bounds Audit

## Purpose
This stage repairs the updated-bounds route by proving natural updated score-window bounds from natural base interval assumptions.

## Removed from this bounds route
The route no longer requires the strong/collapsing assumptions:

```lean
thresholdHi ≤ productScore x
productScore x ≤ thresholdLo
```

## New natural assumptions
```lean
thresholdLo ≤ productScore x
productScore x ≤ thresholdHi
```

Together with score preservation and fixedness, these imply:
```lean
thresholdLo ≤ productScore (productUpdate x)
productScore (productUpdate x) ≤ thresholdHi
```

## Scope
This stage repairs the natural updated-bounds route only.
It does not yet repair the full restrictedProofSpineTarget route.

## Not derived
- hFixed
- score-key preserving condition
- domain semantics
- scientific validation

## Allowed claim
The updated-bounds route can be obtained from natural base interval assumptions plus score preservation and fixedness.

## Forbidden claim
This does not prove full VF-H2 and does not yet repair the entire proof-spine target.
