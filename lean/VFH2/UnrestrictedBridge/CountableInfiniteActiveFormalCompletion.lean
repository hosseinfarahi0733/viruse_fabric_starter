import VFH2.UnrestrictedBridge.CountableInfiniteActiveSemanticProofSpine
import VFH2.Product.ProductRestrictedParamsPreferredAfterOneUpdateProofSpine
import VFH2.Product.ProductFiniteTimeStabilization

/-!
# Countable Infinite-Active Formal Completion

This module is the front door for the completed bounded countable model.  It
combines the exact global-ledger characterization at the initial state with a
fully derived semantic proof spine after one concrete update.

It also closes the conservativity triangle with the existing Product model:
the concrete update and every trajectory time commute exactly with the
canonical Product embedding.  Finally, the preferred Product construction and
the new countable semantic proof spine are assembled in one theorem.

No fixedness, convergence, score-preservation, or score-window premise is
assumed.  The sole semantic premise in the general theorem is the model's
explicit pointwise state-space bound.

Boundary: this is a formal completion of the stated bounded countable model.
It is not an empirical, physical, biological, or unrestricted full-theory
validation claim.
-/

namespace VFH2
namespace UnrestrictedBridge

/--
For every bounded state, the exact global-ledger characterization is available
at time zero and the complete semantic proof spine is reached after one
concrete update, simultaneously for every finite score cutoff.
-/
theorem countableInfiniteActive_boundedFormalCompletion
    (p : InfiniteActiveParamsU)
    (x : StateU)
    (hspace : inInfiniteActiveStateSpaceU p x) :
    ((∀ effect : Nat,
        HasInfiniteActiveGlobalLedgerEffectU p x effect ↔
          ∃ cutoff : Nat,
            (∀ i : Nat,
              cutoff ≤ i → p.active i = true → x i = p.top) ∧
            effect = infiniteActiveLedgerEffectPrefixU p x cutoff) ∧
      ((∃ effect : Nat,
          HasInfiniteActiveGlobalLedgerEffectU p x effect ∧
            ∀ candidate : Nat,
              HasInfiniteActiveGlobalLedgerEffectU p x candidate →
                candidate = effect) ↔
        ∃ cutoff : Nat,
          ∀ i : Nat,
            cutoff ≤ i → p.active i = true → x i = p.top) ∧
      (HasInfiniteActiveGlobalLedgerEffectU p x 0 ↔
        inInfiniteActiveFixedSetU p x) ∧
      (∀ t : Nat,
        HasInfiniteActiveGlobalLedgerEffectU
            p
            (infiniteActiveUpdateTrajectoryU p x t)
            0 ↔
          ∀ u : Nat,
            t ≤ u →
              infiniteActiveUpdateTrajectoryU p x u =
                infiniteActiveUpdateTrajectoryU p x t)) ∧
    ∀ cutoff : Nat,
      InfiniteActiveSemanticProofSpineU
        p
        (updateInfiniteActiveU p x)
        cutoff := by
  exact ⟨
    countableInfiniteActiveGlobalLedger_finalCharacterization p x hspace,
    fun cutoff =>
      infiniteActiveSemanticProofSpineU_after_one_update
        p x hspace cutoff
  ⟩

/-- The infinite-active embedding commutes exactly with one Product update. -/
theorem productEmbedding_updateInfiniteActiveU
    (p : ProductRestrictedParams)
    (x : p.State) :
    updateInfiniteActiveU
        (infiniteActiveParamsUOfParamsU (paramsUOfProduct p))
        (stateUOfProduct p x) =
      stateUOfProduct p (productUpdateState p x) := by
  calc
    updateInfiniteActiveU
        (infiniteActiveParamsUOfParamsU (paramsUOfProduct p))
        (stateUOfProduct p x) =
      updateU (paramsUOfProduct p) (stateUOfProduct p x) :=
        updateInfiniteActiveU_infiniteActiveParamsUOfParamsU
          (paramsUOfProduct p)
          (stateUOfProduct p x)
    _ = stateUOfProduct p (productUpdateState p x) :=
      (stateUOfProduct_productUpdateState p x).symm

