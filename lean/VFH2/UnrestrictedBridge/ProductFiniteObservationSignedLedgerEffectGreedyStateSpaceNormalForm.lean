import VFH2.UnrestrictedBridge.ProductFiniteObservationSignedLedgerEffectStateSpaceNormalForm

/-!
# Product finite-observation relational greedy state-space normal form

This module extends the fixed-anchor admissible normal form to the complete
admissible Product-window effect interval. It constructs a finite greedy
allocation over the canonical `WidthIndex` capacity vector, zero-extends that
allocation to `StateU`, and characterizes the result by a relational prefix
recurrence.

The public theorem does not expose a normalizer definition. Its theorem-local
predicate requires global active support, `inStateSpaceU`, the greedy recurrence
at every bounded coordinate, and the exact signed effect. Uniqueness is proved
from that recurrence by strong induction over the prefix, not by definition.

Capacities are enumerated once over `WidthIndex` and activity is tested by
membership, so active-list ordering and duplicate entries cannot change the
representative. Inactive coordinates and the unobserved tail are forced to
zero.

The result selects one canonical representative from each admissible effect
fiber; it does not claim that the entire fiber is a singleton. Only the
canonical finite Product window is observed. This does not define a global
infinite ledger, is not unrestricted `TTP-VF-H2-004`, and makes no full-theory,
empirical, physical, medical, causal, or biological validation claim. No model
assumption is introduced.
-/

namespace VFH2
namespace UnrestrictedBridge

private def c86GreedyAllocate
    (q : Nat) :
    List Nat → List Nat
  | [] => []
  | c :: cs =>
      min c q :: c86GreedyAllocate (q - c) cs

@[simp]
private theorem c86GreedyAllocate_length
    (q : Nat)
    (caps : List Nat) :
    (c86GreedyAllocate q caps).length = caps.length := by
  induction caps generalizing q with
  | nil =>
      rfl
  | cons c cs ih =>
      simp [c86GreedyAllocate, ih]

private theorem c86GreedyAllocate_sum
    (q : Nat)
    (caps : List Nat) :
    (c86GreedyAllocate q caps).sum =
      min q caps.sum := by
  induction caps generalizing q with
  | nil =>
      simp [c86GreedyAllocate]
  | cons c cs ih =>
      simp only [
        c86GreedyAllocate,
        List.sum_cons,
        ih
      ]
      omega

private theorem c86GreedyAllocate_getD
    (q : Nat)
    (caps : List Nat)
    (j : Nat) :
    (c86GreedyAllocate q caps).getD j 0 =
      min
        (caps.getD j 0)
        (q -
          ((c86GreedyAllocate q caps).take j).sum) := by
  induction caps generalizing q j with
  | nil =>
      simp [c86GreedyAllocate]
  | cons c cs ih =>
      cases j with
      | zero =>
          simp [c86GreedyAllocate]
      | succ j =>
          simp only [
            c86GreedyAllocate,
            List.getD_cons_succ,
            List.take_succ_cons,
            List.sum_cons
          ]
          rw [ih]
          congr 1
          omega

private theorem c86_ofFn_getD_eq_take
    (xs : List Nat)
    (k : Nat)
    (hk : k ≤ xs.length) :
    List.ofFn
        (fun i : Fin k =>
          xs.getD i.val 0) =
      xs.take k := by
  apply List.ext_getElem
  · simp [hk]
  · intro i hiLeft hiRight
    simp only [List.length_ofFn] at hiLeft
    rw [List.getElem_ofFn]
    rw [List.getElem_take]
    rw [List.getElem_eq_getD]

private theorem c86_sum_ofFn_le_sum_ofFn
    (n : Nat)
    (f g : Fin n → Nat)
    (hpointwise : ∀ i : Fin n, f i ≤ g i) :
    (List.ofFn f).sum ≤ (List.ofFn g).sum := by
  induction n with
  | zero =>
      simp
  | succ n ih =>
      simp only [List.ofFn_succ, List.sum_cons]
      exact
        Nat.add_le_add
          (hpointwise (0 : Fin (n + 1)))
          (ih
            (fun i => f i.succ)
            (fun i => g i.succ)
            (fun i => hpointwise i.succ))

