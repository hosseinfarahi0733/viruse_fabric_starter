import VFH2.UnrestrictedBridge.CountableInfiniteActiveInvariantScore

/-!
# Countable Infinite-Active Semantic Proof Spine

This module defines the concrete proof target for the bounded countable model.
Its fields are not assumptions: they record boundedness, fixedness, zero global
residual effect, preservation of the inactive-key score, its derived natural
window, and full trajectory stationarity.

The target is characterized exactly by fixedness and by zero global effect.
After one concrete update it is therefore obtained for every bounded initial
state without an independent fixedness, convergence, score-preservation, or
score-bound premise.
-/

namespace VFH2
namespace UnrestrictedBridge

/-- The fully semantic proof-spine target for one finite score cutoff. -/
structure InfiniteActiveSemanticProofSpineU
    (p : InfiniteActiveParamsU)
    (x : StateU)
    (cutoff : Nat) : Prop where
  bounded : inInfiniteActiveStateSpaceU p x
  fixed : inInfiniteActiveFixedSetU p x
  zeroGlobalEffect : HasInfiniteActiveGlobalLedgerEffectU p x 0
  scorePreserved :
    infiniteActiveInvariantScorePrefixU
        p
        (updateInfiniteActiveU p x)
        cutoff =
      infiniteActiveInvariantScorePrefixU p x cutoff
  scoreLower :
    (0 : Int) ≤
      (infiniteActiveInvariantScorePrefixU p x cutoff : Int)
  scoreUpper :
    (infiniteActiveInvariantScorePrefixU p x cutoff : Int) ≤
      ((cutoff * p.top : Nat) : Int)
  stationary :
    ∀ u : Nat,
      infiniteActiveUpdateTrajectoryU p x u = x

/--
For a bounded state, the complete semantic proof spine is equivalent to the
concrete active-coordinate fixed set.
-/
theorem infiniteActiveSemanticProofSpineU_iff_inInfiniteActiveFixedSetU
    (p : InfiniteActiveParamsU)
    (x : StateU)
    (hspace : inInfiniteActiveStateSpaceU p x)
    (cutoff : Nat) :
    InfiniteActiveSemanticProofSpineU p x cutoff ↔
      inInfiniteActiveFixedSetU p x := by
  constructor
  · intro hSpine
    exact hSpine.fixed
  · intro hfixed
    refine {
      bounded := hspace
      fixed := hfixed
      zeroGlobalEffect := ?_
      scorePreserved := ?_
      scoreLower := ?_
      scoreUpper := ?_
      stationary := ?_
    }
    · exact
        (hasInfiniteActiveGlobalLedgerEffectU_zero_iff_inInfiniteActiveFixedSetU
          p x hspace).2 hfixed
    · exact
        infiniteActiveInvariantScorePrefixU_updateInfiniteActiveU
          p x cutoff
    · exact
        infiniteActiveInvariantScorePrefixU_int_nonneg p x cutoff
    · exact
        infiniteActiveInvariantScorePrefixU_int_le_cutoff_mul_top
          p x hspace cutoff
    · intro u
      induction u with
      | zero =>
          rfl
      | succ u ih =>
          change
            updateInfiniteActiveU p
                (infiniteActiveUpdateTrajectoryU p x u) = x
          rw [ih]
          exact
            (updateInfiniteActiveU_eq_self_iff_inInfiniteActiveFixedSetU
              p x).2 hfixed

/--
For a bounded state, the semantic proof spine is also exactly equivalent to
zero finite global residual effect.
-/
theorem infiniteActiveSemanticProofSpineU_iff_hasGlobalEffect_zero
    (p : InfiniteActiveParamsU)
    (x : StateU)
    (hspace : inInfiniteActiveStateSpaceU p x)
    (cutoff : Nat) :
    InfiniteActiveSemanticProofSpineU p x cutoff ↔
      HasInfiniteActiveGlobalLedgerEffectU p x 0 := by
  calc
    InfiniteActiveSemanticProofSpineU p x cutoff ↔
        inInfiniteActiveFixedSetU p x :=
      infiniteActiveSemanticProofSpineU_iff_inInfiniteActiveFixedSetU
        p x hspace cutoff
    _ ↔ HasInfiniteActiveGlobalLedgerEffectU p x 0 :=
      (hasInfiniteActiveGlobalLedgerEffectU_zero_iff_inInfiniteActiveFixedSetU
        p x hspace).symm

/--
Every bounded initial state enters the complete semantic proof spine after one
concrete update. All semantic obligations are derived internally.
-/
theorem infiniteActiveSemanticProofSpineU_after_one_update
    (p : InfiniteActiveParamsU)
    (x : StateU)
    (hspace : inInfiniteActiveStateSpaceU p x)
    (cutoff : Nat) :
    InfiniteActiveSemanticProofSpineU
      p
      (updateInfiniteActiveU p x)
      cutoff := by
  have hspaceUpdated :
      inInfiniteActiveStateSpaceU p (updateInfiniteActiveU p x) :=
    updateInfiniteActiveU_preserves_inInfiniteActiveStateSpaceU
      p x hspace
  exact
    (infiniteActiveSemanticProofSpineU_iff_inInfiniteActiveFixedSetU
      p
      (updateInfiniteActiveU p x)
      hspaceUpdated
      cutoff).2
      (updateInfiniteActiveU_inInfiniteActiveFixedSetU p x)

/-- Every positive trajectory time satisfies the complete semantic proof spine. -/
theorem infiniteActiveSemanticProofSpineU_trajectory_of_pos
    (p : InfiniteActiveParamsU)
    (x : StateU)
    (hspace : inInfiniteActiveStateSpaceU p x)
    (cutoff t : Nat)
    (ht : 0 < t) :
    InfiniteActiveSemanticProofSpineU
      p
      (infiniteActiveUpdateTrajectoryU p x t)
      cutoff := by
  obtain ⟨u, rfl⟩ := Nat.exists_eq_succ_of_ne_zero (by omega : t ≠ 0)
  rw [infiniteActiveUpdateTrajectoryU_succ_eq_updateInfiniteActiveU]
  exact infiniteActiveSemanticProofSpineU_after_one_update
    p x hspace cutoff

end UnrestrictedBridge
end VFH2
