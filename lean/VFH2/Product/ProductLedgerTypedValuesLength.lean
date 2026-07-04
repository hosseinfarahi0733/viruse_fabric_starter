import VFH2.Product.ProductLedgerTypedBlocks
import VFH2.Product.ProductUnflattenBlocks

/-!
# VF-H2 v11 Transported Typed Ledger Values Length Lemmas

This file proves length facts needed for the eventual decomposition of

  transportedTypedLedgerValues

into the three transported typed ledger blocks.

Boundary:
- This proves length compatibility only.
- It does not prove list equality.
- It does not prove full ledger equivalence.
- It does not prove ledger-effect equivalence.
- It does not prove update equivalence.
- It does not prove the full VF-H2 theory.
-/

namespace VFH2

namespace ProductLedgerTypedValuesLength

/--
The actual transported typed ledger values enumerate `Typed.WidthIndex d`,
therefore their length is `3*d`.
-/
theorem transportedTypedLedgerValues_length
    (p : ProductRestrictedParams)
    (x : p.State) :
    (ProductLedgerEquivalenceTarget.transportedTypedLedgerValues p x).length =
      3 * p.d := by
  unfold ProductLedgerEquivalenceTarget.transportedTypedLedgerValues
  unfold Typed.typedLedgerValues
  simp [ProductParamsTransport.typedParamsOfProduct, Typed.typedWidth]

/--
Each transported typed ledger time block has spatial length `d`.
-/
theorem transportedTypedLedgerValuesAtTime_length
    (p : ProductRestrictedParams)
    (x : p.State)
    (t : TimeLayer) :
    (ProductLedgerTypedBlocks.transportedTypedLedgerValuesAtTime p x t).length =
      p.d := by
  unfold ProductLedgerTypedBlocks.transportedTypedLedgerValuesAtTime
  simp

/--
The three transported typed ledger blocks together have length `3*d`.
-/
theorem transportedTypedLedgerBlockValues_length
    (p : ProductRestrictedParams)
    (x : p.State) :
    (ProductLedgerTypedBlocks.transportedTypedLedgerBlockValues p x).length =
      3 * p.d := by
  unfold ProductLedgerTypedBlocks.transportedTypedLedgerBlockValues
  simp [transportedTypedLedgerValuesAtTime_length]
  omega

/--
The actual transported typed ledger values and the three-block transported
typed ledger values have the same length.

This is the length premise needed for a future `List.ext_getElem` proof.
-/
theorem transportedTypedLedgerValues_length_eq_blockValues_length
    (p : ProductRestrictedParams)
    (x : p.State) :
    (ProductLedgerEquivalenceTarget.transportedTypedLedgerValues p x).length =
      (ProductLedgerTypedBlocks.transportedTypedLedgerBlockValues p x).length := by
  rw [transportedTypedLedgerValues_length]
  rw [transportedTypedLedgerBlockValues_length]

end ProductLedgerTypedValuesLength

end VFH2
