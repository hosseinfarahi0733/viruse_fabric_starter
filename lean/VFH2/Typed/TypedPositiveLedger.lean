import VFH2.Typed.TypedUpdateMonotone

/-!
# VF-H2 v10 Typed Positive Ledger Effect

This file proves the positive ledger-effect half for the current v10 typed
scaffold.

Boundary:
- This proves positive typed ledger effect for nonfixed typed states in the
  current v10 scaffold.
- It does not prove the full Viruse Fabric theory.
- It does not prove unrestricted TTP-VF-H2-004.
- It is not empirical validation.
- It is not biological validation.

Purpose:
The v10 typed scaffold already proves:
1. typed update never decreases any coordinate;
2. nonfixed states have at least one coordinate that strictly increases.

This file lifts those coordinate-level facts to the typed ledger sum.
-/

namespace VFH2
namespace Typed

/-- Local list-sum helper matching the foldl shape used by `typedLedger`. -/
private def natListSum
    (xs : List Nat) : Nat :=
  xs.foldl (fun acc a => acc + a) 0

/-- Foldl-add from any accumulator equals accumulator plus foldl-add from zero. -/
private theorem foldl_add_eq_acc_add_foldl_zero
    (xs : List Nat)
    (acc : Nat) :
    xs.foldl (fun acc a => acc + a) acc =
      acc + xs.foldl (fun acc a => acc + a) 0 := by
  induction xs generalizing acc with
  | nil =>
      simp
  | cons x xs ih =>
      simp [List.foldl]
      rw [ih (acc + x), ih x]
      omega

/-- Sum of a cons list. -/
private theorem natListSum_cons
    (a : Nat)
    (xs : List Nat) :
    natListSum (a :: xs) = a + natListSum xs := by
  unfold natListSum
  simp [List.foldl]
  exact foldl_add_eq_acc_add_foldl_zero xs a

/-- Sum of an empty list. -/
private theorem natListSum_nil :
    natListSum [] = 0 := by
  rfl

/-- Sum over `List.ofFn` decomposes into head plus tail. -/
private theorem natListSum_ofFn_succ
    {n : Nat}
    (f : Fin (n + 1) → Nat) :
    natListSum (List.ofFn f) =
      f ⟨0, Nat.succ_pos n⟩
        + natListSum (List.ofFn (fun i : Fin n => f i.succ)) := by
  unfold natListSum
  simp
  exact foldl_add_eq_acc_add_foldl_zero
    (List.ofFn (fun i : Fin n => f i.succ))
    (f ⟨0, Nat.succ_pos n⟩)

/-- Pointwise nondecrease over a finite typed index family lifts to list-sum
nondecrease.
-/
private theorem natListSum_ofFn_le_of_pointwise
    {n : Nat}
    (f g : Fin n → Nat)
    (hle : ∀ i : Fin n, f i ≤ g i) :
    natListSum (List.ofFn f) ≤ natListSum (List.ofFn g) := by
  induction n with
  | zero =>
      simp [natListSum]
  | succ n ih =>
      rw [natListSum_ofFn_succ f, natListSum_ofFn_succ g]
      have hhead : f ⟨0, Nat.succ_pos n⟩ ≤ g ⟨0, Nat.succ_pos n⟩ :=
        hle ⟨0, Nat.succ_pos n⟩
      have htail :
          natListSum (List.ofFn (fun i : Fin n => f i.succ)) ≤
          natListSum (List.ofFn (fun i : Fin n => g i.succ)) := by
        exact ih
          (fun i : Fin n => f i.succ)
          (fun i : Fin n => g i.succ)
          (fun i => hle i.succ)
      omega

/-- If a strict witness exists in the tail of a successor finite family, expose
it as a strict witness for the tail family.
-/
private theorem exists_tail_strict_of_not_head_strict
    {n : Nat}
    {f g : Fin (n + 1) → Nat}
    (hhead_not : ¬ f ⟨0, Nat.succ_pos n⟩ < g ⟨0, Nat.succ_pos n⟩)
    (hwit : ∃ i : Fin (n + 1), f i < g i) :
    ∃ j : Fin n, f j.succ < g j.succ := by
  obtain ⟨i, hi⟩ := hwit
  rcases i with ⟨k, hk⟩
  cases k with
  | zero =>
      exact False.elim (hhead_not (by simpa using hi))
  | succ k =>
      have hk_tail : k < n := Nat.lt_of_succ_lt_succ hk
      refine ⟨⟨k, hk_tail⟩, ?_⟩
      simpa using hi

