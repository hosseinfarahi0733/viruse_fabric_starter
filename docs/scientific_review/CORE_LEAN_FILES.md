# VF-H2 Core Lean Files for Architecture Review

This file lists the small core subset a reviewer should inspect before reading the full repository.

## Core theory and proof-spine files

- `lean/VFH2/Product/ProductRestrictedParamsFullNaturalProofSpine.lean`
- `lean/VFH2/Product/ProductRestrictedParamsRestrictedProofSpineFreeze.lean`
- `lean/VFH2/Product/ProductRestrictedParamsHFixedSemanticSpecialization.lean`

## Fixedness layer

- `lean/VFH2/Product/ProductFixedSet.lean`
- `lean/VFH2/Product/ProductFixedSetTransport.lean`
- `lean/VFH2/Product/ProductFixedSetGeneralization.lean`
- `lean/VFH2/Product/ProductFixedZero.lean`

## Update and ledger layer

- `lean/VFH2/Product/ProductUpdate.lean`
- `lean/VFH2/Product/ProductNonfixedIncrease.lean`
- `lean/VFH2/Product/ProductPositiveLedger.lean`
- `lean/VFH2/Product/ProductRestrictedBridge.lean`

## Score-preservation / policy layer

- `lean/VFH2/Product/ProductRestrictedParamsScorePreservingPolicyInstantiation.lean`
- `lean/VFH2/Product/ProductRestrictedParamsScorePreservationIff.lean`

## Transport / canonical layer

- `lean/VFH2/Product/ProductParamsTransport.lean`
- `lean/VFH2/Product/ProductStateTransport.lean`
- `lean/VFH2/Product/ProductUpdateTransport.lean`
- `lean/VFH2/Product/ProductRestrictedParamsCanonicalRawEqualities.lean`

## Review note

The exact file names may evolve. Use `grep -RIn` over `lean/VFH2/Product` if any file is renamed.
