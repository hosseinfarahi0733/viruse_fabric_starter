import Lake
open Lake DSL

package «viruse_fabric_starter» where
  -- Restricted VF-H2 Lean scaffold only.
  -- This package does not claim a completed machine-checked proof
  -- of the full Viruse Fabric theory.

@[default_target]
lean_lib VFH2 where
  srcDir := "lean"
  roots := #[
    `VFH2.RestrictedBridge.Scaffold,
    `VFH2.RestrictedBridge.ProofBasics,
    `VFH2.RestrictedBridge.UpdateMap,
    `VFH2.RestrictedBridge.UpdateMapBasics,
    `VFH2.RestrictedBridge.FixedZeroEffect,
    `VFH2.RestrictedBridge.ActiveTopBridge,
    `VFH2.RestrictedBridge.MembershipTopBridge,
    `VFH2.RestrictedBridge.FixedSetBridge,
    `VFH2.RestrictedBridge.ActiveIndexSoundness,
    `VFH2.RestrictedBridge.NonfixedWitness,
    `VFH2.RestrictedBridge.BoundBasics,
    `VFH2.RestrictedBridge.CoordinateIncrease,
    `VFH2.RestrictedBridge.LedgerIncrease,
    `VFH2.RestrictedBridge.FinalRestrictedBridge,
    `VFH2.RestrictedBridge.ActiveRangeBridge,
    `VFH2.RestrictedBridge.WellFormedDomain,
    `VFH2.RestrictedBridge.OfficialRBridge,
    `VFH2.RestrictedBridge.ActiveRangeEquivalence,
    `VFH2.RestrictedBridge.ActiveWidthNecessity,
    `VFH2.RestrictedBridge.WellFormedParams,
    `VFH2.Typed.BoundedCoord,
    `VFH2.Typed.WidthIndex,
    `VFH2.Typed.TypedState,
    `VFH2.Typed.TypedParams,
    `VFH2.Typed.TypedFixedSet,
    `VFH2.Typed.TypedUpdate,
    `VFH2.Typed.TypedLedger,
    `VFH2.Typed.TypedFixedZero,
    `VFH2.Typed.TypedNonfixedIncrease,
    `VFH2.Typed.TypedUpdateMonotone,
    `VFH2.Typed.TypedPositiveLedger,
    `VFH2.Typed.TypedRestrictedBridge,
    `VFH2.Product,
    `VFH2.Product.TimeLayer,
    `VFH2.Product.ProductIndex,
    `VFH2.Product.ProductFlatten,
    `VFH2.Product.ProductFlattenBlocks,
    `VFH2.Product.ProductFlattenInjective,
    `VFH2.Product.ProductFlattenFullInjective,
    `VFH2.Product.ProductFlattenEquiv,
    `VFH2.Product.ProductUnflattenBlocks,
    `VFH2.Product.ProductState,
    `VFH2.Product.ProductStateTransport,

    `VFH2.Product.ProductUpdateTransport,
    `VFH2.Product.ProductLedgerEffectTransport,
  `VFH2.Product.ProductFixedSetTransport,
  `VFH2.Product.ProductBridgeTransport,
    `VFH2.Product.ProductTransportLadderCertificate,
    `VFH2.Product.ProductActiveSetGeneralization,
    `VFH2.Product.ProductPointwiseTransportGeneralization,
    `VFH2.Product.ProductFixedSetGeneralization,
    `VFH2.Product.ProductUpdateGeneralization,
    `VFH2.Product.ProductEffectTransportGeneralization,
    `VFH2.Product.ProductBridgeGeneralization,
    `VFH2.Product.ProductGeneralizedTransportCertificate,
    `VFH2.Product.ProductConditionBridgeGeneralization,
    `VFH2.Product.ProductEffectConditionBridgeGeneralization,
    `VFH2.Product.ProductParams,
    `VFH2.Product.ProductParamsTransport,
    `VFH2.Product.ProductFixedSet,
    `VFH2.Product.ProductUpdate,
    `VFH2.Product.ProductNonfixedIncrease,
    `VFH2.Product.ProductLedger,
    `VFH2.Product.ProductLedgerTransport,
    `VFH2.Product.ProductLedgerEquivalenceTarget,
    `VFH2.Product.ProductLedgerTypedBlocks,
    `VFH2.Product.ProductLedgerTypedValuesLength,

    `VFH2.Product.ProductLedgerTypedValuesGetElem,


    `VFH2.Product.ProductLedgerTypedValuesDecomposition,
    `VFH2.Product.ProductFixedZero,
    `VFH2.Product.ProductPositiveLedger,
    `VFH2.Product.ProductRestrictedBridge
  ]
