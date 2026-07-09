# C29 Not-All-Active Coverage Route

## Summary

C29 adds a minimal and logically safe route from active-list non-coverage to the inactive-index witness required by the C28 certificate path.

Source condition:

    not forall i : ProductIndex p.d, i in p.active

Derived witness:

    exists i : ProductIndex p.d, not i in p.active

Packaged as:

    InactiveIndexCertificate.of_not_all_active

Front-door route:

    restrictedParams_notAllActive_fixedProductState_to_currentBestMainTheorem

## Scientific value

This reduces the downstream burden from providing an explicit inactive-index witness to providing a structural non-coverage condition.

## What C29 does not claim

C29 does not prove inactive indices exist unconditionally.

C29 does not derive inactive existence from List.length.

C29 does not rely on duplicate-free assumptions about p.active.

C29 does not assume ProductIndex p.d has a finite enumeration exposed in the current API.

## Why this is the correct next step

The C29 probe showed that ProductRestrictedParams.active is a List of ProductIndex d, but did not expose enough list-cardinality or enumeration structure to justify a cardinality theorem.

Therefore the safest meaningful source condition is active-list non-coverage.
