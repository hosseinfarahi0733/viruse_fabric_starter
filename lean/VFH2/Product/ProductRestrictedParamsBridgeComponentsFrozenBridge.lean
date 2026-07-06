import VFH2.Product.ProductRestrictedParamsConcretePolicyEndToEndFrozenBridge

namespace VFH2
namespace ProductRestrictedParamsBridgeComponentsFrozenBridge

/--
v17.0.0:
Build the lower bridge-side target from explicit components.

This reduces the v16.9 bridge-side assumption
`genericBridgeTarget fixed (thresholdHi ≤ baseEffect)` to the two explicit
components `fixed` and `thresholdHi ≤ baseEffect`.
-/
theorem genericBridgeTarget_of_fixed_and_lower
  (fixed : Prop)
  (baseEffect thresholdHi : Int)
  (hFixed : fixed)
  (hLower : thresholdHi ≤ baseEffect) :
  VFH2.ProductBridgeGeneralization.genericBridgeTarget fixed (thresholdHi ≤ baseEffect) := by
  exact ⟨hFixed, hLower⟩

/--
v17.0.0:
Build the upper bridge-side target from explicit components.

This reduces the v16.9 bridge-side assumption
`genericBridgeTarget fixed (baseEffect ≤ thresholdLo)` to the two explicit
components `fixed` and `baseEffect ≤ thresholdLo`.
-/
theorem genericBridgeTarget_of_fixed_and_upper
  (fixed : Prop)
  (baseEffect thresholdLo : Int)
  (hFixed : fixed)
  (hUpper : baseEffect ≤ thresholdLo) :
  VFH2.ProductBridgeGeneralization.genericBridgeTarget fixed (baseEffect ≤ thresholdLo) := by
  exact ⟨hFixed, hUpper⟩

/--
v17.0.0:
Score-key concrete-policy route to the frozen restricted proof-spine target,
with bridge-side assumptions replaced by explicit `fixed` and inequality
components.
-/
theorem restrictedParams_scoreKeyCondition_components_to_restrictedProofSpineTarget
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
    typedUpdate
      ⟨VFH2.ProductStateTransport.productToTyped x, Or.inl rfl⟩ =
    ⟨VFH2.ProductStateTransport.productToTyped (productUpdate x), Or.inr rfl⟩)
  (hBaseScore :
    typedScore
      ⟨VFH2.ProductStateTransport.productToTyped x, Or.inl rfl⟩ = productScore x)
  (hUpdatedScore :
    typedScore
      ⟨VFH2.ProductStateTransport.productToTyped (productUpdate x), Or.inr rfl⟩ =
    productScore (productUpdate x))
  (hFixed : fixed)
  (hBaseLower : thresholdHi ≤ baseEffect)
  (hBaseUpper : baseEffect ≤ thresholdLo) :
  VFH2.ProductRestrictedParamsRestrictedProofSpineFreeze.restrictedProofSpineTarget
    p x productUpdate productScore typedUpdate typedScore fixed thresholdLo thresholdHi hThreshold := by
  exact
    VFH2.ProductRestrictedParamsConcretePolicyEndToEndFrozenBridge.restrictedParams_scoreKeyCondition_rawEqualities_to_restrictedProofSpineTarget
      p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi hThreshold
      hEffectBase hCondition hTypedUpdate hBaseScore hUpdatedScore
      (genericBridgeTarget_of_fixed_and_lower fixed baseEffect thresholdHi hFixed hBaseLower)
      (genericBridgeTarget_of_fixed_and_upper fixed baseEffect thresholdLo hFixed hBaseUpper)

/--
v17.0.0:
Score-key concrete-policy route to frozen updated bounds, with bridge-side
assumptions replaced by explicit `fixed` and inequality components.
-/
theorem restrictedParams_scoreKeyCondition_components_to_frozenUpdatedBounds
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
    typedUpdate
      ⟨VFH2.ProductStateTransport.productToTyped x, Or.inl rfl⟩ =
    ⟨VFH2.ProductStateTransport.productToTyped (productUpdate x), Or.inr rfl⟩)
  (hBaseScore :
    typedScore
      ⟨VFH2.ProductStateTransport.productToTyped x, Or.inl rfl⟩ = productScore x)
  (hUpdatedScore :
    typedScore
      ⟨VFH2.ProductStateTransport.productToTyped (productUpdate x), Or.inr rfl⟩ =
    productScore (productUpdate x))
  (hFixed : fixed)
  (hBaseLower : thresholdHi ≤ baseEffect)
  (hBaseUpper : baseEffect ≤ thresholdLo) :
  VFH2.ProductRestrictedParamsRestrictedProofSpineFreeze.restrictedProofSpineUpdatedScoreWindowBounds
    p x productUpdate productScore fixed thresholdLo thresholdHi := by
  exact
    VFH2.ProductRestrictedParamsConcretePolicyEndToEndFrozenBridge.restrictedParams_scoreKeyCondition_rawEqualities_to_frozenUpdatedBounds
      p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi hThreshold
      hEffectBase hCondition hTypedUpdate hBaseScore hUpdatedScore
      (genericBridgeTarget_of_fixed_and_lower fixed baseEffect thresholdHi hFixed hBaseLower)
      (genericBridgeTarget_of_fixed_and_upper fixed baseEffect thresholdLo hFixed hBaseUpper)

