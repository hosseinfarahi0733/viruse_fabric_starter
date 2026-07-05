import VFH2.Product.ProductRestrictedParamsRestrictedProofSpineFreeze

namespace VFH2

namespace ProductRestrictedParamsScorePreservingPolicyInstantiation

def restrictedParamsIdentityLikeUpdate
    (p : VFH2.ProductRestrictedParams)
    (productUpdate : p.State → p.State) : Prop :=
  ∀ y : p.State, productUpdate y = y

def restrictedParamsScoreKeyPreservingUpdateCondition
    (p : VFH2.ProductRestrictedParams)
    (productUpdate : p.State → p.State)
    (productScore : p.State → Int) : Prop :=
  ∃ (ScoreKey : Type)
    (scoreKey : p.State → ScoreKey)
    (scoreOfKey : ScoreKey → Int),
      (∀ y : p.State, productScore y = scoreOfKey (scoreKey y)) ∧
      (∀ y : p.State, scoreKey (productUpdate y) = scoreKey y)

theorem restrictedParams_identityLikeUpdate_to_scorePreservingPolicy
    (p : VFH2.ProductRestrictedParams)
    (productUpdate : p.State → p.State)
    (productScore : p.State → Int)
    (hIdentityLike :
      restrictedParamsIdentityLikeUpdate p productUpdate) :
    VFH2.ProductRestrictedParamsScorePreservationDischarge.restrictedParamsScorePreservingUpdatePolicy
      p productUpdate productScore := by
  intro y
  unfold restrictedParamsIdentityLikeUpdate at hIdentityLike
  rw [hIdentityLike y]

theorem restrictedParams_scoreKeyPreservingUpdateCondition_to_scorePreservingPolicy
    (p : VFH2.ProductRestrictedParams)
    (productUpdate : p.State → p.State)
    (productScore : p.State → Int)
    (hCondition :
      restrictedParamsScoreKeyPreservingUpdateCondition
        p productUpdate productScore) :
    VFH2.ProductRestrictedParamsScorePreservationDischarge.restrictedParamsScorePreservingUpdatePolicy
      p productUpdate productScore := by
  intro y
  unfold restrictedParamsScoreKeyPreservingUpdateCondition at hCondition
  rcases hCondition with ⟨ScoreKey, scoreKey, scoreOfKey, hScoreFactors, hKeyPreserved⟩
  rw [hScoreFactors (productUpdate y), hScoreFactors y, hKeyPreserved y]

theorem restrictedParams_identityLikeUpdate_to_policyPoint
    (p : VFH2.ProductRestrictedParams)
    (x : p.State)
    (productUpdate : p.State → p.State)
    (productScore : p.State → Int)
    (hIdentityLike :
      restrictedParamsIdentityLikeUpdate p productUpdate) :
    productScore (productUpdate x) = productScore x := by
  exact
    VFH2.ProductRestrictedParamsScorePreservationDischarge.restrictedParams_scorePreservingUpdatePolicy_to_point
      p x productUpdate productScore
      (restrictedParams_identityLikeUpdate_to_scorePreservingPolicy
        p productUpdate productScore hIdentityLike)

theorem restrictedParams_scoreKeyCondition_to_policyPoint
    (p : VFH2.ProductRestrictedParams)
    (x : p.State)
    (productUpdate : p.State → p.State)
    (productScore : p.State → Int)
    (hCondition :
      restrictedParamsScoreKeyPreservingUpdateCondition
        p productUpdate productScore) :
    productScore (productUpdate x) = productScore x := by
  exact
    VFH2.ProductRestrictedParamsScorePreservationDischarge.restrictedParams_scorePreservingUpdatePolicy_to_point
      p x productUpdate productScore
      (restrictedParams_scoreKeyPreservingUpdateCondition_to_scorePreservingPolicy
        p productUpdate productScore hCondition)

