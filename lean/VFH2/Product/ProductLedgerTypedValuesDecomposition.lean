import VFH2.Product.ProductLedgerTypedValuesGetElem

/-!
# VF-H2 v11 Transported Typed Ledger Values Decomposition

This file proves that the transported typed ledger values decompose into
the same three time-layer blocks used by the product ledger.

Boundary:
- This proves product/typed ledger value-list decomposition.
- It proves the corresponding ledger target for the current restricted scaffold.
- It does not prove update equivalence.
- It does not prove unrestricted VF-H2.
- It does not prove empirical or biological validation.
-/

namespace VFH2

namespace ProductLedgerTypedValuesDecomposition

theorem transportedTypedLedgerValues_getElem?_first
    (p : ProductRestrictedParams)
    (x : p.State)
    (i : Nat)
    (hi : i < p.d) :
    (ProductLedgerEquivalenceTarget.transportedTypedLedgerValues p x)[i]? =
      some
        ((ProductLedgerTypedBlocks.transportedTypedLedgerValuesAtTime
            p x TimeLayer.t1)[i]'(by
              rw [ProductLedgerTypedValuesLength.transportedTypedLedgerValuesAtTime_length]
              exact hi)) := by
  unfold ProductLedgerEquivalenceTarget.transportedTypedLedgerValues
  unfold Typed.typedLedgerValues

  change
    (List.ofFn
      (fun w : Typed.WidthIndex p.d =>
        (ProductStateTransport.productToTyped x w).val))[i]? =
      some
        ((ProductLedgerTypedBlocks.transportedTypedLedgerValuesAtTime
            p x TimeLayer.t1)[i]'(by
              rw [ProductLedgerTypedValuesLength.transportedTypedLedgerValuesAtTime_length]
              exact hi))

  rw [List.getElem?_ofFn]

  have hwidth : i < Typed.typedWidth p.d := by
    simp [Typed.typedWidth]
    omega

  rw [dif_pos hwidth]
  congr

  rw [ProductUnflattenBlocks.productToTyped_val_of_lt_d
    (x := x)
    (w := (⟨i, hwidth⟩ : Typed.WidthIndex p.d))
    hi]

  unfold ProductLedgerTypedBlocks.transportedTypedLedgerValuesAtTime
  rw [List.getElem_ofFn]
  rw [ProductLedgerTransport.productToTyped_flatten_apply_val]

theorem transportedTypedLedgerValues_getElem?_second
    (p : ProductRestrictedParams)
    (x : p.State)
    (i : Nat)
    (hge : p.d ≤ i)
    (hlt : i < 2 * p.d) :
    (ProductLedgerEquivalenceTarget.transportedTypedLedgerValues p x)[i]? =
      some
        ((ProductLedgerTypedBlocks.transportedTypedLedgerValuesAtTime
            p x TimeLayer.t2)[i - p.d]'(by
              rw [ProductLedgerTypedValuesLength.transportedTypedLedgerValuesAtTime_length]
              omega)) := by
  unfold ProductLedgerEquivalenceTarget.transportedTypedLedgerValues
  unfold Typed.typedLedgerValues

  change
    (List.ofFn
      (fun w : Typed.WidthIndex p.d =>
        (ProductStateTransport.productToTyped x w).val))[i]? =
      some
        ((ProductLedgerTypedBlocks.transportedTypedLedgerValuesAtTime
            p x TimeLayer.t2)[i - p.d]'(by
              rw [ProductLedgerTypedValuesLength.transportedTypedLedgerValuesAtTime_length]
              omega))

  rw [List.getElem?_ofFn]

  have hwidth : i < Typed.typedWidth p.d := by
    simp [Typed.typedWidth]
    omega

  rw [dif_pos hwidth]
  congr

  rw [ProductUnflattenBlocks.productToTyped_val_of_ge_d_lt_two_mul
    (x := x)
    (w := (⟨i, hwidth⟩ : Typed.WidthIndex p.d))
    hge
    hlt]

  unfold ProductLedgerTypedBlocks.transportedTypedLedgerValuesAtTime
  rw [List.getElem_ofFn]
  rw [ProductLedgerTransport.productToTyped_flatten_apply_val]

