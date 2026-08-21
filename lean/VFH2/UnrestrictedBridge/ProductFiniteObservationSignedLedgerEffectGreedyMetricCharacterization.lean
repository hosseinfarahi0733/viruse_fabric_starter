import VFH2.UnrestrictedBridge.ProductFiniteObservationSignedLedgerEffectGreedyCapacityBlockOverlapCharacterization

/-!
# Canonical active-coordinate metric characterization

This module proves that the finite active-coordinate L1 distance between any
two semantic canonical left-greedy Product-window states is exactly the
symmetric distance between their natural ledger-effect ranks.

The proof splits on signed-effect order, uses C95 in both directions to obtain
the required coordinate order, converts the finite masked coordinate sum into
an active-value-sum difference, and closes the identity with the signed
Product-window effect formula.  It is a theorem for arbitrary canonical pairs,
not a wrapper around the C94 chain.

Both distance functions are theorem-local and the finite-sum machinery is
private.  This creates no public metric structure, isometry, normalizer, global
order or successor API, update trajectory, ledger mutation, or infinite ledger.
It remains a finite restricted Product observation result, not unrestricted
TTP-VF-H2-004 and not full-theory, empirical, physical, medical, causal, or
biological validation.
-/


namespace VFH2
namespace UnrestrictedBridge

private theorem c96_sum_ofFn_le_sum_ofFn
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

private theorem c96_sum_ofFn_sub_eq_sub_sum_ofFn
    (n : Nat)
    (f g : Fin n → Nat)
    (hpointwise : ∀ i : Fin n, g i ≤ f i) :
    (List.ofFn (fun i => f i - g i)).sum =
      (List.ofFn f).sum - (List.ofFn g).sum := by
  induction n with
  | zero =>
      simp
  | succ n ih =>
      simp only [List.ofFn_succ, List.sum_cons]
      have hhead := hpointwise (0 : Fin (n + 1))
      have htail :
          (List.ofFn
              (fun i : Fin n => g i.succ)).sum ≤
            (List.ofFn
              (fun i : Fin n => f i.succ)).sum :=
        c96_sum_ofFn_le_sum_ofFn
          n
          (fun i : Fin n => g i.succ)
          (fun i : Fin n => f i.succ)
          (fun i => hpointwise i.succ)
      rw [
        ih
          (fun i => f i.succ)
          (fun i => g i.succ)
          (fun i => hpointwise i.succ)
      ]
      omega

