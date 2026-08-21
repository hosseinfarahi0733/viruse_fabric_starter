import VFH2.Product.ProductOfficialRestrictedBridgeStateSpaceEquivalence
import VFH2.Product.ProductOfficialRestrictedBridgeParameterSpaceEquivalence

/-!
# Product/Official Restricted-Bridge Ledger State-Space Equivalence

The existing forward transport identifies official and Product ledger values
for a canonically serialized Product state.  This module extends that equality
to every state of every official well-formed restricted parameter object.

A canonical combined decoder first converts the official well-formed
parameters to Product parameters and then decodes any official in-space state.
The state round trip is exact.  Consequently both the ledger value and the
one-step ledger effect agree with their Product counterparts on the entire
official restricted state space, not merely on states presented initially as
Product serializations.

Boundary:
- This connects only the two current restricted formalizations.
- Official state-space membership is retained because it supplies list length
  and coordinate bounds for the typed Product state.
- It introduces no new dynamics or ledger definition and no assumptions beyond
  the existing official well-formed state-space domain.
- It is not unrestricted `TTP-VF-H2-004`.
- It is not full-theory, empirical, or biological validation.
-/

namespace VFH2
namespace ProductOfficialRestrictedBridgeLedgerStateSpaceEquivalence

open ProductOfficialRestrictedBridgeStateTransport
open ProductOfficialRestrictedBridgeDynamicsTransport
open ProductOfficialRestrictedBridgeStateSpaceEquivalence
open ProductOfficialRestrictedBridgeParameterSpaceEquivalence

private theorem officialRestrictedParams_productParamsOfOfficialWellFormed_eq_params
    (wp : RestrictedBridge.WellFormedRestrictedParams) :
    officialRestrictedParams
        (productParamsOfOfficialWellFormed wp) =
      wp.params := by
  exact congrArg
    RestrictedBridge.WellFormedRestrictedParams.params
    (officialWellFormedRestrictedParams_productParamsOfOfficialWellFormed wp)

/--
Decode an arbitrary state of arbitrary official well-formed parameters into
the corresponding typed Product state.
-/
def productStateOfOfficialWellFormedState
    (wp : RestrictedBridge.WellFormedRestrictedParams)
    (y : RestrictedBridge.State)
    (hspace :
      RestrictedBridge.inRestrictedStateSpace wp.params y) :
    (productParamsOfOfficialWellFormed wp).State :=
  productStateOfOfficialRestrictedState
    (productParamsOfOfficialWellFormed wp)
    y
    (by
      rw [
        officialRestrictedParams_productParamsOfOfficialWellFormed_eq_params
      ]
      exact hspace)

/-- Canonically serializing the combined decoded state returns the original
official list exactly.
-/
private theorem officialRestrictedState_productStateOfOfficialWellFormedState
    (wp : RestrictedBridge.WellFormedRestrictedParams)
    (y : RestrictedBridge.State)
    (hspace :
      RestrictedBridge.inRestrictedStateSpace wp.params y) :
    officialRestrictedState
        (productParamsOfOfficialWellFormed wp)
        (productStateOfOfficialWellFormedState wp y hspace) =
      y := by
  unfold productStateOfOfficialWellFormedState
  exact
    officialRestrictedState_productStateOfOfficialRestrictedState
      (productParamsOfOfficialWellFormed wp)
      y
      _

/-- On the entire official well-formed state space, the official ledger value
equals the Product ledger of the canonical decoded state.
-/
theorem officialWellFormed_ledgerVR_eq_productLedger
    (wp : RestrictedBridge.WellFormedRestrictedParams)
    (y : RestrictedBridge.State)
    (hspace :
      RestrictedBridge.inRestrictedStateSpace wp.params y) :
    RestrictedBridge.ledgerVR y =
      productLedger
        (productParamsOfOfficialWellFormed wp)
        (productStateOfOfficialWellFormedState wp y hspace) := by
  let p := productParamsOfOfficialWellFormed wp
  let x := productStateOfOfficialWellFormedState wp y hspace
  have hSerialize :
      officialRestrictedState p x = y :=
    officialRestrictedState_productStateOfOfficialWellFormedState
      wp y hspace
  calc
    RestrictedBridge.ledgerVR y =
        RestrictedBridge.ledgerVR (officialRestrictedState p x) :=
      congrArg RestrictedBridge.ledgerVR hSerialize.symm
    _ = productLedger p x :=
      officialRestrictedBridge_ledgerVR_eq_productLedger p x

/-- On the entire official well-formed state space, the official one-step
ledger effect equals the Product ledger effect of the canonical decoded state.
-/
theorem officialWellFormed_ledgerEffectR_eq_productLedgerEffect
    (wp : RestrictedBridge.WellFormedRestrictedParams)
    (y : RestrictedBridge.State)
    (hspace :
      RestrictedBridge.inRestrictedStateSpace wp.params y) :
    RestrictedBridge.ledgerEffectR wp.params y =
      productLedgerEffect
        (productParamsOfOfficialWellFormed wp)
        (productStateOfOfficialWellFormedState wp y hspace) := by
  let p := productParamsOfOfficialWellFormed wp
  let x := productStateOfOfficialWellFormedState wp y hspace
  have hParams :
      officialRestrictedParams p = wp.params :=
    officialRestrictedParams_productParamsOfOfficialWellFormed_eq_params wp
  have hSerialize :
      officialRestrictedState p x = y :=
    officialRestrictedState_productStateOfOfficialWellFormedState
      wp y hspace
  calc
    RestrictedBridge.ledgerEffectR wp.params y =
        RestrictedBridge.ledgerEffectR
          (officialRestrictedParams p) y := by
      rw [hParams]
    _ =
        RestrictedBridge.ledgerEffectR
          (officialRestrictedParams p)
          (officialRestrictedState p x) :=
      congrArg
        (RestrictedBridge.ledgerEffectR (officialRestrictedParams p))
        hSerialize.symm
    _ = productLedgerEffect p x :=
      officialRestrictedBridge_ledgerEffectR_eq_productLedgerEffect p x

end ProductOfficialRestrictedBridgeLedgerStateSpaceEquivalence
end VFH2
