import VFH2.RestrictedBridge.CoordinateIncrease

/-!
# VF-H2 Restricted Bridge Ledger Increase

This file lifts a witnessed coordinate increase to a positive scaffold
ledger effect.

Boundary:
- This proves the scaffold-level positive-effect path under the current
  restricted list-backed update map.
- This is not yet the full machine-checked proof of `RBRIDGE-VF-H2-001-R`.
- This is not a proof of the full Viruse Fabric theory.
- This is not a proof of unrestricted `TTP-VF-H2-004`.
- This is not empirical validation.
- This is not biological validation.

Next proof obligation:
combine the fixed-zero and nonfixed-positive halves into the final restricted
bridge theorem statement for this Lean scaffold.
-/

namespace VFH2
namespace RestrictedBridge

/-- Fold-left summation with an arbitrary accumulator equals the accumulator
plus fold-left summation from zero.
-/
theorem foldl_add_eq_acc_add_foldl_zero
    (xs : State) (acc : Nat) :
    List.foldl (fun acc a => acc + a) acc xs =
      acc + List.foldl (fun acc a => acc + a) 0 xs := by
  induction xs generalizing acc with
  | nil =>
      simp
  | cons a xs ih =>
      calc
        List.foldl (fun acc a => acc + a) acc (a :: xs)
            = List.foldl (fun acc a => acc + a) (acc + a) xs := by
              rfl
        _ = (acc + a) + List.foldl (fun acc a => acc + a) 0 xs := by
              exact ih (acc + a)
        _ = acc + (a + List.foldl (fun acc a => acc + a) 0 xs) := by
              omega
        _ = acc + List.foldl (fun acc a => acc + a) 0 (a :: xs) := by
              have hcons :
                  List.foldl (fun acc a => acc + a) 0 (a :: xs) =
                    a + List.foldl (fun acc a => acc + a) 0 xs := by
                calc
                  List.foldl (fun acc a => acc + a) 0 (a :: xs)
                      = List.foldl (fun acc a => acc + a) (0 + a) xs := by
                          rfl
                  _ = (0 + a) + List.foldl (fun acc a => acc + a) 0 xs := by
                          exact ih (0 + a)
                  _ = a + List.foldl (fun acc a => acc + a) 0 xs := by
                          omega
              rw [hcons]

/-- Ledger value of a cons state splits into head plus tail ledger value. -/
theorem ledgerVR_cons
    (a : Nat) (xs : State) :
    ledgerVR (a :: xs) = a + ledgerVR xs := by
  unfold ledgerVR
  calc
    List.foldl (fun acc a => acc + a) 0 (a :: xs)
        = List.foldl (fun acc a => acc + a) (0 + a) xs := by
            rfl
    _ = (0 + a) + List.foldl (fun acc a => acc + a) 0 xs := by
            exact foldl_add_eq_acc_add_foldl_zero xs (0 + a)
    _ = a + List.foldl (fun acc a => acc + a) 0 xs := by
            omega

/-- A coordinate bounded by top never decreases under the scaffold coordinate
update.
-/
theorem updateCoordinateR_ge_of_le_top
    (p : RestrictedParams) (i a : Nat)
    (hle : a ≤ p.n) :
    a ≤ updateCoordinateR p i a := by
  unfold updateCoordinateR
  by_cases hactive : isActiveIndex p i = true
  · simp [hactive, hle]
  · simp [hactive]

/-- For bounded states, the scaffold update never decreases `ledgerVR`. -/
theorem ledgerVR_le_updateStateAuxR_of_hasLnBounds
    (p : RestrictedParams) :
    ∀ (x : State) (base : Nat),
      hasLnBounds p x →
      ledgerVR x ≤ ledgerVR (updateStateAuxR p base x)
  | [], base, _hb => by
      simp [ledgerVR, updateStateAuxR]
  | a :: xs, base, hb => by
      have ha : a ≤ p.n := hb a (by simp)
      have hbxs : hasLnBounds p xs := by
        intro b hbmem
        exact hb b (by simp [hbmem])
      have hhead : a ≤ updateCoordinateR p base a :=
        updateCoordinateR_ge_of_le_top p base a ha
      have htail : ledgerVR xs ≤ ledgerVR (updateStateAuxR p (base + 1) xs) :=
        ledgerVR_le_updateStateAuxR_of_hasLnBounds p xs (base + 1) hbxs
      have hsum :
          a + ledgerVR xs ≤
            updateCoordinateR p base a + ledgerVR (updateStateAuxR p (base + 1) xs) := by
        omega
      simpa [updateStateAuxR, ledgerVR_cons] using hsum

/-- For bounded states, the scaffold update never decreases `ledgerVR`. -/
theorem ledgerVR_le_updateStateR_of_hasLnBounds
    (p : RestrictedParams) (x : State)
    (hb : hasLnBounds p x) :
    ledgerVR x ≤ ledgerVR (updateStateR p x) := by
  simpa [updateStateR] using
    ledgerVR_le_updateStateAuxR_of_hasLnBounds p x 0 hb

/-- Local witnessed below-top activity from a traversal base.

The offset is required to be in range so that the witness is a real coordinate
of the current list-backed state, not merely a `getD` default value.
-/
def localActiveBelowTopFrom
    (p : RestrictedParams) (base : Nat) (x : State) : Prop :=
  ∃ offset : Nat,
    offset < x.length ∧
    base + offset ∈ p.active ∧
    x.getD offset 0 < p.n

