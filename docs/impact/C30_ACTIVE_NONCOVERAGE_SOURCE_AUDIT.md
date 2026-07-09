# C30 Active Non-Coverage Source Audit

## Summary

C30 audits the source of the C29 condition:

    ¬ ∀ i : ProductIndex p.d, i ∈ p.active

C29 established that this condition is sufficient to derive:

    ∃ i : ProductIndex p.d, ¬ i ∈ p.active

and then feed the inactive-index certificate route into the restricted
proof-spine target.

## Current conclusion

The current product layer exposes:

    ProductRestrictedParams.active : List (ProductIndex d)

and the C29 route:

    exists_inactive_of_not_all_active
    InactiveIndexCertificate.of_not_all_active
    restrictedParams_notAllActive_fixedProductState_to_currentBestMainTheorem

However, the current API does not expose enough structure to derive
not-all-active automatically from list cardinality or finite enumeration.

## Why no cardinality theorem is added

A theorem of the form:

    p.active.length < total number of ProductIndex p.d
    → ¬ ∀ i : ProductIndex p.d, i ∈ p.active

would require a reliable finite enumeration/cardinality of ProductIndex p.d and
a duplicate-control condition such as List.Nodup p.active, or a theorem that
already handles duplicates.

The current audit does not identify such a complete structure as part of the
stable product API.

## Scientific value

C30 prevents the project from smuggling in unsupported assumptions about
coverage, enumeration, or duplicate-free active lists.

The current minimal safe source condition remains:

    ¬ ∀ i : ProductIndex p.d, i ∈ p.active

This is stronger than a raw existential witness in terms of usability, but it
is still explicit enough to avoid false unconditional claims.

## Next recommended step

The next formal step should be one of:

1. Add a small source certificate for active noncoverage.
2. Introduce a principled coverage predicate and derive noncoverage from it.
3. Introduce finite ProductIndex enumeration plus duplicate-control structure,
   then derive noncoverage from a cardinality bound.

Until one of those sources exists, the C29 route is the correct proof-spine
front door.

