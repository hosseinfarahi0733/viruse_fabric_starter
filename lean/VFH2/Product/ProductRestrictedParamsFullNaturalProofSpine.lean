import VFH2.Product.ProductRestrictedParamsNaturalUpdatedBounds
import VFH2.Product.ProductRestrictedParamsScorePreservingUpdate
import VFH2.Product.ProductRestrictedParamsScoreWindow
import VFH2.Product.ProductEffectBoundConditionMonotonicity

namespace VFH2
namespace ProductRestrictedParamsFullNaturalProofSpine

theorem restrictedParams_canonicalRawUpdateScoreTransportCertificate_of_policy
  (p : VFH2.ProductRestrictedParams)
  (x : p.State)
  (productUpdate : p.State → p.State)
  (productScore : p.State → Int)
  (hPolicy :
    VFH2.ProductRestrictedParamsScorePreservationDischarge.restrictedParamsScorePreservingUpdatePolicy
      p productUpdate productScore) :
  VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsRawUpdateScoreTransportCertificate
    p x productUpdate productScore
    (VFH2.ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedUpdate p x productUpdate)
    (VFH2.ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedScore p x productUpdate productScore) := by
  unfold VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsRawUpdateScoreTransportCertificate
  constructor
  · exact
      VFH2.ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedUpdate_base_to_updated
        p x productUpdate
  constructor
  · exact
      VFH2.ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedScore_base
        p x productUpdate productScore
  · exact
      VFH2.ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedScore_updated_of_policy
        p x productUpdate productScore hPolicy

theorem restrictedParams_naturalBaseScoreWindow_of_components
  (p : VFH2.ProductRestrictedParams)
  (x : p.State)
  (productScore : p.State → Int)
  (fixed : Prop)
  (thresholdLo thresholdHi : Int)
  (hFixed : fixed)
  (hBaseLowerNatural : thresholdLo ≤ productScore x)
  (hBaseUpperNatural : productScore x ≤ thresholdHi) :
  VFH2.ProductRestrictedParamsScoreWindow.restrictedParamsBaseScoreWindow
    p x productScore fixed thresholdLo thresholdHi := by
  unfold VFH2.ProductRestrictedParamsScoreWindow.restrictedParamsBaseScoreWindow
  constructor
  · exact ⟨hFixed, hBaseLowerNatural⟩
  · exact ⟨hFixed, hBaseUpperNatural⟩

theorem restrictedParams_scoreKeyCondition_naturalBase_to_baseScoreWindowTarget
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
  (hBaseLowerNatural : thresholdLo ≤ productScore x)
  (hBaseUpperNatural : productScore x ≤ thresholdHi) :
  VFH2.ProductRestrictedParamsScoreWindow.restrictedParamsBaseScoreWindowTarget
    p x productUpdate productScore
    (VFH2.ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedUpdate p x productUpdate)
    (VFH2.ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedScore p x productUpdate productScore)
    fixed thresholdLo thresholdHi hThreshold := by
  have hPolicy :
    VFH2.ProductRestrictedParamsScorePreservationDischarge.restrictedParamsScorePreservingUpdatePolicy
      p productUpdate productScore :=
    VFH2.ProductRestrictedParamsScorePreservingPolicyInstantiation.restrictedParams_scoreKeyPreservingUpdateCondition_to_scorePreservingPolicy
      p productUpdate productScore hCondition
  unfold VFH2.ProductRestrictedParamsScoreWindow.restrictedParamsBaseScoreWindowTarget
  constructor
  · exact
      restrictedParams_naturalBaseScoreWindow_of_components
        p x productScore fixed thresholdLo thresholdHi
        hFixed hBaseLowerNatural hBaseUpperNatural
  constructor
  · exact
      VFH2.ProductEffectBoundConditionMonotonicity.restrictedEffectBoundMonotoneTransport_certificate
        p x thresholdLo thresholdHi hThreshold
  · exact
      restrictedParams_canonicalRawUpdateScoreTransportCertificate_of_policy
        p x productUpdate productScore hPolicy

theorem restrictedParams_identityLikeUpdate_naturalBase_to_baseScoreWindowTarget
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
  (hBaseLowerNatural : thresholdLo ≤ productScore x)
  (hBaseUpperNatural : productScore x ≤ thresholdHi) :
  VFH2.ProductRestrictedParamsScoreWindow.restrictedParamsBaseScoreWindowTarget
    p x productUpdate productScore
    (VFH2.ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedUpdate p x productUpdate)
    (VFH2.ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedScore p x productUpdate productScore)
    fixed thresholdLo thresholdHi hThreshold := by
  have hPolicy :
    VFH2.ProductRestrictedParamsScorePreservationDischarge.restrictedParamsScorePreservingUpdatePolicy
      p productUpdate productScore :=
    VFH2.ProductRestrictedParamsScorePreservingPolicyInstantiation.restrictedParams_identityLikeUpdate_to_scorePreservingPolicy
      p productUpdate productScore hIdentityLike
  unfold VFH2.ProductRestrictedParamsScoreWindow.restrictedParamsBaseScoreWindowTarget
  constructor
  · exact
      restrictedParams_naturalBaseScoreWindow_of_components
        p x productScore fixed thresholdLo thresholdHi
        hFixed hBaseLowerNatural hBaseUpperNatural
  constructor
  · exact
      VFH2.ProductEffectBoundConditionMonotonicity.restrictedEffectBoundMonotoneTransport_certificate
        p x thresholdLo thresholdHi hThreshold
  · exact
      restrictedParams_canonicalRawUpdateScoreTransportCertificate_of_policy
        p x productUpdate productScore hPolicy

