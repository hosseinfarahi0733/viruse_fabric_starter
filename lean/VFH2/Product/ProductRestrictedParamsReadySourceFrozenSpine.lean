import VFH2.Product.ProductRestrictedParamsEffectBaseSourceFrozenSpine

namespace VFH2
namespace ProductRestrictedParamsReadySourceFrozenSpine

/--
v16.7.0 ready source:
Bundles the effect-base source with the score-key-preserving policy-instantiation
condition. This is packaging, not derivation.
-/
def restrictedParamsScoreKeyReadySource
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
  VFH2.ProductRestrictedParamsEffectBaseSourceFrozenSpine.restrictedParamsEffectBaseSource
    p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi ∧
  VFH2.ProductRestrictedParamsScorePreservingPolicyInstantiation.restrictedParamsScoreKeyPreservingUpdateCondition
    p productUpdate productScore

/--
v16.7.0 ready source:
Bundles the effect-base source with the identity-like policy-instantiation
condition. This is packaging, not derivation.
-/
def restrictedParamsIdentityLikeReadySource
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
  VFH2.ProductRestrictedParamsEffectBaseSourceFrozenSpine.restrictedParamsEffectBaseSource
    p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi ∧
  VFH2.ProductRestrictedParamsScorePreservingPolicyInstantiation.restrictedParamsIdentityLikeUpdate
    p productUpdate

/--
v16.7.0:
Score-key ready source route to the frozen restricted proof spine target.
-/
theorem restrictedParams_scoreKeyReadySource_to_restrictedProofSpineTarget
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
  (hReady :
    restrictedParamsScoreKeyReadySource
      p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi) :
  VFH2.ProductRestrictedParamsRestrictedProofSpineFreeze.restrictedProofSpineTarget
    p x productUpdate productScore typedUpdate typedScore fixed thresholdLo thresholdHi hThreshold := by
  exact
    VFH2.ProductRestrictedParamsEffectBaseSourceFrozenSpine.restrictedParams_scoreKeyCondition_effectBaseSource_to_restrictedProofSpineTarget
      p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi hThreshold
      hReady.2
      hReady.1

/--
v16.7.0:
Score-key ready source route to frozen updated score-window bounds.
-/
theorem restrictedParams_scoreKeyReadySource_to_updatedBounds
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
  (hReady :
    restrictedParamsScoreKeyReadySource
      p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi) :
  VFH2.ProductRestrictedParamsRestrictedProofSpineFreeze.restrictedProofSpineUpdatedScoreWindowBounds
    p x productUpdate productScore fixed thresholdLo thresholdHi := by
  exact
    VFH2.ProductRestrictedParamsEffectBaseSourceFrozenSpine.restrictedParams_scoreKeyCondition_effectBaseSource_to_updatedBounds
      p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi hThreshold
      hReady.2
      hReady.1

/--
v16.7.0:
Score-key ready source route to the lower updated score-window side.
-/
theorem restrictedParams_scoreKeyReadySource_to_updatedLower
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
  (hReady :
    restrictedParamsScoreKeyReadySource
      p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi) :
  VFH2.ProductBridgeGeneralization.genericBridgeTarget fixed
    (thresholdLo ≤ productScore (productUpdate x)) := by
  exact
    VFH2.ProductRestrictedParamsEffectBaseSourceFrozenSpine.restrictedParams_scoreKeyCondition_effectBaseSource_to_updatedLower
      p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi hThreshold
      hReady.2
      hReady.1

/--
v16.7.0:
Score-key ready source route to the upper updated score-window side.
-/
theorem restrictedParams_scoreKeyReadySource_to_updatedUpper
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
  (hReady :
    restrictedParamsScoreKeyReadySource
      p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi) :
  VFH2.ProductBridgeGeneralization.genericBridgeTarget fixed
    (productScore (productUpdate x) ≤ thresholdHi) := by
  exact
    VFH2.ProductRestrictedParamsEffectBaseSourceFrozenSpine.restrictedParams_scoreKeyCondition_effectBaseSource_to_updatedUpper
      p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi hThreshold
      hReady.2
      hReady.1

/--
v16.7.0:
Identity-like ready source route to the frozen restricted proof spine target.
-/
theorem restrictedParams_identityLikeReadySource_to_restrictedProofSpineTarget
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
  (hReady :
    restrictedParamsIdentityLikeReadySource
      p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi) :
  VFH2.ProductRestrictedParamsRestrictedProofSpineFreeze.restrictedProofSpineTarget
    p x productUpdate productScore typedUpdate typedScore fixed thresholdLo thresholdHi hThreshold := by
  exact
    VFH2.ProductRestrictedParamsEffectBaseSourceFrozenSpine.restrictedParams_identityLikeUpdate_effectBaseSource_to_restrictedProofSpineTarget
      p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi hThreshold
      hReady.2
      hReady.1

/--
v16.7.0:
Identity-like ready source route to frozen updated score-window bounds.
-/
theorem restrictedParams_identityLikeReadySource_to_updatedBounds
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
  (hReady :
    restrictedParamsIdentityLikeReadySource
      p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi) :
  VFH2.ProductRestrictedParamsRestrictedProofSpineFreeze.restrictedProofSpineUpdatedScoreWindowBounds
    p x productUpdate productScore fixed thresholdLo thresholdHi := by
  exact
    VFH2.ProductRestrictedParamsEffectBaseSourceFrozenSpine.restrictedParams_identityLikeUpdate_effectBaseSource_to_updatedBounds
      p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi hThreshold
      hReady.2
      hReady.1

/--
v16.7.0:
Identity-like ready source route to the lower updated score-window side.
-/
theorem restrictedParams_identityLikeReadySource_to_updatedLower
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
  (hReady :
    restrictedParamsIdentityLikeReadySource
      p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi) :
  VFH2.ProductBridgeGeneralization.genericBridgeTarget fixed
    (thresholdLo ≤ productScore (productUpdate x)) := by
  exact
    VFH2.ProductRestrictedParamsEffectBaseSourceFrozenSpine.restrictedParams_identityLikeUpdate_effectBaseSource_to_updatedLower
      p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi hThreshold
      hReady.2
      hReady.1

/--
v16.7.0:
Identity-like ready source route to the upper updated score-window side.
-/
theorem restrictedParams_identityLikeReadySource_to_updatedUpper
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
  (hReady :
    restrictedParamsIdentityLikeReadySource
      p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi) :
  VFH2.ProductBridgeGeneralization.genericBridgeTarget fixed
    (productScore (productUpdate x) ≤ thresholdHi) := by
  exact
    VFH2.ProductRestrictedParamsEffectBaseSourceFrozenSpine.restrictedParams_identityLikeUpdate_effectBaseSource_to_updatedUpper
      p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi hThreshold
      hReady.2
      hReady.1

end ProductRestrictedParamsReadySourceFrozenSpine
end VFH2