theorem restrictedProofSpine_rawEqualities_and_identityLikeUpdate_to_target
    (p : VFH2.ProductRestrictedParams)
    (x : p.State)
    (productUpdate : p.State → p.State)
    (productScore : p.State → Int)
    (typedUpdate :
      VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsUpdateScoreTransportCarrier p x productUpdate →
        VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsUpdateScoreTransportCarrier p x productUpdate)
    (typedScore :
      VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsUpdateScoreTransportCarrier p x productUpdate → Int)
    (fixed : Prop)
    (baseEffect thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi)
    (hEffectBase : baseEffect = productScore x)
    (hIdentityLike :
      restrictedParamsIdentityLikeUpdate p productUpdate)
    (hTypedUpdate :
      typedUpdate ⟨VFH2.ProductStateTransport.productToTyped x, Or.inl rfl⟩ =
        ⟨VFH2.ProductStateTransport.productToTyped (productUpdate x), Or.inr rfl⟩)
    (hBaseScore :
      typedScore ⟨VFH2.ProductStateTransport.productToTyped x, Or.inl rfl⟩ =
        productScore x)
    (hUpdatedScore :
      typedScore ⟨VFH2.ProductStateTransport.productToTyped (productUpdate x), Or.inr rfl⟩ =
        productScore (productUpdate x))
    (hBaseLowerBridgeStrong :
      ProductBridgeGeneralization.genericBridgeTarget fixed
        (thresholdHi ≤ baseEffect))
    (hBaseUpperBridgeStrong :
      ProductBridgeGeneralization.genericBridgeTarget fixed
        (baseEffect ≤ thresholdLo)) :
    VFH2.ProductRestrictedParamsRestrictedProofSpineFreeze.restrictedProofSpineTarget
      p x productUpdate productScore typedUpdate typedScore
      fixed thresholdLo thresholdHi hThreshold := by
  exact
    VFH2.ProductRestrictedParamsRestrictedProofSpineFreeze.restrictedProofSpine_rawEqualities_to_target
      p x productUpdate productScore typedUpdate typedScore
      fixed baseEffect thresholdLo thresholdHi hThreshold hEffectBase
      (restrictedParams_identityLikeUpdate_to_scorePreservingPolicy
        p productUpdate productScore hIdentityLike)
      hTypedUpdate hBaseScore hUpdatedScore
      hBaseLowerBridgeStrong hBaseUpperBridgeStrong

theorem restrictedProofSpine_rawEqualities_and_scoreKeyCondition_to_target
    (p : VFH2.ProductRestrictedParams)
    (x : p.State)
    (productUpdate : p.State → p.State)
    (productScore : p.State → Int)
    (typedUpdate :
      VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsUpdateScoreTransportCarrier p x productUpdate →
        VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsUpdateScoreTransportCarrier p x productUpdate)
    (typedScore :
      VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsUpdateScoreTransportCarrier p x productUpdate → Int)
    (fixed : Prop)
    (baseEffect thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi)
    (hEffectBase : baseEffect = productScore x)
    (hCondition :
      restrictedParamsScoreKeyPreservingUpdateCondition
        p productUpdate productScore)
    (hTypedUpdate :
      typedUpdate ⟨VFH2.ProductStateTransport.productToTyped x, Or.inl rfl⟩ =
        ⟨VFH2.ProductStateTransport.productToTyped (productUpdate x), Or.inr rfl⟩)
    (hBaseScore :
      typedScore ⟨VFH2.ProductStateTransport.productToTyped x, Or.inl rfl⟩ =
        productScore x)
    (hUpdatedScore :
      typedScore ⟨VFH2.ProductStateTransport.productToTyped (productUpdate x), Or.inr rfl⟩ =
        productScore (productUpdate x))
    (hBaseLowerBridgeStrong :
      ProductBridgeGeneralization.genericBridgeTarget fixed
        (thresholdHi ≤ baseEffect))
    (hBaseUpperBridgeStrong :
      ProductBridgeGeneralization.genericBridgeTarget fixed
        (baseEffect ≤ thresholdLo)) :
    VFH2.ProductRestrictedParamsRestrictedProofSpineFreeze.restrictedProofSpineTarget
      p x productUpdate productScore typedUpdate typedScore
      fixed thresholdLo thresholdHi hThreshold := by
  exact
    VFH2.ProductRestrictedParamsRestrictedProofSpineFreeze.restrictedProofSpine_rawEqualities_to_target
      p x productUpdate productScore typedUpdate typedScore
      fixed baseEffect thresholdLo thresholdHi hThreshold hEffectBase
      (restrictedParams_scoreKeyPreservingUpdateCondition_to_scorePreservingPolicy
        p productUpdate productScore hCondition)
      hTypedUpdate hBaseScore hUpdatedScore
      hBaseLowerBridgeStrong hBaseUpperBridgeStrong

