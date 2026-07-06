import VFH2.Product.ProductRestrictedParamsPolicyEndToEndFrozenSpineBridge
import VFH2.Product.ProductRestrictedParamsScorePreservingPolicyInstantiation

namespace VFH2
namespace ProductRestrictedParamsConcretePolicyEndToEndFrozenBridge

/--
v16.9.0:
Construct the existing policy end-to-end score-window source from concrete
score-key-preserving policy-instantiation evidence plus the remaining raw
equality and bridge-side assumptions.
-/
theorem restrictedParams_scoreKeyCondition_rawEqualities_to_policyEndToEndSource
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
  (hEffectBase : baseEffect = productScore x)
  (hCondition :
    VFH2.ProductRestrictedParamsScorePreservingPolicyInstantiation.restrictedParamsScoreKeyPreservingUpdateCondition
      p productUpdate productScore)
  (hTypedUpdate :
    typedUpdate ⟨VFH2.ProductStateTransport.productToTyped x, Or.inl rfl⟩ =
    ⟨VFH2.ProductStateTransport.productToTyped (productUpdate x), Or.inr rfl⟩)
  (hBaseScore :
    typedScore ⟨VFH2.ProductStateTransport.productToTyped x, Or.inl rfl⟩ = productScore x)
  (hUpdatedScore :
    typedScore ⟨VFH2.ProductStateTransport.productToTyped (productUpdate x), Or.inr rfl⟩ =
    productScore (productUpdate x))
  (hBaseLowerBridgeStrong :
    VFH2.ProductBridgeGeneralization.genericBridgeTarget fixed (thresholdHi ≤ baseEffect))
  (hBaseUpperBridgeStrong :
    VFH2.ProductBridgeGeneralization.genericBridgeTarget fixed (baseEffect ≤ thresholdLo)) :
  VFH2.ProductRestrictedParamsPolicyEndToEndScoreWindow.restrictedParamsPolicyEndToEndScoreWindowSource
    p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi := by
  exact
    { hEffectBase := hEffectBase
      hPolicy :=
        VFH2.ProductRestrictedParamsScorePreservingPolicyInstantiation.restrictedParams_scoreKeyPreservingUpdateCondition_to_scorePreservingPolicy
          p productUpdate productScore hCondition
      hTypedUpdate := hTypedUpdate
      hBaseScore := hBaseScore
      hUpdatedScore := hUpdatedScore
      hBaseLowerBridgeStrong := hBaseLowerBridgeStrong
      hBaseUpperBridgeStrong := hBaseUpperBridgeStrong }

/--
v16.9.0:
Construct the existing policy end-to-end score-window source from concrete
identity-like policy-instantiation evidence plus the remaining raw equality and
bridge-side assumptions.
-/
theorem restrictedParams_identityLikeUpdate_rawEqualities_to_policyEndToEndSource
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
  (hEffectBase : baseEffect = productScore x)
  (hIdentityLike :
    VFH2.ProductRestrictedParamsScorePreservingPolicyInstantiation.restrictedParamsIdentityLikeUpdate
      p productUpdate)
  (hTypedUpdate :
    typedUpdate ⟨VFH2.ProductStateTransport.productToTyped x, Or.inl rfl⟩ =
    ⟨VFH2.ProductStateTransport.productToTyped (productUpdate x), Or.inr rfl⟩)
  (hBaseScore :
    typedScore ⟨VFH2.ProductStateTransport.productToTyped x, Or.inl rfl⟩ = productScore x)
  (hUpdatedScore :
    typedScore ⟨VFH2.ProductStateTransport.productToTyped (productUpdate x), Or.inr rfl⟩ =
    productScore (productUpdate x))
  (hBaseLowerBridgeStrong :
    VFH2.ProductBridgeGeneralization.genericBridgeTarget fixed (thresholdHi ≤ baseEffect))
  (hBaseUpperBridgeStrong :
    VFH2.ProductBridgeGeneralization.genericBridgeTarget fixed (baseEffect ≤ thresholdLo)) :
  VFH2.ProductRestrictedParamsPolicyEndToEndScoreWindow.restrictedParamsPolicyEndToEndScoreWindowSource
    p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi := by
  exact
    { hEffectBase := hEffectBase
      hPolicy :=
        VFH2.ProductRestrictedParamsScorePreservingPolicyInstantiation.restrictedParams_identityLikeUpdate_to_scorePreservingPolicy
          p productUpdate productScore hIdentityLike
      hTypedUpdate := hTypedUpdate
      hBaseScore := hBaseScore
      hUpdatedScore := hUpdatedScore
      hBaseLowerBridgeStrong := hBaseLowerBridgeStrong
      hBaseUpperBridgeStrong := hBaseUpperBridgeStrong }

