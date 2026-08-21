import VFH2.Product.ProductOfficialRestrictedBridgeDynamicalEquivalence
import VFH2.Product.ProductOfficialRestrictedBridgeParameterSpaceEquivalence
import VFH2.Product.ProductRestrictedParamsScoreKeyConditionInactiveCharacterization

/-!
# Product/Official Restricted-Bridge Score-Semantics Equivalence

This module completes the score-preservation connection between the two current
restricted formalizations.  For every official well-formed parameter object,
an integer-valued score is preserved by the official list-backed update on the
entire official restricted state space exactly when its pullback along
canonical Product serialization is preserved by the Product update.

Combining that dynamical equivalence with the exact Product update-fiber
classification shows that official score preservation is also exactly
inactive-insensitivity of the pulled-back Product score.

Both directions use the semantic equivalence: the reverse direction decodes an
arbitrary official in-space state, rather than proving only a result for an
already serialized state.

Boundary:
- This connects only the two current restricted formalizations.
- Official state-space membership is retained for the list-backed side.
- It introduces no score-preservation or inactive-insensitivity assumption.
- It does not claim that every score satisfies the characterized condition.
- It is not unrestricted `TTP-VF-H2-004`.
- It is not full-theory, empirical, or biological validation.
-/

namespace VFH2
namespace ProductOfficialRestrictedBridgeScoreSemanticsEquivalence

open ProductOfficialRestrictedBridgeStateTransport
open ProductOfficialRestrictedBridgeDynamicsTransport
open ProductOfficialRestrictedBridgeStateSpaceEquivalence
open ProductOfficialRestrictedBridgeParameterSpaceEquivalence

/--
For every official well-formed parameter object, score preservation on the
whole official restricted state space is equivalent to preservation of the
pulled-back score by the corresponding Product update.
-/
theorem officialWellFormed_updateScorePreserved_iff_productUpdateScorePreserved
    (wp : RestrictedBridge.WellFormedRestrictedParams)
    (officialScore : RestrictedBridge.State → Int) :
    let p := productParamsOfOfficialWellFormed wp
    (∀ y : RestrictedBridge.State,
      RestrictedBridge.inRestrictedStateSpace wp.params y →
        officialScore (RestrictedBridge.updateStateR wp.params y) =
          officialScore y)
      ↔
    (∀ x : p.State,
      officialScore
          (officialRestrictedState p (productUpdateState p x)) =
        officialScore (officialRestrictedState p x)) := by
  dsimp only
  let p := productParamsOfOfficialWellFormed wp
  have hParams :
      officialRestrictedParams p = wp.params := by
    exact congrArg
      RestrictedBridge.WellFormedRestrictedParams.params
      (officialWellFormedRestrictedParams_productParamsOfOfficialWellFormed wp)
  constructor
  · intro hOfficial x
    have hxSpace :
        RestrictedBridge.inRestrictedStateSpace
          wp.params
          (officialRestrictedState p x) := by
      rw [← hParams]
      exact (officialRestrictedInput_wellFormed p x).1
    rw [officialRestrictedState_productUpdateState_eq_updateStateR]
    rw [hParams]
    exact hOfficial (officialRestrictedState p x) hxSpace
  · intro hProduct y hySpace
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
    have hxPreserved := hProduct x
    rw [
      officialRestrictedState_productUpdateState_eq_updateStateR,
      hSerialize,
      hParams
    ] at hxPreserved
    exact hxPreserved

/--
For every official well-formed parameter object, official score preservation
on the entire official restricted state space is exactly inactive-insensitivity
of the pulled-back Product score.
-/
theorem officialWellFormed_updateScorePreserved_iff_productScoreInactiveInsensitive
    (wp : RestrictedBridge.WellFormedRestrictedParams)
    (officialScore : RestrictedBridge.State → Int) :
    let p := productParamsOfOfficialWellFormed wp
    (∀ y : RestrictedBridge.State,
      RestrictedBridge.inRestrictedStateSpace wp.params y →
        officialScore (RestrictedBridge.updateStateR wp.params y) =
          officialScore y)
      ↔
    ProductRestrictedParamsActiveInsensitiveScore.productScoreInactiveInsensitive
      p
      (fun x : p.State =>
        officialScore (officialRestrictedState p x)) := by
  dsimp only
  let p := productParamsOfOfficialWellFormed wp
  exact
    (officialWellFormed_updateScorePreserved_iff_productUpdateScorePreserved
      wp officialScore).trans
      ((ProductRestrictedParamsScorePreservingPolicyInstantiation.restrictedParams_scoreKeyCondition_iff_policyPoint
        p
        (productUpdateState p)
        (fun x : p.State =>
          officialScore (officialRestrictedState p x))).symm.trans
        (ProductRestrictedParamsScoreKeyConditionInactiveCharacterization.restrictedParams_productUpdateState_scoreKeyCondition_iff_inactiveInsensitive
          p
          (fun x : p.State =>
            officialScore (officialRestrictedState p x))))

end ProductOfficialRestrictedBridgeScoreSemanticsEquivalence
end VFH2
