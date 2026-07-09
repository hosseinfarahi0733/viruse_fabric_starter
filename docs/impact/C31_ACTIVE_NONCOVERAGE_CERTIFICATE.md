# C31 Active Noncoverage Certificate

## Summary

C31 packages the C29 source condition as a first-class certificate.

The source condition is:

    not forall i : ProductIndex p.d, i in p.active

C31 introduces:

    ActiveNoncoverageCertificate p

with the field:

    not_all_active : not forall i : ProductIndex p.d, i in p.active

## New route

The new certificate route is:

    ActiveNoncoverageCertificate p
    -> exists i : ProductIndex p.d, not i in p.active
    -> InactiveIndexCertificate p
    -> restricted proof-spine target

## New Lean declarations

    ActiveNoncoverageCertificate
    ActiveNoncoverageCertificate.of_not_all_active
    ActiveNoncoverageCertificate.exists_inactive
    ActiveNoncoverageCertificate.toInactiveIndexCertificate
    restrictedParams_activeNoncoverageCertificate_fixedProductState_to_currentBestMainTheorem

## Scientific value

C31 does not introduce a new mathematical assumption.

Instead, it packages the existing C29 noncoverage source condition into the
same certificate-oriented style used elsewhere in the product proof spine.

This makes the API cleaner and reduces the use of raw proof arguments at the
front door of the current best theorem route.

## What C31 does not claim

C31 does not prove inactive index existence unconditionally.

C31 does not derive noncoverage from list length.

C31 does not assume duplicate-free active lists.

C31 does not assume finite enumeration of ProductIndex.

## Relation to C29 and C30

C29 showed that active noncoverage implies the existence of an inactive index.

C30 recorded that active noncoverage is currently the minimal safe source
condition because the product API does not yet expose enough cardinality,
coverage, or duplicate-control structure.

C31 packages that minimal safe source condition as a certificate.