/--
v16.9.0:
Score-key-preserving concrete policy route directly reaches the frozen restricted
proof-spine target through the existing policy end-to-end source.
-/
theorem restrictedParams_scoreKeyCondition_rawEqualities_to_restrictedProofSpineTarget
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
  (hTypedUpdate :
    typedUpdate ⟨VFH2.ProductStateTransport.productToTyped x, Or.inl rfl⟩ =
    ⟨VFH2.ProductStateTransport.productToTyped (productUpdate x), Or.inr rfl⟩)
  (hBaseScore :
    typedScore ⟨VFH2.ProductStateTransport.productToTyped x, Or.inl rfl⟩ = productScore x)
  (hUpdatedScore :
    typedScore ⟨VFH2.ProductStateTransport.productToTyped (productUpdate x), Or.inr rfl⟩ =
    productScore (productUpdate x))
  (hBaseLowerBridgeStrong :
    VFH2.ProductBridgeGeneralization.genericBridgeTarget fixed (thresholdHi ≤ baseEffect))
  (hBaseUpperBridgeStrong :
    VFH2.ProductBridgeGeneralization.genericBridgeTarget fixed (baseEffect ≤ thresholdLo)) :
  VFH2.ProductRestrictedParamsRestrictedProofSpineFreeze.restrictedProofSpineTarget
    p x productUpdate productScore typedUpdate typedScore fixed thresholdLo thresholdHi hThreshold := by
  exact
    VFH2.ProductRestrictedParamsPolicyEndToEndFrozenSpineBridge.restrictedParams_policyEndToEndSource_to_restrictedProofSpineTarget
      p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi hThreshold
      (restrictedParams_scoreKeyCondition_rawEqualities_to_policyEndToEndSource
        p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi
        hEffectBase hCondition hTypedUpdate hBaseScore hUpdatedScore
        hBaseLowerBridgeStrong hBaseUpperBridgeStrong)

/--
v16.9.0:
Score-key-preserving concrete policy route directly reaches frozen updated bounds.
-/
theorem restrictedParams_scoreKeyCondition_rawEqualities_to_frozenUpdatedBounds
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
  (hTypedUpdate :
    typedUpdate ⟨VFH2.ProductStateTransport.productToTyped x, Or.inl rfl⟩ =
    ⟨VFH2.ProductStateTransport.productToTyped (productUpdate x), Or.inr rfl⟩)
  (hBaseScore :
    typedScore ⟨VFH2.ProductStateTransport.productToTyped x, Or.inl rfl⟩ = productScore x)
  (hUpdatedScore :
    typedScore ⟨VFH2.ProductStateTransport.productToTyped (productUpdate x), Or.inr rfl⟩ =
    productScore (productUpdate x))
  (hBaseLowerBridgeStrong :
    VFH2.ProductBridgeGeneralization.genericBridgeTarget fixed (thresholdHi ≤ baseEffect))
  (hBaseUpperBridgeStrong :
    VFH2.ProductBridgeGeneralization.genericBridgeTarget fixed (baseEffect ≤ thresholdLo)) :
  VFH2.ProductRestrictedParamsRestrictedProofSpineFreeze.restrictedProofSpineUpdatedScoreWindowBounds
    p x productUpdate productScore fixed thresholdLo thresholdHi := by
  exact
    VFH2.ProductRestrictedParamsPolicyEndToEndFrozenSpineBridge.restrictedParams_policyEndToEndSource_to_frozenUpdatedBounds
      p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi hThreshold
      (restrictedParams_scoreKeyCondition_rawEqualities_to_policyEndToEndSource
        p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi
        hEffectBase hCondition hTypedUpdate hBaseScore hUpdatedScore
        hBaseLowerBridgeStrong hBaseUpperBridgeStrong)

