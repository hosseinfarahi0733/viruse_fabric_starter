import VFH2.Product.ThreeTimeCausalFabricFormalCoreCompletion
import VFH2.Product.ThreeTimeFalsifiabilityContract

/-!
# C122: Constraint-Geometry Mathematical Completion

This is the final bounded mathematical certificate for the present development.
It assembles the C116 three-time/ledger core with:

* direct non-factorization of a genuinely ternary constraint;
* the exact rectangle characterization of adjacent-chain factorization;
* the exact local-to-global gluing-obstruction criterion;
* complete three-time versus incomplete present-only observers; and
* a nontrivial decidable falsifiability interface.

Claim boundary: the theorem completes the stated finite mathematical model.  It
does not establish an empirical law of nature, provide experimental data, or
prove the separate strict-positive Memory Ledger hypothesis.
-/

namespace VFH2
namespace ThreeTime

/-- The assembled C122 mathematical-completion certificate. -/
structure ThreeTimeConstraintGeometryMathematicalCompletionCertificate
    (p : ProductRestrictedParams)
    (x : p.State) : Prop where
  causalFabricCore : ThreeTimeCausalFabricCoreCertificate p x
  directNonChainConstraint : ¬ ChainRepresentable evenParity
  exactChainCriterion :
    forall r : TernaryConstraint Bool,
      ChainRepresentable r <-> MiddleRectangleClosed r
  exactGluingCriterion :
    forall r : TernaryConstraint Bool,
      PairwiseShadowReconstructible r <->
        (¬ HasPairwiseGluingObstruction r)
  concreteGluingObstruction :
    HasPairwiseGluingObstruction evenParity
  completeThreeTimeObservers :
    forall n d : Nat,
      JointlySeparating (namedTimeObserverFamily n d)
  incompletePresentOnlyObserver :
    ¬ JointlySeparating presentOnlyObserverFamily
  nontrivialFalsifiabilityContract :
    Supports boolTruePrediction true /\
      Falsifies boolTruePrediction false
  parityFalsifiesChainPrediction :
    Falsifies rectangleLawPrediction evenParityRectangleTrial

/-- Every restricted product state carries the complete C122 certificate. -/
theorem threeTimeConstraintGeometry_mathematicalCompletionCertificate
    (p : ProductRestrictedParams)
    (x : p.State) :
    ThreeTimeConstraintGeometryMathematicalCompletionCertificate p x := by
  exact {
    causalFabricCore := threeTimeCausalFabric_coreCertificate p x
    directNonChainConstraint := evenParity_not_chainRepresentable
    exactChainCriterion := chainRepresentable_iff_middleRectangleClosed
    exactGluingCriterion :=
      pairwiseShadowReconstructible_iff_no_gluingObstruction
    concreteGluingObstruction :=
      evenParity_has_pairwiseGluingObstruction
    completeThreeTimeObservers :=
      namedTimeObserverFamily_jointlySeparating
    incompletePresentOnlyObserver :=
      presentOnlyObserverFamily_not_jointlySeparating
    nontrivialFalsifiabilityContract :=
      boolTruePrediction_support_and_falsifier
    parityFalsifiesChainPrediction :=
      evenParityRectangleTrial_falsifies_chainPrediction
  }

/--
Final C122 theorem: the mathematical constraint-geometry certificate and the
complete preferred C111 product/countable theorem hold for the same update.
-/
theorem preferred_threeTimeConstraintGeometry_mathematicalCompletion
    (n d : Nat)
    (missing : ProductIndex d)
    (x :
      (ProductRestrictedParamsPreferredFrontDoor.preferredParams
        n d missing).State) :
    let p :=
      ProductRestrictedParamsPreferredFrontDoor.preferredParams
        n d missing
    ThreeTimeConstraintGeometryMathematicalCompletionCertificate p x /\
      C111PreferredProductAndCountableCompletion n d missing x := by
  dsimp only
  constructor
  · exact
      threeTimeConstraintGeometry_mathematicalCompletionCertificate
        (ProductRestrictedParamsPreferredFrontDoor.preferredParams
          n d missing)
        x
  · exact
      (preferred_threeTimeCausalFabric_formalCoreCompletion
        n d missing x).2

end ThreeTime
end VFH2