/-- The infinite-active embedding commutes with the complete Product orbit. -/
theorem productEmbedding_infiniteActiveUpdateTrajectoryU
    (p : ProductRestrictedParams)
    (x : p.State) :
    ∀ t : Nat,
      infiniteActiveUpdateTrajectoryU
          (infiniteActiveParamsUOfParamsU (paramsUOfProduct p))
          (stateUOfProduct p x)
          t =
        stateUOfProduct p (productUpdateTrajectory p x t) := by
  intro t
  induction t with
  | zero =>
      rfl
  | succ t ih =>
      simp only [infiniteActiveUpdateTrajectoryU, productUpdateTrajectory]
      rw [ih]
      exact
        productEmbedding_updateInfiniteActiveU
          p
          (productUpdateTrajectory p x t)

/--
Every embedded Product state reaches the complete countable semantic proof
spine after one update, with no extra Product-side premise.
-/
theorem productEmbedding_semanticProofSpineU_after_one_update
    (p : ProductRestrictedParams)
    (x : p.State)
    (cutoff : Nat) :
    InfiniteActiveSemanticProofSpineU
      (infiniteActiveParamsUOfParamsU (paramsUOfProduct p))
      (stateUOfProduct p (productUpdateState p x))
      cutoff := by
  have hspaceFinite :
      inStateSpaceU (paramsUOfProduct p) (stateUOfProduct p x) :=
    stateUOfProduct_inStateSpaceU p x
  have hspaceInfinite :
      inInfiniteActiveStateSpaceU
        (infiniteActiveParamsUOfParamsU (paramsUOfProduct p))
        (stateUOfProduct p x) :=
    (inInfiniteActiveStateSpaceU_infiniteActiveParamsUOfParamsU_iff
      (paramsUOfProduct p)
      (stateUOfProduct p x)).2 hspaceFinite
  rw [← productEmbedding_updateInfiniteActiveU p x]
  exact
    infiniteActiveSemanticProofSpineU_after_one_update
      (infiniteActiveParamsUOfParamsU (paramsUOfProduct p))
      (stateUOfProduct p x)
      hspaceInfinite
      cutoff

/--
The preferred Product construction simultaneously satisfies the pre-existing
restricted proof spine and, after the same concrete update, the new countable
semantic proof spine.  The final conjunct records exact orbit compatibility.
-/
theorem preferredProductAndCountable_after_one_update_formalCompletion
    (n d : Nat)
    (missing : ProductIndex d)
    (x :
      (ProductRestrictedParamsPreferredFrontDoor.preferredParams
        n d missing).State) :
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
        InfiniteActiveSemanticProofSpineU
          (infiniteActiveParamsUOfParamsU (paramsUOfProduct p))
          (stateUOfProduct p (productUpdateState p x))
          cutoff) ∧
      ∀ t : Nat,
        infiniteActiveUpdateTrajectoryU
            (infiniteActiveParamsUOfParamsU (paramsUOfProduct p))
            (stateUOfProduct p x)
            t =
          stateUOfProduct p (productUpdateTrajectory p x t) := by
  dsimp only
  refine ⟨?_, ?_, ?_⟩
  · exact
      ProductRestrictedParamsPreferredAfterOneUpdateProofSpine.restrictedParams_preferredParams_after_one_update_to_currentBestMainTheorem
        n d missing x
  · intro cutoff
    exact productEmbedding_semanticProofSpineU_after_one_update
      (ProductRestrictedParamsPreferredFrontDoor.preferredParams
        n d missing)
      x
      cutoff
  · exact productEmbedding_infiniteActiveUpdateTrajectoryU
      (ProductRestrictedParamsPreferredFrontDoor.preferredParams
        n d missing)
      x

end UnrestrictedBridge
end VFH2
