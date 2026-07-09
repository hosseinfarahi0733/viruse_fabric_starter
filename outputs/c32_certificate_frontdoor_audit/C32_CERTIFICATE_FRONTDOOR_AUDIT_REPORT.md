# C32 Certificate Front-Door Audit Report

## Purpose

C32 records the certificate front-door state after v17.21.0.

C31 introduced:

    ActiveNoncoverageCertificate p

as a first-class package around the C29 source condition:

    not forall i : ProductIndex p.d, i in p.active

## Current best source-facing front door

The current best front door is:

    ActiveNoncoverageCertificate p

with the route:

    ActiveNoncoverageCertificate p
    -> exists i : ProductIndex p.d, not i in p.active
    -> InactiveIndexCertificate p
    -> restricted proof-spine target

## Why C32 does not add a new theorem

The current product API still does not expose a complete, stable source for
active noncoverage through cardinality or coverage.

A cardinality route would need finite ProductIndex enumeration and duplicate
control for p.active, or an existing theorem that safely handles duplicates.

Without that structure, the certificate introduced in C31 is the correct
source-facing abstraction.

## Scientific conclusion

C32 confirms that the project should treat active noncoverage as the current
minimal safe certificate-level source condition.

No unconditional inactive-index theorem is justified at this point.

No List.length-based source theorem is justified at this point.
