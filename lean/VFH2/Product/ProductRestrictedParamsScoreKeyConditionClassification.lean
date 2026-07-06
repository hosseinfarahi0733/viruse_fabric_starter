import VFH2.Product.ProductRestrictedParamsScorePreservingPolicyInstantiation
import VFH2.Product.ProductRestrictedParamsScorePreservationDischarge

namespace VFH2
namespace ProductRestrictedParamsScorePreservingPolicyInstantiation

/--
C8.1 classification theorem.

The existential score-key preservation condition can be reconstructed from
pointwise score preservation by choosing:

- `ScoreKey := Int`
- `scoreKey := productScore`
- `scoreOfKey := id`

This classifies the score-key condition as a representation of pointwise
score preservation. It does not derive score preservation from domain dynamics.
-/
theorem restrictedParams_policyPoint_to_scoreKeyCondition
    (p : VFH2.ProductRestrictedParams)
    (productUpdate : p.State → p.State)
    (productScore : p.State → Int)
    (hPolicyPoint : ∀ y : p.State, productScore (productUpdate y) = productScore y) :
    restrictedParamsScoreKeyPreservingUpdateCondition
      p productUpdate productScore := by
  unfold restrictedParamsScoreKeyPreservingUpdateCondition
  refine ⟨Int, productScore, id, ?_⟩
  constructor
  · intro y
    rfl
  · intro y
    exact hPolicyPoint y

/--
The score-key condition is equivalent to pointwise score preservation.

This is a classification result, not a domain-semantics derivation.
-/
theorem restrictedParams_scoreKeyCondition_iff_policyPoint
    (p : VFH2.ProductRestrictedParams)
    (productUpdate : p.State → p.State)
    (productScore : p.State → Int) :
    restrictedParamsScoreKeyPreservingUpdateCondition p productUpdate productScore ↔
      (∀ y : p.State, productScore (productUpdate y) = productScore y) := by
  constructor
  · intro hCondition
    intro y
    exact restrictedParams_scoreKeyCondition_to_policyPoint
      p y productUpdate productScore hCondition
  · intro hPolicyPoint
    exact restrictedParams_policyPoint_to_scoreKeyCondition
      p productUpdate productScore hPolicyPoint

/--
The score-key condition is equivalent to the existing restricted score-preserving
update policy.

This sharpens the assumption boundary: the score-key condition is not stronger
than pointwise score preservation; it is an existential factorization form of it.
-/
theorem restrictedParams_scoreKeyCondition_iff_scorePreservingPolicy
    (p : VFH2.ProductRestrictedParams)
    (productUpdate : p.State → p.State)
    (productScore : p.State → Int) :
    restrictedParamsScoreKeyPreservingUpdateCondition p productUpdate productScore ↔
      VFH2.ProductRestrictedParamsScorePreservationDischarge.restrictedParamsScorePreservingUpdatePolicy
        p productUpdate productScore := by
  constructor
  · intro hCondition
    exact restrictedParams_scoreKeyPreservingUpdateCondition_to_scorePreservingPolicy
      p productUpdate productScore hCondition
  · intro hPolicy
    exact restrictedParams_policyPoint_to_scoreKeyCondition
      p productUpdate productScore
      (fun y => hPolicy y)

end ProductRestrictedParamsScorePreservingPolicyInstantiation
end VFH2
