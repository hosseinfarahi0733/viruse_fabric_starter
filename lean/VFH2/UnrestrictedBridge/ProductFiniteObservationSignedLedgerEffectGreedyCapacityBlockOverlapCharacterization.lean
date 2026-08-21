import VFH2.UnrestrictedBridge.ProductFiniteObservationSignedLedgerEffectGreedyFiniteSuccessorChainRealization

/-!
# Arbitrary-gap greedy capacity-block overlap characterization

This module gives an exact coordinate formula for any ordered pair of semantic
canonical left-greedy states in the finite Product observation window.  The
decrease at each bounded coordinate is precisely the overlap of the effect-rank
interval with that coordinate's reverse active-capacity block.

The proof derives a closed one-state coordinate profile from C91 prefix
saturation, proves the finite Nat overlap identity, and uses C88 for the reverse
semantic implication.  C92 is recovered as the adjacent-rank specialization;
C94 chains instantiate this arbitrary-gap result but are not used as a wrapper.

All capacity-block, rank, profile, and canonical predicates remain theorem-local,
and every supporting declaration is private.  This adds no executable
normalizer, public order or successor API, update trajectory, ledger mutation,
or infinite ledger.  It remains a finite restricted Product observation result,
not unrestricted TTP-VF-H2-004 and not full-theory, empirical, physical,
medical, causal, or biological validation.
-/


namespace VFH2
namespace UnrestrictedBridge

private theorem c95_prefixSum_succ
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