theorem transportedTypedLedgerValues_getElem?_third
    (p : ProductRestrictedParams)
    (x : p.State)
    (i : Nat)
    (hge : 2 * p.d ≤ i)
    (hlt : i < 3 * p.d) :
    (ProductLedgerEquivalenceTarget.transportedTypedLedgerValues p x)[i]? =
      some
        ((ProductLedgerTypedBlocks.transportedTypedLedgerValuesAtTime
            p x TimeLayer.t3)[i - 2 * p.d]'(by
              rw [ProductLedgerTypedValuesLength.transportedTypedLedgerValuesAtTime_length]
              omega)) := by
  unfold ProductLedgerEquivalenceTarget.transportedTypedLedgerValues
  unfold Typed.typedLedgerValues

  change
    (List.ofFn
      (fun w : Typed.WidthIndex p.d =>
        (ProductStateTransport.productToTyped x w).val))[i]? =
      some
        ((ProductLedgerTypedBlocks.transportedTypedLedgerValuesAtTime
            p x TimeLayer.t3)[i - 2 * p.d]'(by
              rw [ProductLedgerTypedValuesLength.transportedTypedLedgerValuesAtTime_length]
              omega))

  rw [List.getElem?_ofFn]

  have hwidth : i < Typed.typedWidth p.d := by
    simp [Typed.typedWidth]
    omega

  rw [dif_pos hwidth]
  congr

  rw [ProductUnflattenBlocks.productToTyped_val_of_ge_two_mul
    (x := x)
    (w := (⟨i, hwidth⟩ : Typed.WidthIndex p.d))
    hge]

  unfold ProductLedgerTypedBlocks.transportedTypedLedgerValuesAtTime
  rw [List.getElem_ofFn]
  rw [ProductLedgerTransport.productToTyped_flatten_apply_val]

theorem transportedTypedLedgerValues_getElem?_none
    (p : ProductRestrictedParams)
    (x : p.State)
    (i : Nat)
    (hnot : ¬ i < 3 * p.d) :
    (ProductLedgerEquivalenceTarget.transportedTypedLedgerValues p x)[i]? =
      none := by
  unfold ProductLedgerEquivalenceTarget.transportedTypedLedgerValues
  unfold Typed.typedLedgerValues

  change
    (List.ofFn
      (fun w : Typed.WidthIndex p.d =>
        (ProductStateTransport.productToTyped x w).val))[i]? =
      none

  rw [List.getElem?_ofFn]
  rw [dif_neg]
  intro hwidth
  apply hnot
  simpa [Typed.typedWidth] using hwidth

theorem transportedTypedLedgerBlockValues_getElem?_none
    (p : ProductRestrictedParams)
    (x : p.State)
    (i : Nat)
    (hnot : ¬ i < 3 * p.d) :
    (ProductLedgerTypedBlocks.transportedTypedLedgerBlockValues p x)[i]? =
      none := by
  rw [List.getElem?_eq_none_iff]
  rw [ProductLedgerTypedValuesLength.transportedTypedLedgerBlockValues_length]
  exact Nat.le_of_not_gt hnot

/--
The transported typed ledger values are exactly the same list as the
three transported typed product-time blocks.
-/
theorem transportedTypedLedgerValues_eq_blockValues
    (p : ProductRestrictedParams)
    (x : p.State) :
    ProductLedgerEquivalenceTarget.transportedTypedLedgerValues p x =
      ProductLedgerTypedBlocks.transportedTypedLedgerBlockValues p x := by
  apply List.ext_getElem?
  intro i

  by_cases h3 : i < 3 * p.d
  · by_cases h1 : i < p.d
    · rw [transportedTypedLedgerValues_getElem?_first p x i h1]
      rw [ProductLedgerTypedValuesGetElem.transportedTypedLedgerBlockValues_getElem?_first p x i h1]
    · by_cases h2 : i < 2 * p.d
      · have hge : p.d ≤ i := Nat.le_of_not_gt h1
        rw [transportedTypedLedgerValues_getElem?_second p x i hge h2]
        rw [ProductLedgerTypedValuesGetElem.transportedTypedLedgerBlockValues_getElem?_second p x i hge h2]
      · have hge : 2 * p.d ≤ i := Nat.le_of_not_gt h2
        rw [transportedTypedLedgerValues_getElem?_third p x i hge h3]
        rw [ProductLedgerTypedValuesGetElem.transportedTypedLedgerBlockValues_getElem?_third p x i hge h3]
  · rw [transportedTypedLedgerValues_getElem?_none p x i h3]
    rw [transportedTypedLedgerBlockValues_getElem?_none p x i h3]

/--
The current restricted product ledger equals the transported typed ledger.
-/
theorem ledgerEquivalenceTarget
    (p : ProductRestrictedParams)
    (x : p.State) :
    ProductLedgerEquivalenceTarget.ledgerEquivalenceTarget p x := by
  exact
    ProductLedgerTypedBlocks.ledger_eq_of_transport_values_eq_blocks
      p
      x
      (transportedTypedLedgerValues_eq_blockValues p x)

end ProductLedgerTypedValuesDecomposition

end VFH2
