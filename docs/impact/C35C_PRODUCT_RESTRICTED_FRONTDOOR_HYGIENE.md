# C35C Product Restricted Front-Door Hygiene

## Result

C35C audits the 91 Lean modules imported by `VFH2.Product` at verified release
`v17.25.0` (`8ac8a6a10f6a04f10007ddde8e40f2df3ef029fc`).

The audit found no downstream construction-level caller that bypasses
`ProductRestrictedParamsPreferredFrontDoor`. The only direct consumer of the
C35A erase-construction API is the C35B preferred-front-door module itself.

The raw not-all-active route remains confined to its historical declaration,
certificate/source adapters, and the explicit `Compatibility` wrapper. No
historical declaration or proof is removed.

## Preferred route

New erase-construction callers must use:

```lean
VFH2.ProductRestrictedParamsPreferredFrontDoor.currentBestMainTheorem
```

Callers with arbitrary existing parameters may use the structural-source or
certificate adapters under:

```lean
VFH2.ProductRestrictedParamsPreferredFrontDoor.Compatibility
```

The raw not-all-active adapter remains available for source compatibility, but
is not an approved new project front door.

## Policy matrix

| Caller state | Approved route |
|---|---|
| Parameters built by erasing one product index | `ProductRestrictedParamsPreferredFrontDoor.currentBestMainTheorem` |
| Arbitrary parameters with an active-length source | `Compatibility.currentBestMainTheorem_of_activeLengthSource` |
| Arbitrary parameters with an existing certificate | `Compatibility.currentBestMainTheorem_of_activeNoncoverageCertificate` |
| Raw not-all-active premise | Historical compatibility only; no new project call sites |

## Guard

Run the repository guard from the repository root:

```bash
bash scripts/audit_product_restricted_frontdoors.sh
```

The guard performs two checks:

1. It baseline-locks the existing raw not-all-active and direct
   erase-construction identifiers to their reviewed files and occurrence
   counts.
2. It verifies that the preferred aggregate import, preferred
   `currentBestMainTheorem`, and explicit `Compatibility` namespace remain
   present.

A new match in any downstream Lean source fails the guard. A change inside a
baseline file also fails unless its counts are deliberately reviewed and
updated. This makes architecture drift visible rather than silently accepting
a new raw front door.

This is intentionally a spelling-level quarantine: a forbidden identifier in a
Lean comment or string is also reported. Explanatory mentions belong in
Markdown documentation, while any baseline change requires explicit review.

The quarantine deliberately covers the supporting raw-witness, certificate
constructor, active-list constructor, and construction-derived source helpers—not
only the two final theorem names. New downstream proof work that genuinely needs
a lower-level helper must first introduce or approve an appropriate public
abstraction and then update the reviewed baseline explicitly.

## Reviewed compatibility boundary

Raw and adapter declarations remain in:

- `ProductRestrictedParamsActiveCoverage.lean`
- `ProductRestrictedParamsActiveNoncoverageCertificate.lean`
- `ProductRestrictedParamsActiveCustomEnumKernel.lean`
- `ProductRestrictedParamsActiveLengthLowerBound.lean`
- `ProductRestrictedParamsPreferredFrontDoor.lean`

Direct erase-construction declarations remain in:

- `ProductRestrictedParamsActiveEraseConstruction.lean`
- `ProductRestrictedParamsPreferredFrontDoor.lean`

## Boundary

C35C does not change `ProductRestrictedParams`, does not alter any Lean theorem,
does not remove compatibility APIs, and does not add Mathlib. It is strictly a
dependency/API hygiene milestone.
