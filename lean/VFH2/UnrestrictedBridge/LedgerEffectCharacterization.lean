import VFH2.UnrestrictedBridge.Scaffold

/-!
# Countably Indexed Finite-Observation Ledger-Effect Characterization

This module proves the zero-effect/fixed-set characterization for the
countably indexed state model with a finite observation window.

The observation window must cover every active coordinate. Repetitions and
inactive coordinates in the window are allowed.

Boundary:
- This is a theorem about countably indexed states with finite observation.
- It does not define a global infinite ledger.
- It is not unrestricted `TTP-VF-H2-004`.
- It makes no empirical or biological claim.
-/

namespace VFH2
namespace UnrestrictedBridge

private theorem foldl_observation_add_eq_acc_add_foldl_zero
    (window : List Nat)
    (x : StateU)
    (acc : Nat) :
    List.foldl (fun acc i => acc + x i) acc window =
      acc + List.foldl (fun acc i => acc + x i) 0 window := by
  induction window generalizing acc with
  | nil =>
      simp
  | cons i window ih =>
      calc
        List.foldl (fun acc j => acc + x j) acc (i :: window)
            =
          List.foldl
            (fun acc j => acc + x j)
            (acc + x i)
            window := by
              rfl
        _ =
          (acc + x i) +
            List.foldl (fun acc j => acc + x j) 0 window := by
              exact ih (acc + x i)
        _ =
          acc +
            (x i + List.foldl (fun acc j => acc + x j) 0 window) := by
              omega
        _ =
          acc +
            List.foldl (fun acc j => acc + x j) 0 (i :: window) := by
              have hcons :
                  List.foldl
                      (fun acc j => acc + x j)
                      0
                      (i :: window)
                    =
                  x i +
                    List.foldl
                      (fun acc j => acc + x j)
                      0
                      window := by
                calc
                  List.foldl
                      (fun acc j => acc + x j)
                      0
                      (i :: window)
                      =
                    List.foldl
                      (fun acc j => acc + x j)
                      (0 + x i)
                      window := by
                        rfl
                  _ =
                    (0 + x i) +
                      List.foldl
                        (fun acc j => acc + x j)
                        0
                        window := by
                          exact ih (0 + x i)
                  _ =
                    x i +
                      List.foldl
                        (fun acc j => acc + x j)
                        0
                        window := by
                          omega
              rw [hcons]

private theorem ledgerOn_cons
    (i : Nat)
    (window : List Nat)
    (x : StateU) :
    ledgerOn (i :: window) x =
      x i + ledgerOn window x := by
  unfold ledgerOn
  calc
    List.foldl (fun acc j => acc + x j) 0 (i :: window)
        =
      List.foldl
        (fun acc j => acc + x j)
        (0 + x i)
        window := by
          rfl
    _ =
      (0 + x i) +
        List.foldl (fun acc j => acc + x j) 0 window := by
          exact
            foldl_observation_add_eq_acc_add_foldl_zero
              window
              x
              (0 + x i)
    _ =
      x i +
        List.foldl (fun acc j => acc + x j) 0 window := by
          omega

private theorem ledgerOn_mono_of_pointwise
    (x y : StateU) :
    ∀ window : List Nat,
      (∀ i : Nat, i ∈ window → x i ≤ y i) →
      ledgerOn window x ≤ ledgerOn window y
  | [], _h => by
      simp [ledgerOn]
  | i :: window, h => by
      have hhead : x i ≤ y i :=
        h i (by simp)

      have htail :
          ledgerOn window x ≤ ledgerOn window y :=
        ledgerOn_mono_of_pointwise x y window (by
          intro j hj
          exact h j (by simp [hj]))

      rw [
        ledgerOn_cons i window x,
        ledgerOn_cons i window y
      ]

      omega

private theorem ledgerOn_lt_of_mem_of_pointwise
    (x y : StateU)
    (target : Nat) :
    ∀ window : List Nat,
      target ∈ window →
      (∀ i : Nat, i ∈ window → x i ≤ y i) →
      x target < y target →
      ledgerOn window x < ledgerOn window y
  | [], hmem, _hmono, _hlt => by
      simp at hmem
  | i :: window, hmem, hmono, htarget => by
      rw [
        ledgerOn_cons i window x,
        ledgerOn_cons i window y
      ]

      simp only [List.mem_cons] at hmem

      rcases hmem with hEq | htailMem
      · subst target

        have htailLe :
            ledgerOn window x ≤ ledgerOn window y :=
          ledgerOn_mono_of_pointwise x y window (by
            intro j hj
            exact hmono j (by simp [hj]))

        omega

      · have hheadLe : x i ≤ y i :=
          hmono i (by simp)

        have htailLt :
            ledgerOn window x < ledgerOn window y :=
          ledgerOn_lt_of_mem_of_pointwise
            x
            y
            target
            window
            htailMem
            (by
              intro j hj
              exact hmono j (by simp [hj]))
            htarget

        omega

private theorem le_updateU_of_inStateSpaceU
    (p : ParamsU)
    (x : StateU)
    (hspace : inStateSpaceU p x)
    (i : Nat) :
    x i ≤ updateU p x i := by
  by_cases hi : i ∈ p.active
  · simpa [updateU, hi] using hspace i
  · simp [updateU, hi]

theorem updateU_eq_self_of_inFixedSetU
    (p : ParamsU)
    (x : StateU)
    (hfixed : inFixedSetU p x) :
    updateU p x = x := by
  funext i

  by_cases hi : i ∈ p.active
  · simp [updateU, hi, hfixed i hi]
  · simp [updateU, hi]

/--
C73 finite-observation characterization.

For a bounded countably indexed state, when the finite observation window
covers every active coordinate, the ledger effect is zero exactly at the
active-coordinate fixed set.
-/
theorem ledgerEffectOn_eq_zero_iff_inFixedSetU
    (p : ParamsU)
    (window : List Nat)
    (x : StateU)
    (hspace : inStateSpaceU p x)
    (hcover :
      ∀ i : Nat,
        i ∈ p.active →
        i ∈ window) :
    ledgerEffectOn p window x = 0 ↔
      inFixedSetU p x := by
  constructor

  · intro hzero

    have hLedgerEq :
        ledgerOn window (updateU p x) =
          ledgerOn window x := by
      unfold ledgerEffectOn at hzero
      omega

    intro i hiActive

    have hle : x i ≤ p.top :=
      hspace i

    have hnotlt : ¬x i < p.top := by
      intro hltTop

      have hltCoordinate :
          x i < updateU p x i := by
        simpa [updateU, hiActive] using hltTop

      have hpointwise :
          ∀ j : Nat,
            j ∈ window →
            x j ≤ updateU p x j := by
        intro j _hj
        exact
          le_updateU_of_inStateSpaceU
            p
            x
            hspace
            j

      have hLedgerLt :
          ledgerOn window x <
            ledgerOn window (updateU p x) :=
        ledgerOn_lt_of_mem_of_pointwise
          x
          (updateU p x)
          i
          window
          (hcover i hiActive)
          hpointwise
          hltCoordinate

      rw [hLedgerEq] at hLedgerLt
      exact Nat.lt_irrefl _ hLedgerLt

    exact
      Nat.le_antisymm
        hle
        (Nat.le_of_not_gt hnotlt)

  · intro hfixed

    have hUpdate :
        updateU p x = x :=
      updateU_eq_self_of_inFixedSetU
        p
        x
        hfixed

    simp [ledgerEffectOn, hUpdate]

end UnrestrictedBridge
end VFH2
