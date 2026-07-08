# VF-H2 Core Lean Prints

This file records the core Lean definitions and theorem statements used for scientific review.

Source: generated from Lean with #print / #check.

----

def VFH2.ProductFixedSet : (p : VFH2.ProductRestrictedParams) → p.State → Prop :=
fun p x => ∀ (i : VFH2.ProductIndex p.d), i ∈ p.active → (x i).val = p.n
def VFH2.ProductRestrictedParamsScorePreservingPolicyInstantiation.restrictedParamsScoreKeyPreservingUpdateCondition : (p :
    VFH2.ProductRestrictedParams) →
  (p.State → p.State) → (p.State → Int) → Prop :=
fun p productUpdate productScore =>
  ∃ ScoreKey scoreKey scoreOfKey,
    (∀ (y : p.State), productScore y = scoreOfKey (scoreKey y)) ∧
      ∀ (y : p.State), scoreKey (productUpdate y) = scoreKey y
@[reducible] def VFH2.ProductRestrictedParamsRestrictedProofSpineFreeze.restrictedProofSpineTarget : (p :
    VFH2.ProductRestrictedParams) →
  (x : p.State) →
    (productUpdate : p.State → p.State) →
      (p.State → Int) →
        (VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsUpdateScoreTransportCarrier p x
              productUpdate →
            VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsUpdateScoreTransportCarrier p x
              productUpdate) →
          (VFH2.ProductRestrictedParamsUpdateScoreTransport.restrictedParamsUpdateScoreTransportCarrier p x
                productUpdate →
              Int) →
            Prop → (thresholdLo thresholdHi : Int) → thresholdLo ≤ thresholdHi → Prop :=
fun p x productUpdate productScore typedUpdate typedScore fixed thresholdLo thresholdHi hThreshold =>
  VFH2.ProductRestrictedParamsPolicyEndToEndScoreWindow.restrictedParamsPolicyEndToEndScoreWindowTarget p x
    productUpdate productScore typedUpdate typedScore fixed thresholdLo thresholdHi hThreshold
def VFH2.productUpdateState : (p : VFH2.ProductRestrictedParams) → p.State → p.State :=
fun p x i => if i ∈ p.active then p.topCoord else x i
VFH2.ProductRestrictedParamsFullNaturalProofSpine.restrictedParams_scoreKeyCondition_naturalBase_to_restrictedProofSpineTarget
  (p : VFH2.ProductRestrictedParams) (x : p.State) (productUpdate : p.State → p.State) (productScore : p.State → Int)
  (fixed : Prop) (thresholdLo thresholdHi : Int) (hThreshold : thresholdLo ≤ thresholdHi)
  (hCondition :
    VFH2.ProductRestrictedParamsScorePreservingPolicyInstantiation.restrictedParamsScoreKeyPreservingUpdateCondition p
      productUpdate productScore)
  (hFixed : fixed) (hBaseLowerNatural : thresholdLo ≤ productScore x)
  (hBaseUpperNatural : productScore x ≤ thresholdHi) :
  VFH2.ProductRestrictedParamsRestrictedProofSpineFreeze.restrictedProofSpineTarget p x productUpdate productScore
    (VFH2.ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedUpdate p x productUpdate)
    (VFH2.ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedScore p x productUpdate productScore)
    fixed thresholdLo thresholdHi hThreshold
VFH2.ProductRestrictedParamsFullNaturalProofSpine.restrictedParams_identityLikeUpdate_naturalBase_to_restrictedProofSpineTarget
  (p : VFH2.ProductRestrictedParams) (x : p.State) (productUpdate : p.State → p.State) (productScore : p.State → Int)
  (fixed : Prop) (thresholdLo thresholdHi : Int) (hThreshold : thresholdLo ≤ thresholdHi)
  (hIdentityLike :
    VFH2.ProductRestrictedParamsScorePreservingPolicyInstantiation.restrictedParamsIdentityLikeUpdate p productUpdate)
  (hFixed : fixed) (hBaseLowerNatural : thresholdLo ≤ productScore x)
  (hBaseUpperNatural : productScore x ≤ thresholdHi) :
  VFH2.ProductRestrictedParamsRestrictedProofSpineFreeze.restrictedProofSpineTarget p x productUpdate productScore
    (VFH2.ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedUpdate p x productUpdate)
    (VFH2.ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedScore p x productUpdate productScore)
    fixed thresholdLo thresholdHi hThreshold
VFH2.ProductRestrictedParamsHFixedSemanticSpecialization.restrictedParams_scoreKeyCondition_naturalBase_productFixedSet_to_restrictedProofSpineTarget
  (p : VFH2.ProductRestrictedParams) (x : p.State) (productUpdate : p.State → p.State) (productScore : p.State → Int)
  (thresholdLo thresholdHi : Int) (hThreshold : thresholdLo ≤ thresholdHi)
  (hCondition :
    VFH2.ProductRestrictedParamsScorePreservingPolicyInstantiation.restrictedParamsScoreKeyPreservingUpdateCondition p
      productUpdate productScore)
  (hFixedSet : VFH2.ProductFixedSet p x) (hBaseLowerNatural : thresholdLo ≤ productScore x)
  (hBaseUpperNatural : productScore x ≤ thresholdHi) :
  VFH2.ProductRestrictedParamsRestrictedProofSpineFreeze.restrictedProofSpineTarget p x productUpdate productScore
    (VFH2.ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedUpdate p x productUpdate)
    (VFH2.ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedScore p x productUpdate productScore)
    (VFH2.ProductFixedSet p x) thresholdLo thresholdHi hThreshold
VFH2.ProductRestrictedParamsHFixedSemanticSpecialization.restrictedParams_identityLikeUpdate_naturalBase_productFixedSet_to_restrictedProofSpineTarget
  (p : VFH2.ProductRestrictedParams) (x : p.State) (productUpdate : p.State → p.State) (productScore : p.State → Int)
  (thresholdLo thresholdHi : Int) (hThreshold : thresholdLo ≤ thresholdHi)
  (hIdentityLike :
    VFH2.ProductRestrictedParamsScorePreservingPolicyInstantiation.restrictedParamsIdentityLikeUpdate p productUpdate)
  (hFixedSet : VFH2.ProductFixedSet p x) (hBaseLowerNatural : thresholdLo ≤ productScore x)
  (hBaseUpperNatural : productScore x ≤ thresholdHi) :
  VFH2.ProductRestrictedParamsRestrictedProofSpineFreeze.restrictedProofSpineTarget p x productUpdate productScore
    (VFH2.ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedUpdate p x productUpdate)
    (VFH2.ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedScore p x productUpdate productScore)
    (VFH2.ProductFixedSet p x) thresholdLo thresholdHi hThreshold
