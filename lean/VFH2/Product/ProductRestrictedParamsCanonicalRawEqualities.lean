import VFH2.Product.ProductRestrictedParamsBridgeComponentsFrozenBridge
import VFH2.Product.ProductRestrictedParamsScorePreservingPolicyInstantiation
import VFH2.Product.ProductRestrictedParamsScorePreservationDischarge

namespace VFH2
namespace ProductRestrictedParamsCanonicalRawEqualities

/--
v17.1.0:
Canonical restricted typed update on the two-point restricted carrier.

It sends every allowed carrier state to the updated carrier.

This is deliberately simple: the goal is not to encode the whole update semantics
inside the carrier function, but to discharge the raw update equality required by
the frozen restricted proof-spine route.
-/
def canonicalRestrictedTypedUpdate
  (p : VFH2.ProductRestrictedParams)
  (x : p.State)
  (productUpdate : p.State → p.State) :
  VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsUpdateScoreTransportCarrier
      p x productUpdate →
    VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsUpdateScoreTransportCarrier
      p x productUpdate :=
  fun _ => ⟨VFH2.ProductStateTransport.productToTyped (productUpdate x), Or.inr rfl⟩

/--
v17.1.0:
Canonical restricted typed score on the two-point restricted carrier.

It is constant at the base product score. The updated-score raw equality is then
discharged from the score-preserving policy:

`productScore (productUpdate x) = productScore x`.

This avoids illegal elimination from the proof-valued carrier witness into `Int`.
-/
def canonicalRestrictedTypedScore
  (p : VFH2.ProductRestrictedParams)
  (x : p.State)
  (productUpdate : p.State → p.State)
  (productScore : p.State → Int) :
  VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsUpdateScoreTransportCarrier
      p x productUpdate →
    Int :=
  fun _ => productScore x

/--
The canonical update discharges the raw typed-update equality.
-/
theorem canonicalRestrictedTypedUpdate_base_to_updated
  (p : VFH2.ProductRestrictedParams)
  (x : p.State)
  (productUpdate : p.State → p.State) :
  canonicalRestrictedTypedUpdate p x productUpdate
      ⟨VFH2.ProductStateTransport.productToTyped x, Or.inl rfl⟩ =
    ⟨VFH2.ProductStateTransport.productToTyped (productUpdate x), Or.inr rfl⟩ := by
  rfl

/--
The canonical typed score discharges the base score equality by computation.
-/
theorem canonicalRestrictedTypedScore_base
  (p : VFH2.ProductRestrictedParams)
  (x : p.State)
  (productUpdate : p.State → p.State)
  (productScore : p.State → Int) :
  canonicalRestrictedTypedScore p x productUpdate productScore
      ⟨VFH2.ProductStateTransport.productToTyped x, Or.inl rfl⟩ =
    productScore x := by
  rfl

/--
The canonical typed score discharges the updated score equality using the
score-preserving update policy.
-/
theorem canonicalRestrictedTypedScore_updated_of_policy
  (p : VFH2.ProductRestrictedParams)
  (x : p.State)
  (productUpdate : p.State → p.State)
  (productScore : p.State → Int)
  (hPolicy :
    VFH2.ProductRestrictedParamsScorePreservationDischarge.restrictedParamsScorePreservingUpdatePolicy
      p productUpdate productScore) :
  canonicalRestrictedTypedScore p x productUpdate productScore
      ⟨VFH2.ProductStateTransport.productToTyped (productUpdate x), Or.inr rfl⟩ =
    productScore (productUpdate x) := by
  exact (hPolicy x).symm

/--
Score-key concrete-policy route to the frozen restricted proof-spine target,
with the three raw typed equalities discharged by the canonical typed update and
canonical typed score.

