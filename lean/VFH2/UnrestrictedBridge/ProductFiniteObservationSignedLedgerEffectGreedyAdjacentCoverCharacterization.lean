import VFH2.UnrestrictedBridge.ProductFiniteObservationSignedLedgerEffectGreedyPrefixSaturationCharacterization

/-!
# Product finite-observation greedy adjacent-cover characterization

This module characterizes an adjacent one-unit increase of the signed
Product-window ledger effect between semantic canonical left-greedy states.
The increase occurs exactly when there is one active bounded coordinate at
which the earlier state exceeds the later state by one, every other natural
coordinate agrees, and the ledger-effect-derived quota crosses that
coordinate's static active-capacity prefix. The crossing coordinate is unique.

The forward implication combines reverse pointwise order, a genuine finite
sum-gap argument, global canonical support, and the preceding prefix-saturation
characterization. The reverse implication reconstructs the signed
ledger-effect adjacency from the unique-coordinate data rather than wrapping
an existing bridge theorem. All finite and support machinery remains private,
and all semantic predicates remain theorem-local.

Only adjacent effects inside the canonical finite Product observation window
are characterized. This does not define a global cover relation or infinite
ledger, is not unrestricted `TTP-VF-H2-004`, and makes no full-theory,
empirical, physical, medical, causal, or biological validation claim.
-/

namespace VFH2
namespace UnrestrictedBridge

private theorem c92_sum_ofFn_le_sum_ofFn
    (n : Nat)
    (a b : Fin n → Nat)
    (hpointwise : ∀ i : Fin n, a i ≤ b i) :
    (List.ofFn a).sum ≤ (List.ofFn b).sum := by
  induction n with
  | zero =>
      simp
  | succ n ih =>
      simp only [List.ofFn_succ, List.sum_cons]
      exact
        Nat.add_le_add
          (hpointwise (0 : Fin (n + 1)))
          (ih
            (fun i => a i.succ)
            (fun i => b i.succ)
            (fun i => hpointwise i.succ))

private theorem c92_pointwise_eq_of_le_of_sum_eq
    (n : Nat)
    (a b : Fin n → Nat)
    (hpointwise : ∀ i : Fin n, b i ≤ a i)
    (hsum : (List.ofFn a).sum = (List.ofFn b).sum) :
    ∀ i : Fin n, a i = b i := by
  induction n with
  | zero =>
      intro i
      exact Fin.elim0 i
  | succ n ih =>
      simp only [List.ofFn_succ, List.sum_cons] at hsum
      have htailLe :=
        c92_sum_ofFn_le_sum_ofFn
          n
          (fun i => b i.succ)
          (fun i => a i.succ)
          (fun i => hpointwise i.succ)
      have hzeroLe :=
        hpointwise (0 : Fin (n + 1))
      have hzero :
          a (0 : Fin (n + 1)) =
            b (0 : Fin (n + 1)) := by
        omega
      have htailSum :
          (List.ofFn
              (fun i : Fin n =>
                a i.succ)).sum =
            (List.ofFn
              (fun i : Fin n =>
                b i.succ)).sum := by
        omega
      intro i
      refine Fin.cases hzero ?_ i
      intro j
      exact
        ih
          (fun i => a i.succ)
          (fun i => b i.succ)
          (fun i => hpointwise i.succ)
          htailSum
          j

private theorem c92_sum_eq_add_one_of_unitCoordinate
    (n : Nat) :
    ∀ (a b : Fin n → Nat)
      (w : Fin n),
      a w = b w + 1 →
      (∀ i : Fin n, i ≠ w → a i = b i) →
        (List.ofFn a).sum =
          (List.ofFn b).sum + 1 := by
  induction n with
  | zero =>
      intro a b w
      exact Fin.elim0 w
  | succ n ih =>
      intro a b w hwUnit hOthers
      simp only [List.ofFn_succ, List.sum_cons]
      cases w using Fin.cases with
      | zero =>
        have hTail :
            (fun i : Fin n => a i.succ) =
              (fun i : Fin n => b i.succ) := by
          funext i
          exact
            hOthers
              i.succ
              (by
                intro h
                have hval := congrArg Fin.val h
                simp at hval)
        rw [hTail]
        omega
      | succ j =>
        have hZero :
            a (0 : Fin (n + 1)) =
              b (0 : Fin (n + 1)) := by
          exact
            hOthers
              0
              (by
                intro h
                have hval := congrArg Fin.val h
                simp at hval)
        have hTail :=
          ih
            (fun i => a i.succ)
            (fun i => b i.succ)
            j
            hwUnit
            (by
              intro i hi
              apply hOthers i.succ
              intro h
              apply hi
              exact Fin.succ_inj.mp h)
        omega

