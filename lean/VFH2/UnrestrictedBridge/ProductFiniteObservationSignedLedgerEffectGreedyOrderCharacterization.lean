import VFH2.UnrestrictedBridge.ProductFiniteObservationSignedLedgerEffectGreedyFiberDecomposition

/-!
# Product finite-observation semantic greedy order characterization

This module proves the order structure carried by the semantic canonical
left-greedy representatives from the preceding fiber decomposition. Among
globally active-supported bounded semantic greedy states, Product-window
ledger-effect order is exactly the reverse of global pointwise state order.

The mathematical core is a finite induction showing that, for two vectors
bounded by the same capacity and satisfying the relational left-greedy
condition, order of their sums is equivalent to their pointwise order. The
signed Product-window effect formula reverses that sum order, while global
active support extends the finite masked comparison to every `Nat`
coordinate.

All implementation predicates and lemmas remain private or theorem-local. No
order structure, normalizer, compatibility namespace, alias, or additional
public definition is introduced.

Only the canonical finite Product observation window is involved. This does
not define a global infinite ledger, is not unrestricted `TTP-VF-H2-004`, and
makes no full-theory, empirical, physical, medical, causal, or biological
validation claim. No model assumption is introduced.
-/

namespace VFH2
namespace UnrestrictedBridge

private theorem c88_sum_ofFn_zero
    (n : Nat)
    (f : Fin n → Nat)
    (h : ∀ i, f i = 0) :
    (List.ofFn f).sum = 0 := by
  induction n with
  | zero =>
      simp
  | succ n ih =>
      rw [List.ofFn_succ, List.sum_cons]
      rw [h]
      simp only [Nat.zero_add]
      exact
        ih
          (fun i => f i.succ)
          (fun i => h i.succ)

private theorem c88_sum_ofFn_le_sum_ofFn
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

private def c88FiniteLeftGreedy
    {n : Nat}
    (cap values : Fin n → Nat) :
    Prop :=
  ∀ i j : Fin n,
    i.val < j.val →
    values i < cap i →
      values j = 0

private theorem c88_boundedLeftGreedy_sum_le_iff_pointwise_le
    (n : Nat)
    (cap a b : Fin n → Nat)
    (haBound : ∀ i, a i ≤ cap i)
    (hbBound : ∀ i, b i ≤ cap i)
    (haGreedy : c88FiniteLeftGreedy cap a)
    (hbGreedy : c88FiniteLeftGreedy cap b) :
    (List.ofFn a).sum ≤ (List.ofFn b).sum ↔
      ∀ i : Fin n, a i ≤ b i := by
  induction n with
  | zero =>
      constructor
      · intro _ i
        exact Fin.elim0 i
      · intro _
        simp
  | succ n ih =>
      constructor
      · intro hsum
        have hsumDecomp :
            a (0 : Fin (n + 1)) +
                (List.ofFn
                  (fun i : Fin n =>
                    a i.succ)).sum ≤
              b (0 : Fin (n + 1)) +
                (List.ofFn
                  (fun i : Fin n =>
                    b i.succ)).sum := by
          simpa [List.ofFn_succ] using hsum
        by_cases haHead :
            a (0 : Fin (n + 1)) <
              cap (0 : Fin (n + 1))
        · have haTailZero :
              ∀ i : Fin n,
                a i.succ = 0 := by
            intro i
            exact
              haGreedy
                (0 : Fin (n + 1))
                i.succ
                (by simp)
                haHead
          have haTailSum :
              (List.ofFn
                (fun i : Fin n =>
                  a i.succ)).sum = 0 :=
            c88_sum_ofFn_zero
              n
              (fun i : Fin n =>
                a i.succ)
              haTailZero
          have hhead :
              a (0 : Fin (n + 1)) ≤
                b (0 : Fin (n + 1)) := by
            by_cases hle :
                a (0 : Fin (n + 1)) ≤
                  b (0 : Fin (n + 1))
            · exact hle
            · have hbHead :
                  b (0 : Fin (n + 1)) <
                    cap (0 : Fin (n + 1)) := by
                omega
              have hbTailZero :
                  ∀ i : Fin n,
                    b i.succ = 0 := by
                intro i
                exact
                  hbGreedy
                    (0 : Fin (n + 1))
                    i.succ
                    (by simp)
                    hbHead
              have hbTailSum :
                  (List.ofFn
                    (fun i : Fin n =>
                      b i.succ)).sum = 0 :=
                c88_sum_ofFn_zero
                  n
                  (fun i : Fin n =>
                    b i.succ)
                  hbTailZero
              omega
          intro i
          refine Fin.cases ?_ (fun j => ?_) i
          · exact hhead
          · rw [haTailZero j]
            exact Nat.zero_le _
        · have haHeadTop :
              a (0 : Fin (n + 1)) =
                cap (0 : Fin (n + 1)) := by
            have hbound :=
              haBound (0 : Fin (n + 1))
            omega
          have hbHeadTop :
              b (0 : Fin (n + 1)) =
                cap (0 : Fin (n + 1)) := by
            by_cases htop :
                b (0 : Fin (n + 1)) =
                  cap (0 : Fin (n + 1))
            · exact htop
            · have hbHead :
                  b (0 : Fin (n + 1)) <
                    cap (0 : Fin (n + 1)) := by
                have hbound :=
                  hbBound (0 : Fin (n + 1))
                omega
              have hbTailZero :
                  ∀ i : Fin n,
                    b i.succ = 0 := by
                intro i
                exact
                  hbGreedy
                    (0 : Fin (n + 1))
                    i.succ
                    (by simp)
                    hbHead
              have hbTailSum :
                  (List.ofFn
                    (fun i : Fin n =>
                      b i.succ)).sum = 0 :=
                c88_sum_ofFn_zero
                  n
                  (fun i : Fin n =>
                    b i.succ)
                  hbTailZero
              omega
          have htailSum :
              (List.ofFn
                (fun i : Fin n =>
                  a i.succ)).sum ≤
                (List.ofFn
                  (fun i : Fin n =>
                    b i.succ)).sum := by
            omega
          have htailPointwise :
              ∀ i : Fin n,
                a i.succ ≤ b i.succ :=
            (ih
              (fun i : Fin n =>
                cap i.succ)
              (fun i : Fin n =>
                a i.succ)
              (fun i : Fin n =>
                b i.succ)
              (fun i => haBound i.succ)
              (fun i => hbBound i.succ)
              (by
                intro i j hij hi
                exact
                  haGreedy
                    i.succ
                    j.succ
                    (by simpa using hij)
                    hi)
              (by
                intro i j hij hi
                exact
                  hbGreedy
                    i.succ
                    j.succ
                    (by simpa using hij)
                    hi)).mp
              htailSum
          intro i
          refine Fin.cases ?_ (fun j => ?_) i
          · rw [haHeadTop, hbHeadTop]
            exact Nat.le_refl _
          · exact htailPointwise j
      · intro hpointwise
        exact
          c88_sum_ofFn_le_sum_ofFn
            (n + 1)
            a
            b
            hpointwise