private theorem c86_val_mem_paramsUOfProduct_active_iff
    (p : ProductRestrictedParams)
    (w : Typed.WidthIndex p.d) :
    w.val ∈ (paramsUOfProduct p).active ↔
      ProductIndex.unflatten w ∈ p.active := by
  unfold paramsUOfProduct paramsUOfRestricted
  change
    w.val ∈
        (ProductParamsTransport.typedParamsOfProduct p).active.map
          (fun v => v.val) ↔
      ProductIndex.unflatten w ∈ p.active
  constructor
  · intro hw
    rcases List.mem_map.mp hw with ⟨v, hv, hval⟩
    have hvw : v = w := by
      apply Fin.ext
      exact hval
    subst v
    exact
      (ProductUpdateTransport.mem_typed_active_iff_unflatten_mem_product_active
        p
        w).mp hv
  · intro hw
    exact
      List.mem_map.mpr
        ⟨w,
          (ProductUpdateTransport.mem_typed_active_iff_unflatten_mem_product_active
            p
            w).mpr hw,
          rfl⟩

private theorem c86_mem_paramsUOfProduct_active_lt_typedWidth
    (p : ProductRestrictedParams)
    (j : Nat)
    (hj : j ∈ (paramsUOfProduct p).active) :
    j < Typed.typedWidth p.d := by
  unfold paramsUOfProduct paramsUOfRestricted at hj
  change
    j ∈
      (ProductParamsTransport.typedParamsOfProduct p).active.map
        (fun v => v.val) at hj
  rcases List.mem_map.mp hj with ⟨w, _, rfl⟩
  exact w.isLt

