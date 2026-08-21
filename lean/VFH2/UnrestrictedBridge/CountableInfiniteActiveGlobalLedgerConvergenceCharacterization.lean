import VFH2.UnrestrictedBridge.CountableInfiniteActiveGlobalLedgerEffect

/-!
# Countable Infinite-Active Global Ledger Convergence Characterization

This module characterizes finite convergence of the nonnegative infinite-active
ledger introduced in C103. A finite value exists exactly when all sufficiently
late active coordinates are already fixed. Every convergent value is the prefix
effect at such a cutoff, and that value is unique.

The active predicate remains an arbitrary Boolean function on `Nat`; no finite
support representation or enumeration is introduced.
-/

namespace VFH2
namespace UnrestrictedBridge

private theorem c104_infiniteActiveLedgerEffectPrefixU_succ
    (p : InfiniteActiveParamsU)
    (x : StateU)
    (n : Nat) :
    infiniteActiveLedgerEffectPrefixU p x (Nat.succ n) =
      infiniteActiveLedgerEffectPrefixU p x n +
        (if p.active n then p.top - x n else 0) := by
  simp [infiniteActiveLedgerEffectPrefixU, List.range_succ]

private theorem c104_prefix_eq_of_eventually_fixed_active
    (p : InfiniteActiveParamsU)
    (x : StateU)
    (cutoff : Nat)
    (hTail : ∀ i : Nat,
      cutoff ≤ i → p.active i = true → x i = p.top) :
    ∀ n : Nat,
      cutoff ≤ n →
        infiniteActiveLedgerEffectPrefixU p x n =
          infiniteActiveLedgerEffectPrefixU p x cutoff := by
  intro n hn
  induction n with
  | zero =>
      have hCutoffZero : cutoff = 0 := by omega
      subst cutoff
      rfl
  | succ n ih =>
      by_cases hEq : cutoff = Nat.succ n
      · subst cutoff
        rfl
      · have hle : cutoff ≤ n := by omega
        rw [c104_infiniteActiveLedgerEffectPrefixU_succ]
        rw [ih hle]
        cases hActive : p.active n with
        | false =>
            simp
        | true =>
            have hx : x n = p.top := hTail n hle hActive
            simp [hx]

private theorem c104_hasInfiniteActiveGlobalLedgerEffectU_unique
    (p : InfiniteActiveParamsU)
    (x : StateU)
    {effect₁ effect₂ : Nat}
    (h₁ : HasInfiniteActiveGlobalLedgerEffectU p x effect₁)
    (h₂ : HasInfiniteActiveGlobalLedgerEffectU p x effect₂) :
    effect₁ = effect₂ := by
  rcases h₁ with ⟨cutoff₁, hEventually₁⟩
  rcases h₂ with ⟨cutoff₂, hEventually₂⟩
  let n := Nat.max cutoff₁ cutoff₂
  have h₁n : cutoff₁ ≤ n := Nat.le_max_left _ _
  have h₂n : cutoff₂ ≤ n := Nat.le_max_right _ _
  calc
    effect₁ = infiniteActiveLedgerEffectPrefixU p x n :=
      (hEventually₁ n h₁n).symm
    _ = effect₂ := hEventually₂ n h₂n

/--
A natural number is the finite infinite-active global effect exactly when it is
the prefix value at a cutoff after which every active coordinate is fixed.
-/
theorem hasInfiniteActiveGlobalLedgerEffectU_iff_exists_eventuallyFixedActive_and_eq_prefix
    (p : InfiniteActiveParamsU)
    (x : StateU)
    (hspace : inInfiniteActiveStateSpaceU p x)
    (effect : Nat) :
    HasInfiniteActiveGlobalLedgerEffectU p x effect ↔
      ∃ cutoff : Nat,
        (∀ i : Nat,
          cutoff ≤ i → p.active i = true → x i = p.top) ∧
        effect = infiniteActiveLedgerEffectPrefixU p x cutoff := by
  constructor
  · rintro ⟨cutoff, hEventually⟩
    refine ⟨cutoff, ?_, (hEventually cutoff (by omega)).symm⟩
    intro i hiCutoff hiActive
    have hAtI := hEventually i hiCutoff
    have hAtSucc := hEventually (Nat.succ i) (by omega)
    rw [c104_infiniteActiveLedgerEffectPrefixU_succ] at hAtSucc
    rw [hAtI] at hAtSucc
    have hDeficit :
        (if p.active i then p.top - x i else 0) = 0 := by
      omega
    have hSub : p.top - x i = 0 := by
      simpa [hiActive] using hDeficit
    have hle : x i ≤ p.top := hspace i
    omega
  · rintro ⟨cutoff, hTail, rfl⟩
    refine ⟨cutoff, ?_⟩
    intro n hn
    exact c104_prefix_eq_of_eventually_fixed_active p x cutoff hTail n hn

/--
The infinite-active ledger has a unique finite natural value exactly when all
sufficiently late active coordinates are fixed.
-/
theorem existsUnique_hasInfiniteActiveGlobalLedgerEffectU_iff_eventuallyFixedActive
    (p : InfiniteActiveParamsU)
    (x : StateU)
    (hspace : inInfiniteActiveStateSpaceU p x) :
    (∃ effect : Nat,
      HasInfiniteActiveGlobalLedgerEffectU p x effect ∧
        ∀ candidate : Nat,
          HasInfiniteActiveGlobalLedgerEffectU p x candidate →
            candidate = effect) ↔
      ∃ cutoff : Nat,
        ∀ i : Nat,
          cutoff ≤ i → p.active i = true → x i = p.top := by
  constructor
  · rintro ⟨effect, hEffect, hUnique⟩
    rcases
        (hasInfiniteActiveGlobalLedgerEffectU_iff_exists_eventuallyFixedActive_and_eq_prefix
          p x hspace effect).1 hEffect with
      ⟨cutoff, hTail, hValue⟩
    exact ⟨cutoff, hTail⟩
  · rintro ⟨cutoff, hTail⟩
    let effect := infiniteActiveLedgerEffectPrefixU p x cutoff
    have hEffect : HasInfiniteActiveGlobalLedgerEffectU p x effect :=
      (hasInfiniteActiveGlobalLedgerEffectU_iff_exists_eventuallyFixedActive_and_eq_prefix
        p x hspace effect).2 ⟨cutoff, hTail, rfl⟩
    refine ⟨effect, hEffect, ?_⟩
    intro candidate hCandidate
    exact
      c104_hasInfiniteActiveGlobalLedgerEffectU_unique
        p x hCandidate hEffect

end UnrestrictedBridge
end VFH2