theorem restrictedProofSpine_rawEqualities_and_identityLikeUpdate_to_updatedBounds
    (p : VFH2.ProductRestrictedParams)
    (x : p.State)
    (productUpdate : p.State → p.State)
    (productScore : p.State → Int)
    (typedUpdate :
      VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsUpdateScoreTransportCarrier p x productUpdate →
        VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsUpdateScoreTransportCarrier p x productUpdate)
    (typedScore :
      VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsUpdateScoreTransportCarrier p x productUpdate → Int)
    (fixed : Prop)
    (baseEffect thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi)
    (hEffectBase : baseEffect = productScore x)
    (hIdentityLike :
      restrictedParamsIdentityLikeUpdate p productUpdate)
    (hTypedUpdate :
      typedUpdate ⟨VFH2.ProductStateTransport.productToTyped x, Or.inl rfl⟩ =
        ⟨VFH2.ProductStateTransport.productToTyped (productUpdate x), Or.inr rfl⟩)
    (hBaseScore :
      typedScore ⟨VFH2.ProductStateTransport.productToTyped x, Or.inl rfl⟩ =
        productScore x)
    (hUpdatedScore :
      typedScore ⟨VFH2.ProductStateTransport.productToTyped (productUpdate x), Or.inr rfl⟩ =
        productScore (productUpdate x))
    (hBaseLowerBridgeStrong :
      ProductBridgeGeneralization.genericBridgeTarget fixed
        (thresholdHi ≤ baseEffect))
    (hBaseUpperBridgeStrong :
      ProductBridgeGeneralization.genericBridgeTarget fixed
        (baseEffect ≤ thresholdLo)) :
    VFH2.ProductRestrictedParamsRestrictedProofSpineFreeze.restrictedProofSpineUpdatedScoreWindowBounds
      p x productUpdate productScore fixed thresholdLo thresholdHi := by
  exact
    VFH2.ProductRestrictedParamsRestrictedProofSpineFreeze.restrictedProofSpine_rawEqualities_to_updatedBounds
      p x productUpdate productScore typedUpdate typedScore
      fixed baseEffect thresholdLo thresholdHi hThreshold hEffectBase
      (restrictedParams_identityLikeUpdate_to_scorePreservingPolicy
        p productUpdate productScore hIdentityLike)
      hTypedUpdate hBaseScore hUpdatedScore
      hBaseLowerBridgeStrong hBaseUpperBridgeStrong

theorem restrictedProofSpine_rawEqualities_and_scoreKeyCondition_to_updatedBounds
    (p : VFH2.ProductRestrictedParams)
    (x : p.State)
    (productUpdate : p.State → p.State)
    (productScore : p.State → Int)
    (typedUpdate :
      VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsUpdateScoreTransportCarrier p x productUpdate →
        VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsUpdateScoreTransportCarrier p x productUpdate)
    (typedScore :
      VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsUpdateScoreTransportCarrier p x productUpdate → Int)
    (fixed : Prop)
    (baseEffect thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi)
    (hEffectBase : baseEffect = productScore x)
    (hCondition :
      restrictedParamsScoreKeyPreservingUpdateCondition
        p productUpdate productScore)
    (hTypedUpdate :
      typedUpdate ⟨VFH2.ProductStateTransport.productToTyped x, Or.inl rfl⟩ =
        ⟨VFH2.ProductStateTransport.productToTyped (productUpdate x), Or.inr rfl⟩)
    (hBaseScore :
      typedScore ⟨VFH2.ProductStateTransport.productToTyped x, Or.inl rfl⟩ =
        productScore x)
    (hUpdatedScore :
      typedScore ⟨VFH2.ProductStateTransport.productToTyped (productUpdate x), Or.inr rfl⟩ =
        productScore (productUpdate x))
    (hBaseLowerBridgeStrong :
      ProductBridgeGeneralization.genericBridgeTarget fixed
        (thresholdHi ≤ baseEffect))
    (hBaseUpperBridgeStrong :
      ProductBridgeGeneralization.genericBridgeTarget fixed
        (baseEffect ≤ thresholdLo)) :
    VFH2.ProductRestrictedParamsRestrictedProofSpineFreeze.restrictedProofSpineUpdatedScoreWindowBounds
      p x productUpdate productScore fixed thresholdLo thresholdHi := by
  exact
    VFH2.ProductRestrictedParamsRestrictedProofSpineFreeze.restrictedProofSpine_rawEqualities_to_updatedBounds
      p x productUpdate productScore typedUpdate typedScore
      fixed baseEffect thresholdLo thresholdHi hThreshold hEffectBase
      (restrictedParams_scoreKeyPreservingUpdateCondition_to_scorePreservingPolicy
        p productUpdate productScore hCondition)
      hTypedUpdate hBaseScore hUpdatedScore
      hBaseLowerBridgeStrong hBaseUpperBridgeStrong

