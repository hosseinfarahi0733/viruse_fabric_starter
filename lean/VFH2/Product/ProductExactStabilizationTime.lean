import VFH2.Product.ProductFiniteTimeStabilization

/-!
# VF-H2 Exact Restricted Product Stabilization Time

This file characterizes the first time at which the restricted product
trajectory reaches a fixed state.

Scientific result:
- Every trajectory has a unique first fixed time.
- The first fixed time is zero exactly for initially fixed states.
- The first fixed time is one exactly for initially nonfixed states.
- The first fixed time coincides with the first zero-ledger-effect time.
- Therefore the restricted stabilization time is always at most one.

This upgrades the orbit-level result from finite-time stabilization to an exact
and unique least hitting-time classification.

Boundary:
- The result is only for `ProductRestrictedParams`, `productUpdateState`,
  `productUpdateTrajectory`, and `productLedgerEffect`.
- It does not establish nontrivial multi-step dynamics.
- It does not prove unrestricted TTP-VF-H2-004 or the full Viruse Fabric theory.
- It is not empirical or biological validation.
-/

namespace VFH2

/--
The trajectory reaches the product fixed set for the first time at `t`.
-/
def productTrajectoryFirstFixedAt
    (p : ProductRestrictedParams)
    (x : p.State)
    (t : Nat) : Prop :=
  ProductFixedSet p (productUpdateTrajectory p x t) ∧
    ∀ s : Nat,
      s < t →
        ¬ ProductFixedSet p (productUpdateTrajectory p x s)

/--
The trajectory reaches zero product ledger effect for the first time at `t`.
-/
def productTrajectoryFirstZeroLedgerAt
    (p : ProductRestrictedParams)
    (x : p.State)
    (t : Nat) : Prop :=
  productLedgerEffect p (productUpdateTrajectory p x t) = 0 ∧
    ∀ s : Nat,
      s < t →
        productLedgerEffect p (productUpdateTrajectory p x s) ≠ 0

/--
Exact classification of the first fixed time.

It is zero for an initially fixed state and one for an initially nonfixed
state. No other first fixed time is possible.
-/
theorem productTrajectoryFirstFixedAt_iff
    (p : ProductRestrictedParams)
    (x : p.State)
    (t : Nat) :
    productTrajectoryFirstFixedAt p x t ↔
      (ProductFixedSet p x ∧ t = 0) ∨
      (¬ ProductFixedSet p x ∧ t = 1) := by
  constructor
  · rintro ⟨hFixedAt, hMinimal⟩

    by_cases hInitial : ProductFixedSet p x
    · left
      refine ⟨hInitial, ?_⟩

      cases t with
      | zero =>
          rfl
      | succ k =>
          exfalso

          have hNotInitial :
              ¬ ProductFixedSet p (productUpdateTrajectory p x 0) :=
            hMinimal 0 (Nat.zero_lt_succ k)

          exact hNotInitial (by simpa using hInitial)

    · right
      refine ⟨hInitial, ?_⟩

      cases t with
      | zero =>
          exfalso
          apply hInitial
          simpa using hFixedAt

      | succ k =>
          cases k with
          | zero =>
              rfl

          | succ k =>
              exfalso

              have hNotOne :
                  ¬ ProductFixedSet p
                    (productUpdateTrajectory p x 1) :=
                hMinimal 1 (by omega)

              exact
                hNotOne
                  (productUpdateTrajectory_ProductFixedSet_of_pos
                    p x 1 (by omega))

  · intro hClassification

    rcases hClassification with
      ⟨hInitial, rfl⟩ | ⟨hInitial, rfl⟩

    · refine ⟨?_, ?_⟩
      · simpa using hInitial

      · intro s hs
        omega

    · refine ⟨?_, ?_⟩
      · exact
          productUpdateTrajectory_ProductFixedSet_of_pos
            p x 1 (by omega)

      · intro s hs

        have hsZero : s = 0 := by
          omega

        subst s
        simpa using hInitial

