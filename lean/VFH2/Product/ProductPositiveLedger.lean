import VFH2.Product.ProductFixedZero

/-!
# VF-H2 v11 Product Positive Ledger Effect

This file proves the positive ledger-effect half for the current v11
product-index typed scaffold.

Boundary:
- This proves positive product ledger effect for nonfixed product states in the
  current v11 scaffold.
- It does not prove the product restricted bridge theorem.
- It does not prove the full Viruse Fabric theory.
- It does not prove unrestricted TTP-VF-H2-004.
- It is not empirical validation.
- It is not biological validation.

Purpose:
The v11 product scaffold already proves:
1. product update never decreases any coordinate;
2. nonfixed states have at least one product coordinate that strictly increases.

This file lifts those coordinate-level facts to the product ledger sum.
-/

namespace VFH2

/-- Local list-sum helper matching the foldl shape used by `productLedger`. -/
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

/-- Sum over append decomposes additively. -/
private theorem natListSum_append
    (xs ys : List Nat) :
    natListSum (xs ++ ys) = natListSum xs + natListSum ys := by
  induction xs with
  | nil =>
      simp [natListSum]
  | cons x xs ih =>
      calc
        natListSum ((x :: xs) ++ ys)
            = natListSum (x :: (xs ++ ys)) := by
              rfl
        _ = x + natListSum (xs ++ ys) := by
              exact natListSum_cons x (xs ++ ys)
        _ = x + (natListSum xs + natListSum ys) := by
              rw [ih]
        _ = (x + natListSum xs) + natListSum ys := by
              omega
        _ = natListSum (x :: xs) + natListSum ys := by
              rw [natListSum_cons x xs]

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

/-- Pointwise nondecrease over a finite index family lifts to list-sum nondecrease. -/
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

/-- If a strict witness is not at the head, it is in the tail. -/
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

/-- Pointwise nondecrease plus one strict witness lifts to strict list-sum increase. -/
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

/-- Every `TimeLayer` is one of the three named layers. -/
private theorem timeLayer_eq_t1_or_t2_or_t3
    (t : TimeLayer) :
    t = TimeLayer.t1 ∨ t = TimeLayer.t2 ∨ t = TimeLayer.t3 := by
  rcases t with ⟨k, hk⟩
  cases k with
  | zero =>
      left
      apply Fin.ext
      rfl
  | succ k =>
      cases k with
      | zero =>
          right
          left
          apply Fin.ext
          rfl
      | succ k =>
          cases k with
          | zero =>
              right
              right
              apply Fin.ext
              rfl
          | succ k =>
              omega

/-- Product ledger equals the sum of the three explicit time-layer sums. -/
private theorem productLedger_eq_time_sums
    (p : ProductRestrictedParams)
    (x : p.State) :
    productLedger p x =
      natListSum (productLedgerValuesAtTime p x TimeLayer.t1) +
      natListSum (productLedgerValuesAtTime p x TimeLayer.t2) +
      natListSum (productLedgerValuesAtTime p x TimeLayer.t3) := by
  unfold productLedger
  change natListSum (productLedgerValues p x) =
      natListSum (productLedgerValuesAtTime p x TimeLayer.t1) +
      natListSum (productLedgerValuesAtTime p x TimeLayer.t2) +
      natListSum (productLedgerValuesAtTime p x TimeLayer.t3)
  unfold productLedgerValues
  rw [natListSum_append, natListSum_append]

/-- One time-layer sum is nondecreasing under product update. -/
private theorem productLedgerTimeSum_le_update
    {p : ProductRestrictedParams}
    {x : p.State}
    (hle :
      ∀ i : ProductIndex p.d,
        (x i).val ≤ (productUpdateState p x i).val)
    (t : TimeLayer) :
    natListSum (productLedgerValuesAtTime p x t) ≤
      natListSum (productLedgerValuesAtTime p (productUpdateState p x) t) := by
  unfold productLedgerValuesAtTime
  exact natListSum_ofFn_le_of_pointwise
    (fun s : SpaceIndex p.d => (x (t, s)).val)
    (fun s : SpaceIndex p.d => (productUpdateState p x (t, s)).val)
    (fun s => hle (t, s))

