import VFH2.Product.ProductExactStabilizationTime

/-!
# VF-H2 Restricted Product Trajectory Stationarity

This file connects structural fixedness and zero ledger effect to the genuine
dynamical notion that a trajectory remains constant from a given time onward.

Scientific result:
- A trajectory is stationary from time `t` exactly when its state at time `t`
  belongs to the product fixed set.
- Stationarity from `t` occurs exactly when the initial state is fixed or
  `t` is positive.
- The first stationary time is zero for initially fixed states and one for
  initially nonfixed states.
- The first stationary time is exactly the first fixed time.
- The first stationary time is exactly the first zero-ledger-effect time.
- Every trajectory has a unique first stationary time.

This is not merely an equivalence list: it identifies the structural and ledger
hitting-time results with actual future trajectory constancy.

Boundary:
- The result is only for `ProductRestrictedParams`, `productUpdateState`,
  `productUpdateTrajectory`, `ProductFixedSet`, and `productLedgerEffect`.
- It confirms that the current restricted update has no nontrivial dynamics
  after its first step.
- It does not prove unrestricted TTP-VF-H2-004 or the full Viruse Fabric theory.
- It is not empirical or biological validation.
-/

namespace VFH2

/--
The product trajectory is stationary from time `t` when every later state equals
the state at time `t`.
-/
def productTrajectoryStationaryFrom
    (p : ProductRestrictedParams)
    (x : p.State)
    (t : Nat) : Prop :=
  ∀ u : Nat,
    t ≤ u →
      productUpdateTrajectory p x u =
        productUpdateTrajectory p x t

/--
A fixed trajectory state generates a stationary future.
-/
theorem productTrajectoryStationaryFrom_of_fixedAt
    (p : ProductRestrictedParams)
    (x : p.State)
    (t : Nat)
    (hFixedAt :
      ProductFixedSet p (productUpdateTrajectory p x t)) :
    productTrajectoryStationaryFrom p x t := by
  cases t with
  | zero =>
      have hInitial :
          ProductFixedSet p x := by
        simpa using hFixedAt

      intro u hu

      simpa using
        productUpdateTrajectory_eq_initial_of_fixed
          p x hInitial u

  | succ k =>
      intro u hu

      have huPositive : 0 < u := by
        omega

      exact
        productUpdateTrajectory_eq_of_pos
          p x
          u
          (Nat.succ k)
          huPositive
          (Nat.succ_pos k)

/--
Stationarity from time `t` forces the state at time `t` to be a fixed point.
-/
theorem productTrajectory_fixedAt_of_stationaryFrom
    (p : ProductRestrictedParams)
    (x : p.State)
    (t : Nat)
    (hStationary :
      productTrajectoryStationaryFrom p x t) :
    ProductFixedSet p (productUpdateTrajectory p x t) := by
  have hStep :
      productUpdateTrajectory p x (t + 1) =
        productUpdateTrajectory p x t :=
    hStationary (t + 1) (by omega)

  rw [productUpdateTrajectory_succ] at hStep

  exact
    (productFixedSet_iff_productUpdateState_eq_self
      p
      (productUpdateTrajectory p x t)).2 hStep

/--
Dynamical stationarity and structural fixedness are equivalent at every
trajectory time.
-/
theorem productTrajectoryStationaryFrom_iff_fixedAt
    (p : ProductRestrictedParams)
    (x : p.State)
    (t : Nat) :
    productTrajectoryStationaryFrom p x t ↔
      ProductFixedSet p (productUpdateTrajectory p x t) := by
  constructor
  · exact
      productTrajectory_fixedAt_of_stationaryFrom
        p x t

  · exact
      productTrajectoryStationaryFrom_of_fixedAt
        p x t

/--
Exact classification of all stationary times.

The trajectory is stationary from time `t` exactly when the initial state is
already fixed or `t` is positive.
-/
theorem productTrajectoryStationaryFrom_iff_initialFixed_or_pos
    (p : ProductRestrictedParams)
    (x : p.State)
    (t : Nat) :
    productTrajectoryStationaryFrom p x t ↔
      ProductFixedSet p x ∨ 0 < t := by
  constructor
  · intro hStationary

    have hFixedAt :
        ProductFixedSet p
          (productUpdateTrajectory p x t) :=
      (productTrajectoryStationaryFrom_iff_fixedAt
        p x t).1 hStationary

    cases t with
    | zero =>
        left
        simpa using hFixedAt

    | succ k =>
        right
        exact Nat.succ_pos k

  · intro hClassification

    rcases hClassification with
      hInitial | htPositive

    · apply
        productTrajectoryStationaryFrom_of_fixedAt
          p x t

      rw [
        productUpdateTrajectory_eq_initial_of_fixed
          p x hInitial t
      ]

      exact hInitial

    · apply
        productTrajectoryStationaryFrom_of_fixedAt
          p x t

      exact
        productUpdateTrajectory_ProductFixedSet_of_pos
          p x t htPositive