theorem activeCoordinateL1Distance_eq_ledgerEffectRankDistance_of_canonicalLeftGreedy
    (p : ProductRestrictedParams)
    (x z : StateU) :
    let effect : StateU → Int :=
      fun s =>
        ledgerEffectOn
          (paramsUOfProduct p)
          (productWindowU p)
          s
    let effectRank : StateU → Nat :=
      fun s => Int.toNat (effect s)
    let natDistance : Nat → Nat → Nat :=
      fun a b => (a - b) + (b - a)
    let activeCoordinateL1Distance : StateU → StateU → Nat :=
      fun s t =>
        (List.ofFn
          (fun w : Typed.WidthIndex p.d =>
            if ProductIndex.unflatten w ∈ p.active then
              natDistance (s w.val) (t w.val)
            else
              0)).sum
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
      activeCoordinateL1Distance x z =
        natDistance (effectRank x) (effectRank z) := by
  dsimp only
  intro hx hz
  let effect : StateU → Int :=
    fun s =>
      ledgerEffectOn
        (paramsUOfProduct p)
        (productWindowU p)
        s
  let effectRank : StateU → Nat :=
    fun s => Int.toNat (effect s)
  let natDistance : Nat → Nat → Nat :=
    fun a b => (a - b) + (b - a)
  let activeValue : StateU → Typed.WidthIndex p.d → Nat :=
    fun s w =>
      if ProductIndex.unflatten w ∈ p.active then
        s w.val
      else
        0
  let activeSum : StateU → Nat :=
    fun s => (List.ofFn (activeValue s)).sum
  let activeCapacity : Nat :=
    (List.ofFn
      (fun w : Typed.WidthIndex p.d =>
        if ProductIndex.unflatten w ∈ p.active then
          p.n
        else
          0)).sum
  change
    (List.ofFn
        (fun w : Typed.WidthIndex p.d =>
          if ProductIndex.unflatten w ∈ p.active then
            natDistance (x w.val) (z w.val)
          else
            0)).sum =
      natDistance (effectRank x) (effectRank z)
  have hxNonneg : 0 ≤ effect x := by
    exact
      ledgerEffectOn_nonneg
        (paramsUOfProduct p)
        (productWindowU p)
        x
        hx.2.1
  have hzNonneg : 0 ≤ effect z := by
    exact
      ledgerEffectOn_nonneg
        (paramsUOfProduct p)
        (productWindowU p)
        z
        hz.2.1
  have hxRankCast :
      (effectRank x : Int) = effect x := by
    dsimp [effectRank]
    exact Int.toNat_of_nonneg hxNonneg
  have hzRankCast :
      (effectRank z : Int) = effect z := by
    dsimp [effectRank]
    exact Int.toNat_of_nonneg hzNonneg
  have hxFormula :
      effect x =
        (activeCapacity : Int) - (activeSum x : Int) := by
    simpa [effect, activeCapacity, activeSum, activeValue] using
      ledgerEffectOn_productWindowU_eq_activeCapacity_sub_sum_activeValues
        p
        x
  have hzFormula :
      effect z =
        (activeCapacity : Int) - (activeSum z : Int) := by
    simpa [effect, activeCapacity, activeSum, activeValue] using
      ledgerEffectOn_productWindowU_eq_activeCapacity_sub_sum_activeValues
        p
        z
  by_cases hxzEffect : effect x ≤ effect z
  · have hC95 :=
      ledgerEffectOn_productWindowU_le_iff_forall_coordinateDecrease_eq_reverseCapacityBlockOverlap_of_canonicalLeftGreedy
        p
        x
        z
    dsimp only at hC95
    have hCoordinates := (hC95 hx hz).mp hxzEffect
    have hzxCoordinate :
        ∀ w : Typed.WidthIndex p.d,
          z w.val ≤ x w.val := by
      intro w
      have hw := hCoordinates w
      omega
    have hActivePointwise :
        ∀ w : Typed.WidthIndex p.d,
          activeValue z w ≤ activeValue x w := by
      intro w
      by_cases hw : ProductIndex.unflatten w ∈ p.active
      · simpa [activeValue, hw] using hzxCoordinate w
      · simp [activeValue, hw]
    have hActiveSum :
        activeSum z ≤ activeSum x := by
      exact
        c96_sum_ofFn_le_sum_ofFn
          (Typed.typedWidth p.d)
          (activeValue z)
          (activeValue x)
          hActivePointwise
    have hPointwiseDistance :
        ∀ w : Typed.WidthIndex p.d,
          (if ProductIndex.unflatten w ∈ p.active then
              natDistance (x w.val) (z w.val)
            else
              0) =
            activeValue x w - activeValue z w := by
      intro w
      by_cases hw : ProductIndex.unflatten w ∈ p.active
      · have hwLe := hzxCoordinate w
        simp [natDistance, activeValue, hw]
        omega
      · simp [activeValue, hw]
    have hDistanceSum :
        (List.ofFn
            (fun w : Typed.WidthIndex p.d =>
              if ProductIndex.unflatten w ∈ p.active then
                natDistance (x w.val) (z w.val)
              else
                0)).sum =
          activeSum x - activeSum z := by
      have hLists :
          List.ofFn
              (fun w : Typed.WidthIndex p.d =>
                if ProductIndex.unflatten w ∈ p.active then
                  natDistance (x w.val) (z w.val)
                else
                  0) =
            List.ofFn
              (fun w : Typed.WidthIndex p.d =>
                activeValue x w - activeValue z w) := by
        apply congrArg List.ofFn
        funext w
        exact hPointwiseDistance w
      rw [hLists]
      exact
        c96_sum_ofFn_sub_eq_sub_sum_ofFn
          (Typed.typedWidth p.d)
          (activeValue x)
          (activeValue z)
          hActivePointwise
    have hRankOrder : effectRank x ≤ effectRank z := by
      exact Int.toNat_le_toNat hxzEffect
    have hRankDistance :
        natDistance (effectRank x) (effectRank z) =
          effectRank z - effectRank x := by
      dsimp [natDistance]
      omega
    rw [hDistanceSum, hRankDistance]
    omega
  · have hzxEffect : effect z ≤ effect x := by
      omega
    have hC95 :=
      ledgerEffectOn_productWindowU_le_iff_forall_coordinateDecrease_eq_reverseCapacityBlockOverlap_of_canonicalLeftGreedy
        p
        z
        x
    dsimp only at hC95
    have hCoordinates := (hC95 hz hx).mp hzxEffect
    have hxzCoordinate :
        ∀ w : Typed.WidthIndex p.d,
          x w.val ≤ z w.val := by
      intro w
      have hw := hCoordinates w
      omega
    have hActivePointwise :
        ∀ w : Typed.WidthIndex p.d,
          activeValue x w ≤ activeValue z w := by
      intro w
      by_cases hw : ProductIndex.unflatten w ∈ p.active
      · simpa [activeValue, hw] using hxzCoordinate w
      · simp [activeValue, hw]
    have hActiveSum :
        activeSum x ≤ activeSum z := by
      exact
        c96_sum_ofFn_le_sum_ofFn
          (Typed.typedWidth p.d)
          (activeValue x)
          (activeValue z)
          hActivePointwise
    have hPointwiseDistance :
        ∀ w : Typed.WidthIndex p.d,
          (if ProductIndex.unflatten w ∈ p.active then
              natDistance (x w.val) (z w.val)
            else
              0) =
            activeValue z w - activeValue x w := by
      intro w
      by_cases hw : ProductIndex.unflatten w ∈ p.active
      · have hwLe := hxzCoordinate w
        simp [natDistance, activeValue, hw]
        omega
      · simp [activeValue, hw]
    have hDistanceSum :
        (List.ofFn
            (fun w : Typed.WidthIndex p.d =>
              if ProductIndex.unflatten w ∈ p.active then
                natDistance (x w.val) (z w.val)
              else
                0)).sum =
          activeSum z - activeSum x := by
      have hLists :
          List.ofFn
              (fun w : Typed.WidthIndex p.d =>
                if ProductIndex.unflatten w ∈ p.active then
                  natDistance (x w.val) (z w.val)
                else
                  0) =
            List.ofFn
              (fun w : Typed.WidthIndex p.d =>
                activeValue z w - activeValue x w) := by
        apply congrArg List.ofFn
        funext w
        exact hPointwiseDistance w
      rw [hLists]
      exact
        c96_sum_ofFn_sub_eq_sub_sum_ofFn
          (Typed.typedWidth p.d)
          (activeValue z)
          (activeValue x)
          hActivePointwise
    have hRankOrder : effectRank z ≤ effectRank x := by
      exact Int.toNat_le_toNat hzxEffect
    have hRankDistance :
        natDistance (effectRank x) (effectRank z) =
          effectRank x - effectRank z := by
      dsimp [natDistance]
      omega
    rw [hDistanceSum, hRankDistance]
    omega

end UnrestrictedBridge
end VFH2
