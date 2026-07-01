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
    `VFH2.Typed.TypedFixedSet
  ]