private theorem c92_exists_unitCoordinate_of_pointwise_le_of_sum_eq_add_one
    (n : Nat)
    (a b : Fin n → Nat)
    (hpointwise : ∀ i : Fin n, b i ≤ a i)
    (hsum :
      (List.ofFn a).sum =
        (List.ofFn b).sum + 1) :
    ∃ w : Fin n,
      a w = b w + 1 ∧
      ∀ i : Fin n,
        i ≠ w →
          a i = b i := by
  induction n with
  | zero =>
      simp at hsum
  | succ n ih =>
      simp only [List.ofFn_succ, List.sum_cons] at hsum
      have htailLe :=
        c92_sum_ofFn_le_sum_ofFn
          n
          (fun i => b i.succ)
          (fun i => a i.succ)
          (fun i => hpointwise i.succ)
      have hzeroLe :=
        hpointwise (0 : Fin (n + 1))
      by_cases hzero :
          a (0 : Fin (n + 1)) =
            b (0 : Fin (n + 1))
      · have htailGap :
            (List.ofFn
                (fun i : Fin n =>
                  a i.succ)).sum =
              (List.ofFn
                (fun i : Fin n =>
                  b i.succ)).sum +
                1 := by
          omega
        obtain ⟨w, hwUnit, hOthers⟩ :=
          ih
            (fun i => a i.succ)
            (fun i => b i.succ)
            (fun i => hpointwise i.succ)
            htailGap
        refine ⟨w.succ, hwUnit, ?_⟩
        intro i hi
        cases i using Fin.cases with
        | zero =>
            exact hzero
        | succ j =>
            apply hOthers j
            intro hj
            apply hi
            exact Fin.succ_inj.mpr hj
      · have hzeroUnit :
            a (0 : Fin (n + 1)) =
              b (0 : Fin (n + 1)) +
                1 := by
          omega
        have htailSum :
            (List.ofFn
                (fun i : Fin n =>
                  a i.succ)).sum =
              (List.ofFn
                (fun i : Fin n =>
                  b i.succ)).sum := by
          omega
        have htailPointwise :=
          c92_pointwise_eq_of_le_of_sum_eq
            n
            (fun i => a i.succ)
            (fun i => b i.succ)
            (fun i => hpointwise i.succ)
            htailSum
        refine ⟨0, hzeroUnit, ?_⟩
        intro i hi
        cases i using Fin.cases with
        | zero =>
            exact False.elim (hi rfl)
        | succ j =>
            exact htailPointwise j

private theorem c92_sum_eq_add_one_iff_exists_unitCoordinate
    (n : Nat)
    (a b : Fin n → Nat)
    (hpointwise : ∀ i : Fin n, b i ≤ a i) :
    ((List.ofFn a).sum =
      (List.ofFn b).sum + 1) ↔
    ∃ w : Fin n,
      a w = b w + 1 ∧
      ∀ i : Fin n,
        i ≠ w →
          a i = b i := by
  constructor
  · exact
      c92_exists_unitCoordinate_of_pointwise_le_of_sum_eq_add_one
        n
        a
        b
        hpointwise
  · rintro ⟨w, hwUnit, hOthers⟩
    exact
      c92_sum_eq_add_one_of_unitCoordinate
        n
        a
        b
        w
        hwUnit
        hOthers

private theorem c92_prefixSum_succ
    (a : Nat → Nat)
    (k : Nat) :
    (List.ofFn
        (fun v : Fin (k + 1) =>
          a v.val)).sum =
      (List.ofFn
          (fun v : Fin k =>
            a v.val)).sum +
        a k := by
  rw [List.ofFn_succ_last, List.sum_append]
  simp

