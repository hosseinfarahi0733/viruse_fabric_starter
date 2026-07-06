import VFH2.Product.ProductRestrictedParamsCanonicalRawEqualities

namespace VFH2
namespace ProductRestrictedParamsCanonicalBaseEffectFrozenBridge

theorem restrictedParams_scoreKeyCondition_canonicalBaseEffect_to_restrictedProofSpineTarget
  (p : VFH2.ProductRestrictedParams)
  (x : p.State)
  (productUpdate : p.State → p.State)
  (productScore : p.State → Int)
  (fixed : Prop)
  (thresholdLo thresholdHi : Int)
  (hThreshold : thresholdLo ≤ thresholdHi)
  (hCondition :
    VFH2.ProductRestrictedParamsScorePreservingPolicyInstantiation.restrictedParamsScoreKeyPreservingUpdateCondition
      p productUpdate productScore)
  (hFixed : fixed)
  (hBaseLower : thresholdHi ≤ productScore x)
  (hBaseUpper : productScore x ≤ thresholdLo) :
  VFH2.ProductRestrictedParamsRestrictedProofSpineFreeze.restrictedProofSpineTarget
    p x productUpdate productScore
    (VFH2.ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedUpdate p x productUpdate)
    (VFH2.ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedScore p x productUpdate productScore)
    fixed thresholdLo thresholdHi hThreshold := by
  exact
    VFH2.ProductRestrictedParamsCanonicalRawEqualities.restrictedParams_scoreKeyCondition_canonicalRaw_to_restrictedProofSpineTarget
      p x productUpdate productScore fixed
      (productScore x)
      thresholdLo thresholdHi hThreshold
      rfl
      hCondition
      hFixed
      hBaseLower
      hBaseUpper

theorem restrictedParams_scoreKeyCondition_canonicalBaseEffect_to_frozenUpdatedBounds
  (p : VFH2.ProductRestrictedParams)
  (x : p.State)
  (productUpdate : p.State → p.State)
  (productScore : p.State → Int)
  (fixed : Prop)
  (thresholdLo thresholdHi : Int)
  (hThreshold : thresholdLo ≤ thresholdHi)
  (hCondition :
    VFH2.ProductRestrictedParamsScorePreservingPolicyInstantiation.restrictedParamsScoreKeyPreservingUpdateCondition
      p productUpdate productScore)
  (hFixed : fixed)
  (hBaseLower : thresholdHi ≤ productScore x)
  (hBaseUpper : productScore x ≤ thresholdLo) :
  VFH2.ProductRestrictedParamsRestrictedProofSpineFreeze.restrictedProofSpineUpdatedScoreWindowBounds
    p x productUpdate productScore fixed thresholdLo thresholdHi := by
  exact
    VFH2.ProductRestrictedParamsCanonicalRawEqualities.restrictedParams_scoreKeyCondition_canonicalRaw_to_frozenUpdatedBounds
      p x productUpdate productScore fixed
      (productScore x)
      thresholdLo thresholdHi hThreshold
      rfl
      hCondition
      hFixed
      hBaseLower
      hBaseUpper

theorem restrictedParams_identityLikeUpdate_canonicalBaseEffect_to_restrictedProofSpineTarget
  (p : VFH2.ProductRestrictedParams)
  (x : p.State)
  (productUpdate : p.State → p.State)
  (productScore : p.State → Int)
  (fixed : Prop)
  (thresholdLo thresholdHi : Int)
  (hThreshold : thresholdLo ≤ thresholdHi)
  (hIdentityLike :
    VFH2.ProductRestrictedParamsScorePreservingPolicyInstantiation.restrictedParamsIdentityLikeUpdate
      p productUpdate)
  (hFixed : fixed)
  (hBaseLower : thresholdHi ≤ productScore x)
  (hBaseUpper : productScore x ≤ thresholdLo) :
  VFH2.ProductRestrictedParamsRestrictedProofSpineFreeze.restrictedProofSpineTarget
    p x productUpdate productScore
    (VFH2.ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedUpdate p x productUpdate)
    (VFH2.ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedScore p x productUpdate productScore)
    fixed thresholdLo thresholdHi hThreshold := by
  exact
    VFH2.ProductRestrictedParamsCanonicalRawEqualities.restrictedParams_identityLikeUpdate_canonicalRaw_to_restrictedProofSpineTarget
      p x productUpdate productScore fixed
      (productScore x)
      thresholdLo thresholdHi hThreshold
      rfl
      hIdentityLike
      hFixed
      hBaseLower
      hBaseUpper

theorem restrictedParams_identityLikeUpdate_canonicalBaseEffect_to_frozenUpdatedBounds
  (p : VFH2.ProductRestrictedParams)
  (x : p.State)
  (productUpdate : p.State → p.State)
  (productScore : p.State → Int)
  (fixed : Prop)
  (thresholdLo thresholdHi : Int)
  (hThreshold : thresholdLo ≤ thresholdHi)
  (hIdentityLike :
    VFH2.ProductRestrictedParamsScorePreservingPolicyInstantiation.restrictedParamsIdentityLikeUpdate
      p productUpdate)
  (hFixed : fixed)
  (hBaseLower : thresholdHi ≤ productScore x)
  (hBaseUpper : productScore x ≤ thresholdLo) :
  VFH2.ProductRestrictedParamsRestrictedProofSpineFreeze.restrictedProofSpineUpdatedScoreWindowBounds
    p x productUpdate productScore fixed thresholdLo thresholdHi := by
  exact
    VFH2.ProductRestrictedParamsCanonicalRawEqualities.restrictedParams_identityLikeUpdate_canonicalRaw_to_frozenUpdatedBounds
      p x productUpdate productScore fixed
      (productScore x)
      thresholdLo thresholdHi hThreshold
      rfl
      hIdentityLike
      hFixed
      hBaseLower
      hBaseUpper


end ProductRestrictedParamsCanonicalBaseEffectFrozenBridge
end VFH2
