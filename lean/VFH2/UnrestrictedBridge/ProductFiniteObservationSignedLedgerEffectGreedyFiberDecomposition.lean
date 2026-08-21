import VFH2.UnrestrictedBridge.ProductFiniteObservationSignedLedgerEffectGreedyStateSpaceNormalForm
import VFH2.UnrestrictedBridge.ProductFiniteObservationLevelSetCharacterization

/-!
# Product finite-observation semantic greedy fiber decomposition

This module upgrades the prefix recurrence normal form to a semantic canonical
transversal for every admissible Product-window ledger-effect fiber. Its
canonical predicate is independent of the chosen state and effect: a globally
active-supported bounded state is left-greedy when every later active value is
zero after an earlier active coordinate is unsaturated.

The recurrence normal form supplies existence. A separate finite induction
proves that two bounded relationally left-greedy active vectors with the same
sum are equal; the uniqueness proof therefore does not reuse the recurrence
normal form's uniqueness clause. The complete admissible fiber is then
characterized by the existing active-value-sum level set.

All implementation predicates and lemmas remain private or theorem-local. No
normalizer, compatibility namespace, alias, or additional public definition is
introduced. Uniqueness is only within the semantic canonical class; the full
fiber can contain many states.

Only the canonical finite Product observation window is involved. This does
not define a global infinite ledger, is not unrestricted `TTP-VF-H2-004`, and
makes no full-theory, empirical, physical, medical, causal, or biological
validation claim. No model assumption is introduced.
-/

namespace VFH2
namespace UnrestrictedBridge

private theorem c87_sum_ofFn_zero
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

private theorem c87_sum_ofFn_split
    (x : Nat → Nat)
    (k m : Nat) :
    (List.ofFn
      (fun i : Fin (k + m) =>
        x i.val)).sum =
      (List.ofFn
        (fun i : Fin k =>
          x i.val)).sum +
      (List.ofFn
        (fun i : Fin m =>
          x (k + i.val))).sum := by
  rw [List.ofFn_add, List.sum_append]
  congr 1

private theorem c87_prefix_succ
    (x : Nat → Nat)
    (k : Nat) :
    (List.ofFn
      (fun i : Fin (k + 1) =>
        x i.val)).sum =
      (List.ofFn
        (fun i : Fin k =>
          x i.val)).sum +
        x k := by
  rw [List.ofFn_succ_last, List.sum_append, List.sum_singleton]
  congr 1

private theorem c87_prefix_add_apply_le_prefix
    (x : Nat → Nat)
    {u v : Nat}
    (huv : u < v) :
    (List.ofFn
      (fun i : Fin u =>
        x i.val)).sum +
        x u ≤
      (List.ofFn
        (fun i : Fin v =>
          x i.val)).sum := by
  have hdecomp :=
    c87_sum_ofFn_split x (u + 1) (v - (u + 1))
  have hlength :
      u + 1 + (v - (u + 1)) = v := by
    omega
  rw [hlength] at hdecomp
  rw [c87_prefix_succ] at hdecomp
  omega

private theorem c87_val_mem_paramsUOfProduct_active_iff
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

private theorem c87_recurrence_implies_relationalLeftGreedy
    (p : ProductRestrictedParams)
    (q : Nat)
    (x : StateU)
    (hxRecurrence :
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
                  x v.val)).sum)) :
    ∀ u v : Typed.WidthIndex p.d,
      u.val < v.val →
      ProductIndex.unflatten u ∈ p.active →
      ProductIndex.unflatten v ∈ p.active →
      x u.val < p.n →
        x v.val = 0 := by
  intro u v huv huActive hvActive huUnsaturated
  have huRec := hxRecurrence u
  have hvRec := hxRecurrence v
  simp only [huActive, hvActive, ↓reduceIte] at huRec hvRec
  have hprefixLe :=
    c87_prefix_add_apply_le_prefix
      x
      huv
  have hqLeAtU :
      q ≤
        (List.ofFn
          (fun i : Fin u.val =>
            x i.val)).sum +
          x u.val := by
    by_cases hcap :
        p.n ≤
          q -
            (List.ofFn
              (fun i : Fin u.val =>
                x i.val)).sum
    · rw [Nat.min_eq_left hcap] at huRec
      omega
    · have hremaining :
          q -
              (List.ofFn
                (fun i : Fin u.val =>
                  x i.val)).sum ≤
            p.n := by
        omega
      rw [Nat.min_eq_right hremaining] at huRec
      omega
  have hqLeAtV :
      q ≤
        (List.ofFn
          (fun i : Fin v.val =>
            x i.val)).sum := by
    omega
  have hzero :
      q -
          (List.ofFn
            (fun i : Fin v.val =>
              x i.val)).sum =
        0 := by
    omega
  rw [hzero] at hvRec
  simpa using hvRec

