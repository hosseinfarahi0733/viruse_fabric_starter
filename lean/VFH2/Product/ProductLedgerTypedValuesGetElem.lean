import VFH2.Product.ProductLedgerTypedValuesLength

/-!
# VF-H2 v11 Transported Typed Ledger Block getElem Lemmas

This file proves `getElem?` lemmas for the three transported typed
ledger blocks.

Boundary:
- This proves block-level optional indexing facts.
- It does not prove full transported typed ledger decomposition yet.
- It does not prove full ledger equivalence yet.
- It does not prove update equivalence.
- It does not prove the full VF-H2 theory.
-/

namespace VFH2

namespace ProductLedgerTypedValuesGetElem

theorem transportedTypedLedgerBlockValues_getElem?_first
    (p : ProductRestrictedParams)
    (x : p.State)
    (i : Nat)
    (hi : i < p.d) :
    (ProductLedgerTypedBlocks.transportedTypedLedgerBlockValues p x)[i]? =
      some
        ((ProductLedgerTypedBlocks.transportedTypedLedgerValuesAtTime
            p x TimeLayer.t1)[i]'(by
              rw [ProductLedgerTypedValuesLength.transportedTypedLedgerValuesAtTime_length]
              exact hi)) := by
  unfold ProductLedgerTypedBlocks.transportedTypedLedgerBlockValues

  have hlt12 :
      i <
        (ProductLedgerTypedBlocks.transportedTypedLedgerValuesAtTime p x TimeLayer.t1 ++
          ProductLedgerTypedBlocks.transportedTypedLedgerValuesAtTime p x TimeLayer.t2).length := by
    rw [List.length_append]
    rw [ProductLedgerTypedValuesLength.transportedTypedLedgerValuesAtTime_length]
    rw [ProductLedgerTypedValuesLength.transportedTypedLedgerValuesAtTime_length]
    omega

  rw [List.getElem?_append_left hlt12]

  have hlt1 :
      i <
        (ProductLedgerTypedBlocks.transportedTypedLedgerValuesAtTime
          p x TimeLayer.t1).length := by
    rw [ProductLedgerTypedValuesLength.transportedTypedLedgerValuesAtTime_length]
    exact hi

  rw [List.getElem?_append_left hlt1]
  rw [List.getElem?_eq_getElem]

theorem transportedTypedLedgerBlockValues_getElem?_second
    (p : ProductRestrictedParams)
    (x : p.State)
    (i : Nat)
    (hge : p.d ≤ i)
    (hlt : i < 2 * p.d) :
    (ProductLedgerTypedBlocks.transportedTypedLedgerBlockValues p x)[i]? =
      some
        ((ProductLedgerTypedBlocks.transportedTypedLedgerValuesAtTime
            p x TimeLayer.t2)[i - p.d]'(by
              rw [ProductLedgerTypedValuesLength.transportedTypedLedgerValuesAtTime_length]
              omega)) := by
  unfold ProductLedgerTypedBlocks.transportedTypedLedgerBlockValues

  have hlt12 :
      i <
        (ProductLedgerTypedBlocks.transportedTypedLedgerValuesAtTime p x TimeLayer.t1 ++
          ProductLedgerTypedBlocks.transportedTypedLedgerValuesAtTime p x TimeLayer.t2).length := by
    rw [List.length_append]
    rw [ProductLedgerTypedValuesLength.transportedTypedLedgerValuesAtTime_length]
    rw [ProductLedgerTypedValuesLength.transportedTypedLedgerValuesAtTime_length]
    omega

  rw [List.getElem?_append_left hlt12]

  have hge1 :
      (ProductLedgerTypedBlocks.transportedTypedLedgerValuesAtTime
        p x TimeLayer.t1).length ≤ i := by
    rw [ProductLedgerTypedValuesLength.transportedTypedLedgerValuesAtTime_length]
    exact hge

  rw [List.getElem?_append_right hge1]
  rw [ProductLedgerTypedValuesLength.transportedTypedLedgerValuesAtTime_length]
  rw [List.getElem?_eq_getElem]

theorem transportedTypedLedgerBlockValues_getElem?_third
    (p : ProductRestrictedParams)
    (x : p.State)
    (i : Nat)
    (hge : 2 * p.d ≤ i)
    (hlt : i < 3 * p.d) :
    (ProductLedgerTypedBlocks.transportedTypedLedgerBlockValues p x)[i]? =
      some
        ((ProductLedgerTypedBlocks.transportedTypedLedgerValuesAtTime
            p x TimeLayer.t3)[i - 2 * p.d]'(by
              rw [ProductLedgerTypedValuesLength.transportedTypedLedgerValuesAtTime_length]
              omega)) := by
  unfold ProductLedgerTypedBlocks.transportedTypedLedgerBlockValues

  have hlen12 :
      (ProductLedgerTypedBlocks.transportedTypedLedgerValuesAtTime p x TimeLayer.t1 ++
        ProductLedgerTypedBlocks.transportedTypedLedgerValuesAtTime p x TimeLayer.t2).length =
        2 * p.d := by
    rw [List.length_append]
    rw [ProductLedgerTypedValuesLength.transportedTypedLedgerValuesAtTime_length]
    rw [ProductLedgerTypedValuesLength.transportedTypedLedgerValuesAtTime_length]
    omega

  have hge12 :
      (ProductLedgerTypedBlocks.transportedTypedLedgerValuesAtTime p x TimeLayer.t1 ++
        ProductLedgerTypedBlocks.transportedTypedLedgerValuesAtTime p x TimeLayer.t2).length ≤ i := by
    rw [hlen12]
    exact hge

  rw [List.getElem?_append_right hge12]
  rw [hlen12]
  rw [List.getElem?_eq_getElem]

end ProductLedgerTypedValuesGetElem

end VFH2