/--
Every restricted product trajectory has a unique first fixed time.
-/
theorem productTrajectoryFirstFixedAt_existsUnique
    (p : ProductRestrictedParams)
    (x : p.State) :
    ∃ t : Nat,
      productTrajectoryFirstFixedAt p x t ∧
        ∀ s : Nat,
          productTrajectoryFirstFixedAt p x s → s = t := by
  by_cases hInitial : ProductFixedSet p x

  · refine ⟨0, ?_, ?_⟩

    · exact
        (productTrajectoryFirstFixedAt_iff p x 0).2
          (Or.inl ⟨hInitial, rfl⟩)

    · intro t ht

      rcases
          (productTrajectoryFirstFixedAt_iff p x t).1 ht with
        htZero | htOne

      · exact htZero.2

      · exact False.elim (htOne.1 hInitial)

  · refine ⟨1, ?_, ?_⟩

    · exact
        (productTrajectoryFirstFixedAt_iff p x 1).2
          (Or.inr ⟨hInitial, rfl⟩)

    · intro t ht

      rcases
          (productTrajectoryFirstFixedAt_iff p x t).1 ht with
        htZero | htOne

      · exact False.elim (hInitial htZero.1)

      · exact htOne.2

/--
Every first fixed time is bounded above by one.
-/
theorem productTrajectoryFirstFixedAt_le_one
    (p : ProductRestrictedParams)
    (x : p.State)
    (t : Nat)
    (hFirst : productTrajectoryFirstFixedAt p x t) :
    t ≤ 1 := by
  rcases
      (productTrajectoryFirstFixedAt_iff p x t).1 hFirst with
    htZero | htOne

  · omega
  · omega

/--
First fixed time and first zero-ledger-effect time are the same notion for the
restricted product trajectory.
-/
theorem productTrajectoryFirstZeroLedgerAt_iff_firstFixedAt
    (p : ProductRestrictedParams)
    (x : p.State)
    (t : Nat) :
    productTrajectoryFirstZeroLedgerAt p x t ↔
      productTrajectoryFirstFixedAt p x t := by
  unfold productTrajectoryFirstZeroLedgerAt
  unfold productTrajectoryFirstFixedAt

  constructor
  · rintro ⟨hZeroAt, hMinimalZero⟩

    refine ⟨
      (productLedgerEffect_eq_zero_iff_productFixedSet
        p
        (productUpdateTrajectory p x t)).mp hZeroAt,
      ?_
    ⟩

    intro s hs hFixedEarlier

    exact
      hMinimalZero s hs
        ((productLedgerEffect_eq_zero_iff_productFixedSet
          p
          (productUpdateTrajectory p x s)).mpr hFixedEarlier)

  · rintro ⟨hFixedAt, hMinimalFixed⟩

    refine ⟨
      (productLedgerEffect_eq_zero_iff_productFixedSet
        p
        (productUpdateTrajectory p x t)).mpr hFixedAt,
      ?_
    ⟩

    intro s hs hZeroEarlier

    exact
      hMinimalFixed s hs
        ((productLedgerEffect_eq_zero_iff_productFixedSet
          p
          (productUpdateTrajectory p x s)).mp hZeroEarlier)

/--
Exact classification of the first zero-ledger-effect time.
-/
theorem productTrajectoryFirstZeroLedgerAt_iff
    (p : ProductRestrictedParams)
    (x : p.State)
    (t : Nat) :
    productTrajectoryFirstZeroLedgerAt p x t ↔
      (ProductFixedSet p x ∧ t = 0) ∨
      (¬ ProductFixedSet p x ∧ t = 1) := by
  exact
    (productTrajectoryFirstZeroLedgerAt_iff_firstFixedAt
      p x t).trans
      (productTrajectoryFirstFixedAt_iff p x t)

/--
Every restricted product trajectory has a unique first zero-ledger-effect time.
-/
theorem productTrajectoryFirstZeroLedgerAt_existsUnique
    (p : ProductRestrictedParams)
    (x : p.State) :
    ∃ t : Nat,
      productTrajectoryFirstZeroLedgerAt p x t ∧
        ∀ s : Nat,
          productTrajectoryFirstZeroLedgerAt p x s → s = t := by
  rcases
      productTrajectoryFirstFixedAt_existsUnique p x with
    ⟨t, hFirstFixed, hUniqueFixed⟩

  refine ⟨
    t,
    (productTrajectoryFirstZeroLedgerAt_iff_firstFixedAt
      p x t).2 hFirstFixed,
    ?_
  ⟩

  intro s hFirstZero

  exact
    hUniqueFixed s
      ((productTrajectoryFirstZeroLedgerAt_iff_firstFixedAt
        p x s).1 hFirstZero)

end VFH2
