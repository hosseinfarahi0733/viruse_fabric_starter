import VFH2.Product.ProductRestrictedParamsPolicyInstantiatedSourceFrozenSpine

namespace VFH2
namespace ProductRestrictedParamsEffectBaseSourceFrozenSpine

/--
v16.6.0 source packaging:
The remaining base-effect equality is not derived here. It is bundled with the
restricted raw update-score transport source so downstream theorem surfaces do
not repeat it as a separate parameter.
-/
def restrictedParamsEffectBaseSource
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
  (baseEffect thresholdLo thresholdHi : Int) : Prop :=
  baseEffect = productScore x ∧
    VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsRawUpdateScoreTransportSource
      p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi

/--
v16.6.0:
Score-key-preserving route from the packaged effect-base source to the frozen
restricted proof spine target.
-/
theorem restrictedParams_scoreKeyCondition_effectBaseSource_to_restrictedProofSpineTarget
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
  (hCondition :
    VFH2.ProductRestrictedParamsScorePreservingPolicyInstantiation.restrictedParamsScoreKeyPreservingUpdateCondition
      p productUpdate productScore)
  (hEffectSource :
    restrictedParamsEffectBaseSource
      p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi) :
  VFH2.ProductRestrictedParamsRestrictedProofSpineFreeze.restrictedProofSpineTarget
    p x productUpdate productScore typedUpdate typedScore fixed thresholdLo thresholdHi hThreshold := by
  exact
    VFH2.ProductRestrictedParamsPolicyInstantiatedSourceFrozenSpine.restrictedParams_scoreKeyCondition_source_to_restrictedProofSpineTarget
      p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi hThreshold
      hEffectSource.1
      hCondition
      hEffectSource.2

/--
v16.6.0:
Score-key-preserving route from the packaged effect-base source to updated bounds.
-/
theorem restrictedParams_scoreKeyCondition_effectBaseSource_to_updatedBounds
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
  (hCondition :
    VFH2.ProductRestrictedParamsScorePreservingPolicyInstantiation.restrictedParamsScoreKeyPreservingUpdateCondition
      p productUpdate productScore)
  (hEffectSource :
    restrictedParamsEffectBaseSource
      p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi) :
  VFH2.ProductRestrictedParamsRestrictedProofSpineFreeze.restrictedProofSpineUpdatedScoreWindowBounds
    p x productUpdate productScore fixed thresholdLo thresholdHi := by
  exact
    VFH2.ProductRestrictedParamsPolicyInstantiatedSourceFrozenSpine.restrictedParams_scoreKeyCondition_source_to_updatedBounds
      p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi hThreshold
      hEffectSource.1
      hCondition
      hEffectSource.2

/--
v16.6.0:
Score-key-preserving route from the packaged effect-base source to the lower
updated score-window side.
-/
theorem restrictedParams_scoreKeyCondition_effectBaseSource_to_updatedLower
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
  (hCondition :
    VFH2.ProductRestrictedParamsScorePreservingPolicyInstantiation.restrictedParamsScoreKeyPreservingUpdateCondition
      p productUpdate productScore)
  (hEffectSource :
    restrictedParamsEffectBaseSource
      p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi) :
  VFH2.ProductBridgeGeneralization.genericBridgeTarget fixed
    (thresholdLo ≤ productScore (productUpdate x)) := by
  exact
    VFH2.ProductRestrictedParamsPolicyInstantiatedSourceFrozenSpine.restrictedParams_scoreKeyCondition_source_to_updatedLower
      p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi hThreshold
      hEffectSource.1
      hCondition
      hEffectSource.2

/--
v16.6.0:
Score-key-preserving route from the packaged effect-base source to the upper
updated score-window side.
-/
theorem restrictedParams_scoreKeyCondition_effectBaseSource_to_updatedUpper
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
  (hCondition :
    VFH2.ProductRestrictedParamsScorePreservingPolicyInstantiation.restrictedParamsScoreKeyPreservingUpdateCondition
      p productUpdate productScore)
  (hEffectSource :
    restrictedParamsEffectBaseSource
      p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi) :
  VFH2.ProductBridgeGeneralization.genericBridgeTarget fixed
    (productScore (productUpdate x) ≤ thresholdHi) := by
  exact
    VFH2.ProductRestrictedParamsPolicyInstantiatedSourceFrozenSpine.restrictedParams_scoreKeyCondition_source_to_updatedUpper
      p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi hThreshold
      hEffectSource.1
      hCondition
      hEffectSource.2