private theorem c87_mem_paramsUOfProduct_active_lt_typedWidth
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

private def c87FiniteLeftGreedy
    {n : Nat}
    (cap values : Fin n → Nat) :
    Prop :=
  ∀ i j : Fin n,
    i.val < j.val →
    values i < cap i →
      values j = 0

private def c87Capacity
    (p : ProductRestrictedParams)
    (w : Typed.WidthIndex p.d) :
    Nat :=
  if ProductIndex.unflatten w ∈ p.active then
    p.n
  else
    0

private def c87Masked
    (p : ProductRestrictedParams)
    (s : StateU)
    (w : Typed.WidthIndex p.d) :
    Nat :=
  if ProductIndex.unflatten w ∈ p.active then
    s w.val
  else
    0

private theorem c87_boundedLeftGreedy_eq_of_sum_eq
    (n : Nat)
    (cap a b : Fin n → Nat)
    (haBound : ∀ i, a i ≤ cap i)
    (hbBound : ∀ i, b i ≤ cap i)
    (haGreedy : c87FiniteLeftGreedy cap a)
    (hbGreedy : c87FiniteLeftGreedy cap b)
    (hsum :
      (List.ofFn a).sum =
        (List.ofFn b).sum) :
    a = b := by
  induction n with
  | zero =>
      funext i
      exact Fin.elim0 i
  | succ n ih =>
      have hsumDecomp :
          a (0 : Fin (n + 1)) +
              (List.ofFn
                (fun i : Fin n =>
                  a i.succ)).sum =
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
          c87_sum_ofFn_zero
            n
            (fun i : Fin n =>
              a i.succ)
            haTailZero
        have hbHead :
            b (0 : Fin (n + 1)) <
              cap (0 : Fin (n + 1)) := by
          have hbHeadBound :=
            hbBound (0 : Fin (n + 1))
          by_cases hlt :
              b (0 : Fin (n + 1)) <
                cap (0 : Fin (n + 1))
          · exact hlt
          · have hbHeadTop :
                b (0 : Fin (n + 1)) =
                  cap (0 : Fin (n + 1)) := by
              omega
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
          c87_sum_ofFn_zero
            n
            (fun i : Fin n =>
              b i.succ)
            hbTailZero
        have hhead :
            a (0 : Fin (n + 1)) =
              b (0 : Fin (n + 1)) := by
          omega
        funext i
        refine Fin.cases ?_ (fun j => ?_) i
        · exact hhead
        · rw [haTailZero j, hbTailZero j]
      · have haHeadTop :
            a (0 : Fin (n + 1)) =
              cap (0 : Fin (n + 1)) := by
          have := haBound (0 : Fin (n + 1))
          omega
        have hbHeadTop :
            b (0 : Fin (n + 1)) =
              cap (0 : Fin (n + 1)) := by
          have hbHeadBound :=
            hbBound (0 : Fin (n + 1))
          by_cases htop :
              b (0 : Fin (n + 1)) =
                cap (0 : Fin (n + 1))
          · exact htop
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
              c87_sum_ofFn_zero
                n
                (fun i : Fin n =>
                  b i.succ)
                hbTailZero
            omega
        have htailSum :
            (List.ofFn
              (fun i : Fin n =>
                a i.succ)).sum =
              (List.ofFn
                (fun i : Fin n =>
                  b i.succ)).sum := by
          omega
        have htailEq :
            (fun i : Fin n =>
              a i.succ) =
            (fun i : Fin n =>
              b i.succ) := by
          apply
            ih
              (fun i : Fin n =>
                cap i.succ)
              (fun i : Fin n =>
                a i.succ)
              (fun i : Fin n =>
                b i.succ)
          · intro i
            exact haBound i.succ
          · intro i
            exact hbBound i.succ
          · intro i j hij hi
            exact
              haGreedy
                i.succ
                j.succ
                (by simpa using hij)
                hi
          · intro i j hij hi
            exact
              hbGreedy
                i.succ
                j.succ
                (by simpa using hij)
                hi
          · exact htailSum
        funext i
        refine Fin.cases ?_ (fun j => ?_) i
        · rw [haHeadTop, hbHeadTop]
        · exact congrFun htailEq j

