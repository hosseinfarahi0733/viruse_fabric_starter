import VFH2.Product.ProductRestrictedParamsAfterOneUpdateProofSpineCharacterization
import VFH2.Product.ProductOfficialRestrictedBridgeStateSpaceEquivalence
import VFH2.Product.ProductOfficialRestrictedBridgeParameterSpaceEquivalence

/-!
# Official Well-Formed After-One-Update Proof-Spine Characterization

This module transports the exact global after-one-update characterization from
the typed Product model to every official well-formed list-backed restricted
parameter object.

For an official score, pullback along canonical Product-state serialization
places every Product update image in the current restricted proof spine
exactly when the original official score lies in the requested window on every
official fixed state in the official restricted state space.  Both parameter
surjectivity and state-space surjectivity are used, so the result covers all
official well-formed parameters and all official in-space fixed states rather
than only a preselected canonical example.

Boundary:
- This connects only the two current restricted formalizations.
- Official state-space membership is retained; raw malformed lists are outside
  the Product/state-space equivalence.
- It introduces no score bound or score-invariance assumption.
- It does not claim that every score satisfies the characterized condition.
- It is not unrestricted `TTP-VF-H2-004`.
- It is not full-theory, empirical, or biological validation.
-/

namespace VFH2
namespace ProductOfficialRestrictedBridgeAfterOneUpdateProofSpineCharacterization

open ProductOfficialRestrictedBridgeStateTransport
open ProductOfficialRestrictedBridgeStateSpaceEquivalence
open ProductOfficialRestrictedBridgeParameterSpaceEquivalence

/--
For every official well-formed parameter object, universal entry of the
pulled-back score into the Product proof spine after one update is equivalent
to the original official score being bounded on the entire official fixed
state space.
-/
theorem officialWellFormed_all_after_one_update_proofSpineTarget_iff_scoreBoundedOnFixedStateSpace
    (wp : RestrictedBridge.WellFormedRestrictedParams)
    (officialScore : RestrictedBridge.State → Int)
    (thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi) :
    let p := productParamsOfOfficialWellFormed wp
    (∀ x : p.State,
      ProductRestrictedParamsRestrictedProofSpineFreeze.restrictedProofSpineTarget
        p
        (productUpdateState p x)
        (productUpdateState p)
        (fun z : p.State =>
          officialScore (officialRestrictedState p z))
        (ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedUpdate
          p
          (productUpdateState p x)
          (productUpdateState p))
        (ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedScore
          p
          (productUpdateState p x)
          (productUpdateState p)
          (fun z : p.State =>
            officialScore (officialRestrictedState p z)))
        (ProductFixedSet p (productUpdateState p x))
        thresholdLo
        thresholdHi
        hThreshold)
      ↔
    (∀ y : RestrictedBridge.State,
      RestrictedBridge.inRestrictedStateSpace wp.params y →
      RestrictedBridge.inFixedSetR wp.params y →
        thresholdLo ≤ officialScore y ∧
        officialScore y ≤ thresholdHi) := by
  dsimp only
  let p := productParamsOfOfficialWellFormed wp
  have hParams :
      officialRestrictedParams p = wp.params := by
    exact congrArg
      RestrictedBridge.WellFormedRestrictedParams.params
      (officialWellFormedRestrictedParams_productParamsOfOfficialWellFormed wp)
  apply
    (ProductRestrictedParamsAfterOneUpdateProofSpineCharacterization.restrictedParams_all_after_one_update_proofSpineTarget_iff_scoreBoundedOnFixedSet
      p
      (fun z : p.State =>
        officialScore (officialRestrictedState p z))
      thresholdLo
      thresholdHi
      hThreshold).trans
  constructor
  · intro hProduct y hySpace hyFixed
    have hySpaceProductParams :
        RestrictedBridge.inRestrictedStateSpace
          (officialRestrictedParams p) y := by
      rw [hParams]
      exact hySpace
    let x :=
      productStateOfOfficialRestrictedState
        p y hySpaceProductParams
    have hSerialize :
        officialRestrictedState p x = y :=
      officialRestrictedState_productStateOfOfficialRestrictedState
        p y hySpaceProductParams
    have hyFixedProductParams :
        RestrictedBridge.inFixedSetR
          (officialRestrictedParams p) y := by
      rw [hParams]
      exact hyFixed
    have hxFixed : ProductFixedSet p x := by
      apply
        (productFixedSet_iff_officialRestrictedBridge_inFixedSetR
          p x).mpr
      rw [hSerialize]
      exact hyFixedProductParams
    have hBounds := hProduct x hxFixed
    rw [hSerialize] at hBounds
    exact hBounds
  · intro hOfficial x hxFixed
    have hxSpaceProductParams :
        RestrictedBridge.inRestrictedStateSpace
          (officialRestrictedParams p)
          (officialRestrictedState p x) :=
      (officialRestrictedInput_wellFormed p x).1
    have hxSpace :
        RestrictedBridge.inRestrictedStateSpace
          wp.params
          (officialRestrictedState p x) := by
      rw [← hParams]
      exact hxSpaceProductParams
    have hxFixedProductParams :
        RestrictedBridge.inFixedSetR
          (officialRestrictedParams p)
          (officialRestrictedState p x) :=
      (productFixedSet_iff_officialRestrictedBridge_inFixedSetR
        p x).mp hxFixed
    have hxOfficialFixed :
        RestrictedBridge.inFixedSetR
          wp.params
          (officialRestrictedState p x) := by
      rw [← hParams]
      exact hxFixedProductParams
    exact
      hOfficial
        (officialRestrictedState p x)
        hxSpace
        hxOfficialFixed

end ProductOfficialRestrictedBridgeAfterOneUpdateProofSpineCharacterization
end VFH2
