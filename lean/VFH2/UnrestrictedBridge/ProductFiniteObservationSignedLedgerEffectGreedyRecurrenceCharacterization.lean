import VFH2.UnrestrictedBridge.ProductFiniteObservationSignedLedgerEffectGreedyOrderCharacterization

/-!
# Product finite-observation semantic greedy recurrence characterization

This module identifies the semantic canonical class used by the Product-window
fiber and order theorems with its intrinsic prefix recurrence. A globally
active-supported bounded state is relationally left-greedy exactly when every
bounded coordinate consumes the remaining part of that state's own masked
active sum, up to the coordinate capacity.

The forward implication is a direct finite decomposition: after an
unsaturated active coordinate, relational greediness and global support make
the entire suffix zero; at a saturated coordinate, prefix monotonicity supplies
the required remaining quota. The reverse implication reconstructs both the
state-space bound and relational greediness from the recurrence. It does not
invoke either canonical existence/uniqueness theorem.

All supporting lemmas are private and the semantic predicates remain
theorem-local. No normalizer, alias, compatibility namespace, public
definition, or model assumption is introduced.

Only the canonical finite Product observation window is involved. This does
not define a global infinite ledger, is not unrestricted `TTP-VF-H2-004`, and
makes no full-theory, empirical, physical, medical, causal, or biological
validation claim.
-/

namespace VFH2
namespace UnrestrictedBridge

private theorem c89_sum_ofFn_zero
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

private theorem c89_sum_ofFn_split
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

private theorem c89_prefix_succ
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

private theorem c89_prefix_add_apply_le_prefix
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
    c89_sum_ofFn_split x (u + 1) (v - (u + 1))
  have hlength :
      u + 1 + (v - (u + 1)) = v := by
    omega
  rw [hlength] at hdecomp
  rw [c89_prefix_succ] at hdecomp
  omega

private theorem c89_sum_ofFn_eq_prefix_add_apply_of_suffix_zero
    (x : Nat → Nat)
    (u n : Nat)
    (hu : u < n)
    (hsuffix :
      ∀ j : Nat,
        u < j →
        j < n →
          x j = 0) :
    (List.ofFn
      (fun i : Fin n =>
        x i.val)).sum =
      (List.ofFn
        (fun i : Fin u =>
          x i.val)).sum +
        x u := by
  have hdecomp :=
    c89_sum_ofFn_split x (u + 1) (n - (u + 1))
  have hlength :
      u + 1 + (n - (u + 1)) = n := by
    omega
  rw [hlength] at hdecomp
  rw [c89_prefix_succ] at hdecomp
  have htailZero :
      (List.ofFn
        (fun i : Fin (n - (u + 1)) =>
          x (u + 1 + i.val))).sum = 0 := by
    apply c89_sum_ofFn_zero
    intro i
    exact
      hsuffix
        (u + 1 + i.val)
        (by omega)
        (by
          have hi := i.isLt
          omega)
  rw [htailZero, Nat.add_zero] at hdecomp
  exact hdecomp

private theorem c89_val_mem_paramsUOfProduct_active_iff
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

private theorem c89_recurrence_implies_relationalLeftGreedy
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
    c89_prefix_add_apply_le_prefix
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