private theorem c87Masked_le_capacity
    (p : ProductRestrictedParams)
    (s : StateU)
    (hs : inStateSpaceU (paramsUOfProduct p) s) :
    ∀ w,
      c87Masked p s w ≤
        c87Capacity p w := by
  intro w
  by_cases hw :
      ProductIndex.unflatten w ∈ p.active
  · simp only [
      c87Masked,
      c87Capacity,
      hw,
      ↓reduceIte
    ]
    have hbound := hs w.val
    change s w.val ≤ p.n at hbound
    exact hbound
  · simp [c87Masked, c87Capacity, hw]

private theorem c87Masked_finiteLeftGreedy
    (p : ProductRestrictedParams)
    (s : StateU)
    (hrel :
      ∀ u v : Typed.WidthIndex p.d,
        u.val < v.val →
        ProductIndex.unflatten u ∈ p.active →
        ProductIndex.unflatten v ∈ p.active →
        s u.val < p.n →
          s v.val = 0) :
    c87FiniteLeftGreedy
      (c87Capacity p)
      (c87Masked p s) := by
  intro u v huv huValue
  by_cases hu :
      ProductIndex.unflatten u ∈ p.active
  · by_cases hv :
        ProductIndex.unflatten v ∈ p.active
    · simpa [c87Masked, hv] using
        hrel
          u
          v
          huv
          hu
          hv
          (by
            simpa [
              c87Masked,
              c87Capacity,
              hu
            ] using huValue)
    · simp [c87Masked, hv]
  · simp [c87Masked, c87Capacity, hu] at huValue

private theorem c87_state_eq_of_masked_eq
    (p : ProductRestrictedParams)
    (a b : StateU)
    (haSupport :
      ∀ j : Nat,
        j ∉ (paramsUOfProduct p).active →
          a j = 0)
    (hbSupport :
      ∀ j : Nat,
        j ∉ (paramsUOfProduct p).active →
          b j = 0)
    (hmasked :
      c87Masked p a =
        c87Masked p b) :
    a = b := by
  funext j
  by_cases hjWidth :
      j < Typed.typedWidth p.d
  · let w : Typed.WidthIndex p.d :=
      ⟨j, hjWidth⟩
    by_cases hw :
        ProductIndex.unflatten w ∈ p.active
    · have hvalue :=
        congrFun hmasked w
      simpa [c87Masked, hw, w] using hvalue
    · have hjInactive :
          j ∉ (paramsUOfProduct p).active := by
        intro hjActive
        exact
          hw
            ((c87_val_mem_paramsUOfProduct_active_iff
              p
              w).mp hjActive)
      rw [
        haSupport j hjInactive,
        hbSupport j hjInactive
      ]
  · have hjInactive :
        j ∉ (paramsUOfProduct p).active := by
      intro hjActive
      exact
        hjWidth
          (c87_mem_paramsUOfProduct_active_lt_typedWidth
            p
            j
            hjActive)
    rw [
      haSupport j hjInactive,
      hbSupport j hjInactive
    ]

