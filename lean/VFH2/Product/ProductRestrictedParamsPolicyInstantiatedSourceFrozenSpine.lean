import VFH2.Product.ProductRestrictedParamsSourceCertificateFrozenSpine
import VFH2.Product.ProductRestrictedParamsScorePreservingPolicyInstantiation

namespace VFH2
namespace ProductRestrictedParamsPolicyInstantiatedSourceFrozenSpine

/--
v16.5.0:
The score-key-preserving update condition instantiates the abstract
score-preserving update policy needed by the v16.4 source-to-frozen-spine bridge.
-/
theorem restrictedParams_scoreKeyCondition_source_to_restrictedProofSpineTarget
  (p : VFH2.ProductRestrictedParams)
  (x : p.State)
  (productUpdate : p.State → p.State)
  (productScore : p.State → Int)
  (typedUpdate :
    VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsUpdateScoreTransportCarrier
      p x productUpdate →
    VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsUpdateScoreTransportCarrier
      p x productUpdate)
  (typedScore :
    VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsUpdateScoreTransportCarrier
      p x productUpdate →
    Int)
  (fixed : Prop)
  (baseEffect thresholdLo thresholdHi : Int)
  (hThreshold : thresholdLo ≤ thresholdHi)
  (hEffectBase : baseEffect = productScore x)
  (hCondition :
    VFH2.ProductRestrictedParamsScorePreservingPolicyInstantiation.restrictedParamsScoreKeyPreservingUpdateCondition
      p productUpdate productScore)
  (hSource :
    VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsRawUpdateScoreTransportSource
      p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi) :
  VFH2.ProductRestrictedParamsRestrictedProofSpineFreeze.restrictedProofSpineTarget
    p x productUpdate productScore typedUpdate typedScore fixed thresholdLo thresholdHi hThreshold := by
  exact
    VFH2.ProductRestrictedParamsSourceCertificateFrozenSpine.restrictedParams_rawUpdateScoreTransportSource_to_restrictedProofSpineTarget_noExtraBridge
      p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi hThreshold
      hEffectBase
      (VFH2.ProductRestrictedParamsScorePreservingPolicyInstantiation.restrictedParams_scoreKeyPreservingUpdateCondition_to_scorePreservingPolicy
        p productUpdate productScore hCondition)
      hSource

/--
v16.5.0:
Score-key-preserving update condition route to frozen updated score-window bounds.
-/
theorem restrictedParams_scoreKeyCondition_source_to_updatedBounds
  (p : VFH2.ProductRestrictedParams)
  (x : p.State)
  (productUpdate : p.State → p.State)
  (productScore : p.State → Int)
  (typedUpdate :
    VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsUpdateScoreTransportCarrier
      p x productUpdate →
    VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsUpdateScoreTransportCarrier
      p x productUpdate)
  (typedScore :
    VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsUpdateScoreTransportCarrier
      p x productUpdate →
    Int)
  (fixed : Prop)
  (baseEffect thresholdLo thresholdHi : Int)
  (hThreshold : thresholdLo ≤ thresholdHi)
  (hEffectBase : baseEffect = productScore x)
  (hCondition :
    VFH2.ProductRestrictedParamsScorePreservingPolicyInstantiation.restrictedParamsScoreKeyPreservingUpdateCondition
      p productUpdate productScore)
  (hSource :
    VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsRawUpdateScoreTransportSource
      p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi) :
  VFH2.ProductRestrictedParamsRestrictedProofSpineFreeze.restrictedProofSpineUpdatedScoreWindowBounds
    p x productUpdate productScore fixed thresholdLo thresholdHi := by
  exact
    VFH2.ProductRestrictedParamsSourceCertificateFrozenSpine.restrictedParams_rawUpdateScoreTransportSource_to_updatedBounds_noExtraBridge
      p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi hThreshold
      hEffectBase
      (VFH2.ProductRestrictedParamsScorePreservingPolicyInstantiation.restrictedParams_scoreKeyPreservingUpdateCondition_to_scorePreservingPolicy
        p productUpdate productScore hCondition)
      hSource