private theorem c95_coordinateProfile
    (p : ProductRestrictedParams)
    (s : StateU) :
    let capacities : List Nat :=
      List.ofFn
        (fun w : Typed.WidthIndex p.d =>
          if ProductIndex.unflatten w ∈ p.active then p.n else 0)
    let activeCapacity : Nat := capacities.sum
    let effect : StateU → Int :=
      fun y =>
        ledgerEffectOn
          (paramsUOfProduct p)
          (productWindowU p)
          y
    let effectRank : StateU → Nat :=
      fun y => Int.toNat (effect y)
    let capacityPrefix : Nat → Nat :=
      fun k => (capacities.take k).sum
    let reverseCapacityBlockStart :
        Typed.WidthIndex p.d → Nat :=
      fun w =>
        activeCapacity - capacityPrefix (w.val + 1)
    let reverseCapacityBlockEnd :
        Typed.WidthIndex p.d → Nat :=
      fun w =>
        activeCapacity - capacityPrefix w.val
    let IsCanonicalLeftGreedy : StateU → Prop :=
      fun y =>
        (∀ j : Nat,
          j ∉ (paramsUOfProduct p).active → y j = 0) ∧
        inStateSpaceU (paramsUOfProduct p) y ∧
        ∀ u v : Typed.WidthIndex p.d,
          u.val < v.val →
          ProductIndex.unflatten u ∈ p.active →
          ProductIndex.unflatten v ∈ p.active →
          y u.val < p.n →
          y v.val = 0
    IsCanonicalLeftGreedy s →
      ∀ w : Typed.WidthIndex p.d,
        s w.val =
          reverseCapacityBlockEnd w -
            max (effectRank s) (reverseCapacityBlockStart w) := by
  dsimp only
  intro hs w
  let capacities : List Nat :=
    List.ofFn
      (fun u : Typed.WidthIndex p.d =>
        if ProductIndex.unflatten u ∈ p.active then p.n else 0)
  let activeCapacity : Nat := capacities.sum
  let effect : StateU → Int :=
    fun y =>
      ledgerEffectOn
        (paramsUOfProduct p)
        (productWindowU p)
        y
  let effectRank : StateU → Nat :=
    fun y => Int.toNat (effect y)
  let quota : StateU → Nat :=
    fun y => Int.toNat ((activeCapacity : Int) - effect y)
  let capacityPrefix : Nat → Nat :=
    fun k => (capacities.take k).sum
  change
    s w.val =
      activeCapacity - capacityPrefix w.val -
        max (effectRank s)
          (activeCapacity - capacityPrefix (w.val + 1))
  have hCharacterization :=
    canonicalLeftGreedyActiveSupport_iff_ledgerEffect_capacityPrefixSaturation
      p
      s
  dsimp only at hCharacterization
  have hSaturation := (hCharacterization.mp hs).2
  have hBefore := hSaturation w.val (by omega)
  have hThrough := hSaturation (w.val + 1) (by omega)
  change
    (List.ofFn
        (fun v : Fin w.val =>
          s v.val)).sum =
      min (quota s) (capacityPrefix w.val) at hBefore
  change
    (List.ofFn
        (fun v : Fin (w.val + 1) =>
          s v.val)).sum =
      min (quota s) (capacityPrefix (w.val + 1)) at hThrough
  have hPrefixStep :
      (List.ofFn
          (fun v : Fin (w.val + 1) =>
            s v.val)).sum =
        (List.ofFn
            (fun v : Fin w.val =>
              s v.val)).sum +
          s w.val :=
    c95_prefixSum_succ s w.val
  have hBeforeBound :
      capacityPrefix w.val ≤ activeCapacity := by
    have hTake :=
      congrArg List.sum
        (List.take_append_drop w.val capacities)
    simp only [List.sum_append] at hTake
    change
      capacityPrefix w.val +
          (capacities.drop w.val).sum =
        activeCapacity at hTake
    omega
  have hThroughBound :
      capacityPrefix (w.val + 1) ≤ activeCapacity := by
    have hTake :=
      congrArg List.sum
        (List.take_append_drop (w.val + 1) capacities)
    simp only [List.sum_append] at hTake
    change
      capacityPrefix (w.val + 1) +
          (capacities.drop (w.val + 1)).sum =
        activeCapacity at hTake
    omega
  have hEffectNonneg : 0 ≤ effect s := by
    exact
      ledgerEffectOn_nonneg
        (paramsUOfProduct p)
        (productWindowU p)
        s
        hs.2.1
  have hEffectFormula :
      effect s =
        (activeCapacity : Int) -
          ((List.ofFn
            (fun u : Typed.WidthIndex p.d =>
              if ProductIndex.unflatten u ∈ p.active then
                s u.val
              else
                0)).sum : Int) := by
    simpa [effect, activeCapacity, capacities] using
      ledgerEffectOn_productWindowU_eq_activeCapacity_sub_sum_activeValues
        p
        s
  have hEffectUpper :
      effect s ≤ (activeCapacity : Int) := by
    omega
  have hEffectRankCast :
      (effectRank s : Int) = effect s := by
    dsimp [effectRank]
    exact Int.toNat_of_nonneg hEffectNonneg
  have hQuotaCast :
      (quota s : Int) =
        (activeCapacity : Int) - effect s := by
    dsimp [quota]
    exact Int.toNat_of_nonneg (by omega)
  have hQuota :
      quota s = activeCapacity - effectRank s := by
    omega
  have hPrefixMonotone :
      capacityPrefix w.val ≤ capacityPrefix (w.val + 1) := by
    have hwLength : w.val < capacities.length := by
      simpa only [capacities, List.length_ofFn] using w.isLt
    have hTakeStep := List.take_add_one (l := capacities) (i := w.val)
    rw [List.getElem?_eq_getElem hwLength] at hTakeStep
    have hSumStep := congrArg List.sum hTakeStep
    simp only [List.sum_append] at hSumStep
    change
      capacityPrefix (w.val + 1) =
        capacityPrefix w.val + capacities.get ⟨w.val, hwLength⟩ at hSumStep
    omega
  omega


private theorem c95_nat_reverse_capacity_block_overlap
    (rx rz start finish : Nat)
    (hrank : rx ≤ rz) :
    finish - max rx start =
      (finish - max rz start) +
        (min rz finish - max rx start) := by
  omega