Remaining assumptions are explicit and real:
`hEffectBase`, `hFixed`, the two base bridge inequalities, and the concrete
score-key condition.
-/
theorem restrictedParams_scoreKeyCondition_canonicalRaw_to_restrictedProofSpineTarget
  (p : VFH2.ProductRestrictedParams)
  (x : p.State)
  (productUpdate : p.State → p.State)
  (productScore : p.State → Int)
  (fixed : Prop)
  (baseEffect thresholdLo thresholdHi : Int)
  (hThreshold : thresholdLo ≤ thresholdHi)
  (hEffectBase : baseEffect = productScore x)
  (hCondition :
    VFH2.ProductRestrictedParamsScorePreservingPolicyInstantiation.restrictedParamsScoreKeyPreservingUpdateCondition
      p productUpdate productScore)
  (hFixed : fixed)
  (hBaseLower : thresholdHi ≤ baseEffect)
  (hBaseUpper : baseEffect ≤ thresholdLo) :
  VFH2.ProductRestrictedParamsRestrictedProofSpineFreeze.restrictedProofSpineTarget
    p x productUpdate productScore
    (canonicalRestrictedTypedUpdate p x productUpdate)
    (canonicalRestrictedTypedScore p x productUpdate productScore)
    fixed thresholdLo thresholdHi hThreshold := by
  have hPolicy :
    VFH2.ProductRestrictedParamsScorePreservationDischarge.restrictedParamsScorePreservingUpdatePolicy
      p productUpdate productScore :=
    VFH2.ProductRestrictedParamsScorePreservingPolicyInstantiation.restrictedParams_scoreKeyPreservingUpdateCondition_to_scorePreservingPolicy
      p productUpdate productScore hCondition
  exact
    VFH2.ProductRestrictedParamsBridgeComponentsFrozenBridge.restrictedParams_scoreKeyCondition_components_to_restrictedProofSpineTarget
      p x productUpdate productScore
      (canonicalRestrictedTypedUpdate p x productUpdate)
      (canonicalRestrictedTypedScore p x productUpdate productScore)
      fixed baseEffect thresholdLo thresholdHi hThreshold
      hEffectBase hCondition
      (canonicalRestrictedTypedUpdate_base_to_updated p x productUpdate)
      (canonicalRestrictedTypedScore_base p x productUpdate productScore)
      (canonicalRestrictedTypedScore_updated_of_policy p x productUpdate productScore hPolicy)
      hFixed hBaseLower hBaseUpper

/--
Score-key concrete-policy route to frozen updated bounds, with canonical raw
typed equalities.
-/
theorem restrictedParams_scoreKeyCondition_canonicalRaw_to_frozenUpdatedBounds
  (p : VFH2.ProductRestrictedParams)
  (x : p.State)
  (productUpdate : p.State → p.State)
  (productScore : p.State → Int)
  (fixed : Prop)
  (baseEffect thresholdLo thresholdHi : Int)
  (hThreshold : thresholdLo ≤ thresholdHi)
  (hEffectBase : baseEffect = productScore x)
  (hCondition :
    VFH2.ProductRestrictedParamsScorePreservingPolicyInstantiation.restrictedParamsScoreKeyPreservingUpdateCondition
      p productUpdate productScore)
  (hFixed : fixed)
  (hBaseLower : thresholdHi ≤ baseEffect)
  (hBaseUpper : baseEffect ≤ thresholdLo) :
  VFH2.ProductRestrictedParamsRestrictedProofSpineFreeze.restrictedProofSpineUpdatedScoreWindowBounds
    p x productUpdate productScore fixed thresholdLo thresholdHi := by
  have hPolicy :
    VFH2.ProductRestrictedParamsScorePreservationDischarge.restrictedParamsScorePreservingUpdatePolicy
      p productUpdate productScore :=
    VFH2.ProductRestrictedParamsScorePreservingPolicyInstantiation.restrictedParams_scoreKeyPreservingUpdateCondition_to_scorePreservingPolicy
      p productUpdate productScore hCondition
  exact
    VFH2.ProductRestrictedParamsBridgeComponentsFrozenBridge.restrictedParams_scoreKeyCondition_components_to_frozenUpdatedBounds
      p x productUpdate productScore
      (canonicalRestrictedTypedUpdate p x productUpdate)
      (canonicalRestrictedTypedScore p x productUpdate productScore)
      fixed baseEffect thresholdLo thresholdHi hThreshold
      hEffectBase hCondition
      (canonicalRestrictedTypedUpdate_base_to_updated p x productUpdate)
      (canonicalRestrictedTypedScore_base p x productUpdate productScore)
      (canonicalRestrictedTypedScore_updated_of_policy p x productUpdate productScore hPolicy)
      hFixed hBaseLower hBaseUpper

/--
Score-key lower side projected from the canonical raw updated-bounds theorem.
-/
theorem restrictedParams_scoreKeyCondition_canonicalRaw_to_frozenUpdatedLower
  (p : VFH2.ProductRestrictedParams)
  (x : p.State)
  (productUpdate : p.State → p.State)
  (productScore : p.State → Int)
  (fixed : Prop)
  (baseEffect thresholdLo thresholdHi : Int)
  (hThreshold : thresholdLo ≤ thresholdHi)
  (hEffectBase : baseEffect = productScore x)
  (hCondition :
    VFH2.ProductRestrictedParamsScorePreservingPolicyInstantiation.restrictedParamsScoreKeyPreservingUpdateCondition
      p productUpdate productScore)
  (hFixed : fixed)
  (hBaseLower : thresholdHi ≤ baseEffect)
  (hBaseUpper : baseEffect ≤ thresholdLo) :
  VFH2.ProductBridgeGeneralization.genericBridgeTarget fixed
    (thresholdLo ≤ productScore (productUpdate x)) := by
  exact
    (restrictedParams_scoreKeyCondition_canonicalRaw_to_frozenUpdatedBounds
      p x productUpdate productScore fixed baseEffect thresholdLo thresholdHi hThreshold
      hEffectBase hCondition hFixed hBaseLower hBaseUpper).1

