import VFH2.Product.ProductFixedSet
import VFH2.Product.ProductRestrictedParamsFullNaturalProofSpine

/-!
# C9.1 hFixed Semantic Specialization

This file specializes the formerly arbitrary `fixed : Prop` parameter in the
v17.4 full natural restricted proof-spine theorem to the concrete product-side
fixed-set predicate:

```lean
ProductFixedSet p x
```

Boundary:

* This is a semantic specialization of the `fixed` proposition.
* It does not derive `ProductFixedSet p x` from update/domain dynamics.
* It does not prove full VF-H2.
-/

namespace VFH2
namespace ProductRestrictedParamsHFixedSemanticSpecialization

/--
Score-key-condition route with `fixed` semantically instantiated as
`ProductFixedSet p x`.

This removes the arbitrary `fixed : Prop` choice from the public statement, but
it still requires the fixed-set evidence `hFixedSet : ProductFixedSet p x`.
-/
theorem restrictedParams_scoreKeyCondition_naturalBase_productFixedSet_to_restrictedProofSpineTarget
    (p : ProductRestrictedParams) (x : p.State)
    (productUpdate : p.State → p.State) (productScore : p.State → Int)
    (thresholdLo thresholdHi : Int) (hThreshold : thresholdLo ≤ thresholdHi)
    (hCondition :
      ProductRestrictedParamsScorePreservingPolicyInstantiation.restrictedParamsScoreKeyPreservingUpdateCondition
        p productUpdate productScore)
    (hFixedSet : ProductFixedSet p x)
    (hBaseLowerNatural : thresholdLo ≤ productScore x)
    (hBaseUpperNatural : productScore x ≤ thresholdHi) :
    ProductRestrictedParamsRestrictedProofSpineFreeze.restrictedProofSpineTarget
      p x productUpdate productScore
      (ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedUpdate p x productUpdate)
      (ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedScore p x productUpdate productScore)
      (ProductFixedSet p x) thresholdLo thresholdHi hThreshold := by
  exact
    ProductRestrictedParamsFullNaturalProofSpine.restrictedParams_scoreKeyCondition_naturalBase_to_restrictedProofSpineTarget
      p x productUpdate productScore
      (ProductFixedSet p x) thresholdLo thresholdHi hThreshold
      hCondition hFixedSet hBaseLowerNatural hBaseUpperNatural

/--
Identity-like-update route with `fixed` semantically instantiated as
`ProductFixedSet p x`.

This route inherits the same boundary: it requires `hFixedSet` and does not
derive fixedness from update/domain dynamics.
-/
theorem restrictedParams_identityLikeUpdate_naturalBase_productFixedSet_to_restrictedProofSpineTarget
    (p : ProductRestrictedParams) (x : p.State)
    (productUpdate : p.State → p.State) (productScore : p.State → Int)
    (thresholdLo thresholdHi : Int) (hThreshold : thresholdLo ≤ thresholdHi)
    (hIdentityLike :
      ProductRestrictedParamsScorePreservingPolicyInstantiation.restrictedParamsIdentityLikeUpdate
        p productUpdate)
    (hFixedSet : ProductFixedSet p x)
    (hBaseLowerNatural : thresholdLo ≤ productScore x)
    (hBaseUpperNatural : productScore x ≤ thresholdHi) :
    ProductRestrictedParamsRestrictedProofSpineFreeze.restrictedProofSpineTarget
      p x productUpdate productScore
      (ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedUpdate p x productUpdate)
      (ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedScore p x productUpdate productScore)
      (ProductFixedSet p x) thresholdLo thresholdHi hThreshold := by
  exact
    ProductRestrictedParamsFullNaturalProofSpine.restrictedParams_identityLikeUpdate_naturalBase_to_restrictedProofSpineTarget
      p x productUpdate productScore
      (ProductFixedSet p x) thresholdLo thresholdHi hThreshold
      hIdentityLike hFixedSet hBaseLowerNatural hBaseUpperNatural

end ProductRestrictedParamsHFixedSemanticSpecialization
end VFH2
