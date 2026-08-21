import VFH2.UnrestrictedBridge.CountableInfiniteActiveGlobalLedgerConvergenceCharacterization

/-!
# Countable Infinite-Active Global Ledger Positive Characterization

This module gives the strict-positive branch of the convergent countable
nonnegative ledger.  Once a finite global effect exists, it is positive
exactly when some active coordinate remains strictly below the common top.

The active predicate may have genuinely infinite support.  Convergence of the
named effect remains explicit, and no finite-support representation is
introduced.  This is a theorem about the bounded countable mathematical model;
it does not identify the ledger with an experimental observable or compare
memory and null interventions.
-/

namespace VFH2
namespace UnrestrictedBridge

private theorem c123_sum_pos_iff_exists_pos (values : List Nat) :
    0 < values.sum ↔ ∃ value : Nat, value ∈ values ∧ 0 < value := by
  induction values with
  | nil =>
      simp
  | cons head tail ih =>
      simp only [List.sum_cons, List.mem_cons]
      constructor
      · intro hpos
        by_cases hHeadPos : 0 < head
        · exact ⟨head, Or.inl rfl, hHeadPos⟩
        · have hHeadZero : head = 0 := by omega
          have hTailPos : 0 < tail.sum := by omega
          rcases ih.mp hTailPos with ⟨value, hmem, hValuePos⟩
          exact ⟨value, Or.inr hmem, hValuePos⟩
      · rintro ⟨value, rfl | hmem, hValuePos⟩
        · omega
        · have hTailPos : 0 < tail.sum :=
            ih.mpr ⟨value, hmem, hValuePos⟩
          omega

/--
A convergent finite global ledger effect is strictly positive exactly when an
active coordinate has a strictly positive deficit from the common top.
-/
theorem hasInfiniteActiveGlobalLedgerEffectU_pos_iff_exists_active_lt_top
    (p : InfiniteActiveParamsU)
    (x : StateU)
    (hspace : inInfiniteActiveStateSpaceU p x)
    (effect : Nat)
    (hEffect : HasInfiniteActiveGlobalLedgerEffectU p x effect) :
    0 < effect ↔
      ∃ i : Nat, p.active i = true ∧ x i < p.top := by
  rcases
      (hasInfiniteActiveGlobalLedgerEffectU_iff_exists_eventuallyFixedActive_and_eq_prefix
        p x hspace effect).1 hEffect with
    ⟨cutoff, hTail, hValue⟩
  constructor
  · intro hPositive
    rw [hValue] at hPositive
    unfold infiniteActiveLedgerEffectPrefixU at hPositive
    rcases (c123_sum_pos_iff_exists_pos _).1 hPositive with
      ⟨deficit, hDeficitMem, hDeficitPos⟩
    rcases List.mem_map.mp hDeficitMem with ⟨i, hiRange, rfl⟩
    cases hiActive : p.active i with
    | false =>
        simp [hiActive] at hDeficitPos
    | true =>
        have hle : x i ≤ p.top := hspace i
        have hlt : x i < p.top := by
          simp [hiActive] at hDeficitPos
          omega
        exact ⟨i, hiActive, hlt⟩
  · rintro ⟨i, hiActive, hlt⟩
    have hiCutoff : i < cutoff := by
      by_cases hiLt : i < cutoff
      · exact hiLt
      · have hCutoffLe : cutoff ≤ i := by omega
        have hiTop : x i = p.top := hTail i hCutoffLe hiActive
        omega
    rw [hValue]
    unfold infiniteActiveLedgerEffectPrefixU
    apply (c123_sum_pos_iff_exists_pos _).2
    refine ⟨p.top - x i, ?_, by omega⟩
    exact
      List.mem_map.mpr
        ⟨i, List.mem_range.mpr hiCutoff, by simp [hiActive]⟩

end UnrestrictedBridge
end VFH2