/--
Score-key upper side projected from the canonical raw updated-bounds theorem.
-/
theorem restrictedParams_scoreKeyCondition_canonicalRaw_to_frozenUpdatedUpper
  (p : VFH2.ProductRestrictedParams)
  (x : p.State)
  (productUpdate : p.State → p.State)
  (productScore : p.State → Int)
  (fixed : Prop)
  (baseEffect thresholdLo thresholdHi : Int)
  (hThreshold : thresholdLo ≤ thresholdHi)
  (hEffectBase : baseEffect = productScore x)
  (hCondition :
    VFH2.ProductRestrictedParamsScorePreservingPolicyInstantiation.restrictedParamsScoreKeyPreservingUpdateCondition
      p productUpdate productScore)
  (hFixed : fixed)
  (hBaseLower : thresholdHi ≤ baseEffect)
  (hBaseUpper : baseEffect ≤ thresholdLo) :
  VFH2.ProductBridgeGeneralization.genericBridgeTarget fixed
    (productScore (productUpdate x) ≤ thresholdHi) := by
  exact
    (restrictedParams_scoreKeyCondition_canonicalRaw_to_frozenUpdatedBounds
      p x productUpdate productScore fixed baseEffect thresholdLo thresholdHi hThreshold
      hEffectBase hCondition hFixed hBaseLower hBaseUpper).2

/--
Identity-like concrete-policy route to the frozen restricted proof-spine target,
with the three raw typed equalities discharged by the canonical typed update and
canonical typed score.
-/
theorem restrictedParams_identityLikeUpdate_canonicalRaw_to_restrictedProofSpineTarget
  (p : VFH2.ProductRestrictedParams)
  (x : p.State)
  (productUpdate : p.State → p.State)
  (productScore : p.State → Int)
  (fixed : Prop)
  (baseEffect thresholdLo thresholdHi : Int)
  (hThreshold : thresholdLo ≤ thresholdHi)
  (hEffectBase : baseEffect = productScore x)
  (hIdentityLike :
    VFH2.ProductRestrictedParamsScorePreservingPolicyInstantiation.restrictedParamsIdentityLikeUpdate
      p productUpdate)
  (hFixed : fixed)
  (hBaseLower : thresholdHi ≤ baseEffect)
  (hBaseUpper : baseEffect ≤ thresholdLo) :
  VFH2.ProductRestrictedParamsRestrictedProofSpineFreeze.restrictedProofSpineTarget
    p x productUpdate productScore
    (canonicalRestrictedTypedUpdate p x productUpdate)
    (canonicalRestrictedTypedScore p x productUpdate productScore)
    fixed thresholdLo thresholdHi hThreshold := by
  have hPolicy :
    VFH2.ProductRestrictedParamsScorePreservationDischarge.restrictedParamsScorePreservingUpdatePolicy
      p productUpdate productScore :=
    VFH2.ProductRestrictedParamsScorePreservingPolicyInstantiation.restrictedParams_identityLikeUpdate_to_scorePreservingPolicy
      p productUpdate productScore hIdentityLike
  exact
    VFH2.ProductRestrictedParamsBridgeComponentsFrozenBridge.restrictedParams_identityLikeUpdate_components_to_restrictedProofSpineTarget
      p x productUpdate productScore
      (canonicalRestrictedTypedUpdate p x productUpdate)
      (canonicalRestrictedTypedScore p x productUpdate productScore)
      fixed baseEffect thresholdLo thresholdHi hThreshold
      hEffectBase hIdentityLike
      (canonicalRestrictedTypedUpdate_base_to_updated p x productUpdate)
      (canonicalRestrictedTypedScore_base p x productUpdate productScore)
      (canonicalRestrictedTypedScore_updated_of_policy p x productUpdate productScore hPolicy)
      hFixed hBaseLower hBaseUpper