theorem ledgerEffectOn_productWindowU_le_iff_forall_coordinateDecrease_eq_reverseCapacityBlockOverlap_of_canonicalLeftGreedy
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
    let effectRank : StateU → Nat :=
      fun s => Int.toNat (effect s)
    let capacityPrefix : Nat → Nat :=
      fun k => (capacities.take k).sum
    let reverseCapacityBlockStart :
        Typed.WidthIndex p.d → Nat :=
      fun w =>
        activeCapacity - capacityPrefix (w.val + 1)
    let reverseCapacityBlockEnd :
        Typed.WidthIndex p.d → Nat :=
      fun w =>
        activeCapacity - capacityPrefix w.val
    let IsCanonicalLeftGreedy : StateU → Prop :=
      fun s =>
        (∀ j : Nat,
          j ∉ (paramsUOfProduct p).active → s j = 0) ∧
        inStateSpaceU (paramsUOfProduct p) s ∧
        ∀ u v : Typed.WidthIndex p.d,
          u.val < v.val →
          ProductIndex.unflatten u ∈ p.active →
          ProductIndex.unflatten v ∈ p.active →
          s u.val < p.n →
          s v.val = 0
    IsCanonicalLeftGreedy x →
    IsCanonicalLeftGreedy z →
      (effect x ≤ effect z ↔
        ∀ w : Typed.WidthIndex p.d,
          x w.val =
            z w.val +
              (min
                  (effectRank z)
                  (reverseCapacityBlockEnd w) -
                max
                  (effectRank x)
                  (reverseCapacityBlockStart w))) := by
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
  let effectRank : StateU → Nat :=
    fun s => Int.toNat (effect s)
  let capacityPrefix : Nat → Nat :=
    fun k => (capacities.take k).sum
  let reverseCapacityBlockStart :
      Typed.WidthIndex p.d → Nat :=
    fun w =>
      activeCapacity - capacityPrefix (w.val + 1)
  let reverseCapacityBlockEnd :
      Typed.WidthIndex p.d → Nat :=
    fun w =>
      activeCapacity - capacityPrefix w.val
  change
    effect x ≤ effect z ↔
      ∀ w : Typed.WidthIndex p.d,
        x w.val =
          z w.val +
            (min
                (effectRank z)
                (reverseCapacityBlockEnd w) -
              max
                (effectRank x)
                (reverseCapacityBlockStart w))
  have hxProfileRaw := c95_coordinateProfile p x
  have hzProfileRaw := c95_coordinateProfile p z
  dsimp only at hxProfileRaw hzProfileRaw
  have hxProfileRaw := hxProfileRaw hx
  have hzProfileRaw := hzProfileRaw hz
  change
    ∀ w : Typed.WidthIndex p.d,
      x w.val =
        reverseCapacityBlockEnd w -
          max
            (effectRank x)
            (reverseCapacityBlockStart w) at hxProfileRaw
  change
    ∀ w : Typed.WidthIndex p.d,
      z w.val =
        reverseCapacityBlockEnd w -
          max
            (effectRank z)
            (reverseCapacityBlockStart w) at hzProfileRaw
  constructor
  · intro hEffect w
    have hRank :
        effectRank x ≤ effectRank z := by
      exact Int.toNat_le_toNat hEffect
    rw [hxProfileRaw w, hzProfileRaw w]
    exact
      c95_nat_reverse_capacity_block_overlap
        (effectRank x)
        (effectRank z)
        (reverseCapacityBlockStart w)
        (reverseCapacityBlockEnd w)
        hRank
  · intro hCoordinates
    have hOrder :=
      ledgerEffectOn_productWindowU_le_iff_forall_reverse_le_of_canonicalLeftGreedy
        p
        x
        z
    dsimp only at hOrder
    apply (hOrder hx hz).mpr
    intro j
    by_cases hjWidth : j < Typed.typedWidth p.d
    · let w : Typed.WidthIndex p.d := ⟨j, hjWidth⟩
      have hwEquation := hCoordinates w
      have hwLe : z w.val ≤ x w.val := by
        omega
      simpa [w] using hwLe
    · have hjInactive :
          j ∉ (paramsUOfProduct p).active := by
        intro hjActive
        have hjWindow :=
          productWindowU_covers_active p j hjActive
        change
          j ∈ List.range (Typed.typedWidth p.d) at hjWindow
        exact hjWidth (List.mem_range.mp hjWindow)
      rw [hz.1 j hjInactive, hx.1 j hjInactive]
      exact Nat.zero_le _

end UnrestrictedBridge
end VFH2
