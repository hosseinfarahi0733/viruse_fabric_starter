# C35D Preferred Front-Door Validation Integration

## Result

C35D connects the C35C product front-door hygiene guard to the repository's
existing GitHub Actions validation workflow and adds one compiled downstream
consumer of the preferred construction-level API.

The release base is verified v17.26.0 at
`d460b3f4606f7c6acc556af40f1cb410400819b1`.

## Automated validation

The existing workflow at:

`.github/workflows/validate-proof-artifacts.yml`

now also runs when the Lean source tree, Lake configuration or manifest, Lean
toolchain, or front-door guard changes. A dedicated `validate-lean` job:

1. checks out the repository;
2. runs `scripts/audit_product_restricted_frontdoors.sh`;
3. uses `leanprover/lean-action@v1` to run an explicit Lake build;
4. disables Mathlib cache use because VF-H2 does not depend on Mathlib.

The existing proof-artifact validation job remains unchanged.

## Downstream preferred usage

The module:

`VFH2.Product.ProductRestrictedParamsPreferredUsageExample`

contains a small anonymous downstream example that consumes:

`ProductRestrictedParamsPreferredFrontDoor.currentBestMainTheorem`

It accepts only `n`, `d`, and the selected missing product index. No raw
not-all-active premise, manually manufactured certificate, or direct
erase-construction theorem is used at the call site.

The example deliberately does not create another named alias or front door.
The aggregate `VFH2.Product` module imports the module, so the normal Lake
build compiles this downstream route.

## Boundary

C35D does not modify `ProductRestrictedParams`, the proof spine, historical
proof declarations, or Compatibility APIs. It introduces no Mathlib dependency
and no operational biological content.
