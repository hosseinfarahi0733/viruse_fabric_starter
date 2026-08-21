import VFH2.UnrestrictedBridge.CountableInfiniteActiveGlobalLedgerPositiveCharacterization

/-!
# Countable Infinite-Active Global Ledger Strict Comparison

This module compares two convergent nonnegative ledgers for the same
countably indexed Boolean-active parameters.  If the lower state is pointwise
below the upper state on active coordinates, then the upper state's remaining
effect is strictly smaller exactly when the two states differ strictly at an
active coordinate.

The upper state-space hypothesis bounds both active values by the common top;
no lower-state-space hypothesis is needed because active pointwise dominance
then bounds every lower coordinate that contributes to a prefix.  Inactive
coordinates never contribute.  Convergence remains explicit for both named
effects, and the active predicate may have genuinely infinite support.

This is a proof-only comparison inside the countable mathematical model.  It
does not identify the ledger with an empirical observable or compare memory
and null interventions.
-/

namespace VFH2
namespace UnrestrictedBridge

private theorem c124_sum_map_le_sum_map
    (support : List Nat)
    (f g : Nat → Nat)
    (hLe : ∀ i : Nat, i ∈ support → f i ≤ g i) :
    (support.map f).sum ≤ (support.map g).sum := by
  induction support with
  | nil =>
      simp
  | cons head tail ih =>
      have hHead : f head ≤ g head := hLe head (by simp)
      have hTail : ∀ i : Nat, i ∈ tail → f i ≤ g i := by
        intro i hi
        exact hLe i (by simp [hi])
      simp only [List.map_cons, List.sum_cons]
      exact Nat.add_le_add hHead (ih hTail)

private theorem c124_sum_map_lt_sum_map_of_mem_lt
    (support : List Nat)
    (f g : Nat → Nat)
    (hLe : ∀ i : Nat, i ∈ support → f i ≤ g i)
    (witness : Nat)
    (hWitnessMem : witness ∈ support)
    (hWitnessLt : f witness < g witness) :
    (support.map f).sum < (support.map g).sum := by
  induction support with
  | nil =>
      simp at hWitnessMem
  | cons head tail ih =>
      have hHead : f head ≤ g head := hLe head (by simp)
      have hTailLe : ∀ i : Nat, i ∈ tail → f i ≤ g i := by
        intro i hi
        exact hLe i (by simp [hi])
      simp only [List.mem_cons] at hWitnessMem
      simp only [List.map_cons, List.sum_cons]
      rcases hWitnessMem with rfl | hWitnessTail
      · have hTailSumLe :
            (tail.map f).sum ≤ (tail.map g).sum :=
          c124_sum_map_le_sum_map tail f g hTailLe
        omega
      · have hTailSumLt :
            (tail.map f).sum < (tail.map g).sum :=
          ih hTailLe hWitnessTail
        omega

private theorem c124_exists_mem_lt_of_sum_map_lt
    (support : List Nat)
    (f g : Nat → Nat)
    (hLe : ∀ i : Nat, i ∈ support → f i ≤ g i)
    (hSumLt : (support.map f).sum < (support.map g).sum) :
    ∃ i : Nat, i ∈ support ∧ f i < g i := by
  induction support with
  | nil =>
      simp at hSumLt
  | cons head tail ih =>
      have hHead : f head ≤ g head := hLe head (by simp)
      have hTailLe : ∀ i : Nat, i ∈ tail → f i ≤ g i := by
        intro i hi
        exact hLe i (by simp [hi])
      by_cases hHeadLt : f head < g head
      · exact ⟨head, by simp, hHeadLt⟩
      · have hHeadEq : f head = g head := by omega
        simp only [List.map_cons, List.sum_cons, hHeadEq] at hSumLt
        have hTailSumLt :
            (tail.map f).sum < (tail.map g).sum := by
          omega
        rcases ih hTailLe hTailSumLt with ⟨i, hi, hlt⟩
        exact ⟨i, by simp [hi], hlt⟩

private theorem c124_activeDeficit_le_of_le
    (p : InfiniteActiveParamsU)
    (lower upper : StateU)
    (hUpperSpace : inInfiniteActiveStateSpaceU p upper)
    (hActiveLe :
      ∀ i : Nat, p.active i = true → lower i ≤ upper i)
    (i : Nat) :
    (if p.active i then p.top - upper i else 0) ≤
      (if p.active i then p.top - lower i else 0) := by
  cases hActive : p.active i with
  | false =>
      simp
  | true =>
      have hle : lower i ≤ upper i := hActiveLe i hActive
      have hUpperBound : upper i ≤ p.top := hUpperSpace i
      simp
      omega

private theorem c124_activeDeficit_lt_iff_lt
    (p : InfiniteActiveParamsU)
    (lower upper : StateU)
    (hUpperSpace : inInfiniteActiveStateSpaceU p upper)
    (hActiveLe :
      ∀ i : Nat, p.active i = true → lower i ≤ upper i)
    (i : Nat)
    (hActive : p.active i = true) :
    (if p.active i then p.top - upper i else 0) <
        (if p.active i then p.top - lower i else 0) ↔
      lower i < upper i := by
  have hle : lower i ≤ upper i := hActiveLe i hActive
  have hUpperBound : upper i ≤ p.top := hUpperSpace i
  simp only [hActive, if_true]
  omega

