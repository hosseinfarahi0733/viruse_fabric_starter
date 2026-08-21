import VFH2.Product.ProductOfficialRestrictedBridgeTransitionReflection

/-!
# Product/Official Restricted-Bridge State-Space Equivalence

The canonical serialization from the typed Product model reaches exactly the
official list-backed restricted state space.  This completes the state-level
semantic connection between the two current restricted formalizations: every
well-bounded list of the expected width comes from one unique Product state.

Boundary:
- This connects only the two current restricted formalizations.
- It is not unrestricted `TTP-VF-H2-004`.
- It is not full-theory, empirical, or biological validation.
- It introduces no new dynamics, ledger semantics, or assumptions.
- It makes no claim about raw lists outside the official restricted state
  space.
-/

namespace VFH2
namespace ProductOfficialRestrictedBridgeStateSpaceEquivalence

open ProductOfficialRestrictedBridgeStateTransport
open ProductOfficialRestrictedBridgeTransitionReflection

/--
Decode an official restricted state into the typed Product state whose
coordinate at `i` is the list entry at the flattened index of `i`.

The restricted state-space hypotheses provide both the in-range lookup proof
and the coordinate bound required by the Product state type.
-/
def productStateOfOfficialRestrictedState
    (p : ProductRestrictedParams)
    (y : RestrictedBridge.State)
    (hspace :
      RestrictedBridge.inRestrictedStateSpace
        (officialRestrictedParams p) y) :
    p.State :=
  fun i =>
    let hwidth :
        y.length = 3 * p.d := by
      exact hspace.1
    let hindex :
        (ProductIndex.flatten i).val < y.length := by
      rw [hwidth]
      exact (ProductIndex.flatten i).isLt
    let value := y[(ProductIndex.flatten i).val]'hindex
    ⟨value, hspace.2 value (List.get_mem y ⟨_, hindex⟩)⟩

/--
Decoding and then canonically serializing an official restricted state returns
the original list.
-/
theorem officialRestrictedState_productStateOfOfficialRestrictedState
    (p : ProductRestrictedParams)
    (y : RestrictedBridge.State)
    (hspace :
      RestrictedBridge.inRestrictedStateSpace
        (officialRestrictedParams p) y) :
    officialRestrictedState p
        (productStateOfOfficialRestrictedState p y hspace) = y := by
  apply List.ext_get
  · exact officialRestrictedState_length p
      (productStateOfOfficialRestrictedState p y hspace) |>.trans hspace.1.symm
  · intro n hserialized hy
    simp only [officialRestrictedState, List.get_eq_getElem,
      List.getElem_ofFn, ProductStateTransport.productToTyped_apply,
      productStateOfOfficialRestrictedState]
    simp [ProductIndex.flatten_unflatten]

/--
Official restricted state-space membership is exactly unique representability
by canonical Product-state serialization.
-/
theorem existsUnique_officialRestrictedState_iff_inRestrictedStateSpace
    (p : ProductRestrictedParams)
    (y : RestrictedBridge.State) :
    (∃ x : p.State,
      officialRestrictedState p x = y ∧
        ∀ z : p.State, officialRestrictedState p z = y → z = x) ↔
      RestrictedBridge.inRestrictedStateSpace
        (officialRestrictedParams p) y := by
  constructor
  · rintro ⟨x, hx, _⟩
    rw [← hx]
    exact (officialRestrictedInput_wellFormed p x).1
  · intro hspace
    let x := productStateOfOfficialRestrictedState p y hspace
    have hx : officialRestrictedState p x = y :=
      officialRestrictedState_productStateOfOfficialRestrictedState p y hspace
    refine ⟨x, hx, ?_⟩
    intro z hz
    exact officialRestrictedState_injective p (hz.trans hx.symm)

end ProductOfficialRestrictedBridgeStateSpaceEquivalence
end VFH2
