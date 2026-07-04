# VF-H2 v11.9.0 Restricted Scaffold Audit and Theorem Inventory

Generated: 2026-07-04T23:20:06+03:30  
Repository: `https://github.com/hosseinfarahi0733/viruse_fabric_starter.git`  
Branch: `master`  
Base milestone: `v11.8.0` at `03e40d7`  
Audit base HEAD: `03e40d7` / `03e40d7eb8342b4c3f54374e152fc46578a74123`

## Purpose

This audit records the current restricted Product/Typed transport ladder for the VF-H2 scaffold. It is a manuscript-safe inventory and claim-boundary document. It does not assert a full VF-H2 theory, unrestricted coverage, empirical validation, or biological validation.

## Build and hygiene status

- Full `lake build`: passed before audit creation.
- Lean Product/Typed forbidden-marker scan: clean for the configured proof-marker pattern.
- Working tree before audit generation: clean.
- Baseline tag: `v11.8.0` resolved to current HEAD.

## Version ladder

| Milestone | Commit | Conservative claim |
|---|---:|---|
| `v11.0.0` | `a2de5cc` | Product restricted bridge theorem for the current restricted scaffold. |
| `v11.1.0` | `4b6e622` | ProductIndex and Typed.WidthIndex equivalence. |
| `v11.2.0` | `8c24841` | ProductTypedState and Typed.TypedState transport. |
| `v11.3.0` | `a098eb7` | Product/Typed ledger equivalence. |
| `v11.4.0` | `6fe5666` | Product/Typed update-state transport. |
| `v11.5.0` | `66a2509` | Product/Typed ledger-effect transport. |
| `v11.6.0` | `3405b55` | Product/Typed fixed-set transport. |
| `v11.7.0` | `2101265` | Product/Typed restricted bridge-target transport. |
| `v11.8.0` | `03e40d7` | Product/Typed transport ladder certificate. |

## Lean theorem inventory

The following theorem/function names were checked by Lean during this audit:

```text
VFH2.ProductIndex.flattenEquiv (d : Nat) : VFH2.ProductIndex.ProductWidthIndexEquiv d
VFH2.ProductStateTransport.typedToProduct_productToTyped {n d : Nat} (x : VFH2.ProductTypedState n d) :
  VFH2.ProductStateTransport.typedToProduct (VFH2.ProductStateTransport.productToTyped x) = x
VFH2.ProductStateTransport.productToTyped_typedToProduct {n d : Nat} (x : VFH2.Typed.TypedState n d) :
  VFH2.ProductStateTransport.productToTyped (VFH2.ProductStateTransport.typedToProduct x) = x
VFH2.ProductParamsTransport.flatten_mem_typed_active_iff_mem_product_active {p : VFH2.ProductRestrictedParams}
  {i : VFH2.ProductIndex p.d} : i.flatten ∈ (VFH2.ProductParamsTransport.typedParamsOfProduct p).active ↔ i ∈ p.active
VFH2.ProductLedgerTypedValuesDecomposition.ledgerEquivalenceTarget (p : VFH2.ProductRestrictedParams) (x : p.State) :
  VFH2.ProductLedgerEquivalenceTarget.ledgerEquivalenceTarget p x
VFH2.ProductUpdateTransport.productToTyped_productUpdateState_eq_typedUpdateState (p : VFH2.ProductRestrictedParams)
  (x : p.State) :
  VFH2.ProductStateTransport.productToTyped (VFH2.productUpdateState p x) =
    VFH2.Typed.typedUpdateState (VFH2.ProductParamsTransport.typedParamsOfProduct p)
      (VFH2.ProductStateTransport.productToTyped x)
VFH2.ProductLedgerEffectTransport.typedLedgerEffect_eq_productLedgerEffect (p : VFH2.ProductRestrictedParams)
  (x : p.State) :
  VFH2.Typed.typedLedgerEffect (VFH2.ProductParamsTransport.typedParamsOfProduct p)
      (VFH2.ProductStateTransport.productToTyped x) =
    VFH2.productLedgerEffect p x
VFH2.ProductFixedSetTransport.typedFixedSet_iff_productFixedSet (p : VFH2.ProductRestrictedParams) (x : p.State) :
  VFH2.Typed.TypedFixedSet (VFH2.ProductParamsTransport.typedParamsOfProduct p)
      (VFH2.ProductStateTransport.productToTyped x) ↔
    VFH2.ProductFixedSet p x
VFH2.ProductBridgeTransport.typedRestrictedBridgeTarget_iff_productRestrictedBridgeTarget
  (p : VFH2.ProductRestrictedParams) (x : p.State) :
  VFH2.Typed.typedRestrictedBridgeTarget (VFH2.ProductParamsTransport.typedParamsOfProduct p)
      (VFH2.ProductStateTransport.productToTyped x) ↔
    VFH2.productRestrictedBridgeTarget p x
VFH2.ProductTransportLadderCertificate.transportLadder_certificate (p : VFH2.ProductRestrictedParams) (x : p.State) :
  (∀ (w : VFH2.Typed.WidthIndex p.d),
      w ∈ (VFH2.ProductParamsTransport.typedParamsOfProduct p).active ↔ VFH2.ProductIndex.unflatten w ∈ p.active) ∧
    VFH2.ProductStateTransport.productToTyped (VFH2.productUpdateState p x) =
        VFH2.Typed.typedUpdateState (VFH2.ProductParamsTransport.typedParamsOfProduct p)
          (VFH2.ProductStateTransport.productToTyped x) ∧
      VFH2.Typed.typedLedger (VFH2.ProductParamsTransport.typedParamsOfProduct p)
            (VFH2.ProductStateTransport.productToTyped x) =
          VFH2.productLedger p x ∧
        VFH2.Typed.typedLedgerEffect (VFH2.ProductParamsTransport.typedParamsOfProduct p)
              (VFH2.ProductStateTransport.productToTyped x) =
            VFH2.productLedgerEffect p x ∧
          (VFH2.Typed.TypedFixedSet (VFH2.ProductParamsTransport.typedParamsOfProduct p)
                (VFH2.ProductStateTransport.productToTyped x) ↔
              VFH2.ProductFixedSet p x) ∧
            (VFH2.Typed.typedRestrictedBridgeTarget (VFH2.ProductParamsTransport.typedParamsOfProduct p)
                (VFH2.ProductStateTransport.productToTyped x) ↔
              VFH2.productRestrictedBridgeTarget p x)
VFH2.ProductTransportLadderCertificate.productBridge_certificate_component (p : VFH2.ProductRestrictedParams)
  (x : p.State) :
  VFH2.productRestrictedBridgeTarget p x ↔
    VFH2.Typed.typedRestrictedBridgeTarget (VFH2.ProductParamsTransport.typedParamsOfProduct p)
      (VFH2.ProductStateTransport.productToTyped x)
```

## Safe aggregate claim

As of `v11.8.0`, the project provides a clean Lean-machine-checked restricted Product/Typed transport ladder certificate for the current VF-H2 scaffold. The certificate collects active-set membership, update-state, ledger, ledger-effect, fixed-set, and restricted bridge-target compatibility.

## Explicit claim boundaries

The current milestone supports only restricted-scaffold claims. The following are not established by this audit:

- Full VF-H2 theory.
- Unrestricted VF-H2 theorem.
- Empirical validation.
- Biological validation.
- Complete manuscript readiness for a full-theory paper.

## Recommended next technical direction

A conservative next step is `v12.0.0`: controlled generalization beyond the restricted scaffold, beginning with a gap register that identifies exactly which restrictions are structural, which are simplifications, and which can be relaxed without changing the already-checked transport ladder.