/--
Under active-coordinate pointwise dominance, two convergent global effects
are strictly ordered exactly when the states are strictly ordered at some
active coordinate.  The direction is contravariant because the effect sums
the remaining deficits from `p.top`.
-/
theorem hasInfiniteActiveGlobalLedgerEffectU_lt_iff_exists_active_lt_of_active_pointwise_le
    (p : InfiniteActiveParamsU)
    (lower upper : StateU)
    (hUpperSpace : inInfiniteActiveStateSpaceU p upper)
    (lowerEffect upperEffect : Nat)
    (hLowerEffect :
      HasInfiniteActiveGlobalLedgerEffectU p lower lowerEffect)
    (hUpperEffect :
      HasInfiniteActiveGlobalLedgerEffectU p upper upperEffect)
    (hActiveLe :
      ∀ i : Nat, p.active i = true → lower i ≤ upper i) :
    upperEffect < lowerEffect ↔
      ∃ i, p.active i = true ∧ lower i < upper i := by
  rcases hLowerEffect with ⟨lowerCutoff, hLowerEventually⟩
  rcases hUpperEffect with ⟨upperCutoff, hUpperEventually⟩
  constructor
  · intro hEffectLt
    let cutoff := Nat.max lowerCutoff upperCutoff
    have hLowerCutoff : lowerCutoff ≤ cutoff := Nat.le_max_left _ _
    have hUpperCutoff : upperCutoff ≤ cutoff := Nat.le_max_right _ _
    have hPrefixLt :
        infiniteActiveLedgerEffectPrefixU p upper cutoff <
          infiniteActiveLedgerEffectPrefixU p lower cutoff := by
      calc
        infiniteActiveLedgerEffectPrefixU p upper cutoff = upperEffect :=
          hUpperEventually cutoff hUpperCutoff
        _ < lowerEffect := hEffectLt
        _ = infiniteActiveLedgerEffectPrefixU p lower cutoff :=
          (hLowerEventually cutoff hLowerCutoff).symm
    unfold infiniteActiveLedgerEffectPrefixU at hPrefixLt
    let upperDeficit := fun i : Nat =>
      if p.active i then p.top - upper i else 0
    let lowerDeficit := fun i : Nat =>
      if p.active i then p.top - lower i else 0
    have hDeficitLe : ∀ i : Nat, i ∈ List.range cutoff →
        upperDeficit i ≤ lowerDeficit i := by
      intro i hi
      exact
        c124_activeDeficit_le_of_le
          p lower upper hUpperSpace hActiveLe i
    have hMappedLt :
        (List.range cutoff |>.map upperDeficit).sum <
          (List.range cutoff |>.map lowerDeficit).sum := by
      simpa [upperDeficit, lowerDeficit] using hPrefixLt
    rcases
        c124_exists_mem_lt_of_sum_map_lt
          (List.range cutoff)
          upperDeficit
          lowerDeficit
          hDeficitLe
          hMappedLt with
      ⟨i, hiRange, hDeficitLt⟩
    cases hActive : p.active i with
    | false =>
        simp [upperDeficit, lowerDeficit, hActive] at hDeficitLt
    | true =>
        refine ⟨i, hActive, ?_⟩
        exact
          (c124_activeDeficit_lt_iff_lt
            p lower upper hUpperSpace hActiveLe i hActive).1
            (by simpa [upperDeficit, lowerDeficit] using hDeficitLt)
  · rintro ⟨witness, hWitnessActive, hWitnessLt⟩
    let cutoff :=
      Nat.max (Nat.max lowerCutoff upperCutoff) (Nat.succ witness)
    have hLowerCutoff : lowerCutoff ≤ cutoff := by
      have hInner : lowerCutoff ≤ Nat.max lowerCutoff upperCutoff :=
        Nat.le_max_left _ _
      have hOuter : Nat.max lowerCutoff upperCutoff ≤ cutoff :=
        Nat.le_max_left _ _
      omega
    have hUpperCutoff : upperCutoff ≤ cutoff := by
      have hInner : upperCutoff ≤ Nat.max lowerCutoff upperCutoff :=
        Nat.le_max_right _ _
      have hOuter : Nat.max lowerCutoff upperCutoff ≤ cutoff :=
        Nat.le_max_left _ _
      omega
    have hWitnessLtCutoff : witness < cutoff := by
      have hSuccLe : Nat.succ witness ≤ cutoff := Nat.le_max_right _ _
      omega
    let upperDeficit := fun i : Nat =>
      if p.active i then p.top - upper i else 0
    let lowerDeficit := fun i : Nat =>
      if p.active i then p.top - lower i else 0
    have hDeficitLe : ∀ i : Nat, i ∈ List.range cutoff →
        upperDeficit i ≤ lowerDeficit i := by
      intro i hi
      exact
        c124_activeDeficit_le_of_le
          p lower upper hUpperSpace hActiveLe i
    have hWitnessDeficitLt :
        upperDeficit witness < lowerDeficit witness := by
      exact
        (c124_activeDeficit_lt_iff_lt
          p lower upper hUpperSpace hActiveLe witness hWitnessActive).2
          hWitnessLt
    have hPrefixLt :
        infiniteActiveLedgerEffectPrefixU p upper cutoff <
          infiniteActiveLedgerEffectPrefixU p lower cutoff := by
      unfold infiniteActiveLedgerEffectPrefixU
      exact
        c124_sum_map_lt_sum_map_of_mem_lt
          (List.range cutoff)
          upperDeficit
          lowerDeficit
          hDeficitLe
          witness
          (List.mem_range.mpr hWitnessLtCutoff)
          hWitnessDeficitLt
    calc
      upperEffect = infiniteActiveLedgerEffectPrefixU p upper cutoff :=
        (hUpperEventually cutoff hUpperCutoff).symm
      _ < infiniteActiveLedgerEffectPrefixU p lower cutoff := hPrefixLt
      _ = lowerEffect := hLowerEventually cutoff hLowerCutoff

end UnrestrictedBridge
end VFH2