/--
For every admissible signed effect, canonical left-greedy allocation across
the active Product coordinates gives a unique globally active-supported
state.
-/
theorem existsUnique_leftGreedyActiveSupport_inStateSpaceU_ledgerEffectOn_productWindowU_eq_iff_nonneg_and_le_activeCapacity
    (p : ProductRestrictedParams)
    (e : Int) :
    let caps : List Nat :=
      List.ofFn
        (fun w : Typed.WidthIndex p.d =>
          if ProductIndex.unflatten w ∈ p.active then
            p.n
          else
            0)
    let capacity : Nat := caps.sum
    let q : Nat :=
      Int.toNat ((capacity : Int) - e)
    let IsLeftGreedy : StateU → Prop :=
      fun x =>
        (∀ j : Nat,
          j ∉ (paramsUOfProduct p).active →
            x j = 0) ∧
        inStateSpaceU (paramsUOfProduct p) x ∧
        (∀ w : Typed.WidthIndex p.d,
          x w.val =
            min
              (if ProductIndex.unflatten w ∈ p.active then
                p.n
              else
                0)
              (q -
                (List.ofFn
                  (fun v : Fin w.val =>
                    x v.val)).sum)) ∧
        ledgerEffectOn
          (paramsUOfProduct p)
          (productWindowU p)
          x = e
    (∃ x : StateU,
      IsLeftGreedy x ∧
      ∀ z : StateU,
        IsLeftGreedy z →
          z = x) ↔
      0 ≤ e ∧
      e ≤ (capacity : Int) := by
  dsimp only
  let caps : List Nat :=
    List.ofFn
      (fun w : Typed.WidthIndex p.d =>
        if ProductIndex.unflatten w ∈ p.active then
          p.n
        else
          0)
  let capacity : Nat := caps.sum
  let q : Nat :=
    Int.toNat ((capacity : Int) - e)
  constructor
  · rintro ⟨x, hx, _⟩
    have hxFormula :=
      ledgerEffectOn_productWindowU_eq_activeCapacity_sub_sum_activeValues
        p
        x
    have hxSumLe :
        (List.ofFn
          (fun w : Typed.WidthIndex p.d =>
            if ProductIndex.unflatten w ∈ p.active then
              x w.val
            else
              0)).sum ≤
          (List.ofFn
            (fun w : Typed.WidthIndex p.d =>
              if ProductIndex.unflatten w ∈ p.active then
                p.n
              else
                0)).sum := by
      apply
        c86_sum_ofFn_le_sum_ofFn
          (Typed.typedWidth p.d)
      intro w
      by_cases hw :
          ProductIndex.unflatten w ∈ p.active
      · simp only [hw, ↓reduceIte]
        have hbound := hx.2.1 w.val
        change x w.val ≤ p.n at hbound
        exact hbound
      · simp [hw]
    change
      ledgerEffectOn
          (paramsUOfProduct p)
          (productWindowU p)
          x =
        (capacity : Int) -
          ((List.ofFn
            (fun w : Typed.WidthIndex p.d =>
              if ProductIndex.unflatten w ∈ p.active then
                x w.val
              else
                0)).sum : Int) at hxFormula
    change
      (List.ofFn
        (fun w : Typed.WidthIndex p.d =>
          if ProductIndex.unflatten w ∈ p.active then
            x w.val
          else
            0)).sum ≤
        capacity at hxSumLe
    have hxEffect :
        ledgerEffectOn
            (paramsUOfProduct p)
            (productWindowU p)
            x =
          e :=
      hx.2.2.2
    change
      0 ≤ e ∧
        e ≤ (capacity : Int)
    constructor <;> omega
  · rintro ⟨heNonneg, heUpper⟩
    have heUpper' :
        e ≤ (capacity : Int) := by
      simpa [capacity, caps] using heUpper
    have hgapNonneg :
        0 ≤ (capacity : Int) - e := by
      omega
    have hqCast :
        (q : Int) = (capacity : Int) - e := by
      exact Int.toNat_of_nonneg hgapNonneg
    have hqLe :
        q ≤ capacity := by
      apply Int.ofNat_le.mp
      rw [hqCast]
      omega
    let values : List Nat :=
      c86GreedyAllocate q caps
    let x : StateU :=
      fun j => values.getD j 0
    have hvaluesLength :
        values.length = Typed.typedWidth p.d := by
      rw [show values.length = caps.length by
        simp [values]]
      simp [caps]
    have hcapsGetD :
        ∀ w : Typed.WidthIndex p.d,
          caps.getD w.val 0 =
            if ProductIndex.unflatten w ∈ p.active then
              p.n
            else
              0 := by
      intro w
      have hw :
          w.val < caps.length := by
        simp [caps]
      rw [
        ← List.getElem_eq_getD
          (l := caps)
          (i := w.val)
          (h := hw)
          0
      ]
      simp [caps]
    have hxGreedy :
        ∀ w : Typed.WidthIndex p.d,
          x w.val =
            min
              (if ProductIndex.unflatten w ∈ p.active then
                p.n
              else
                0)
              (q -
                (List.ofFn
                  (fun v : Fin w.val =>
                    x v.val)).sum) := by
      intro w
      have hwValues :
          w.val ≤ values.length := by
        rw [hvaluesLength]
        exact Nat.le_of_lt w.isLt
      have hprefix :
          List.ofFn
              (fun v : Fin w.val =>
                x v.val) =
            values.take w.val := by
        simpa [x] using
          c86_ofFn_getD_eq_take
            values
            w.val
            hwValues
      rw [hprefix]
      change
        values.getD w.val 0 =
          min
            (if ProductIndex.unflatten w ∈ p.active then
              p.n
            else
              0)
            (q - (values.take w.val).sum)
      rw [
        show values.getD w.val 0 =
            min
              (caps.getD w.val 0)
              (q - (values.take w.val).sum) by
          simpa [values] using
            c86GreedyAllocate_getD q caps w.val
      ]
      rw [hcapsGetD w]
    have hxSupport :
        ∀ j : Nat,
          j ∉ (paramsUOfProduct p).active →
            x j = 0 := by
      intro j hj
      by_cases hjWidth :
          j < Typed.typedWidth p.d
      · let w : Typed.WidthIndex p.d :=
          ⟨j, hjWidth⟩
        have hwInactive :
            ProductIndex.unflatten w ∉ p.active := by
          intro hw
          exact
            hj
              ((c86_val_mem_paramsUOfProduct_active_iff p w).mpr
                hw)
        have hgreedy := hxGreedy w
        simpa [w, hwInactive] using hgreedy
      · have hjValues :
          values.length ≤ j := by
          rw [hvaluesLength]
          exact Nat.le_of_not_gt hjWidth
        simp [
          x,
          List.getD_eq_getElem?_getD,
          List.getElem?_eq_none hjValues
        ]
    have hxSpace :
        inStateSpaceU (paramsUOfProduct p) x := by
      intro j
      change x j ≤ p.n
      by_cases hjWidth :
          j < Typed.typedWidth p.d
      · let w : Typed.WidthIndex p.d :=
          ⟨j, hjWidth⟩
        have hgreedy := hxGreedy w
        rw [hgreedy]
        by_cases hw :
            ProductIndex.unflatten w ∈ p.active
        · simp only [hw, ↓reduceIte]
          exact Nat.min_le_left _ _
        · simp [hw]
      · have hjValues :
          values.length ≤ j := by
          rw [hvaluesLength]
          exact Nat.le_of_not_gt hjWidth
        rw [show x j = 0 by
          simp [
            x,
            List.getD_eq_getElem?_getD,
            List.getElem?_eq_none hjValues
          ]]
        exact Nat.zero_le _
    have hvaluesSum :
        values.sum = q := by
      rw [show values.sum = min q caps.sum by
        simpa [values] using c86GreedyAllocate_sum q caps]
      change min q capacity = q
      omega
    have hxActiveValues :
        (List.ofFn
          (fun w : Typed.WidthIndex p.d =>
            if ProductIndex.unflatten w ∈ p.active then
              x w.val
            else
              0)).sum =
          q := by
      have hlist :
          List.ofFn
              (fun w : Typed.WidthIndex p.d =>
                if ProductIndex.unflatten w ∈ p.active then
                  x w.val
                else
                  0) =
            values := by
        apply List.ext_getElem
        · simp [hvaluesLength]
        · intro j hjLeft hjRight
          simp only [List.length_ofFn] at hjLeft
          let w : Typed.WidthIndex p.d :=
            ⟨j, hjLeft⟩
          rw [List.getElem_ofFn]
          change
            (if ProductIndex.unflatten w ∈ p.active then
              x w.val
            else
              0) =
              values[j]
          by_cases hw :
              ProductIndex.unflatten w ∈ p.active
          · simp only [hw, ↓reduceIte]
            exact
              (List.getElem_eq_getD
                (l := values)
                (i := j)
                0).symm
          · have hxZero :
                x w.val = 0 := by
              have hgreedy := hxGreedy w
              simpa [hw] using hgreedy
            simp only [hw, ↓reduceIte]
            rw [← hxZero]
            exact
              (List.getElem_eq_getD
                (l := values)
                (i := j)
                0).symm
      rw [hlist, hvaluesSum]
    have hxEffect :
        ledgerEffectOn
            (paramsUOfProduct p)
            (productWindowU p)
            x =
          e := by
      rw [
        ledgerEffectOn_productWindowU_eq_activeCapacity_sub_sum_activeValues,
        hxActiveValues
      ]
      change (capacity : Int) - (q : Int) = e
      rw [hqCast]
      omega
    refine
      ⟨x,
        ⟨hxSupport, hxSpace, hxGreedy, hxEffect⟩,
        ?_⟩
    intro z hz
    have hwithin :
        ∀ j : Nat,
          j < Typed.typedWidth p.d →
            z j = x j := by
      intro j
      induction j using Nat.strongRecOn with
      | ind j ih =>
          intro hjWidth
          let w : Typed.WidthIndex p.d :=
            ⟨j, hjWidth⟩
          have hxRec := hxGreedy w
          have hzRec := hz.2.2.1 w
          have hprefix :
              List.ofFn
                  (fun v : Fin w.val =>
                    z v.val) =
                List.ofFn
                  (fun v : Fin w.val =>
                    x v.val) := by
            apply congrArg List.ofFn
            funext v
            exact
              ih
                v.val
                v.isLt
                (Nat.lt_trans v.isLt hjWidth)
          rw [hprefix] at hzRec
          exact hzRec.trans hxRec.symm
    funext j
    by_cases hjWidth :
        j < Typed.typedWidth p.d
    · exact hwithin j hjWidth
    · have hjNotActive :
          j ∉ (paramsUOfProduct p).active := by
        intro hjActive
        exact
          hjWidth
            (c86_mem_paramsUOfProduct_active_lt_typedWidth
              p
              j
              hjActive)
      rw [hz.1 j hjNotActive, hxSupport j hjNotActive]

end UnrestrictedBridge
end VFH2