private theorem c92_val_mem_paramsUOfProduct_active_iff
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

private theorem c92_mem_paramsUOfProduct_active_lt_typedWidth
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

theorem ledgerEffectOn_productWindowU_eq_add_one_iff_existsUnique_activeCapacityCrossingUnitCoordinate_of_canonicalLeftGreedy
    (p : ProductRestrictedParams)
    (x z : StateU) :
    let capacities : List Nat :=
      List.ofFn
        (fun w : Typed.WidthIndex p.d =>
          if ProductIndex.unflatten w ∈ p.active then p.n else 0)
    let activeCapacity : Nat := capacities.sum
    let effect : StateU → Int :=
      fun s =>
        ledgerEffectOn
          (paramsUOfProduct p)
          (productWindowU p)
          s
    let quota : StateU → Nat :=
      fun s =>
        Int.toNat ((activeCapacity : Int) - effect s)
    let capacityPrefix : Nat → Nat :=
      fun k => (capacities.take k).sum
    let IsCanonicalLeftGreedy : StateU → Prop :=
      fun s =>
        (∀ j : Nat,
          j ∉ (paramsUOfProduct p).active → s j = 0) ∧
        inStateSpaceU (paramsUOfProduct p) s ∧
        ∀ u v : Typed.WidthIndex p.d,
          u.val < v.val →
          ProductIndex.unflatten u ∈ p.active →
          ProductIndex.unflatten v ∈ p.active →
          s u.val < p.n → s v.val = 0
    let IsActiveCapacityCrossingUnitCoordinate :
        Typed.WidthIndex p.d → Prop :=
      fun w =>
        ProductIndex.unflatten w ∈ p.active ∧
        capacityPrefix w.val < quota x ∧
        quota x ≤ capacityPrefix (w.val + 1) ∧
        x w.val = z w.val + 1 ∧
        ∀ j : Nat,
          j ≠ w.val → x j = z j
    IsCanonicalLeftGreedy x →
    IsCanonicalLeftGreedy z →
      (effect z = effect x + 1 ↔
        ∃ w : Typed.WidthIndex p.d,
          IsActiveCapacityCrossingUnitCoordinate w ∧
          ∀ w' : Typed.WidthIndex p.d,
            IsActiveCapacityCrossingUnitCoordinate w' → w' = w) := by
  dsimp only
  intro hx hz
  let capacities : List Nat :=
    List.ofFn
      (fun w : Typed.WidthIndex p.d =>
        if ProductIndex.unflatten w ∈ p.active then p.n else 0)
  let activeCapacity : Nat := capacities.sum
  let effect : StateU → Int :=
    fun s =>
      ledgerEffectOn
        (paramsUOfProduct p)
        (productWindowU p)
        s
  let quota : StateU → Nat :=
    fun s =>
      Int.toNat ((activeCapacity : Int) - effect s)
  let capacityPrefix : Nat → Nat :=
    fun k => (capacities.take k).sum
  let IsActiveCapacityCrossingUnitCoordinate :
      Typed.WidthIndex p.d → Prop :=
    fun w =>
      ProductIndex.unflatten w ∈ p.active ∧
      capacityPrefix w.val < quota x ∧
      quota x ≤ capacityPrefix (w.val + 1) ∧
      x w.val = z w.val + 1 ∧
      ∀ j : Nat,
        j ≠ w.val → x j = z j
  let xValues : Typed.WidthIndex p.d → Nat :=
    fun w =>
      if ProductIndex.unflatten w ∈ p.active then x w.val else 0
  let zValues : Typed.WidthIndex p.d → Nat :=
    fun w =>
      if ProductIndex.unflatten w ∈ p.active then z w.val else 0
  change
    effect z = effect x + 1 ↔
      ∃ w : Typed.WidthIndex p.d,
        IsActiveCapacityCrossingUnitCoordinate w ∧
        ∀ w' : Typed.WidthIndex p.d,
          IsActiveCapacityCrossingUnitCoordinate w' → w' = w
  have hxFormula :
      effect x =
        (activeCapacity : Int) -
          ((List.ofFn xValues).sum : Int) := by
    simpa [effect, activeCapacity, capacities, xValues] using
      ledgerEffectOn_productWindowU_eq_activeCapacity_sub_sum_activeValues
        p
        x
  have hzFormula :
      effect z =
        (activeCapacity : Int) -
          ((List.ofFn zValues).sum : Int) := by
    simpa [effect, activeCapacity, capacities, zValues] using
      ledgerEffectOn_productWindowU_eq_activeCapacity_sub_sum_activeValues
        p
        z
  have hQuotaX :
      quota x = (List.ofFn xValues).sum := by
    dsimp [quota]
    rw [hxFormula]
    omega
  have hQuotaZ :
      quota z = (List.ofFn zValues).sum := by
    dsimp [quota]
    rw [hzFormula]
    omega
  constructor
  · intro heffect
    have hOrderTheorem :=
      ledgerEffectOn_productWindowU_le_iff_forall_reverse_le_of_canonicalLeftGreedy
        p
        x
        z
    dsimp only at hOrderTheorem
    have hPointwise :
        ∀ j : Nat, z j ≤ x j :=
      (hOrderTheorem hx hz).mp (by
        change effect x ≤ effect z
        omega)
    have hValuesPointwise :
        ∀ w : Typed.WidthIndex p.d,
          zValues w ≤ xValues w := by
      intro w
      by_cases hw : ProductIndex.unflatten w ∈ p.active
      · simpa [xValues, zValues, hw] using hPointwise w.val
      · simp [xValues, zValues, hw]
    have hSumCast :
        ((List.ofFn xValues).sum : Int) =
          ((List.ofFn zValues).sum : Int) + 1 := by
      omega
    have hSum :
        (List.ofFn xValues).sum =
          (List.ofFn zValues).sum + 1 := by
      exact_mod_cast hSumCast
    obtain ⟨w, hwUnitMasked, hOthersMasked⟩ :=
      (c92_sum_eq_add_one_iff_exists_unitCoordinate
        (Typed.typedWidth p.d)
        xValues
        zValues
        hValuesPointwise).mp hSum
    have hwActive :
        ProductIndex.unflatten w ∈ p.active := by
      by_cases hw : ProductIndex.unflatten w ∈ p.active
      · exact hw
      · simp [xValues, zValues, hw] at hwUnitMasked
    have hwUnit :
        x w.val = z w.val + 1 := by
      simpa [xValues, zValues, hwActive] using hwUnitMasked
    have hOthers :
        ∀ j : Nat,
          j ≠ w.val → x j = z j := by
      intro j hj
      by_cases hjWidth : j < Typed.typedWidth p.d
      · let v : Typed.WidthIndex p.d := ⟨j, hjWidth⟩
        by_cases hvActive : ProductIndex.unflatten v ∈ p.active
        · have hvNe : v ≠ w := by
            intro hvw
            apply hj
            exact congrArg Fin.val hvw
          have hvEq := hOthersMasked v hvNe
          simpa [xValues, zValues, hvActive, v] using hvEq
        · have hjInactive :
              j ∉ (paramsUOfProduct p).active := by
            intro hjActive
            exact
              hvActive
                ((c92_val_mem_paramsUOfProduct_active_iff
                  p
                  v).mp (by simpa [v] using hjActive))
          rw [hx.1 j hjInactive, hz.1 j hjInactive]
      · have hjInactive :
            j ∉ (paramsUOfProduct p).active := by
          intro hjActive
          exact
            hjWidth
              (c92_mem_paramsUOfProduct_active_lt_typedWidth
                p
                j
                hjActive)
        rw [hx.1 j hjInactive, hz.1 j hjInactive]
    have hQuotaGap : quota x = quota z + 1 := by
      rw [hQuotaX, hQuotaZ]
      exact hSum
    have hPrefixBefore :
        (List.ofFn
            (fun v : Fin w.val =>
              x v.val)).sum =
          (List.ofFn
            (fun v : Fin w.val =>
              z v.val)).sum := by
      apply congrArg List.sum
      apply congrArg List.ofFn
      funext v
      exact hOthers v.val (by omega)
    have hPrefixThrough :
        (List.ofFn
            (fun v : Fin (w.val + 1) =>
              x v.val)).sum =
          (List.ofFn
            (fun v : Fin (w.val + 1) =>
              z v.val)).sum + 1 := by
      rw [c92_prefixSum_succ, c92_prefixSum_succ, hPrefixBefore, hwUnit]
      omega
    have hxCharacterization :=
      canonicalLeftGreedyActiveSupport_iff_ledgerEffect_capacityPrefixSaturation
        p
        x
    have hzCharacterization :=
      canonicalLeftGreedyActiveSupport_iff_ledgerEffect_capacityPrefixSaturation
        p
        z
    dsimp only at hxCharacterization hzCharacterization
    have hxSaturation := (hxCharacterization.mp hx).2
    have hzSaturation := (hzCharacterization.mp hz).2
    have hxBefore := hxSaturation w.val (by omega)
    have hzBefore := hzSaturation w.val (by omega)
    have hxThrough := hxSaturation (w.val + 1) (by omega)
    have hzThrough := hzSaturation (w.val + 1) (by omega)
    change
      (List.ofFn
          (fun v : Fin w.val =>
            x v.val)).sum =
        min (quota x) (capacityPrefix w.val) at hxBefore
    change
      (List.ofFn
          (fun v : Fin w.val =>
            z v.val)).sum =
        min (quota z) (capacityPrefix w.val) at hzBefore
    change
      (List.ofFn
          (fun v : Fin (w.val + 1) =>
            x v.val)).sum =
        min (quota x) (capacityPrefix (w.val + 1)) at hxThrough
    change
      (List.ofFn
          (fun v : Fin (w.val + 1) =>
            z v.val)).sum =
        min (quota z) (capacityPrefix (w.val + 1)) at hzThrough
    have hCrossingLower :
        capacityPrefix w.val < quota x := by
      by_cases hxLe : quota x ≤ capacityPrefix w.val
      · have hzLe : quota z ≤ capacityPrefix w.val := by omega
        rw [Nat.min_eq_left hxLe] at hxBefore
        rw [Nat.min_eq_left hzLe] at hzBefore
        omega
      · omega
    have hCrossingUpper :
        quota x ≤ capacityPrefix (w.val + 1) := by
      by_cases hxLe : quota x ≤ capacityPrefix (w.val + 1)
      · exact hxLe
      · have hCapacityLeX :
            capacityPrefix (w.val + 1) ≤ quota x := by
          omega
        have hCapacityLeZ :
            capacityPrefix (w.val + 1) ≤ quota z := by
          omega
        rw [Nat.min_eq_right hCapacityLeX] at hxThrough
        rw [Nat.min_eq_right hCapacityLeZ] at hzThrough
        omega
    refine ⟨w, ?_, ?_⟩
    · dsimp [IsActiveCapacityCrossingUnitCoordinate]
      exact
        ⟨hwActive,
          hCrossingLower,
          hCrossingUpper,
          hwUnit,
          hOthers⟩
    · intro w' hw'
      dsimp [IsActiveCapacityCrossingUnitCoordinate] at hw'
      apply Fin.ext
      by_cases hval : w'.val = w.val
      · exact hval
      · have hSame := hOthers w'.val hval
        omega
  · rintro ⟨w, hw, _⟩
    dsimp [IsActiveCapacityCrossingUnitCoordinate] at hw
    rcases hw with ⟨hwActive, _, _, hwUnit, hOthers⟩
    have hwUnitMasked :
        xValues w = zValues w + 1 := by
      simpa [xValues, zValues, hwActive] using hwUnit
    have hOthersMasked :
        ∀ i : Typed.WidthIndex p.d,
          i ≠ w → xValues i = zValues i := by
      intro i hi
      have hiVal : i.val ≠ w.val := by
        intro hval
        apply hi
        exact Fin.ext hval
      have hiEq := hOthers i.val hiVal
      simp [xValues, zValues, hiEq]
    have hSum :=
      c92_sum_eq_add_one_of_unitCoordinate
        (Typed.typedWidth p.d)
        xValues
        zValues
        w
        hwUnitMasked
        hOthersMasked
    omega

end UnrestrictedBridge
end VFH2