theorem restrictedProofSpine_rawEqualities_and_identityLikeUpdate_to_updatedLower
    (p : VFH2.ProductRestrictedParams)
    (x : p.State)
    (productUpdate : p.State → p.State)
    (productScore : p.State → Int)
    (typedUpdate :
      VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsUpdateScoreTransportCarrier p x productUpdate →
        VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsUpdateScoreTransportCarrier p x productUpdate)
    (typedScore :
      VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsUpdateScoreTransportCarrier p x productUpdate → Int)
    (fixed : Prop)
    (baseEffect thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi)
    (hEffectBase : baseEffect = productScore x)
    (hIdentityLike :
      restrictedParamsIdentityLikeUpdate p productUpdate)
    (hTypedUpdate :
      typedUpdate ⟨VFH2.ProductStateTransport.productToTyped x, Or.inl rfl⟩ =
        ⟨VFH2.ProductStateTransport.productToTyped (productUpdate x), Or.inr rfl⟩)
    (hBaseScore :
      typedScore ⟨VFH2.ProductStateTransport.productToTyped x, Or.inl rfl⟩ =
        productScore x)
    (hUpdatedScore :
      typedScore ⟨VFH2.ProductStateTransport.productToTyped (productUpdate x), Or.inr rfl⟩ =
        productScore (productUpdate x))
    (hBaseLowerBridgeStrong :
      ProductBridgeGeneralization.genericBridgeTarget fixed
        (thresholdHi ≤ baseEffect))
    (hBaseUpperBridgeStrong :
      ProductBridgeGeneralization.genericBridgeTarget fixed
        (baseEffect ≤ thresholdLo)) :
    ProductBridgeGeneralization.genericBridgeTarget fixed
      (thresholdLo ≤ productScore (productUpdate x)) := by
  exact
    (restrictedProofSpine_rawEqualities_and_identityLikeUpdate_to_updatedBounds
      p x productUpdate productScore typedUpdate typedScore
      fixed baseEffect thresholdLo thresholdHi hThreshold hEffectBase
      hIdentityLike hTypedUpdate hBaseScore hUpdatedScore
      hBaseLowerBridgeStrong hBaseUpperBridgeStrong).1

theorem restrictedProofSpine_rawEqualities_and_identityLikeUpdate_to_updatedUpper
    (p : VFH2.ProductRestrictedParams)
    (x : p.State)
    (productUpdate : p.State → p.State)
    (productScore : p.State → Int)
    (typedUpdate :
      VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsUpdateScoreTransportCarrier p x productUpdate →
        VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsUpdateScoreTransportCarrier p x productUpdate)
    (typedScore :
      VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsUpdateScoreTransportCarrier p x productUpdate → Int)
    (fixed : Prop)
    (baseEffect thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi)
    (hEffectBase : baseEffect = productScore x)
    (hIdentityLike :
      restrictedParamsIdentityLikeUpdate p productUpdate)
    (hTypedUpdate :
      typedUpdate ⟨VFH2.ProductStateTransport.productToTyped x, Or.inl rfl⟩ =
        ⟨VFH2.ProductStateTransport.productToTyped (productUpdate x), Or.inr rfl⟩)
    (hBaseScore :
      typedScore ⟨VFH2.ProductStateTransport.productToTyped x, Or.inl rfl⟩ =
        productScore x)
    (hUpdatedScore :
      typedScore ⟨VFH2.ProductStateTransport.productToTyped (productUpdate x), Or.inr rfl⟩ =
        productScore (productUpdate x))
    (hBaseLowerBridgeStrong :
      ProductBridgeGeneralization.genericBridgeTarget fixed
        (thresholdHi ≤ baseEffect))
    (hBaseUpperBridgeStrong :
      ProductBridgeGeneralization.genericBridgeTarget fixed
        (baseEffect ≤ thresholdLo)) :
    ProductBridgeGeneralization.genericBridgeTarget fixed
      (productScore (productUpdate x) ≤ thresholdHi) := by
  exact
    (restrictedProofSpine_rawEqualities_and_identityLikeUpdate_to_updatedBounds
      p x productUpdate productScore typedUpdate typedScore
      fixed baseEffect thresholdLo thresholdHi hThreshold hEffectBase
      hIdentityLike hTypedUpdate hBaseScore hUpdatedScore
      hBaseLowerBridgeStrong hBaseUpperBridgeStrong).2

