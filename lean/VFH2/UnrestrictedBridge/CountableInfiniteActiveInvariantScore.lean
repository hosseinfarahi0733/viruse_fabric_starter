import VFH2.UnrestrictedBridge.CountableInfiniteActiveOneStepSemanticClosure

/-!
# Countable Infinite-Active Invariant Score

The concrete infinite-active update changes exactly the selected coordinates.
This module therefore defines its semantic key as the complete inactive
projection and defines a finite score by summing that key below a cutoff.

The update preserves the key and every cutoff score by computation.  For a
bounded state, the score also lies in the derived natural interval
`[0, cutoff * p.top]`.  No score-preservation or score-bound premise is used.
-/

namespace VFH2
namespace UnrestrictedBridge

/-- The complete inactive projection of a countably indexed state. -/
def infiniteActiveInactiveKeyU
    (p : InfiniteActiveParamsU)
    (x : StateU) : StateU :=
  fun i => if p.active i then 0 else x i

/-- The concrete update preserves the complete inactive projection exactly. -/
theorem infiniteActiveInactiveKeyU_updateInfiniteActiveU
    (p : InfiniteActiveParamsU)
    (x : StateU) :
    infiniteActiveInactiveKeyU p (updateInfiniteActiveU p x) =
      infiniteActiveInactiveKeyU p x := by
  funext i
  cases hi : p.active i with
  | false =>
      simp [infiniteActiveInactiveKeyU, updateInfiniteActiveU, hi]
  | true =>
      simp [infiniteActiveInactiveKeyU, hi]

/-- The semantic score is the inactive-key sum below a finite cutoff. -/
def infiniteActiveInvariantScorePrefixU
    (p : InfiniteActiveParamsU)
    (x : StateU)
    (cutoff : Nat) : Nat :=
  ((List.range cutoff).map (infiniteActiveInactiveKeyU p x)).sum

/-- Every finite semantic score is preserved by the concrete update. -/
theorem infiniteActiveInvariantScorePrefixU_updateInfiniteActiveU
    (p : InfiniteActiveParamsU)
    (x : StateU)
    (cutoff : Nat) :
    infiniteActiveInvariantScorePrefixU
        p
        (updateInfiniteActiveU p x)
        cutoff =
      infiniteActiveInvariantScorePrefixU p x cutoff := by
  unfold infiniteActiveInvariantScorePrefixU
  rw [infiniteActiveInactiveKeyU_updateInfiniteActiveU]

/-- The inactive key remains pointwise bounded whenever the state is bounded. -/
theorem infiniteActiveInactiveKeyU_le_top
    (p : InfiniteActiveParamsU)
    (x : StateU)
    (hspace : inInfiniteActiveStateSpaceU p x)
    (i : Nat) :
    infiniteActiveInactiveKeyU p x i ≤ p.top := by
  cases hi : p.active i with
  | false =>
      simpa [infiniteActiveInactiveKeyU, hi] using hspace i
  | true =>
      simp [infiniteActiveInactiveKeyU, hi]

private theorem c109_sum_map_le_length_mul
    (values : Nat → Nat)
    (top : Nat)
    (hbound : ∀ i : Nat, values i ≤ top) :
    ∀ indices : List Nat,
      (indices.map values).sum ≤ indices.length * top := by
  intro indices
  induction indices with
  | nil =>
      simp
  | cons i tail ih =>
      have hi : values i ≤ top := hbound i
      simp only [
        List.map_cons,
        List.sum_cons,
        List.length_cons,
        Nat.succ_mul
      ]
      omega

/-- Boundedness derives the natural upper score bound at every cutoff. -/
theorem infiniteActiveInvariantScorePrefixU_le_cutoff_mul_top
    (p : InfiniteActiveParamsU)
    (x : StateU)
    (hspace : inInfiniteActiveStateSpaceU p x)
    (cutoff : Nat) :
    infiniteActiveInvariantScorePrefixU p x cutoff ≤
      cutoff * p.top := by
  unfold infiniteActiveInvariantScorePrefixU
  have hBound :=
    c109_sum_map_le_length_mul
      (infiniteActiveInactiveKeyU p x)
      p.top
      (infiniteActiveInactiveKeyU_le_top p x hspace)
      (List.range cutoff)
  simpa using hBound

/-- The integer embedding of every semantic score has natural lower bound zero. -/
theorem infiniteActiveInvariantScorePrefixU_int_nonneg
    (p : InfiniteActiveParamsU)
    (x : StateU)
    (cutoff : Nat) :
    (0 : Int) ≤
      (infiniteActiveInvariantScorePrefixU p x cutoff : Int) := by
  exact Int.natCast_nonneg _

/-- The natural upper bound transports exactly to the integer score window. -/
theorem infiniteActiveInvariantScorePrefixU_int_le_cutoff_mul_top
    (p : InfiniteActiveParamsU)
    (x : StateU)
    (hspace : inInfiniteActiveStateSpaceU p x)
    (cutoff : Nat) :
    (infiniteActiveInvariantScorePrefixU p x cutoff : Int) ≤
      ((cutoff * p.top : Nat) : Int) := by
  exact_mod_cast
    infiniteActiveInvariantScorePrefixU_le_cutoff_mul_top
      p x hspace cutoff

/--
The updated score lies in the same derived interval, with preservation and
bounds all discharged from the concrete semantics.
-/
theorem infiniteActiveInvariantScorePrefixU_update_window
    (p : InfiniteActiveParamsU)
    (x : StateU)
    (hspace : inInfiniteActiveStateSpaceU p x)
    (cutoff : Nat) :
    (0 : Int) ≤
        (infiniteActiveInvariantScorePrefixU
          p
          (updateInfiniteActiveU p x)
          cutoff : Int) ∧
      (infiniteActiveInvariantScorePrefixU
          p
          (updateInfiniteActiveU p x)
          cutoff : Int) ≤
        ((cutoff * p.top : Nat) : Int) := by
  rw [infiniteActiveInvariantScorePrefixU_updateInfiniteActiveU]
  exact ⟨
    infiniteActiveInvariantScorePrefixU_int_nonneg p x cutoff,
    infiniteActiveInvariantScorePrefixU_int_le_cutoff_mul_top
      p x hspace cutoff
  ⟩

end UnrestrictedBridge
end VFH2