/--
v17.0.0:
Score-key lower side, projected from the repaired bounds theorem instead of a
nonexistent v16.9 lower theorem.
-/
theorem restrictedParams_scoreKeyCondition_components_to_frozenUpdatedLower
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
    typedUpdate
      ⟨VFH2.ProductStateTransport.productToTyped x, Or.inl rfl⟩ =
    ⟨VFH2.ProductStateTransport.productToTyped (productUpdate x), Or.inr rfl⟩)
  (hBaseScore :
    typedScore
      ⟨VFH2.ProductStateTransport.productToTyped x, Or.inl rfl⟩ = productScore x)
  (hUpdatedScore :
    typedScore
      ⟨VFH2.ProductStateTransport.productToTyped (productUpdate x), Or.inr rfl⟩ =
    productScore (productUpdate x))
  (hFixed : fixed)
  (hBaseLower : thresholdHi ≤ baseEffect)
  (hBaseUpper : baseEffect ≤ thresholdLo) :
  VFH2.ProductBridgeGeneralization.genericBridgeTarget fixed
    (thresholdLo ≤ productScore (productUpdate x)) := by
  exact
    (restrictedParams_scoreKeyCondition_components_to_frozenUpdatedBounds
      p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi hThreshold
      hEffectBase hCondition hTypedUpdate hBaseScore hUpdatedScore hFixed hBaseLower hBaseUpper).1

/--
v17.0.0:
Score-key upper side, projected from the repaired bounds theorem instead of a
nonexistent v16.9 upper theorem.
-/
theorem restrictedParams_scoreKeyCondition_components_to_frozenUpdatedUpper
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
    typedUpdate
      ⟨VFH2.ProductStateTransport.productToTyped x, Or.inl rfl⟩ =
    ⟨VFH2.ProductStateTransport.productToTyped (productUpdate x), Or.inr rfl⟩)
  (hBaseScore :
    typedScore
      ⟨VFH2.ProductStateTransport.productToTyped x, Or.inl rfl⟩ = productScore x)
  (hUpdatedScore :
    typedScore
      ⟨VFH2.ProductStateTransport.productToTyped (productUpdate x), Or.inr rfl⟩ =
    productScore (productUpdate x))
  (hFixed : fixed)
  (hBaseLower : thresholdHi ≤ baseEffect)
  (hBaseUpper : baseEffect ≤ thresholdLo) :
  VFH2.ProductBridgeGeneralization.genericBridgeTarget fixed
    (productScore (productUpdate x) ≤ thresholdHi) := by
  exact
    (restrictedParams_scoreKeyCondition_components_to_frozenUpdatedBounds
      p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi hThreshold
      hEffectBase hCondition hTypedUpdate hBaseScore hUpdatedScore hFixed hBaseLower hBaseUpper).2

/--
v17.0.0:
Identity-like concrete-policy route to the frozen restricted proof-spine target,
with bridge-side assumptions replaced by explicit `fixed` and inequality
components.
-/
theorem restrictedParams_identityLikeUpdate_components_to_restrictedProofSpineTarget
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
    typedUpdate
      ⟨VFH2.ProductStateTransport.productToTyped x, Or.inl rfl⟩ =
    ⟨VFH2.ProductStateTransport.productToTyped (productUpdate x), Or.inr rfl⟩)
  (hBaseScore :
    typedScore
      ⟨VFH2.ProductStateTransport.productToTyped x, Or.inl rfl⟩ = productScore x)
  (hUpdatedScore :
    typedScore
      ⟨VFH2.ProductStateTransport.productToTyped (productUpdate x), Or.inr rfl⟩ =
    productScore (productUpdate x))
  (hFixed : fixed)
  (hBaseLower : thresholdHi ≤ baseEffect)
  (hBaseUpper : baseEffect ≤ thresholdLo) :
  VFH2.ProductRestrictedParamsRestrictedProofSpineFreeze.restrictedProofSpineTarget
    p x productUpdate productScore typedUpdate typedScore fixed thresholdLo thresholdHi hThreshold := by
  exact
    VFH2.ProductRestrictedParamsConcretePolicyEndToEndFrozenBridge.restrictedParams_identityLikeUpdate_rawEqualities_to_restrictedProofSpineTarget
      p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi hThreshold
      hEffectBase hIdentityLike hTypedUpdate hBaseScore hUpdatedScore
      (genericBridgeTarget_of_fixed_and_lower fixed baseEffect thresholdHi hFixed hBaseLower)
      (genericBridgeTarget_of_fixed_and_upper fixed baseEffect thresholdLo hFixed hBaseUpper)