private def c88Capacity
    (p : ProductRestrictedParams)
    (w : Typed.WidthIndex p.d) :
    Nat :=
  if ProductIndex.unflatten w ∈ p.active then
    p.n
  else
    0

private def c88Masked
    (p : ProductRestrictedParams)
    (s : StateU)
    (w : Typed.WidthIndex p.d) :
    Nat :=
  if ProductIndex.unflatten w ∈ p.active then
    s w.val
  else
    0

private theorem c88Masked_le_capacity
    (p : ProductRestrictedParams)
    (s : StateU)
    (hs : inStateSpaceU (paramsUOfProduct p) s) :
    ∀ w,
      c88Masked p s w ≤
        c88Capacity p w := by
  intro w
  by_cases hw :
      ProductIndex.unflatten w ∈ p.active
  · simp only [
      c88Masked,
      c88Capacity,
      hw,
      ↓reduceIte
    ]
    have hbound := hs w.val
    change s w.val ≤ p.n at hbound
    exact hbound
  · simp [c88Masked, c88Capacity, hw]

private theorem c88Masked_finiteLeftGreedy
    (p : ProductRestrictedParams)
    (s : StateU)
    (hrel :
      ∀ u v : Typed.WidthIndex p.d,
        u.val < v.val →
        ProductIndex.unflatten u ∈ p.active →
        ProductIndex.unflatten v ∈ p.active →
        s u.val < p.n →
          s v.val = 0) :
    c88FiniteLeftGreedy
      (c88Capacity p)
      (c88Masked p s) := by
  intro u v huv huValue
  by_cases hu :
      ProductIndex.unflatten u ∈ p.active
  · by_cases hv :
        ProductIndex.unflatten v ∈ p.active
    · simpa [c88Masked, hv] using
        hrel
          u
          v
          huv
          hu
          hv
          (by
            simpa [
              c88Masked,
              c88Capacity,
              hu
            ] using huValue)
    · simp [c88Masked, hv]
  · simp [c88Masked, c88Capacity, hu] at huValue

private theorem c88_val_mem_paramsUOfProduct_active_iff
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

