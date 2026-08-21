import VFH2.UnrestrictedBridge.CountableFiniteActiveToInfiniteActiveConservativity

/-!
# Countable Infinite-Active Global Ledger Final Characterization

This module exposes a single front-door certificate for the completed
countable nonnegative-ledger layer. It assembles the exact value
characterization, unique-existence criterion, zero/fixed-set equivalence, and
all-time trajectory stationarity theorem. A second certificate records the
exact conservativity of the earlier finite-active model.

The formal scope is the explicitly defined countable Boolean-active model with
bounded natural-valued coordinates and eventual prefix convergence. These
theorems do not make an empirical, physical, or biological validation claim.
-/

namespace VFH2
namespace UnrestrictedBridge

/--
The complete characterization certificate for a bounded countable
infinite-active state: exact convergent values, exact unique-existence
criterion, zero/fixedness, and trajectory stationarity are all available
simultaneously.
-/
theorem countableInfiniteActiveGlobalLedger_finalCharacterization
    (p : InfiniteActiveParamsU)
    (x : StateU)
    (hspace : inInfiniteActiveStateSpaceU p x) :
    (∀ effect : Nat,
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
              infiniteActiveUpdateTrajectoryU p x t) := by
  refine ⟨?_, ?_, ?_, ?_⟩
  · intro effect
    exact
      hasInfiniteActiveGlobalLedgerEffectU_iff_exists_eventuallyFixedActive_and_eq_prefix
        p x hspace effect
  · exact
      existsUnique_hasInfiniteActiveGlobalLedgerEffectU_iff_eventuallyFixedActive
        p x hspace
  · exact
      hasInfiniteActiveGlobalLedgerEffectU_zero_iff_inInfiniteActiveFixedSetU
        p x hspace
  · intro t
    exact
      hasInfiniteActiveGlobalLedgerEffectU_infiniteActiveUpdateTrajectoryU_zero_iff_stationaryFrom
        p x hspace t

/--
The finite-active source model embeds conservatively into the completed
countable ledger layer: fixedness, one-step dynamics, the entire trajectory,
and existence with uniqueness of a finite global effect are certified in one
statement.
-/
theorem countableFiniteActiveEmbedding_finalCertificate
    (p : ParamsU)
    (x : StateU)
    (hspace : inStateSpaceU p x) :
    (inInfiniteActiveFixedSetU (infiniteActiveParamsUOfParamsU p) x ↔
      inFixedSetU p x) ∧
    updateInfiniteActiveU (infiniteActiveParamsUOfParamsU p) x =
      updateU p x ∧
    (∀ t : Nat,
      infiniteActiveUpdateTrajectoryU
          (infiniteActiveParamsUOfParamsU p)
          x
          t =
        updateUTrajectory p x t) ∧
    ∃ effect : Nat,
      HasInfiniteActiveGlobalLedgerEffectU
          (infiniteActiveParamsUOfParamsU p)
          x
          effect ∧
        ∀ candidate : Nat,
          HasInfiniteActiveGlobalLedgerEffectU
              (infiniteActiveParamsUOfParamsU p)
              x
              candidate →
            candidate = effect := by
  refine ⟨?_, ?_, ?_, ?_⟩
  · exact inInfiniteActiveFixedSetU_infiniteActiveParamsUOfParamsU_iff p x
  · exact updateInfiniteActiveU_infiniteActiveParamsUOfParamsU p x
  · exact infiniteActiveUpdateTrajectoryU_infiniteActiveParamsUOfParamsU p x
  · exact
      existsUnique_hasInfiniteActiveGlobalLedgerEffectU_infiniteActiveParamsUOfParamsU
        p x hspace

end UnrestrictedBridge
end VFH2