/-- A local active below-top witness makes the scaffold auxiliary update
strictly increase `ledgerVR`.
-/
theorem ledgerVR_lt_updateStateAuxR_of_localActiveBelowTop
    (p : RestrictedParams) :
    ∀ (x : State) (base : Nat),
      hasLnBounds p x →
      localActiveBelowTopFrom p base x →
      ledgerVR x < ledgerVR (updateStateAuxR p base x)
  | [], base, _hb, hw => by
      obtain ⟨offset, hlen, _hmem, _hlt⟩ := hw
      simp at hlen
  | a :: xs, base, hb, hw => by
      obtain ⟨offset, hlen, hmem, hbelow⟩ := hw
      have ha : a ≤ p.n := hb a (by simp)
      have hbxs : hasLnBounds p xs := by
        intro b hbmem
        exact hb b (by simp [hbmem])
      cases offset with
      | zero =>
          have hhead : a < updateCoordinateR p base a := by
            have hbelow_head : a < p.n := by
              simpa using hbelow
            have hmem_head : base ∈ p.active := by
              simpa using hmem
            exact updateCoordinateR_gt_of_mem_below_top p hmem_head hbelow_head
          have htail :
              ledgerVR xs ≤ ledgerVR (updateStateAuxR p (base + 1) xs) :=
            ledgerVR_le_updateStateAuxR_of_hasLnBounds p xs (base + 1) hbxs
          have hsum :
              a + ledgerVR xs <
                updateCoordinateR p base a + ledgerVR (updateStateAuxR p (base + 1) xs) := by
            omega
          simpa [updateStateAuxR, ledgerVR_cons] using hsum
      | succ offset =>
          have hhead :
              a ≤ updateCoordinateR p base a :=
            updateCoordinateR_ge_of_le_top p base a ha
          have hlen_tail : offset < xs.length := by
            simpa using hlen
          have hmem_tail : base + 1 + offset ∈ p.active := by
            have heq : base + Nat.succ offset = base + 1 + offset := by
              omega
            rwa [heq] at hmem
          have hbelow_tail : xs.getD offset 0 < p.n := by
            simpa using hbelow
          have hw_tail : localActiveBelowTopFrom p (base + 1) xs :=
            ⟨offset, hlen_tail, hmem_tail, hbelow_tail⟩
          have htail :
              ledgerVR xs < ledgerVR (updateStateAuxR p (base + 1) xs) :=
            ledgerVR_lt_updateStateAuxR_of_localActiveBelowTop
              p xs (base + 1) hbxs hw_tail
          have hsum :
              a + ledgerVR xs <
                updateCoordinateR p base a + ledgerVR (updateStateAuxR p (base + 1) xs) := by
            omega
          simpa [updateStateAuxR, ledgerVR_cons] using hsum

/-- A global active below-top witness plus active-index range gives a local
witness from base zero.
-/
theorem localActiveBelowTopFrom_zero_of_exists_active_below_top
    {p : RestrictedParams} {x : State}
    (hrange : activeIndicesInRange p x)
    (hw : ∃ i : Nat, i ∈ p.active ∧ x.getD i 0 < p.n) :
    localActiveBelowTopFrom p 0 x := by
  obtain ⟨i, hi, hbelow⟩ := hw
  exact ⟨i, hrange i hi, by simpa using hi, hbelow⟩

/-- A nonfixed restricted state strictly increases `ledgerVR` under the
scaffold update, provided active indices are in range.
-/
theorem ledgerVR_lt_updateStateR_of_not_inFixedSetR
    {p : RestrictedParams} {x : State}
    (hspace : inRestrictedStateSpace p x)
    (hrange : activeIndicesInRange p x)
    (hnotfixed : ¬ inFixedSetR p x) :
    ledgerVR x < ledgerVR (updateStateR p x) := by
  have hw_global :
      ∃ i : Nat, i ∈ p.active ∧ x.getD i 0 < p.n :=
    exists_active_below_top_of_not_inFixedSetR hspace hrange hnotfixed
  have hw_local : localActiveBelowTopFrom p 0 x :=
    localActiveBelowTopFrom_zero_of_exists_active_below_top hrange hw_global
  simpa [updateStateR] using
    ledgerVR_lt_updateStateAuxR_of_localActiveBelowTop
      p x 0 hspace.2 hw_local

/-- A nonfixed restricted state has positive scaffold ledger effect, provided
active indices are in range.
-/
theorem ledgerEffectR_pos_of_not_inFixedSetR
    {p : RestrictedParams} {x : State}
    (hspace : inRestrictedStateSpace p x)
    (hrange : activeIndicesInRange p x)
    (hnotfixed : ¬ inFixedSetR p x) :
    0 < ledgerEffectR p x := by
  have hlt : ledgerVR x < ledgerVR (updateStateR p x) :=
    ledgerVR_lt_updateStateR_of_not_inFixedSetR hspace hrange hnotfixed
  unfold ledgerEffectR
  change (0 : Int) < (ledgerVR (updateStateR p x) : Int) - (ledgerVR x : Int)
  omega

end RestrictedBridge
end VFH2