/--
v16.5.0:
Score-key-preserving update condition route to the lower updated score-window side.
-/
theorem restrictedParams_scoreKeyCondition_source_to_updatedLower
  (p : VFH2.ProductRestrictedParams)
  (x : p.State)
  (productUpdate : p.State → p.State)
  (productScore : p.State → Int)
  (typedUpdate :
    VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsUpdateScoreTransportCarrier
      p x productUpdate →
    VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsUpdateScoreTransportCarrier
      p x productUpdate)
  (typedScore :
    VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsUpdateScoreTransportCarrier
      p x productUpdate →
    Int)
  (fixed : Prop)
  (baseEffect thresholdLo thresholdHi : Int)
  (hThreshold : thresholdLo ≤ thresholdHi)
  (hEffectBase : baseEffect = productScore x)
  (hCondition :
    VFH2.ProductRestrictedParamsScorePreservingPolicyInstantiation.restrictedParamsScoreKeyPreservingUpdateCondition
      p productUpdate productScore)
  (hSource :
    VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsRawUpdateScoreTransportSource
      p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi) :
  VFH2.ProductBridgeGeneralization.genericBridgeTarget fixed
    (thresholdLo ≤ productScore (productUpdate x)) := by
  exact
    VFH2.ProductRestrictedParamsSourceCertificateFrozenSpine.restrictedParams_rawUpdateScoreTransportSource_to_updatedLower_noExtraBridge
      p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi hThreshold
      hEffectBase
      (VFH2.ProductRestrictedParamsScorePreservingPolicyInstantiation.restrictedParams_scoreKeyPreservingUpdateCondition_to_scorePreservingPolicy
        p productUpdate productScore hCondition)
      hSource

/--
v16.5.0:
Score-key-preserving update condition route to the upper updated score-window side.
-/
theorem restrictedParams_scoreKeyCondition_source_to_updatedUpper
  (p : VFH2.ProductRestrictedParams)
  (x : p.State)
  (productUpdate : p.State → p.State)
  (productScore : p.State → Int)
  (typedUpdate :
    VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsUpdateScoreTransportCarrier
      p x productUpdate →
    VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsUpdateScoreTransportCarrier
      p x productUpdate)
  (typedScore :
    VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsUpdateScoreTransportCarrier
      p x productUpdate →
    Int)
  (fixed : Prop)
  (baseEffect thresholdLo thresholdHi : Int)
  (hThreshold : thresholdLo ≤ thresholdHi)
  (hEffectBase : baseEffect = productScore x)
  (hCondition :
    VFH2.ProductRestrictedParamsScorePreservingPolicyInstantiation.restrictedParamsScoreKeyPreservingUpdateCondition
      p productUpdate productScore)
  (hSource :
    VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsRawUpdateScoreTransportSource
      p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi) :
  VFH2.ProductBridgeGeneralization.genericBridgeTarget fixed
    (productScore (productUpdate x) ≤ thresholdHi) := by
  exact
    VFH2.ProductRestrictedParamsSourceCertificateFrozenSpine.restrictedParams_rawUpdateScoreTransportSource_to_updatedUpper_noExtraBridge
      p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi hThreshold
      hEffectBase
      (VFH2.ProductRestrictedParamsScorePreservingPolicyInstantiation.restrictedParams_scoreKeyPreservingUpdateCondition_to_scorePreservingPolicy
        p productUpdate productScore hCondition)
      hSource

/--
v16.5.0:
The identity-like update condition instantiates the abstract score-preserving
update policy needed by the v16.4 source-to-frozen-spine bridge.
-/
theorem restrictedParams_identityLikeUpdate_source_to_restrictedProofSpineTarget
  (p : VFH2.ProductRestrictedParams)
  (x : p.State)
  (productUpdate : p.State → p.State)
  (productScore : p.State → Int)
  (typedUpdate :
    VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsUpdateScoreTransportCarrier
      p x productUpdate →
    VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsUpdateScoreTransportCarrier
      p x productUpdate)
  (typedScore :
    VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsUpdateScoreTransportCarrier
      p x productUpdate →
    Int)
  (fixed : Prop)
  (baseEffect thresholdLo thresholdHi : Int)
  (hThreshold : thresholdLo ≤ thresholdHi)
  (hEffectBase : baseEffect = productScore x)
  (hIdentityLike :
    VFH2.ProductRestrictedParamsScorePreservingPolicyInstantiation.restrictedParamsIdentityLikeUpdate
      p productUpdate)
  (hSource :
    VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsRawUpdateScoreTransportSource
      p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi) :
  VFH2.ProductRestrictedParamsRestrictedProofSpineFreeze.restrictedProofSpineTarget
    p x productUpdate productScore typedUpdate typedScore fixed thresholdLo thresholdHi hThreshold := by
  exact
    VFH2.ProductRestrictedParamsSourceCertificateFrozenSpine.restrictedParams_rawUpdateScoreTransportSource_to_restrictedProofSpineTarget_noExtraBridge
      p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi hThreshold
      hEffectBase
      (VFH2.ProductRestrictedParamsScorePreservingPolicyInstantiation.restrictedParams_identityLikeUpdate_to_scorePreservingPolicy
        p productUpdate productScore hIdentityLike)
      hSource