/--
Every admissible state has a unique semantic left-greedy representative in its
Product-window effect fiber, and the complete admissible fiber is exactly the
active-value-sum level set through that representative.
-/
theorem existsUnique_canonicalLeftGreedyActiveSupport_in_productWindowUFiber_and_levelSet
    (p : ProductRestrictedParams)
    (x : StateU)
    (hx : inStateSpaceU (paramsUOfProduct p) x) :
    let activeSum : StateU → Nat :=
      fun s =>
        (List.ofFn
          (fun w : Typed.WidthIndex p.d =>
            if ProductIndex.unflatten w ∈ p.active then
              s w.val
            else
              0)).sum
    let IsCanonicalLeftGreedy : StateU → Prop :=
      fun s =>
        (∀ j : Nat,
          j ∉ (paramsUOfProduct p).active →
            s j = 0) ∧
        inStateSpaceU (paramsUOfProduct p) s ∧
        ∀ u v : Typed.WidthIndex p.d,
          u.val < v.val →
          ProductIndex.unflatten u ∈ p.active →
          ProductIndex.unflatten v ∈ p.active →
          s u.val < p.n →
            s v.val = 0
    let InFiber : StateU → Prop :=
      fun s =>
        ledgerEffectOn
            (paramsUOfProduct p)
            (productWindowU p)
            s =
          ledgerEffectOn
            (paramsUOfProduct p)
            (productWindowU p)
            x
    ∃ y : StateU,
      ((IsCanonicalLeftGreedy y ∧ InFiber y) ∧
        ∀ y' : StateU,
          (IsCanonicalLeftGreedy y' ∧ InFiber y') →
            y' = y) ∧
      ∀ z : StateU,
        inStateSpaceU (paramsUOfProduct p) z →
          (InFiber z ↔ activeSum z = activeSum y) := by
  dsimp only
  let e : Int :=
    ledgerEffectOn
      (paramsUOfProduct p)
      (productWindowU p)
      x
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
    fun s =>
      (∀ j : Nat,
        j ∉ (paramsUOfProduct p).active →
          s j = 0) ∧
      inStateSpaceU (paramsUOfProduct p) s ∧
      (∀ w : Typed.WidthIndex p.d,
        s w.val =
          min
            (if ProductIndex.unflatten w ∈ p.active then
              p.n
            else
              0)
            (q -
              (List.ofFn
                (fun v : Fin w.val =>
                  s v.val)).sum)) ∧
      ledgerEffectOn
        (paramsUOfProduct p)
        (productWindowU p)
        s = e
  obtain ⟨u, _, huEffect, _⟩ :=
    exists_productState_finiteObservationRepresentative
      p
      x
      hx
  have heRange :
      0 ≤ e ∧
      e ≤ (capacity : Int) := by
    have hrange :=
      (exists_productLedgerEffect_eq_iff_nonneg_and_le_activeCapacity
        p
        e).mp
        ⟨u, huEffect⟩
    simpa [capacity, caps] using hrange
  have hcanonical :=
    (existsUnique_leftGreedyActiveSupport_inStateSpaceU_ledgerEffectOn_productWindowU_eq_iff_nonneg_and_le_activeCapacity
      p
      e).mpr
      heRange
  change
    ∃ y : StateU,
      IsLeftGreedy y ∧
      ∀ y' : StateU,
        IsLeftGreedy y' →
          y' = y at hcanonical
  rcases hcanonical with ⟨y, hy, _⟩
  have hyCanonical :
      (∀ j : Nat,
        j ∉ (paramsUOfProduct p).active →
          y j = 0) ∧
      inStateSpaceU (paramsUOfProduct p) y ∧
      ∀ u v : Typed.WidthIndex p.d,
        u.val < v.val →
        ProductIndex.unflatten u ∈ p.active →
        ProductIndex.unflatten v ∈ p.active →
        y u.val < p.n →
          y v.val = 0 := by
    exact
      ⟨hy.1,
        hy.2.1,
        c87_recurrence_implies_relationalLeftGreedy
          p
          q
          y
          hy.2.2.1⟩
  have hyFiber :
      ledgerEffectOn
          (paramsUOfProduct p)
          (productWindowU p)
          y =
        ledgerEffectOn
          (paramsUOfProduct p)
          (productWindowU p)
          x := by
    simpa [e] using hy.2.2.2
  refine
    ⟨y,
      ⟨⟨hyCanonical, hyFiber⟩, ?_⟩,
      ?_⟩
  · intro y' hy'
    have hy'EffectY :
        ledgerEffectOn
            (paramsUOfProduct p)
            (productWindowU p)
            y' =
          ledgerEffectOn
            (paramsUOfProduct p)
            (productWindowU p)
            y :=
      hy'.2.trans hyFiber.symm
    have hsum :=
      (ledgerEffectOn_productWindowU_eq_iff_sum_activeValues_eq
        p
        y'
        y
        hy'.1.2.1
        hyCanonical.2.1).mp
        hy'EffectY
    have hmasked :
        c87Masked p y' =
          c87Masked p y :=
      c87_boundedLeftGreedy_eq_of_sum_eq
        (Typed.typedWidth p.d)
        (c87Capacity p)
        (c87Masked p y')
        (c87Masked p y)
        (c87Masked_le_capacity
          p
          y'
          hy'.1.2.1)
        (c87Masked_le_capacity
          p
          y
          hyCanonical.2.1)
        (c87Masked_finiteLeftGreedy
          p
          y'
          hy'.1.2.2)
        (c87Masked_finiteLeftGreedy
          p
          y
          hyCanonical.2.2)
        (by
          change
            (List.ofFn
              (fun w : Typed.WidthIndex p.d =>
                if ProductIndex.unflatten w ∈ p.active then
                  y' w.val
                else
                  0)).sum =
              (List.ofFn
                (fun w : Typed.WidthIndex p.d =>
                  if ProductIndex.unflatten w ∈ p.active then
                    y w.val
                  else
                    0)).sum
          exact hsum)
    exact
      c87_state_eq_of_masked_eq
        p
        y'
        y
        hy'.1.1
        hyCanonical.1
        hmasked
  · intro z hz
    have hlevel :=
      ledgerEffectOn_productWindowU_eq_iff_sum_activeValues_eq
        p
        z
        y
        hz
        hy.2.1
    rw [hyFiber] at hlevel
    exact hlevel

end UnrestrictedBridge
end VFH2
