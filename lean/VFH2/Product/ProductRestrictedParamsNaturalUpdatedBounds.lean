import VFH2.Product.ProductRestrictedParamsCanonicalBaseEffectFrozenBridge

namespace VFH2
namespace ProductRestrictedParamsNaturalUpdatedBounds

theorem restrictedParams_scoreKeyCondition_naturalBase_to_frozenUpdatedBounds
  (p : VFH2.ProductRestrictedParams)
  (x : p.State)
  (productUpdate : p.State → p.State)
  (productScore : p.State → Int)
  (fixed : Prop)
  (thresholdLo thresholdHi : Int)
  (hCondition :
    VFH2.ProductRestrictedParamsScorePreservingPolicyInstantiation.restrictedParamsScoreKeyPreservingUpdateCondition
      p productUpdate productScore)
  (hFixed : fixed)
  (hBaseLowerNatural : thresholdLo ≤ productScore x)
  (hBaseUpperNatural : productScore x ≤ thresholdHi) :
  VFH2.ProductRestrictedParamsRestrictedProofSpineFreeze.restrictedProofSpineUpdatedScoreWindowBounds
    p x productUpdate productScore fixed thresholdLo thresholdHi := by
  have hPolicy :
    VFH2.ProductRestrictedParamsScorePreservationDischarge.restrictedParamsScorePreservingUpdatePolicy
      p productUpdate productScore :=
    VFH2.ProductRestrictedParamsScorePreservingPolicyInstantiation.restrictedParams_scoreKeyPreservingUpdateCondition_to_scorePreservingPolicy
      p productUpdate productScore hCondition
  have hScore :
    productScore (productUpdate x) = productScore x :=
    hPolicy x
  constructor
  · constructor
    · exact hFixed
    · rw [hScore]
      exact hBaseLowerNatural
  · constructor
    · exact hFixed
    · rw [hScore]
      exact hBaseUpperNatural

theorem restrictedParams_identityLikeUpdate_naturalBase_to_frozenUpdatedBounds
  (p : VFH2.ProductRestrictedParams)
  (x : p.State)
  (productUpdate : p.State → p.State)
  (productScore : p.State → Int)
  (fixed : Prop)
  (thresholdLo thresholdHi : Int)
  (hIdentityLike :
    VFH2.ProductRestrictedParamsScorePreservingPolicyInstantiation.restrictedParamsIdentityLikeUpdate
      p productUpdate)
  (hFixed : fixed)
  (hBaseLowerNatural : thresholdLo ≤ productScore x)
  (hBaseUpperNatural : productScore x ≤ thresholdHi) :
  VFH2.ProductRestrictedParamsRestrictedProofSpineFreeze.restrictedProofSpineUpdatedScoreWindowBounds
    p x productUpdate productScore fixed thresholdLo thresholdHi := by
  have hPolicy :
    VFH2.ProductRestrictedParamsScorePreservationDischarge.restrictedParamsScorePreservingUpdatePolicy
      p productUpdate productScore :=
    VFH2.ProductRestrictedParamsScorePreservingPolicyInstantiation.restrictedParams_identityLikeUpdate_to_scorePreservingPolicy
      p productUpdate productScore hIdentityLike
  have hScore :
    productScore (productUpdate x) = productScore x :=
    hPolicy x
  constructor
  · constructor
    · exact hFixed
    · rw [hScore]
      exact hBaseLowerNatural
  · constructor
    · exact hFixed
    · rw [hScore]
      exact hBaseUpperNatural


end ProductRestrictedParamsNaturalUpdatedBounds
end VFH2