/-- Pointwise nondecrease plus one strict witness over a finite typed index
family lifts to strict list-sum increase.
-/
private theorem natListSum_ofFn_lt_of_pointwise_and_exists
    {n : Nat}
    (f g : Fin n → Nat)
    (hle : ∀ i : Fin n, f i ≤ g i)
    (hwit : ∃ i : Fin n, f i < g i) :
    natListSum (List.ofFn f) < natListSum (List.ofFn g) := by
  induction n with
  | zero =>
      obtain ⟨i, _hi⟩ := hwit
      exact False.elim (Fin.elim0 i)
  | succ n ih =>
      rw [natListSum_ofFn_succ f, natListSum_ofFn_succ g]
      by_cases hhead :
          f ⟨0, Nat.succ_pos n⟩ < g ⟨0, Nat.succ_pos n⟩
      · have htail_le :
            natListSum (List.ofFn (fun i : Fin n => f i.succ)) ≤
            natListSum (List.ofFn (fun i : Fin n => g i.succ)) := by
          exact natListSum_ofFn_le_of_pointwise
            (fun i : Fin n => f i.succ)
            (fun i : Fin n => g i.succ)
            (fun i => hle i.succ)
        omega
      · have htail_wit :
            ∃ j : Fin n, f j.succ < g j.succ :=
          exists_tail_strict_of_not_head_strict hhead hwit
        have htail_lt :
            natListSum (List.ofFn (fun i : Fin n => f i.succ)) <
            natListSum (List.ofFn (fun i : Fin n => g i.succ)) := by
          exact ih
            (fun i : Fin n => f i.succ)
            (fun i : Fin n => g i.succ)
            (fun i => hle i.succ)
            htail_wit
        have hhead_le :
            f ⟨0, Nat.succ_pos n⟩ ≤ g ⟨0, Nat.succ_pos n⟩ :=
          hle ⟨0, Nat.succ_pos n⟩
        omega

/-- If every typed coordinate is nondecreasing and at least one strictly
increases, then the typed ledger strictly increases.
-/
theorem typedLedger_lt_update_of_pointwise_and_exists
    {p : TypedRestrictedParams}
    {x : p.State}
    (hle :
      ∀ i : WidthIndex p.d,
        (x i).val ≤ (typedUpdateState p x i).val)
    (hwit :
      ∃ i : WidthIndex p.d,
        (x i).val < (typedUpdateState p x i).val) :
    typedLedger p x < typedLedger p (typedUpdateState p x) := by
  unfold typedLedger typedLedgerValues
  exact natListSum_ofFn_lt_of_pointwise_and_exists
    (fun i : WidthIndex p.d => (x i).val)
    (fun i : WidthIndex p.d => (typedUpdateState p x i).val)
    hle
    hwit

/-- Nonfixed typed states strictly increase the typed ledger under update. -/
theorem typedLedger_lt_update_of_not_fixed
    {p : TypedRestrictedParams}
    {x : p.State}
    (hnotfixed : ¬ TypedFixedSet p x) :
    typedLedger p x < typedLedger p (typedUpdateState p x) := by
  have hpre :=
    typed_nonfixed_pointwise_and_strict_witness hnotfixed
  obtain ⟨hle, hwit_active⟩ := hpre
  have hwit :
      ∃ i : WidthIndex p.d,
        (x i).val < (typedUpdateState p x i).val := by
    obtain ⟨i, _hi, hlt⟩ := hwit_active
    exact ⟨i, hlt⟩
  exact typedLedger_lt_update_of_pointwise_and_exists hle hwit

/-- Nonfixed typed states have positive typed ledger effect. -/
theorem typedLedgerEffect_pos_of_not_fixed
    {p : TypedRestrictedParams}
    {x : p.State}
    (hnotfixed : ¬ TypedFixedSet p x) :
    0 < typedLedgerEffect p x := by
  have hlt :
      typedLedger p x < typedLedger p (typedUpdateState p x) :=
    typedLedger_lt_update_of_not_fixed hnotfixed
  unfold typedLedgerEffect
  omega

/-- Positive-effect target for the current v10 typed scaffold. -/
def typedPositiveLedgerEffectTarget
    (p : TypedRestrictedParams)
    (x : p.State) : Prop :=
  ¬ TypedFixedSet p x → 0 < typedLedgerEffect p x

/-- The current v10 typed scaffold proves positive ledger effect for nonfixed
typed states.
-/
theorem typedPositiveLedgerEffectTarget_proved
    (p : TypedRestrictedParams)
    (x : p.State) :
    typedPositiveLedgerEffectTarget p x := by
  intro hnotfixed
  exact typedLedgerEffect_pos_of_not_fixed hnotfixed

end Typed
end VFH2