/--
v16.6.0:
Identity-like route from the packaged effect-base source to the frozen restricted
proof spine target.
-/
theorem restrictedParams_identityLikeUpdate_effectBaseSource_to_restrictedProofSpineTarget
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
  (hIdentityLike :
    VFH2.ProductRestrictedParamsScorePreservingPolicyInstantiation.restrictedParamsIdentityLikeUpdate
      p productUpdate)
  (hEffectSource :
    restrictedParamsEffectBaseSource
      p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi) :
  VFH2.ProductRestrictedParamsRestrictedProofSpineFreeze.restrictedProofSpineTarget
    p x productUpdate productScore typedUpdate typedScore fixed thresholdLo thresholdHi hThreshold := by
  exact
    VFH2.ProductRestrictedParamsPolicyInstantiatedSourceFrozenSpine.restrictedParams_identityLikeUpdate_source_to_restrictedProofSpineTarget
      p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi hThreshold
      hEffectSource.1
      hIdentityLike
      hEffectSource.2

/--
v16.6.0:
Identity-like route from the packaged effect-base source to updated bounds.
-/
theorem restrictedParams_identityLikeUpdate_effectBaseSource_to_updatedBounds
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
  (hIdentityLike :
    VFH2.ProductRestrictedParamsScorePreservingPolicyInstantiation.restrictedParamsIdentityLikeUpdate
      p productUpdate)
  (hEffectSource :
    restrictedParamsEffectBaseSource
      p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi) :
  VFH2.ProductRestrictedParamsRestrictedProofSpineFreeze.restrictedProofSpineUpdatedScoreWindowBounds
    p x productUpdate productScore fixed thresholdLo thresholdHi := by
  exact
    VFH2.ProductRestrictedParamsPolicyInstantiatedSourceFrozenSpine.restrictedParams_identityLikeUpdate_source_to_updatedBounds
      p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi hThreshold
      hEffectSource.1
      hIdentityLike
      hEffectSource.2

/--
v16.6.0:
Identity-like route from the packaged effect-base source to the lower updated
score-window side.
-/
theorem restrictedParams_identityLikeUpdate_effectBaseSource_to_updatedLower
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
  (hIdentityLike :
    VFH2.ProductRestrictedParamsScorePreservingPolicyInstantiation.restrictedParamsIdentityLikeUpdate
      p productUpdate)
  (hEffectSource :
    restrictedParamsEffectBaseSource
      p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi) :
  VFH2.ProductBridgeGeneralization.genericBridgeTarget fixed
    (thresholdLo ≤ productScore (productUpdate x)) := by
  exact
    VFH2.ProductRestrictedParamsPolicyInstantiatedSourceFrozenSpine.restrictedParams_identityLikeUpdate_source_to_updatedLower
      p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi hThreshold
      hEffectSource.1
      hIdentityLike
      hEffectSource.2

/--
v16.6.0:
Identity-like route from the packaged effect-base source to the upper updated
score-window side.
-/
theorem restrictedParams_identityLikeUpdate_effectBaseSource_to_updatedUpper
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
  (hIdentityLike :
    VFH2.ProductRestrictedParamsScorePreservingPolicyInstantiation.restrictedParamsIdentityLikeUpdate
      p productUpdate)
  (hEffectSource :
    restrictedParamsEffectBaseSource
      p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi) :
  VFH2.ProductBridgeGeneralization.genericBridgeTarget fixed
    (productScore (productUpdate x) ≤ thresholdHi) := by
  exact
    VFH2.ProductRestrictedParamsPolicyInstantiatedSourceFrozenSpine.restrictedParams_identityLikeUpdate_source_to_updatedUpper
      p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi hThreshold
      hEffectSource.1
      hIdentityLike
      hEffectSource.2

end ProductRestrictedParamsEffectBaseSourceFrozenSpine
end VFH2