theorem restrictedParams_scoreKeyCondition_naturalBase_to_restrictedProofSpineTarget
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
  (hBaseLowerNatural : thresholdLo ≤ productScore x)
  (hBaseUpperNatural : productScore x ≤ thresholdHi) :
  VFH2.ProductRestrictedParamsRestrictedProofSpineFreeze.restrictedProofSpineTarget
    p x productUpdate productScore
    (VFH2.ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedUpdate p x productUpdate)
    (VFH2.ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedScore p x productUpdate productScore)
    fixed thresholdLo thresholdHi hThreshold := by
  have hPolicy :
    VFH2.ProductRestrictedParamsScorePreservationDischarge.restrictedParamsScorePreservingUpdatePolicy
      p productUpdate productScore :=
    VFH2.ProductRestrictedParamsScorePreservingPolicyInstantiation.restrictedParams_scoreKeyPreservingUpdateCondition_to_scorePreservingPolicy
      p productUpdate productScore hCondition
  have hScorePreserved :
    productScore (productUpdate x) = productScore x :=
    hPolicy x
  have hBaseTarget :
    VFH2.ProductRestrictedParamsScoreWindow.restrictedParamsBaseScoreWindowTarget
      p x productUpdate productScore
      (VFH2.ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedUpdate p x productUpdate)
      (VFH2.ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedScore p x productUpdate productScore)
      fixed thresholdLo thresholdHi hThreshold :=
    restrictedParams_scoreKeyCondition_naturalBase_to_baseScoreWindowTarget
      p x productUpdate productScore fixed thresholdLo thresholdHi
      hThreshold hCondition hFixed hBaseLowerNatural hBaseUpperNatural
  unfold VFH2.ProductRestrictedParamsRestrictedProofSpineFreeze.restrictedProofSpineTarget
  unfold VFH2.ProductRestrictedParamsPolicyEndToEndScoreWindow.restrictedParamsPolicyEndToEndScoreWindowTarget
  unfold VFH2.ProductRestrictedParamsScorePreservationDischarge.restrictedParamsScorePreservationDischargeTarget
  exact
    VFH2.ProductRestrictedParamsScorePreservingUpdate.restrictedParams_scorePreservingUpdate_baseWindow_to_baseAndUpdatedWindowTarget
      p x productUpdate productScore
      (VFH2.ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedUpdate p x productUpdate)
      (VFH2.ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedScore p x productUpdate productScore)
      fixed thresholdLo thresholdHi hThreshold
      hBaseTarget hScorePreserved

theorem restrictedParams_identityLikeUpdate_naturalBase_to_restrictedProofSpineTarget
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
  (hBaseLowerNatural : thresholdLo ≤ productScore x)
  (hBaseUpperNatural : productScore x ≤ thresholdHi) :
  VFH2.ProductRestrictedParamsRestrictedProofSpineFreeze.restrictedProofSpineTarget
    p x productUpdate productScore
    (VFH2.ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedUpdate p x productUpdate)
    (VFH2.ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedScore p x productUpdate productScore)
    fixed thresholdLo thresholdHi hThreshold := by
  have hPolicy :
    VFH2.ProductRestrictedParamsScorePreservationDischarge.restrictedParamsScorePreservingUpdatePolicy
      p productUpdate productScore :=
    VFH2.ProductRestrictedParamsScorePreservingPolicyInstantiation.restrictedParams_identityLikeUpdate_to_scorePreservingPolicy
      p productUpdate productScore hIdentityLike
  have hScorePreserved :
    productScore (productUpdate x) = productScore x :=
    hPolicy x
  have hBaseTarget :
    VFH2.ProductRestrictedParamsScoreWindow.restrictedParamsBaseScoreWindowTarget
      p x productUpdate productScore
      (VFH2.ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedUpdate p x productUpdate)
      (VFH2.ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedScore p x productUpdate productScore)
      fixed thresholdLo thresholdHi hThreshold :=
    restrictedParams_identityLikeUpdate_naturalBase_to_baseScoreWindowTarget
      p x productUpdate productScore fixed thresholdLo thresholdHi
      hThreshold hIdentityLike hFixed hBaseLowerNatural hBaseUpperNatural
  unfold VFH2.ProductRestrictedParamsRestrictedProofSpineFreeze.restrictedProofSpineTarget
  unfold VFH2.ProductRestrictedParamsPolicyEndToEndScoreWindow.restrictedParamsPolicyEndToEndScoreWindowTarget
  unfold VFH2.ProductRestrictedParamsScorePreservationDischarge.restrictedParamsScorePreservationDischargeTarget
  exact
    VFH2.ProductRestrictedParamsScorePreservingUpdate.restrictedParams_scorePreservingUpdate_baseWindow_to_baseAndUpdatedWindowTarget
      p x productUpdate productScore
      (VFH2.ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedUpdate p x productUpdate)
      (VFH2.ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedScore p x productUpdate productScore)
      fixed thresholdLo thresholdHi hThreshold
      hBaseTarget hScorePreserved


end ProductRestrictedParamsFullNaturalProofSpine
end VFH2