/-- A strict witness at one product coordinate gives strict increase for its time-layer sum. -/
private theorem productLedgerTimeSum_lt_update_of_witness
    {p : ProductRestrictedParams}
    {x : p.State}
    (hle :
      ∀ i : ProductIndex p.d,
        (x i).val ≤ (productUpdateState p x i).val)
    (t : TimeLayer)
    (s : SpaceIndex p.d)
    (hlt : (x (t, s)).val < (productUpdateState p x (t, s)).val) :
    natListSum (productLedgerValuesAtTime p x t) <
      natListSum (productLedgerValuesAtTime p (productUpdateState p x) t) := by
  unfold productLedgerValuesAtTime
  exact natListSum_ofFn_lt_of_pointwise_and_exists
    (fun r : SpaceIndex p.d => (x (t, r)).val)
    (fun r : SpaceIndex p.d => (productUpdateState p x (t, r)).val)
    (fun r => hle (t, r))
    ⟨s, hlt⟩

/-- If every product coordinate is nondecreasing and at least one strictly increases, then the ledger strictly increases. -/
theorem productLedger_lt_update_of_pointwise_and_exists
    {p : ProductRestrictedParams}
    {x : p.State}
    (hle :
      ∀ i : ProductIndex p.d,
        (x i).val ≤ (productUpdateState p x i).val)
    (hwit :
      ∃ i : ProductIndex p.d,
        (x i).val < (productUpdateState p x i).val) :
    productLedger p x < productLedger p (productUpdateState p x) := by
  have ht1_le := productLedgerTimeSum_le_update hle TimeLayer.t1
  have ht2_le := productLedgerTimeSum_le_update hle TimeLayer.t2
  have ht3_le := productLedgerTimeSum_le_update hle TimeLayer.t3
  obtain ⟨i, hi_lt⟩ := hwit
  rcases i with ⟨t, s⟩
  have ht_lt := productLedgerTimeSum_lt_update_of_witness hle t s hi_lt
  rw [productLedger_eq_time_sums p x]
  rw [productLedger_eq_time_sums p (productUpdateState p x)]
  rcases timeLayer_eq_t1_or_t2_or_t3 t with ht | ht | ht
  · rw [ht] at ht_lt
    omega
  · rw [ht] at ht_lt
    omega
  · rw [ht] at ht_lt
    omega

/-- Nonfixed product states strictly increase the product ledger under update. -/
theorem productLedger_lt_update_of_not_fixed
    {p : ProductRestrictedParams}
    {x : p.State}
    (hnotfixed : ¬ ProductFixedSet p x) :
    productLedger p x < productLedger p (productUpdateState p x) := by
  have hle := productUpdateState_pointwise_monotone p x
  have hwit_active :=
    product_exists_active_update_val_lt_of_not_fixed hnotfixed
  have hwit :
      ∃ i : ProductIndex p.d,
        (x i).val < (productUpdateState p x i).val := by
    obtain ⟨i, _hi, hlt⟩ := hwit_active
    exact ⟨i, hlt⟩
  exact productLedger_lt_update_of_pointwise_and_exists hle hwit

/-- Nonfixed product states have positive product ledger effect. -/
theorem productLedgerEffect_pos_of_not_fixed
    {p : ProductRestrictedParams}
    {x : p.State}
    (hnotfixed : ¬ ProductFixedSet p x) :
    0 < productLedgerEffect p x := by
  have hlt :
      productLedger p x < productLedger p (productUpdateState p x) :=
    productLedger_lt_update_of_not_fixed hnotfixed
  unfold productLedgerEffect
  omega

/-- Positive-effect target for the current v11 product-index typed scaffold. -/
def productPositiveLedgerEffectTarget
    (p : ProductRestrictedParams)
    (x : p.State) : Prop :=
  ¬ ProductFixedSet p x → 0 < productLedgerEffect p x

/-- The current v11 scaffold proves positive product ledger effect for nonfixed states. -/
theorem productPositiveLedgerEffectTarget_proved
    (p : ProductRestrictedParams)
    (x : p.State) :
    productPositiveLedgerEffectTarget p x := by
  intro hnotfixed
  exact productLedgerEffect_pos_of_not_fixed hnotfixed

end VFH2
