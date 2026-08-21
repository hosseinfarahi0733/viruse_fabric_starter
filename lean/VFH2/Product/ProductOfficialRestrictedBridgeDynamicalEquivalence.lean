import VFH2.Product.ProductOfficialRestrictedBridgeStateSpaceEquivalence

/-!
# Product/Official Restricted-Bridge Dynamical Equivalence

The official list-backed update and the typed Product update are the same
dynamics after restricting the official model to its declared state space.
C53 proved the forward commutation law on serialized Product states. C55 proved
that every official restricted state has a unique Product representation. This
module supplies the inverse commutation law on the entire official restricted
state space.

Boundary:
- This connects only the two current restricted formalizations.
- It is not unrestricted `TTP-VF-H2-004`.
- It is not full-theory, empirical, or biological validation.
- It introduces no new update, assumption, compatibility API, or workflow.
- It makes no claim about raw lists outside the official restricted state
  space.
-/

namespace VFH2
namespace ProductOfficialRestrictedBridgeDynamicalEquivalence

open ProductOfficialRestrictedBridgeStateTransport
open ProductOfficialRestrictedBridgeDynamicsTransport
open ProductOfficialRestrictedBridgeTransitionReflection
open ProductOfficialRestrictedBridgeStateSpaceEquivalence

/--
For canonically serialized Product parameters, the official update maps every
official restricted state back into the same restricted state space.
-/
theorem officialRestrictedBridge_updateStateR_inRestrictedStateSpace
    (p : ProductRestrictedParams)
    (y : RestrictedBridge.State)
    (hspace :
      RestrictedBridge.inRestrictedStateSpace
        (officialRestrictedParams p) y) :
    RestrictedBridge.inRestrictedStateSpace
      (officialRestrictedParams p)
      (RestrictedBridge.updateStateR (officialRestrictedParams p) y) := by
  let x := productStateOfOfficialRestrictedState p y hspace
  have hserialize : officialRestrictedState p x = y :=
    officialRestrictedState_productStateOfOfficialRestrictedState p y hspace
  rw [← hserialize]
  rw [← officialRestrictedState_productUpdateState_eq_updateStateR]
  exact (officialRestrictedInput_wellFormed p (productUpdateState p x)).1

/--
Decoding the official update of any official restricted state gives exactly
the Product update of its decoded Product state.

Together with the C53 forward commutation law and the C55 unique state-space
representation theorem, this is the inverse dynamical transport law.
-/
theorem productStateOfOfficialRestrictedState_updateStateR
    (p : ProductRestrictedParams)
    (y : RestrictedBridge.State)
    (hspace :
      RestrictedBridge.inRestrictedStateSpace
        (officialRestrictedParams p) y) :
    productStateOfOfficialRestrictedState
        p
        (RestrictedBridge.updateStateR (officialRestrictedParams p) y)
        (officialRestrictedBridge_updateStateR_inRestrictedStateSpace
          p y hspace) =
      productUpdateState p
        (productStateOfOfficialRestrictedState p y hspace) := by
  apply officialRestrictedState_injective p
  rw [
    officialRestrictedState_productStateOfOfficialRestrictedState,
    officialRestrictedState_productUpdateState_eq_updateStateR,
    officialRestrictedState_productStateOfOfficialRestrictedState
  ]

end ProductOfficialRestrictedBridgeDynamicalEquivalence
end VFH2
