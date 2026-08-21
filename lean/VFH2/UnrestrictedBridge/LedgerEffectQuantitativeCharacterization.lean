import VFH2.UnrestrictedBridge.LedgerEffectCharacterization

/-!
# Quantitative Finite-Observation Ledger-Effect Characterization

This module strengthens the C73 zero-effect characterization with an exact
formula for the ledger increase. Each occurrence of an active coordinate in
the finite observation window contributes precisely its deficit from `p.top`;
inactive coordinates contribute zero. Repeated window entries are therefore
counted repeatedly, exactly as in `ledgerOn`.

The exact formula does not require the window to cover every active coordinate.
Coverage is needed only when positivity is characterized by failure of
`inFixedSetU`.

Boundary:
- This concerns countably indexed states with a finite observation window.
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

/--
The updated finite ledger is the original ledger plus the exact sum of active
coordinate deficits observed by the window.
-/
theorem ledgerOn_updateU_eq_add_activeDeficits
    (p : ParamsU)
    (window : List Nat)
    (x : StateU)
    (hspace : inStateSpaceU p x) :
    ledgerOn window (updateU p x) =
      ledgerOn window x +
        (window.map fun i =>
          if i ∈ p.active then p.top - x i else 0).sum := by
  induction window with
  | nil =>
      simp [ledgerOn]
  | cons i window ih =>
      rw [
        ledgerOn_cons i window (updateU p x),
        ledgerOn_cons i window x,
        ih
      ]
      simp only [List.map_cons, List.sum_cons]
      by_cases hi : i ∈ p.active
      · have hle : x i ≤ p.top :=
          hspace i
        simp [updateU, hi]
        omega
      · simp [updateU, hi]
        omega

/--
The integer ledger effect is exactly the natural active-deficit sum embedded
in `Int`.
-/
theorem ledgerEffectOn_eq_sum_activeDeficits
    (p : ParamsU)
    (window : List Nat)
    (x : StateU)
    (hspace : inStateSpaceU p x) :
    ledgerEffectOn p window x =
      ((window.map fun i =>
        if i ∈ p.active then p.top - x i else 0).sum : Int) := by
  unfold ledgerEffectOn
  rw [ledgerOn_updateU_eq_add_activeDeficits p window x hspace]
  simp
  omega

/-- A bounded state has nonnegative finite-observation ledger effect. -/
theorem ledgerEffectOn_nonneg
    (p : ParamsU)
    (window : List Nat)
    (x : StateU)
    (hspace : inStateSpaceU p x) :
    0 ≤ ledgerEffectOn p window x := by
  rw [ledgerEffectOn_eq_sum_activeDeficits p window x hspace]
  omega

/--
When the observation window covers every active coordinate, the ledger effect
is positive exactly away from the active-coordinate fixed set.
-/
theorem ledgerEffectOn_pos_iff_not_inFixedSetU
    (p : ParamsU)
    (window : List Nat)
    (x : StateU)
    (hspace : inStateSpaceU p x)
    (hcover :
      ∀ i : Nat,
        i ∈ p.active →
        i ∈ window) :
    0 < ledgerEffectOn p window x ↔
      ¬ inFixedSetU p x := by
  constructor
  · intro hpos hfixed
    have hzero :
        ledgerEffectOn p window x = 0 :=
      (ledgerEffectOn_eq_zero_iff_inFixedSetU
        p
        window
        x
        hspace
        hcover).2 hfixed
    omega
  · intro hnotfixed
    have hnonneg :
        0 ≤ ledgerEffectOn p window x :=
      ledgerEffectOn_nonneg p window x hspace
    have hne :
        ledgerEffectOn p window x ≠ 0 := by
      intro hzero
      exact
        hnotfixed
          ((ledgerEffectOn_eq_zero_iff_inFixedSetU
            p
            window
            x
            hspace
            hcover).1 hzero)
    omega

end UnrestrictedBridge
end VFH2