theorem restrictedProofSpine_rawEqualities_and_scoreKeyCondition_to_updatedLower
    (p : VFH2.ProductRestrictedParams)
    (x : p.State)
    (productUpdate : p.State → p.State)
    (productScore : p.State → Int)
    (typedUpdate :
      VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsUpdateScoreTransportCarrier p x productUpdate →
        VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsUpdateScoreTransportCarrier p x productUpdate)
    (typedScore :
      VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsUpdateScoreTransportCarrier p x productUpdate → Int)
    (fixed : Prop)
    (baseEffect thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi)
    (hEffectBase : baseEffect = productScore x)
    (hCondition :
      restrictedParamsScoreKeyPreservingUpdateCondition
        p productUpdate productScore)
    (hTypedUpdate :
      typedUpdate ⟨VFH2.ProductStateTransport.productToTyped x, Or.inl rfl⟩ =
        ⟨VFH2.ProductStateTransport.productToTyped (productUpdate x), Or.inr rfl⟩)
    (hBaseScore :
      typedScore ⟨VFH2.ProductStateTransport.productToTyped x, Or.inl rfl⟩ =
        productScore x)
    (hUpdatedScore :
      typedScore ⟨VFH2.ProductStateTransport.productToTyped (productUpdate x), Or.inr rfl⟩ =
        productScore (productUpdate x))
    (hBaseLowerBridgeStrong :
      ProductBridgeGeneralization.genericBridgeTarget fixed
        (thresholdHi ≤ baseEffect))
    (hBaseUpperBridgeStrong :
      ProductBridgeGeneralization.genericBridgeTarget fixed
        (baseEffect ≤ thresholdLo)) :
    ProductBridgeGeneralization.genericBridgeTarget fixed
      (thresholdLo ≤ productScore (productUpdate x)) := by
  exact
    (restrictedProofSpine_rawEqualities_and_scoreKeyCondition_to_updatedBounds
      p x productUpdate productScore typedUpdate typedScore
      fixed baseEffect thresholdLo thresholdHi hThreshold hEffectBase
      hCondition hTypedUpdate hBaseScore hUpdatedScore
      hBaseLowerBridgeStrong hBaseUpperBridgeStrong).1

theorem restrictedProofSpine_rawEqualities_and_scoreKeyCondition_to_updatedUpper
    (p : VFH2.ProductRestrictedParams)
    (x : p.State)
    (productUpdate : p.State → p.State)
    (productScore : p.State → Int)
    (typedUpdate :
      VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsUpdateScoreTransportCarrier p x productUpdate →
        VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsUpdateScoreTransportCarrier p x productUpdate)
    (typedScore :
      VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsUpdateScoreTransportCarrier p x productUpdate → Int)
    (fixed : Prop)
    (baseEffect thresholdLo thresholdHi : Int)
    (hThreshold : thresholdLo ≤ thresholdHi)
    (hEffectBase : baseEffect = productScore x)
    (hCondition :
      restrictedParamsScoreKeyPreservingUpdateCondition
        p productUpdate productScore)
    (hTypedUpdate :
      typedUpdate ⟨VFH2.ProductStateTransport.productToTyped x, Or.inl rfl⟩ =
        ⟨VFH2.ProductStateTransport.productToTyped (productUpdate x), Or.inr rfl⟩)
    (hBaseScore :
      typedScore ⟨VFH2.ProductStateTransport.productToTyped x, Or.inl rfl⟩ =
        productScore x)
    (hUpdatedScore :
      typedScore ⟨VFH2.ProductStateTransport.productToTyped (productUpdate x), Or.inr rfl⟩ =
        productScore (productUpdate x))
    (hBaseLowerBridgeStrong :
      ProductBridgeGeneralization.genericBridgeTarget fixed
        (thresholdHi ≤ baseEffect))
    (hBaseUpperBridgeStrong :
      ProductBridgeGeneralization.genericBridgeTarget fixed
        (baseEffect ≤ thresholdLo)) :
    ProductBridgeGeneralization.genericBridgeTarget fixed
      (productScore (productUpdate x) ≤ thresholdHi) := by
  exact
    (restrictedProofSpine_rawEqualities_and_scoreKeyCondition_to_updatedBounds
      p x productUpdate productScore typedUpdate typedScore
      fixed baseEffect thresholdLo thresholdHi hThreshold hEffectBase
      hCondition hTypedUpdate hBaseScore hUpdatedScore
      hBaseLowerBridgeStrong hBaseUpperBridgeStrong).2

end ProductRestrictedParamsScorePreservingPolicyInstantiation

end VFH2