/--
v16.5.0:
Identity-like update route to frozen updated score-window bounds.
-/
theorem restrictedParams_identityLikeUpdate_source_to_updatedBounds
  (p : VFH2.ProductRestrictedParams)
  (x : p.State)
  (productUpdate : p.State → p.State)
  (productScore : p.State → Int)
  (typedUpdate :
    VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsUpdateScoreTransportCarrier
      p x productUpdate →
    VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsUpdateScoreTransportCarrier
      p x productUpdate)
  (typedScore :
    VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsUpdateScoreTransportCarrier
      p x productUpdate →
    Int)
  (fixed : Prop)
  (baseEffect thresholdLo thresholdHi : Int)
  (hThreshold : thresholdLo ≤ thresholdHi)
  (hEffectBase : baseEffect = productScore x)
  (hIdentityLike :
    VFH2.ProductRestrictedParamsScorePreservingPolicyInstantiation.restrictedParamsIdentityLikeUpdate
      p productUpdate)
  (hSource :
    VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsRawUpdateScoreTransportSource
      p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi) :
  VFH2.ProductRestrictedParamsRestrictedProofSpineFreeze.restrictedProofSpineUpdatedScoreWindowBounds
    p x productUpdate productScore fixed thresholdLo thresholdHi := by
  exact
    VFH2.ProductRestrictedParamsSourceCertificateFrozenSpine.restrictedParams_rawUpdateScoreTransportSource_to_updatedBounds_noExtraBridge
      p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi hThreshold
      hEffectBase
      (VFH2.ProductRestrictedParamsScorePreservingPolicyInstantiation.restrictedParams_identityLikeUpdate_to_scorePreservingPolicy
        p productUpdate productScore hIdentityLike)
      hSource

/--
v16.5.0:
Identity-like update route to the lower updated score-window side.
-/
theorem restrictedParams_identityLikeUpdate_source_to_updatedLower
  (p : VFH2.ProductRestrictedParams)
  (x : p.State)
  (productUpdate : p.State → p.State)
  (productScore : p.State → Int)
  (typedUpdate :
    VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsUpdateScoreTransportCarrier
      p x productUpdate →
    VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsUpdateScoreTransportCarrier
      p x productUpdate)
  (typedScore :
    VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsUpdateScoreTransportCarrier
      p x productUpdate →
    Int)
  (fixed : Prop)
  (baseEffect thresholdLo thresholdHi : Int)
  (hThreshold : thresholdLo ≤ thresholdHi)
  (hEffectBase : baseEffect = productScore x)
  (hIdentityLike :
    VFH2.ProductRestrictedParamsScorePreservingPolicyInstantiation.restrictedParamsIdentityLikeUpdate
      p productUpdate)
  (hSource :
    VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsRawUpdateScoreTransportSource
      p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi) :
  VFH2.ProductBridgeGeneralization.genericBridgeTarget fixed
    (thresholdLo ≤ productScore (productUpdate x)) := by
  exact
    VFH2.ProductRestrictedParamsSourceCertificateFrozenSpine.restrictedParams_rawUpdateScoreTransportSource_to_updatedLower_noExtraBridge
      p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi hThreshold
      hEffectBase
      (VFH2.ProductRestrictedParamsScorePreservingPolicyInstantiation.restrictedParams_identityLikeUpdate_to_scorePreservingPolicy
        p productUpdate productScore hIdentityLike)
      hSource

/--
v16.5.0:
Identity-like update route to the upper updated score-window side.
-/
theorem restrictedParams_identityLikeUpdate_source_to_updatedUpper
  (p : VFH2.ProductRestrictedParams)
  (x : p.State)
  (productUpdate : p.State → p.State)
  (productScore : p.State → Int)
  (typedUpdate :
    VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsUpdateScoreTransportCarrier
      p x productUpdate →
    VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsUpdateScoreTransportCarrier
      p x productUpdate)
  (typedScore :
    VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsUpdateScoreTransportCarrier
      p x productUpdate →
    Int)
  (fixed : Prop)
  (baseEffect thresholdLo thresholdHi : Int)
  (hThreshold : thresholdLo ≤ thresholdHi)
  (hEffectBase : baseEffect = productScore x)
  (hIdentityLike :
    VFH2.ProductRestrictedParamsScorePreservingPolicyInstantiation.restrictedParamsIdentityLikeUpdate
      p productUpdate)
  (hSource :
    VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsRawUpdateScoreTransportSource
      p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi) :
  VFH2.ProductBridgeGeneralization.genericBridgeTarget fixed
    (productScore (productUpdate x) ≤ thresholdHi) := by
  exact
    VFH2.ProductRestrictedParamsSourceCertificateFrozenSpine.restrictedParams_rawUpdateScoreTransportSource_to_updatedUpper_noExtraBridge
      p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi hThreshold
      hEffectBase
      (VFH2.ProductRestrictedParamsScorePreservingPolicyInstantiation.restrictedParams_identityLikeUpdate_to_scorePreservingPolicy
        p productUpdate productScore hIdentityLike)
      hSource

end ProductRestrictedParamsPolicyInstantiatedSourceFrozenSpine
end VFH2
