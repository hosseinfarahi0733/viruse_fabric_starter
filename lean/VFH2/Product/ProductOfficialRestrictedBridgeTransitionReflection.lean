import VFH2.Product.ProductOfficialRestrictedBridgeDynamicsTransport

/-!
# Product/Official Restricted-Bridge Transition Reflection

C53 proved that canonical serialization preserves the restricted Product
update. This module proves the missing reverse semantic direction: canonical
state serialization is injective, and an official list-backed transition
between serialized Product states holds exactly when the corresponding Product
transition holds.

Boundary:
- This connects only the two current restricted formalizations.
- The reflection theorem concerns canonical serialized Product states, not
  arbitrary raw list-backed states.
- It is not unrestricted `TTP-VF-H2-004`.
- It is not full-theory, empirical, or biological validation.
- It introduces no new dynamics or assumptions.
-/

namespace VFH2
namespace ProductOfficialRestrictedBridgeTransitionReflection

open ProductOfficialRestrictedBridgeStateTransport
open ProductOfficialRestrictedBridgeDynamicsTransport

/-- Canonical serialization reflects equality of Product states. -/
theorem officialRestrictedState_injective
    (p : ProductRestrictedParams) :
    Function.Injective (officialRestrictedState p) := by
  intro x z hserialized
  funext i
  have hlookup :=
    congrArg
      (fun state =>
        state.getD (ProductIndex.flatten i).val 0)
      hserialized
  have hval :
      (x i).val = (z i).val := by
    simpa only [officialRestrictedState_getD_flatten] using hlookup
  cases hx : x i with
  | mk xv hxb =>
      cases hz : z i with
      | mk zv hzb =>
          simp only [hx, hz] at hval ⊢
          cases hval
          rfl

/--
The official update graph on canonical serialized states is exactly the
restricted Product update graph.
-/
theorem officialRestrictedBridge_updateStateR_eq_serialized_iff_productUpdateState_eq
    (p : ProductRestrictedParams)
    (x z : p.State) :
    RestrictedBridge.updateStateR
        (officialRestrictedParams p)
        (officialRestrictedState p x) =
      officialRestrictedState p z ↔
    productUpdateState p x = z := by
  constructor
  · intro htransition
    apply officialRestrictedState_injective p
    rw [officialRestrictedState_productUpdateState_eq_updateStateR]
    exact htransition
  · intro hupdate
    rw [← officialRestrictedState_productUpdateState_eq_updateStateR]
    rw [hupdate]

end ProductOfficialRestrictedBridgeTransitionReflection
end VFH2