private theorem c88_mem_paramsUOfProduct_active_lt_typedWidth
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
On semantic canonical left-greedy Product states, signed Product-window
ledger-effect order is exactly reverse pointwise state order.
-/
theorem ledgerEffectOn_productWindowU_le_iff_forall_reverse_le_of_canonicalLeftGreedy
    (p : ProductRestrictedParams)
    (x z : StateU) :
    let IsCanonicalLeftGreedy : StateU → Prop :=
      fun s =>
        (∀ j : Nat,
          j ∉ (paramsUOfProduct p).active →
            s j = 0) ∧
        inStateSpaceU
          (paramsUOfProduct p)
          s ∧
        ∀ u v : Typed.WidthIndex p.d,
          u.val < v.val →
          ProductIndex.unflatten u ∈ p.active →
          ProductIndex.unflatten v ∈ p.active →
          s u.val < p.n →
            s v.val = 0
    IsCanonicalLeftGreedy x →
    IsCanonicalLeftGreedy z →
      (ledgerEffectOn
          (paramsUOfProduct p)
          (productWindowU p)
          x ≤
        ledgerEffectOn
          (paramsUOfProduct p)
          (productWindowU p)
          z ↔
        ∀ j : Nat,
          z j ≤ x j) := by
  dsimp only
  intro hx hz
  have hxMaskedBound :=
    c88Masked_le_capacity
      p
      x
      hx.2.1
  have hzMaskedBound :=
    c88Masked_le_capacity
      p
      z
      hz.2.1
  have hxMaskedGreedy :=
    c88Masked_finiteLeftGreedy
      p
      x
      hx.2.2
  have hzMaskedGreedy :=
    c88Masked_finiteLeftGreedy
      p
      z
      hz.2.2
  have hfinite :=
    c88_boundedLeftGreedy_sum_le_iff_pointwise_le
      (Typed.typedWidth p.d)
      (c88Capacity p)
      (c88Masked p z)
      (c88Masked p x)
      hzMaskedBound
      hxMaskedBound
      hzMaskedGreedy
      hxMaskedGreedy
  constructor
  · intro heffect
    have hxFormula :=
      ledgerEffectOn_productWindowU_eq_activeCapacity_sub_sum_activeValues
        p
        x
    have hzFormula :=
      ledgerEffectOn_productWindowU_eq_activeCapacity_sub_sum_activeValues
        p
        z
    have hsumCast :
        ((List.ofFn
          (fun w : Typed.WidthIndex p.d =>
            if ProductIndex.unflatten w ∈ p.active then
              z w.val
            else
              0)).sum : Int) ≤
          ((List.ofFn
            (fun w : Typed.WidthIndex p.d =>
              if ProductIndex.unflatten w ∈ p.active then
                x w.val
              else
                0)).sum : Int) := by
      omega
    have hsum :
        (List.ofFn
          (fun w : Typed.WidthIndex p.d =>
            if ProductIndex.unflatten w ∈ p.active then
              z w.val
            else
              0)).sum ≤
          (List.ofFn
            (fun w : Typed.WidthIndex p.d =>
              if ProductIndex.unflatten w ∈ p.active then
                x w.val
              else
                0)).sum :=
      Int.ofNat_le.mp hsumCast
    have hmasked :
        ∀ w : Typed.WidthIndex p.d,
          c88Masked p z w ≤
            c88Masked p x w :=
      hfinite.mp
        (by
          change
            (List.ofFn
              (c88Masked p z)).sum ≤
              (List.ofFn
                (c88Masked p x)).sum
          exact hsum)
    intro j
    by_cases hjWidth :
        j < Typed.typedWidth p.d
    · let w : Typed.WidthIndex p.d :=
        ⟨j, hjWidth⟩
      by_cases hw :
          ProductIndex.unflatten w ∈ p.active
      · have hwOrder := hmasked w
        simpa [c88Masked, hw, w] using hwOrder
      · have hjInactive :
            j ∉ (paramsUOfProduct p).active := by
          intro hjActive
          exact
            hw
              ((c88_val_mem_paramsUOfProduct_active_iff
                p
                w).mp hjActive)
        rw [hz.1 j hjInactive, hx.1 j hjInactive]
        exact Nat.zero_le _
    · have hjInactive :
          j ∉ (paramsUOfProduct p).active := by
        intro hjActive
        exact
          hjWidth
            (c88_mem_paramsUOfProduct_active_lt_typedWidth
              p
              j
              hjActive)
      rw [hz.1 j hjInactive, hx.1 j hjInactive]
      exact Nat.zero_le _
  · intro hpointwise
    have hsum :
        (List.ofFn
          (fun w : Typed.WidthIndex p.d =>
            if ProductIndex.unflatten w ∈ p.active then
              z w.val
            else
              0)).sum ≤
          (List.ofFn
            (fun w : Typed.WidthIndex p.d =>
              if ProductIndex.unflatten w ∈ p.active then
                x w.val
              else
                0)).sum := by
      apply
        c88_sum_ofFn_le_sum_ofFn
          (Typed.typedWidth p.d)
      intro w
      by_cases hw :
          ProductIndex.unflatten w ∈ p.active
      · simpa [hw] using hpointwise w.val
      · simp [hw]
    have hxFormula :=
      ledgerEffectOn_productWindowU_eq_activeCapacity_sub_sum_activeValues
        p
        x
    have hzFormula :=
      ledgerEffectOn_productWindowU_eq_activeCapacity_sub_sum_activeValues
        p
        z
    have hsumCast :
        ((List.ofFn
          (fun w : Typed.WidthIndex p.d =>
            if ProductIndex.unflatten w ∈ p.active then
              z w.val
            else
              0)).sum : Int) ≤
          ((List.ofFn
            (fun w : Typed.WidthIndex p.d =>
              if ProductIndex.unflatten w ∈ p.active then
                x w.val
              else
                0)).sum : Int) := by
      exact_mod_cast hsum
    omega

end UnrestrictedBridge
end VFH2