private theorem c89_mem_paramsUOfProduct_active_lt_typedWidth
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
Global active support, admissibility, and semantic relational left-greediness
are equivalent to the exact prefix recurrence whose quota is the state's own
masked active-value sum.
-/
theorem canonicalLeftGreedyActiveSupport_iff_activeSum_prefixRecurrence
    (p : ProductRestrictedParams)
    (s : StateU) :
    let activeSum : Nat :=
      (List.ofFn
        (fun w : Typed.WidthIndex p.d =>
          if ProductIndex.unflatten w ∈ p.active then
            s w.val
          else
            0)).sum
    let HasGlobalActiveSupport : Prop :=
      ∀ j : Nat,
        j ∉ (paramsUOfProduct p).active →
          s j = 0
    let IsRelationalLeftGreedy : Prop :=
      ∀ u v : Typed.WidthIndex p.d,
        u.val < v.val →
        ProductIndex.unflatten u ∈ p.active →
        ProductIndex.unflatten v ∈ p.active →
        s u.val < p.n →
          s v.val = 0
    let HasActiveSumPrefixRecurrence : Prop :=
      ∀ w : Typed.WidthIndex p.d,
        s w.val =
          min
            (if ProductIndex.unflatten w ∈ p.active then
              p.n
            else
              0)
            (activeSum -
              (List.ofFn
                (fun v : Fin w.val =>
                  s v.val)).sum)
    (HasGlobalActiveSupport ∧
      inStateSpaceU (paramsUOfProduct p) s ∧
      IsRelationalLeftGreedy) ↔
    (HasGlobalActiveSupport ∧
      HasActiveSumPrefixRecurrence) := by
  dsimp only
  constructor
  · rintro ⟨hSupport, hSpace, hRelational⟩
    refine ⟨hSupport, ?_⟩
    have hmaskedValues :
        (fun w : Typed.WidthIndex p.d =>
          if ProductIndex.unflatten w ∈ p.active then
            s w.val
          else
            0) =
        (fun w : Typed.WidthIndex p.d =>
          s w.val) := by
      funext w
      by_cases hw : ProductIndex.unflatten w ∈ p.active
      · simp [hw]
      · have hwInactive :
            w.val ∉ (paramsUOfProduct p).active := by
          intro hwActive
          exact
            hw
              ((c89_val_mem_paramsUOfProduct_active_iff
                p
                w).mp hwActive)
        have hwZero := hSupport w.val hwInactive
        simp [hw, hwZero]
    have hactiveSum :=
      congrArg
        (fun f : Typed.WidthIndex p.d → Nat =>
          (List.ofFn f).sum)
        hmaskedValues
    intro w
    by_cases hw : ProductIndex.unflatten w ∈ p.active
    · have hwBound := hSpace w.val
      change s w.val ≤ p.n at hwBound
      by_cases hwUnsaturated : s w.val < p.n
      · have hsuffix :
            ∀ j : Nat,
              w.val < j →
              j < Typed.typedWidth p.d →
                s j = 0 := by
          intro j hwj hjWidth
          let v : Typed.WidthIndex p.d := ⟨j, hjWidth⟩
          by_cases hv : ProductIndex.unflatten v ∈ p.active
          · simpa [v] using
              hRelational
                w
                v
                (by simpa [v] using hwj)
                hw
                hv
                hwUnsaturated
          · have hvInactive :
                v.val ∉ (paramsUOfProduct p).active := by
              intro hvActive
              exact
                hv
                  ((c89_val_mem_paramsUOfProduct_active_iff
                    p
                    v).mp hvActive)
            simpa [v] using hSupport v.val hvInactive
        have htotal :=
          c89_sum_ofFn_eq_prefix_add_apply_of_suffix_zero
            s
            w.val
            (Typed.typedWidth p.d)
            w.isLt
            hsuffix
        have hremaining :
            (List.ofFn
                (fun u : Typed.WidthIndex p.d =>
                  if ProductIndex.unflatten u ∈ p.active then
                    s u.val
                  else
                    0)).sum -
                (List.ofFn
                  (fun v : Fin w.val =>
                    s v.val)).sum =
              s w.val := by
          rw [hactiveSum, htotal]
          omega
        simp only [hw, ↓reduceIte]
        rw [hremaining, Nat.min_eq_right (Nat.le_of_lt hwUnsaturated)]
      · have hwSaturated : s w.val = p.n := by
          omega
        have hprefixLe :=
          c89_prefix_add_apply_le_prefix
            s
            w.isLt
        have hremaining :
            p.n ≤
              (List.ofFn
                  (fun u : Typed.WidthIndex p.d =>
                    if ProductIndex.unflatten u ∈ p.active then
                      s u.val
                    else
                      0)).sum -
                  (List.ofFn
                    (fun v : Fin w.val =>
                      s v.val)).sum := by
          rw [hactiveSum]
          apply Nat.le_sub_of_add_le
          simpa [hwSaturated, Nat.add_comm] using hprefixLe
        simp only [hw, ↓reduceIte]
        rw [Nat.min_eq_left hremaining]
        exact hwSaturated
    · have hwInactive :
          w.val ∉ (paramsUOfProduct p).active := by
        intro hwActive
        exact
          hw
            ((c89_val_mem_paramsUOfProduct_active_iff
              p
              w).mp hwActive)
      have hwZero := hSupport w.val hwInactive
      simp [hw, hwZero]
  · rintro ⟨hSupport, hRecurrence⟩
    refine ⟨hSupport, ?_, ?_⟩
    · intro j
      change s j ≤ p.n
      by_cases hjWidth : j < Typed.typedWidth p.d
      · let w : Typed.WidthIndex p.d := ⟨j, hjWidth⟩
        have hwRecurrence := hRecurrence w
        change s w.val ≤ p.n
        rw [hwRecurrence]
        by_cases hw : ProductIndex.unflatten w ∈ p.active
        · simp only [hw, ↓reduceIte]
          exact Nat.min_le_left _ _
        · simp [hw]
      · have hjInactive :
            j ∉ (paramsUOfProduct p).active := by
          intro hjActive
          exact
            hjWidth
              (c89_mem_paramsUOfProduct_active_lt_typedWidth
                p
                j
                hjActive)
        rw [hSupport j hjInactive]
        exact Nat.zero_le _
    · exact
        c89_recurrence_implies_relationalLeftGreedy
          p
          (List.ofFn
            (fun w : Typed.WidthIndex p.d =>
              if ProductIndex.unflatten w ∈ p.active then
                s w.val
              else
                0)).sum
          s
          hRecurrence

end UnrestrictedBridge
end VFH2