/--
Identity-like concrete-policy route to frozen updated bounds, with canonical raw
typed equalities.
-/
theorem restrictedParams_identityLikeUpdate_canonicalRaw_to_frozenUpdatedBounds
  (p : VFH2.ProductRestrictedParams)
  (x : p.State)
  (productUpdate : p.State → p.State)
  (productScore : p.State → Int)
  (fixed : Prop)
  (baseEffect thresholdLo thresholdHi : Int)
  (hThreshold : thresholdLo ≤ thresholdHi)
  (hEffectBase : baseEffect = productScore x)
  (hIdentityLike :
    VFH2.ProductRestrictedParamsScorePreservingPolicyInstantiation.restrictedParamsIdentityLikeUpdate
      p productUpdate)
  (hFixed : fixed)
  (hBaseLower : thresholdHi ≤ baseEffect)
  (hBaseUpper : baseEffect ≤ thresholdLo) :
  VFH2.ProductRestrictedParamsRestrictedProofSpineFreeze.restrictedProofSpineUpdatedScoreWindowBounds
    p x productUpdate productScore fixed thresholdLo thresholdHi := by
  have hPolicy :
    VFH2.ProductRestrictedParamsScorePreservationDischarge.restrictedParamsScorePreservingUpdatePolicy
      p productUpdate productScore :=
    VFH2.ProductRestrictedParamsScorePreservingPolicyInstantiation.restrictedParams_identityLikeUpdate_to_scorePreservingPolicy
      p productUpdate productScore hIdentityLike
  exact
    VFH2.ProductRestrictedParamsBridgeComponentsFrozenBridge.restrictedParams_identityLikeUpdate_components_to_frozenUpdatedBounds
      p x productUpdate productScore
      (canonicalRestrictedTypedUpdate p x productUpdate)
      (canonicalRestrictedTypedScore p x productUpdate productScore)
      fixed baseEffect thresholdLo thresholdHi hThreshold
      hEffectBase hIdentityLike
      (canonicalRestrictedTypedUpdate_base_to_updated p x productUpdate)
      (canonicalRestrictedTypedScore_base p x productUpdate productScore)
      (canonicalRestrictedTypedScore_updated_of_policy p x productUpdate productScore hPolicy)
      hFixed hBaseLower hBaseUpper

/--
Identity-like lower side projected from the canonical raw updated-bounds theorem.
-/
theorem restrictedParams_identityLikeUpdate_canonicalRaw_to_frozenUpdatedLower
  (p : VFH2.ProductRestrictedParams)
  (x : p.State)
  (productUpdate : p.State → p.State)
  (productScore : p.State → Int)
  (fixed : Prop)
  (baseEffect thresholdLo thresholdHi : Int)
  (hThreshold : thresholdLo ≤ thresholdHi)
  (hEffectBase : baseEffect = productScore x)
  (hIdentityLike :
    VFH2.ProductRestrictedParamsScorePreservingPolicyInstantiation.restrictedParamsIdentityLikeUpdate
      p productUpdate)
  (hFixed : fixed)
  (hBaseLower : thresholdHi ≤ baseEffect)
  (hBaseUpper : baseEffect ≤ thresholdLo) :
  VFH2.ProductBridgeGeneralization.genericBridgeTarget fixed
    (thresholdLo ≤ productScore (productUpdate x)) := by
  exact
    (restrictedParams_identityLikeUpdate_canonicalRaw_to_frozenUpdatedBounds
      p x productUpdate productScore fixed baseEffect thresholdLo thresholdHi hThreshold
      hEffectBase hIdentityLike hFixed hBaseLower hBaseUpper).1

/--
Identity-like upper side projected from the canonical raw updated-bounds theorem.
-/
theorem restrictedParams_identityLikeUpdate_canonicalRaw_to_frozenUpdatedUpper
  (p : VFH2.ProductRestrictedParams)
  (x : p.State)
  (productUpdate : p.State → p.State)
  (productScore : p.State → Int)
  (fixed : Prop)
  (baseEffect thresholdLo thresholdHi : Int)
  (hThreshold : thresholdLo ≤ thresholdHi)
  (hEffectBase : baseEffect = productScore x)
  (hIdentityLike :
    VFH2.ProductRestrictedParamsScorePreservingPolicyInstantiation.restrictedParamsIdentityLikeUpdate
      p productUpdate)
  (hFixed : fixed)
  (hBaseLower : thresholdHi ≤ baseEffect)
  (hBaseUpper : baseEffect ≤ thresholdLo) :
  VFH2.ProductBridgeGeneralization.genericBridgeTarget fixed
    (productScore (productUpdate x) ≤ thresholdHi) := by
  exact
    (restrictedParams_identityLikeUpdate_canonicalRaw_to_frozenUpdatedBounds
      p x productUpdate productScore fixed baseEffect thresholdLo thresholdHi hThreshold
      hEffectBase hIdentityLike hFixed hBaseLower hBaseUpper).2

end ProductRestrictedParamsCanonicalRawEqualities
end VFH2