/--
v17.0.0:
Identity-like concrete-policy route to frozen updated bounds, with bridge-side
assumptions replaced by explicit components.
-/
theorem restrictedParams_identityLikeUpdate_components_to_frozenUpdatedBounds
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
    typedUpdate
      ⟨VFH2.ProductStateTransport.productToTyped x, Or.inl rfl⟩ =
    ⟨VFH2.ProductStateTransport.productToTyped (productUpdate x), Or.inr rfl⟩)
  (hBaseScore :
    typedScore
      ⟨VFH2.ProductStateTransport.productToTyped x, Or.inl rfl⟩ = productScore x)
  (hUpdatedScore :
    typedScore
      ⟨VFH2.ProductStateTransport.productToTyped (productUpdate x), Or.inr rfl⟩ =
    productScore (productUpdate x))
  (hFixed : fixed)
  (hBaseLower : thresholdHi ≤ baseEffect)
  (hBaseUpper : baseEffect ≤ thresholdLo) :
  VFH2.ProductRestrictedParamsRestrictedProofSpineFreeze.restrictedProofSpineUpdatedScoreWindowBounds
    p x productUpdate productScore fixed thresholdLo thresholdHi := by
  exact
    VFH2.ProductRestrictedParamsConcretePolicyEndToEndFrozenBridge.restrictedParams_identityLikeUpdate_rawEqualities_to_frozenUpdatedBounds
      p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi hThreshold
      hEffectBase hIdentityLike hTypedUpdate hBaseScore hUpdatedScore
      (genericBridgeTarget_of_fixed_and_lower fixed baseEffect thresholdHi hFixed hBaseLower)
      (genericBridgeTarget_of_fixed_and_upper fixed baseEffect thresholdLo hFixed hBaseUpper)

/--
v17.0.0:
Identity-like lower side, projected from the repaired bounds theorem instead of
a nonexistent v16.9 lower theorem.
-/
theorem restrictedParams_identityLikeUpdate_components_to_frozenUpdatedLower
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
    typedUpdate
      ⟨VFH2.ProductStateTransport.productToTyped x, Or.inl rfl⟩ =
    ⟨VFH2.ProductStateTransport.productToTyped (productUpdate x), Or.inr rfl⟩)
  (hBaseScore :
    typedScore
      ⟨VFH2.ProductStateTransport.productToTyped x, Or.inl rfl⟩ = productScore x)
  (hUpdatedScore :
    typedScore
      ⟨VFH2.ProductStateTransport.productToTyped (productUpdate x), Or.inr rfl⟩ =
    productScore (productUpdate x))
  (hFixed : fixed)
  (hBaseLower : thresholdHi ≤ baseEffect)
  (hBaseUpper : baseEffect ≤ thresholdLo) :
  VFH2.ProductBridgeGeneralization.genericBridgeTarget fixed
    (thresholdLo ≤ productScore (productUpdate x)) := by
  exact
    (restrictedParams_identityLikeUpdate_components_to_frozenUpdatedBounds
      p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi hThreshold
      hEffectBase hIdentityLike hTypedUpdate hBaseScore hUpdatedScore hFixed hBaseLower hBaseUpper).1

/--
v17.0.0:
Identity-like upper side, projected from the repaired bounds theorem instead of
a nonexistent v16.9 upper theorem.
-/
theorem restrictedParams_identityLikeUpdate_components_to_frozenUpdatedUpper
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
    typedUpdate
      ⟨VFH2.ProductStateTransport.productToTyped x, Or.inl rfl⟩ =
    ⟨VFH2.ProductStateTransport.productToTyped (productUpdate x), Or.inr rfl⟩)
  (hBaseScore :
    typedScore
      ⟨VFH2.ProductStateTransport.productToTyped x, Or.inl rfl⟩ = productScore x)
  (hUpdatedScore :
    typedScore
      ⟨VFH2.ProductStateTransport.productToTyped (productUpdate x), Or.inr rfl⟩ =
    productScore (productUpdate x))
  (hFixed : fixed)
  (hBaseLower : thresholdHi ≤ baseEffect)
  (hBaseUpper : baseEffect ≤ thresholdLo) :
  VFH2.ProductBridgeGeneralization.genericBridgeTarget fixed
    (productScore (productUpdate x) ≤ thresholdHi) := by
  exact
    (restrictedParams_identityLikeUpdate_components_to_frozenUpdatedBounds
      p x productUpdate productScore typedUpdate typedScore fixed baseEffect thresholdLo thresholdHi hThreshold
      hEffectBase hIdentityLike hTypedUpdate hBaseScore hUpdatedScore hFixed hBaseLower hBaseUpper).2

end ProductRestrictedParamsBridgeComponentsFrozenBridge
end VFH2