/--
The trajectory becomes stationary for the first time at `t`.
-/
def productTrajectoryFirstStationaryAt
    (p : ProductRestrictedParams)
    (x : p.State)
    (t : Nat) : Prop :=
  productTrajectoryStationaryFrom p x t ∧
    ∀ s : Nat,
      s < t →
        ¬ productTrajectoryStationaryFrom p x s

/--
The first stationary time is exactly the first fixed time.
-/
theorem productTrajectoryFirstStationaryAt_iff_firstFixedAt
    (p : ProductRestrictedParams)
    (x : p.State)
    (t : Nat) :
    productTrajectoryFirstStationaryAt p x t ↔
      productTrajectoryFirstFixedAt p x t := by
  unfold productTrajectoryFirstStationaryAt
  unfold productTrajectoryFirstFixedAt

  constructor
  · rintro ⟨hStationaryAt, hMinimalStationary⟩

    refine ⟨
      (productTrajectoryStationaryFrom_iff_fixedAt
        p x t).1 hStationaryAt,
      ?_
    ⟩

    intro s hs hFixedEarlier

    exact
      hMinimalStationary s hs
        ((productTrajectoryStationaryFrom_iff_fixedAt
          p x s).2 hFixedEarlier)

  · rintro ⟨hFixedAt, hMinimalFixed⟩

    refine ⟨
      (productTrajectoryStationaryFrom_iff_fixedAt
        p x t).2 hFixedAt,
      ?_
    ⟩

    intro s hs hStationaryEarlier

    exact
      hMinimalFixed s hs
        ((productTrajectoryStationaryFrom_iff_fixedAt
          p x s).1 hStationaryEarlier)

/--
Exact classification of the first stationary time.
-/
theorem productTrajectoryFirstStationaryAt_iff
    (p : ProductRestrictedParams)
    (x : p.State)
    (t : Nat) :
    productTrajectoryFirstStationaryAt p x t ↔
      (ProductFixedSet p x ∧ t = 0) ∨
      (¬ ProductFixedSet p x ∧ t = 1) := by
  exact
    (productTrajectoryFirstStationaryAt_iff_firstFixedAt
      p x t).trans
      (productTrajectoryFirstFixedAt_iff p x t)

/--
Every restricted product trajectory has a unique first stationary time.
-/
theorem productTrajectoryFirstStationaryAt_existsUnique
    (p : ProductRestrictedParams)
    (x : p.State) :
    ∃ t : Nat,
      productTrajectoryFirstStationaryAt p x t ∧
        ∀ s : Nat,
          productTrajectoryFirstStationaryAt p x s →
            s = t := by
  rcases
      productTrajectoryFirstFixedAt_existsUnique p x with
    ⟨t, hFirstFixed, hUniqueFixed⟩

  refine ⟨
    t,
    (productTrajectoryFirstStationaryAt_iff_firstFixedAt
      p x t).2 hFirstFixed,
    ?_
  ⟩

  intro s hFirstStationary

  exact
    hUniqueFixed s
      ((productTrajectoryFirstStationaryAt_iff_firstFixedAt
        p x s).1 hFirstStationary)

/--
Every first stationary time is at most one.
-/
theorem productTrajectoryFirstStationaryAt_le_one
    (p : ProductRestrictedParams)
    (x : p.State)
    (t : Nat)
    (hFirst :
      productTrajectoryFirstStationaryAt p x t) :
    t ≤ 1 := by
  rcases
      (productTrajectoryFirstStationaryAt_iff
        p x t).1 hFirst with
    htZero | htOne

  · omega
  · omega

/--
The first stationary time is exactly the first zero-ledger-effect time.
-/
theorem productTrajectoryFirstStationaryAt_iff_firstZeroLedgerAt
    (p : ProductRestrictedParams)
    (x : p.State)
    (t : Nat) :
    productTrajectoryFirstStationaryAt p x t ↔
      productTrajectoryFirstZeroLedgerAt p x t := by
  exact
    (productTrajectoryFirstStationaryAt_iff_firstFixedAt
      p x t).trans
      (productTrajectoryFirstZeroLedgerAt_iff_firstFixedAt
        p x t).symm

end VFH2