/--
v16.9.0:
Identity-like concrete policy route directly reaches the frozen restricted proof-spine target.
-/
theorem restrictedParams_identityLikeUpdate_rawEqualities_to_restrictedProofSpineTarget
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
  (hTypedUpdate :
    typedUpdate ⟨VFH2.ProductStateTransport.productToTyped x, Or.inl rfl⟩ =
    ⟨VFH2.ProductStateTransport.productToTyped (productUpdate x), Or.inr rfl⟩)
  (hBaseScore :
    typedScore ⟨VFH2.ProductStateTransport.productToTyped x, Or.inl rfl⟩ = productScore x)
  (hUpdatedScore :
    typedScore ⟨VFH2.ProductStateTransport.productToTyped (productUpdate x), Or.inr rfl⟩ =
    productScore (productUpdate x))
  (hBaseLowerBridgeStrong :
    VFH2.ProductBridgeGeneralization.genericBridgeTarget fixed (thresholdHi ≤ baseEffect))
  (hBaseUpperBridgeStrong :
    VFH2.ProductBridgeGeneralization.genericBridgeTarget fixed (baseEffect ≤ thresholdLo)) :
  VFH2.ProductRestrictedParamsRestrictedProofSpineFreeze.restrictedProofSpineTarget
    p x productUpdate productScore typedUpdate typedScore fixed thresholdLo thresholdHi hThreshold := by
  exact
    VFH2.ProductRestrictedParamsPolicyEndToEndFrozenSpineBridge.restrictedParams_policyEndToEndSource_to_restrictedProofSpineTarget
      p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi hThreshold
      (restrictedParams_identityLikeUpdate_rawEqualities_to_policyEndToEndSource
        p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi
        hEffectBase hIdentityLike hTypedUpdate hBaseScore hUpdatedScore
        hBaseLowerBridgeStrong hBaseUpperBridgeStrong)

/--
v16.9.0:
Identity-like concrete policy route directly reaches frozen updated bounds.
-/
theorem restrictedParams_identityLikeUpdate_rawEqualities_to_frozenUpdatedBounds
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
  (hTypedUpdate :
    typedUpdate ⟨VFH2.ProductStateTransport.productToTyped x, Or.inl rfl⟩ =
    ⟨VFH2.ProductStateTransport.productToTyped (productUpdate x), Or.inr rfl⟩)
  (hBaseScore :
    typedScore ⟨VFH2.ProductStateTransport.productToTyped x, Or.inl rfl⟩ = productScore x)
  (hUpdatedScore :
    typedScore ⟨VFH2.ProductStateTransport.productToTyped (productUpdate x), Or.inr rfl⟩ =
    productScore (productUpdate x))
  (hBaseLowerBridgeStrong :
    VFH2.ProductBridgeGeneralization.genericBridgeTarget fixed (thresholdHi ≤ baseEffect))
  (hBaseUpperBridgeStrong :
    VFH2.ProductBridgeGeneralization.genericBridgeTarget fixed (baseEffect ≤ thresholdLo)) :
  VFH2.ProductRestrictedParamsRestrictedProofSpineFreeze.restrictedProofSpineUpdatedScoreWindowBounds
    p x productUpdate productScore fixed thresholdLo thresholdHi := by
  exact
    VFH2.ProductRestrictedParamsPolicyEndToEndFrozenSpineBridge.restrictedParams_policyEndToEndSource_to_frozenUpdatedBounds
      p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi hThreshold
      (restrictedParams_identityLikeUpdate_rawEqualities_to_policyEndToEndSource
        p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi
        hEffectBase hIdentityLike hTypedUpdate hBaseScore hUpdatedScore
        hBaseLowerBridgeStrong hBaseUpperBridgeStrong)

end ProductRestrictedParamsConcretePolicyEndToEndFrozenBridge
end VFH2
