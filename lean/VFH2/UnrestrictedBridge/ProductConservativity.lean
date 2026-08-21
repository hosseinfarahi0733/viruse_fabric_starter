import VFH2.UnrestrictedBridge.OfficialRestrictedEmbedding
import VFH2.Product.ProductOfficialRestrictedBridgeDynamicsTransport

/-!
# Product Conservativity for the Countably Indexed Finite-Observation Model

This module composes the existing verified Product/Official RestrictedBridge
transport with the countably indexed finite-observation embedding.

It proves that the new scaffold agrees with the existing Product semantics on:

- one-step update;
- finite ledger value;
- finite ledger effect;
- fixed-set membership.

Boundary:
- This is a conservativity result for the existing finite restricted Product
  model.
- It is not unrestricted `TTP-VF-H2-004`.
- It does not define or use a global infinite ledger.
- It makes no empirical or biological claim.
- It introduces no new assumptions.
-/

namespace VFH2
namespace UnrestrictedBridge

open ProductOfficialRestrictedBridgeStateTransport
open ProductOfficialRestrictedBridgeDynamicsTransport

/-- Embed Product parameters through the canonical official restricted bridge. -/
def paramsUOfProduct
    (p : ProductRestrictedParams) :
    ParamsU :=
  paramsUOfRestricted (officialRestrictedParams p)

/-- Embed a Product state through its canonical official serialization. -/
def stateUOfProduct
    (p : ProductRestrictedParams)
    (x : p.State) :
    StateU :=
  stateUOfRestricted (officialRestrictedState p x)

/-- The finite observation window associated with a Product parameter object. -/
def productWindowU
    (p : ProductRestrictedParams) :
    List Nat :=
  restrictedWindow (officialRestrictedParams p)

/--
The countably indexed update agrees exactly with the existing Product update
after canonical embedding.
-/
theorem stateUOfProduct_productUpdateState
    (p : ProductRestrictedParams)
    (x : p.State) :
    stateUOfProduct p (productUpdateState p x) =
      updateU
        (paramsUOfProduct p)
        (stateUOfProduct p x) := by
  unfold stateUOfProduct paramsUOfProduct

  rw [
    officialRestrictedState_productUpdateState_eq_updateStateR
  ]

  exact
    stateUOfRestricted_updateStateR
      (officialWellFormedRestrictedParams p)
      (officialRestrictedState p x)
      (officialRestrictedInput_wellFormed p x).1

/--
The finite-observation ledger of an embedded Product state is exactly the
existing Product ledger.
-/
theorem ledgerOn_productWindowU_stateUOfProduct
    (p : ProductRestrictedParams)
    (x : p.State) :
    ledgerOn
        (productWindowU p)
        (stateUOfProduct p x) =
      productLedger p x := by
  unfold productWindowU stateUOfProduct

  calc
    ledgerOn
        (restrictedWindow (officialRestrictedParams p))
        (stateUOfRestricted (officialRestrictedState p x))
        =
      RestrictedBridge.ledgerVR
        (officialRestrictedState p x) :=
      ledgerOn_restrictedWindow_stateUOfRestricted
        (officialRestrictedParams p)
        (officialRestrictedState p x)
        (officialRestrictedInput_wellFormed p x).1.1

    _ = productLedger p x :=
      officialRestrictedBridge_ledgerVR_eq_productLedger p x

/--
The finite-observation ledger effect of an embedded Product state is exactly
the existing Product ledger effect.
-/
theorem ledgerEffectOn_productWindowU_stateUOfProduct
    (p : ProductRestrictedParams)
    (x : p.State) :
    ledgerEffectOn
        (paramsUOfProduct p)
        (productWindowU p)
        (stateUOfProduct p x) =
      productLedgerEffect p x := by
  unfold paramsUOfProduct productWindowU stateUOfProduct

  calc
    ledgerEffectOn
        (paramsUOfRestricted (officialRestrictedParams p))
        (restrictedWindow (officialRestrictedParams p))
        (stateUOfRestricted (officialRestrictedState p x))
        =
      RestrictedBridge.ledgerEffectR
        (officialRestrictedParams p)
        (officialRestrictedState p x) :=
      ledgerEffectOn_restrictedWindow_stateUOfRestricted
        (officialWellFormedRestrictedParams p)
        (officialRestrictedState p x)
        (officialRestrictedInput_wellFormed p x).1

    _ = productLedgerEffect p x :=
      officialRestrictedBridge_ledgerEffectR_eq_productLedgerEffect p x

/--
Fixed-set membership is preserved and reflected exactly by the Product
embedding.
-/
theorem inFixedSetU_stateUOfProduct_iff
    (p : ProductRestrictedParams)
    (x : p.State) :
    inFixedSetU
        (paramsUOfProduct p)
        (stateUOfProduct p x)
      ↔
    ProductFixedSet p x := by
  unfold paramsUOfProduct stateUOfProduct

  calc
    inFixedSetU
        (paramsUOfRestricted (officialRestrictedParams p))
        (stateUOfRestricted (officialRestrictedState p x))
        ↔
      RestrictedBridge.inFixedSetR
        (officialRestrictedParams p)
        (officialRestrictedState p x) :=
      inFixedSetU_stateUOfRestricted_iff
        (officialRestrictedParams p)
        (officialRestrictedState p x)

    _ ↔ ProductFixedSet p x :=
      (productFixedSet_iff_officialRestrictedBridge_inFixedSetR p x).symm

/--
C72 conservativity theorem.

The new countably indexed finite-observation layer reproduces the existing
restricted Product update, ledger, ledger effect, and fixed-set semantics.
-/
theorem productRestrictedSemantics_conservative
    (p : ProductRestrictedParams)
    (x : p.State) :
    stateUOfProduct p (productUpdateState p x) =
        updateU
          (paramsUOfProduct p)
          (stateUOfProduct p x)
      ∧
    ledgerOn
        (productWindowU p)
        (stateUOfProduct p x) =
        productLedger p x
      ∧
    ledgerEffectOn
        (paramsUOfProduct p)
        (productWindowU p)
        (stateUOfProduct p x) =
        productLedgerEffect p x
      ∧
    (
      inFixedSetU
          (paramsUOfProduct p)
          (stateUOfProduct p x)
        ↔
      ProductFixedSet p x
    ) := by
  constructor
  · exact stateUOfProduct_productUpdateState p x

  constructor
  · exact ledgerOn_productWindowU_stateUOfProduct p x

  constructor
  · exact ledgerEffectOn_productWindowU_stateUOfProduct p x

  · exact inFixedSetU_stateUOfProduct_iff p x

end UnrestrictedBridge
end VFH2
