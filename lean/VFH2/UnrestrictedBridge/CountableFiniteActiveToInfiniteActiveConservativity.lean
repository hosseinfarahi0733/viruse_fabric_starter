import VFH2.UnrestrictedBridge.CountableInfiniteActiveGlobalLedgerTrajectoryStationarity

/-!
# Finite-Active to Infinite-Active Conservativity

This module embeds the earlier finite-list active model into the countable
Boolean-predicate model. It proves exact preservation of the state space,
fixed set, one-step update, and complete update trajectory. It also proves
that every embedded finite-active bounded state has one and only one finite
global ledger effect.

The last result is derived from the general convergence characterization: past
the sum of the listed active indices, the embedded active predicate is empty.
No distinctness or sorting premise is imposed on the finite active list.
-/

namespace VFH2
namespace UnrestrictedBridge

/-- Embed a finite-list active parameter into the Boolean active predicate. -/
def infiniteActiveParamsUOfParamsU
    (p : ParamsU) : InfiniteActiveParamsU where
  top := p.top
  active := fun i => decide (i ∈ p.active)

private theorem c106_le_sum_of_mem
    (i : Nat)
    (indices : List Nat)
    (hi : i ∈ indices) :
    i ≤ indices.sum := by
  induction indices with
  | nil =>
      simp at hi
  | cons head tail ih =>
      simp only [List.mem_cons] at hi
      simp only [List.sum_cons]
      rcases hi with rfl | hiTail
      · omega
      · have hle := ih hiTail
        omega

/-- The embedding preserves the pointwise bounded state space exactly. -/
theorem inInfiniteActiveStateSpaceU_infiniteActiveParamsUOfParamsU_iff
    (p : ParamsU)
    (x : StateU) :
    inInfiniteActiveStateSpaceU (infiniteActiveParamsUOfParamsU p) x ↔
      inStateSpaceU p x := by
  rfl

/-- The embedding preserves the active-coordinate fixed set exactly. -/
theorem inInfiniteActiveFixedSetU_infiniteActiveParamsUOfParamsU_iff
    (p : ParamsU)
    (x : StateU) :
    inInfiniteActiveFixedSetU (infiniteActiveParamsUOfParamsU p) x ↔
      inFixedSetU p x := by
  constructor
  · intro hfixed i hi
    apply hfixed i
    simp [infiniteActiveParamsUOfParamsU, hi]
  · intro hfixed i hiActive
    have hi : i ∈ p.active := by
      simpa [infiniteActiveParamsUOfParamsU] using hiActive
    exact hfixed i hi

/-- The embedded infinite-active update is the original finite-active update. -/
theorem updateInfiniteActiveU_infiniteActiveParamsUOfParamsU
    (p : ParamsU)
    (x : StateU) :
    updateInfiniteActiveU (infiniteActiveParamsUOfParamsU p) x =
      updateU p x := by
  funext i
  by_cases hi : i ∈ p.active
  · simp [updateInfiniteActiveU, infiniteActiveParamsUOfParamsU, updateU, hi]
  · simp [updateInfiniteActiveU, infiniteActiveParamsUOfParamsU, updateU, hi]

/-- The embedding preserves every time of the generated update trajectory. -/
theorem infiniteActiveUpdateTrajectoryU_infiniteActiveParamsUOfParamsU
    (p : ParamsU)
    (x : StateU) :
    ∀ t : Nat,
      infiniteActiveUpdateTrajectoryU
          (infiniteActiveParamsUOfParamsU p)
          x
          t =
        updateUTrajectory p x t := by
  intro t
  induction t with
  | zero =>
      rfl
  | succ t ih =>
      simp only [infiniteActiveUpdateTrajectoryU, updateUTrajectory]
      rw [ih, updateInfiniteActiveU_infiniteActiveParamsUOfParamsU]

/--
Every bounded state in the embedded finite-active model has exactly one finite
global ledger effect. The statement is expressed without a finite-support
premise on the target model; finiteness follows constructively from the source
list through the explicit cutoff `p.active.sum + 1`.
-/
theorem existsUnique_hasInfiniteActiveGlobalLedgerEffectU_infiniteActiveParamsUOfParamsU
    (p : ParamsU)
    (x : StateU)
    (hspace : inStateSpaceU p x) :
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
  have hspaceInfinite :
      inInfiniteActiveStateSpaceU (infiniteActiveParamsUOfParamsU p) x :=
    (inInfiniteActiveStateSpaceU_infiniteActiveParamsUOfParamsU_iff p x).2 hspace
  rw [
    existsUnique_hasInfiniteActiveGlobalLedgerEffectU_iff_eventuallyFixedActive
      (infiniteActiveParamsUOfParamsU p)
      x
      hspaceInfinite
  ]
  refine ⟨p.active.sum + 1, ?_⟩
  intro i hcutoff hiActive
  have hi : i ∈ p.active := by
    simpa [infiniteActiveParamsUOfParamsU] using hiActive
  have hle : i ≤ p.active.sum := c106_le_sum_of_mem i p.active hi
  omega

end UnrestrictedBridge
end VFH2
