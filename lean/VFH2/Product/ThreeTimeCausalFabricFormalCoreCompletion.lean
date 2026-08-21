import VFH2.Product.ThreeTimeTemporalUnity
import VFH2.Product.ProductTrajectoryStationarity
import VFH2.UnrestrictedBridge.CountableInfiniteActiveFormalCompletion

/-!
# C116: Three-Time Causal-Fabric Formal-Core Completion

This module assembles C112--C115 with the C111 ledger/update completion.
The resulting certificate simultaneously records:

* three distinct time layers forming one losslessly reconstructible state;
* a proof that pairwise/chain shadows do not determine global constraints;
* a concrete non-injective single-narrative observer;
* one-step fixedness, zero residual ledger effect, and stationarity;
* exact compatibility with the bounded countable semantic proof spine;
* the complete pre-existing preferred C111 theorem.

Claim boundary: this is a machine-checked formal core for the explicitly defined
model. It is not an empirical proof that nature implements these definitions,
nor an unrestricted physical theory of causality or time.
-/

namespace VFH2
namespace ThreeTime

/-- The complete C111 preferred theorem, retained as an explicit dependency. -/
abbrev C111PreferredProductAndCountableCompletion
    (n d : Nat)
    (missing : ProductIndex d)
    (x :
      (ProductRestrictedParamsPreferredFrontDoor.preferredParams
        n d missing).State) : Prop :=
  let p :=
    ProductRestrictedParamsPreferredFrontDoor.preferredParams
      n d missing
  let cert :=
    ProductRestrictedParamsPreferredAfterOneUpdateProofSpine.preferredInactiveIndexCertificate
      n d missing
  ProductRestrictedParamsRestrictedProofSpineFreeze.restrictedProofSpineTarget
      p
      (productUpdateState p x)
      (productUpdateState p)
      (ProductRestrictedParamsInactiveCoordScore.inactiveCoordScore
        p cert.i)
      (ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedUpdate
        p
        (productUpdateState p x)
        (productUpdateState p))
      (ProductRestrictedParamsCanonicalRawEqualities.canonicalRestrictedTypedScore
        p
        (productUpdateState p x)
        (productUpdateState p)
        (ProductRestrictedParamsInactiveCoordScore.inactiveCoordScore
          p cert.i))
      (ProductFixedSet p (productUpdateState p x))
      0
      (Int.ofNat p.n)
      (Int.natCast_nonneg p.n) ∧
    (∀ cutoff : Nat,
      UnrestrictedBridge.InfiniteActiveSemanticProofSpineU
        (UnrestrictedBridge.infiniteActiveParamsUOfParamsU
          (UnrestrictedBridge.paramsUOfProduct p))
        (UnrestrictedBridge.stateUOfProduct p (productUpdateState p x))
        cutoff) ∧
    ∀ t : Nat,
      UnrestrictedBridge.infiniteActiveUpdateTrajectoryU
          (UnrestrictedBridge.infiniteActiveParamsUOfParamsU
            (UnrestrictedBridge.paramsUOfProduct p))
          (UnrestrictedBridge.stateUOfProduct p x)
          t =
        UnrestrictedBridge.stateUOfProduct p
          (productUpdateTrajectory p x t)

/--
The generic structural/dynamical certificate that connects the three-time
fabric to the C111 bounded countable ledger semantics.
-/
structure ThreeTimeCausalFabricCoreCertificate
    (p : ProductRestrictedParams)
    (x : p.State) : Prop where
  layersDistinct :
    TimeLayer.t1 ≠ TimeLayer.t2 ∧
      TimeLayer.t1 ≠ TimeLayer.t3 ∧
      TimeLayer.t2 ≠ TimeLayer.t3
  updatedUniquelyReconstructed :
    ∀ y : p.State,
      pastSlice y = pastSlice (productUpdateState p x) →
      presentSlice y = presentSlice (productUpdateState p x) →
      futureSlice y = futureSlice (productUpdateState p x) →
      y = productUpdateState p x
  nonChainGeometry :
    ∃ r s : TernaryConstraint Bool,
      PairwiseIndistinguishable r s ∧
        ¬ GloballyEquivalent r s
  observerCompressionLoss :
    ∃ a b : GlobalFabricState 1 1,
      a ≠ b ∧
        (presentObserverProjection 1 1).observe a =
          (presentObserverProjection 1 1).observe b
  updatedFixed :
    ProductFixedSet p (productUpdateState p x)
  updatedZeroLedger :
    productLedgerEffect p (productUpdateState p x) = 0
  stationaryFromOne :
    productTrajectoryStationaryFrom p x 1
  countableSemanticClosure :
    ∀ cutoff : Nat,
      UnrestrictedBridge.InfiniteActiveSemanticProofSpineU
        (UnrestrictedBridge.infiniteActiveParamsUOfParamsU
          (UnrestrictedBridge.paramsUOfProduct p))
        (UnrestrictedBridge.stateUOfProduct p (productUpdateState p x))
        cutoff
  productCountableOrbitCommutes :
    ∀ t : Nat,
      UnrestrictedBridge.infiniteActiveUpdateTrajectoryU
          (UnrestrictedBridge.infiniteActiveParamsUOfParamsU
            (UnrestrictedBridge.paramsUOfProduct p))
          (UnrestrictedBridge.stateUOfProduct p x)
          t =
        UnrestrictedBridge.stateUOfProduct p
          (productUpdateTrajectory p x t)

/-- Every restricted product state produces the complete formal-core certificate. -/
theorem threeTimeCausalFabric_coreCertificate
    (p : ProductRestrictedParams)
    (x : p.State) :
    ThreeTimeCausalFabricCoreCertificate p x := by
  refine {
    layersDistinct := named_timeLayers_pairwise_distinct
    updatedUniquelyReconstructed := ?_
    nonChainGeometry := pairwise_shadows_do_not_determine_global_constraint
    observerCompressionLoss := exists_distinct_fabrics_same_present_narrative
    updatedFixed := productUpdateState_ProductFixedSet p x
    updatedZeroLedger := productLedgerEffect_after_update_zero p x
    stationaryFromOne := ?_
    countableSemanticClosure := ?_
    productCountableOrbitCommutes := ?_
  }
  · intro y hpast hpresent hfuture
    exact ext_namedSlices hpast hpresent hfuture
  · exact
      (productTrajectoryStationaryFrom_iff_initialFixed_or_pos p x 1).2
        (Or.inr (by omega))
  · intro cutoff
    exact
      UnrestrictedBridge.productEmbedding_semanticProofSpineU_after_one_update
        p x cutoff
  · exact
      UnrestrictedBridge.productEmbedding_infiniteActiveUpdateTrajectoryU
        p x

/--
Final C116 theorem: the new three-time core and the full preferred C111 ledger
completion hold together for the same concrete update and orbit.
-/
theorem preferred_threeTimeCausalFabric_formalCoreCompletion
    (n d : Nat)
    (missing : ProductIndex d)
    (x :
      (ProductRestrictedParamsPreferredFrontDoor.preferredParams
        n d missing).State) :
    let p :=
      ProductRestrictedParamsPreferredFrontDoor.preferredParams
        n d missing
    ThreeTimeCausalFabricCoreCertificate p x ∧
      C111PreferredProductAndCountableCompletion n d missing x := by
  dsimp only
  constructor
  · exact
      threeTimeCausalFabric_coreCertificate
        (ProductRestrictedParamsPreferredFrontDoor.preferredParams
          n d missing)
        x
  · exact
      UnrestrictedBridge.preferredProductAndCountable_after_one_update_formalCompletion
        n d missing x

end ThreeTime
end VFH2
