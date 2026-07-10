import VFH2.Product.ProductRestrictedParamsActiveLengthLowerBound

namespace VFH2
open ProductRestrictedParamsActiveCustomEnumKernel
open ProductRestrictedParamsActiveLengthLowerBound
namespace ProductRestrictedParamsActiveEraseConstruction

/--
Construction-local active list obtained by deleting one selected product index
from the complete noduplicate product-index enumeration.

Unlike a raw noncoverage premise, this definition records how the active list is
built. The selected `missing` index can exist only when the product dimension is
positive.
-/
def activeWithoutProductIndex
    (d : Nat)
    (missing : ProductIndex d) :
    List (ProductIndex d) :=
  (productIndexEnum d).erase missing

/--
Restricted parameters whose active list is built by erasing one selected index
from the complete product-index enumeration.
-/
def paramsWithInactiveProductIndex
    (n d : Nat)
    (missing : ProductIndex d) :
    ProductRestrictedParams :=
  { n := n
    d := d
    active := activeWithoutProductIndex d missing }

@[simp] theorem paramsWithInactiveProductIndex_n
    (n d : Nat)
    (missing : ProductIndex d) :
    (paramsWithInactiveProductIndex n d missing).n = n := by
  rfl

@[simp] theorem paramsWithInactiveProductIndex_d
    (n d : Nat)
    (missing : ProductIndex d) :
    (paramsWithInactiveProductIndex n d missing).d = d := by
  rfl

@[simp] theorem paramsWithInactiveProductIndex_active
    (n d : Nat)
    (missing : ProductIndex d) :
    (paramsWithInactiveProductIndex n d missing).active =
      activeWithoutProductIndex d missing := by
  rfl

/--
The erase construction has exactly one fewer entry than the complete typed-width
enumeration.
-/
theorem activeWithoutProductIndex_length_eq_typedWidth_sub_one
    (d : Nat)
    (missing : ProductIndex d) :
    (activeWithoutProductIndex d missing).length = Typed.typedWidth d - 1 := by
  have hmem : missing ∈ productIndexEnum d :=
    productIndexEnum_complete d missing
  unfold activeWithoutProductIndex
  rw [List.length_erase_of_mem hmem, productIndexEnum_length_typedWidth]

/--
Erasing a product index from the complete enumeration makes the resulting active
list strictly shorter than the typed product width.
-/
theorem activeWithoutProductIndex_length_lt_typedWidth
    (d : Nat)
    (missing : ProductIndex d) :
    (activeWithoutProductIndex d missing).length < Typed.typedWidth d := by
  have hd : 0 < d := by
    have hspace : missing.2.val < d := missing.2.isLt
    omega
  have hwidthPos : 0 < Typed.typedWidth d :=
    Typed.WidthIndex.typedWidth_pos_of_pos hd
  rw [activeWithoutProductIndex_length_eq_typedWidth_sub_one d missing]
  omega

/--
The construction-local parameter object satisfies the C34 active-length source.
-/
theorem paramsWithInactiveProductIndex_active_length_lt_typedWidth
    (n d : Nat)
    (missing : ProductIndex d) :
    (paramsWithInactiveProductIndex n d missing).active.length <
      Typed.typedWidth (paramsWithInactiveProductIndex n d missing).d := by
  exact activeWithoutProductIndex_length_lt_typedWidth d missing

/--
Package the erase-construction theorem as the existing active-length source.
-/
def activeLengthLtTypedWidthSource_of_paramsWithInactiveProductIndex
    (n d : Nat)
    (missing : ProductIndex d) :
    ActiveLengthLtTypedWidthSource
      (paramsWithInactiveProductIndex n d missing) :=
  { active_length_lt_typedWidth :=
      paramsWithInactiveProductIndex_active_length_lt_typedWidth n d missing }

/--
The erase constructor yields the existing active-noncoverage certificate without
requiring a raw `¬ ∀ i, i ∈ p.active` premise at the API boundary.
-/
def activeNoncoverageCertificate_of_paramsWithInactiveProductIndex
    (n d : Nat)
    (missing : ProductIndex d) :
    ProductRestrictedParamsInactiveCoordScore.ActiveNoncoverageCertificate
      (paramsWithInactiveProductIndex n d missing) :=
  activeNoncoverageCertificate_of_active_length_lt_typedWidth
    (paramsWithInactiveProductIndex n d missing)
    (activeLengthLtTypedWidthSource_of_paramsWithInactiveProductIndex n d missing)

/--
Construction-level front door into the current restricted proof-spine route.

The active-length deficit, noncoverage certificate, inactive coordinate score,
score range, fixed-state construction, and final restricted target are all
selected by the existing certificate chain.
-/
noncomputable def
    restrictedParams_paramsWithInactiveProductIndex_fixedProductState_to_currentBestMainTheorem
    (n d : Nat)
    (missing : ProductIndex d) :=
  ProductRestrictedParamsInactiveCoordScore.restrictedParams_activeNoncoverageCertificate_fixedProductState_to_currentBestMainTheorem
    (paramsWithInactiveProductIndex n d missing)
    (activeNoncoverageCertificate_of_paramsWithInactiveProductIndex n d missing)

#check activeWithoutProductIndex
#check paramsWithInactiveProductIndex
#check activeWithoutProductIndex_length_eq_typedWidth_sub_one
#check activeWithoutProductIndex_length_lt_typedWidth
#check paramsWithInactiveProductIndex_active_length_lt_typedWidth
#check activeLengthLtTypedWidthSource_of_paramsWithInactiveProductIndex
#check activeNoncoverageCertificate_of_paramsWithInactiveProductIndex
#check restrictedParams_paramsWithInactiveProductIndex_fixedProductState_to_currentBestMainTheorem

end ProductRestrictedParamsActiveEraseConstruction
end VFH2
