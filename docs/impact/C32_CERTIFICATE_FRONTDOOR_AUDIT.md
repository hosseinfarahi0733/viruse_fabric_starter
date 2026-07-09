# C32 Certificate Front-Door Audit

## Summary

C32 records the current certificate-based front-door architecture after C31.

The current best source-facing front door is:

    ActiveNoncoverageCertificate p

This certificate packages the C29 noncoverage condition:

    not forall i : ProductIndex p.d, i in p.active

and feeds the existing inactive-index route:

    ActiveNoncoverageCertificate p
    -> exists inactive ProductIndex
    -> InactiveIndexCertificate p
    -> restricted proof-spine target

## Why this matters

Earlier routes exposed either a raw inactive witness or a raw noncoverage proof.
C31 moved the source condition into a certificate. C32 records this as the
preferred source-facing boundary.

This keeps the proof-spine interface consistent with the project's broader
certificate-based architecture.

## What C32 does not claim

C32 does not prove that inactive indices exist unconditionally.

C32 does not derive active noncoverage from List.length.

C32 does not assume duplicate-free active lists.

C32 does not assume finite enumeration of ProductIndex.

C32 does not replace future work on a principled coverage or cardinality source.

## Next recommended step

Future work should identify or introduce one principled source for
ActiveNoncoverageCertificate:

1. A coverage predicate whose negation yields active noncoverage.
2. A finite ProductIndex enumeration plus duplicate-control structure.
3. A domain-level source certificate supplied by product semantics.

Until then, ActiveNoncoverageCertificate is the correct current front door.
