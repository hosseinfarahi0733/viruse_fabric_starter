import VFH2.Product.ProductParamsTransport
import VFH2.Product.ProductStateTransport
import VFH2.Product.ProductFixedSet
import VFH2.RestrictedBridge.WellFormedParams

/-!
# VF-H2 Product/Official Restricted-Bridge State Transport

This file connects two restricted formalizations: the typed product model and
the official list-backed `RestrictedBridge` model.  Product active indices are
flattened to natural indices, and product states are serialized in canonical
`WidthIndex` order.

Boundary:
- This is only a transport between the two current restricted formalizations.
- It is not unrestricted `TTP-VF-H2-004`.
- It is not full-theory, empirical, or biological validation.
- It does not transport updates, ledgers, effects, or the official bridge
  theorem.
-/

namespace VFH2
namespace ProductOfficialRestrictedBridgeStateTransport

/--
Serialize product parameters into the official list-backed restricted model.

The typed parameter transport supplies the canonical flattened active list;
this serialization then stores the natural value of every bounded index.
-/
def officialRestrictedParams
    (p : ProductRestrictedParams) :
    RestrictedBridge.RestrictedParams :=
  { n := p.n
    d := p.d
    active :=
      (ProductParamsTransport.typedParamsOfProduct p).active.map
        (fun w => w.val) }

/--
Serialize a product state by enumerating every flattened width index in
canonical order and storing the corresponding bounded coordinate's value.
-/
def officialRestrictedState
    (p : ProductRestrictedParams)
    (x : p.State) :
    RestrictedBridge.State :=
  List.ofFn
    (fun w : Typed.WidthIndex p.d =>
      (ProductStateTransport.productToTyped x w).val)

/-- Canonical parameter serialization preserves both `n` and `d`. -/
theorem officialRestrictedParams_preserves_n_and_d
    (p : ProductRestrictedParams) :
    (officialRestrictedParams p).n = p.n ∧
      (officialRestrictedParams p).d = p.d := by
  exact ⟨rfl, rfl⟩

/-- Canonical state serialization has exactly the official expected width. -/
theorem officialRestrictedState_length
    (p : ProductRestrictedParams)
    (x : p.State) :
    (officialRestrictedState p x).length = 3 * p.d := by
  simp [officialRestrictedState, Typed.typedWidth]

/-- Every value in a serialized product state remains bounded by `p.n`. -/
theorem officialRestrictedState_values_le
    (p : ProductRestrictedParams)
    (x : p.State) :
    ∀ a ∈ officialRestrictedState p x, a ≤ p.n := by
  intro a ha
  unfold officialRestrictedState at ha
  rw [List.mem_ofFn] at ha
  rcases ha with ⟨w, hw⟩
  rw [← hw]
  exact (ProductStateTransport.productToTyped x w).bound

/--
Lookup at a flattened product index recovers the original product coordinate.

This is the semantic link used below; it follows directly from canonical
`List.ofFn` enumeration and the flatten/unflatten round trip.
-/
theorem officialRestrictedState_getD_flatten
    (p : ProductRestrictedParams)
    (x : p.State)
    (i : ProductIndex p.d) :
    (officialRestrictedState p x).getD (ProductIndex.flatten i).val 0 =
      (x i).val := by
  unfold officialRestrictedState
  rw [List.getD_eq_getElem?_getD]
  rw [List.getElem?_ofFn]
  rw [dif_pos (ProductIndex.flatten i).isLt]
  change
    (x (ProductIndex.unflatten (ProductIndex.flatten i))).val = (x i).val
  rw [ProductIndex.unflatten_flatten]

/--
Every active index of serialized product parameters is within official width,
because it came from a typed `WidthIndex`.
-/
theorem officialRestrictedParams_activeIndicesWithinWidth
    (p : ProductRestrictedParams) :
    RestrictedBridge.activeIndicesWithinWidth
      (officialRestrictedParams p) := by
  intro k hk
  change k < 3 * p.d
  unfold officialRestrictedParams at hk
  rcases List.mem_map.mp hk with ⟨w, _hw, rfl⟩
  exact w.isLt

/-- Every product parameter object canonically yields well-formed official parameters. -/
def officialWellFormedRestrictedParams
    (p : ProductRestrictedParams) :
    RestrictedBridge.WellFormedRestrictedParams :=
  { params := officialRestrictedParams p
    activeWithinWidth :=
      officialRestrictedParams_activeIndicesWithinWidth p }

/--
Every serialized product state and parameter pair is automatically a
well-formed input for the official list-backed restricted model.
-/
theorem officialRestrictedInput_wellFormed
    (p : ProductRestrictedParams)
    (x : p.State) :
    RestrictedBridge.wellFormedRestrictedInput
      (officialRestrictedParams p)
      (officialRestrictedState p x) := by
  have hparams := officialRestrictedParams_preserves_n_and_d p
  constructor
  · constructor
    · change
        (officialRestrictedState p x).length =
          3 * (officialRestrictedParams p).d
      rw [hparams.2]
      exact officialRestrictedState_length p x
    · change
        ∀ a ∈ officialRestrictedState p x,
          a ≤ (officialRestrictedParams p).n
      rw [hparams.1]
      exact officialRestrictedState_values_le p x
  · exact (officialWellFormedRestrictedParams p).activeWithinWidth

/--
Product fixedness is exactly official list-backed restricted fixedness after
canonical serialization.

Both directions are proved directly from active-list membership and the
serialized coordinate lookup above; no product/typed or official bridge
theorem is used.
-/
theorem productFixedSet_iff_officialRestrictedBridge_inFixedSetR
    (p : ProductRestrictedParams)
    (x : p.State) :
    ProductFixedSet p x ↔
      RestrictedBridge.inFixedSetR
        (officialRestrictedParams p)
        (officialRestrictedState p x) := by
  constructor
  · intro hfixed k hk
    unfold officialRestrictedParams at hk
    rcases List.mem_map.mp hk with ⟨w, hw, rfl⟩
    rcases
        (ProductParamsTransport.mem_typed_active_iff_exists_product_active
          (p := p) (w := w)).mp hw with
      ⟨i, hi, hflat⟩
    rw [← hflat]
    rw [officialRestrictedState_getD_flatten]
    exact hfixed i hi
  · intro hofficial i hi
    have hw :
        ProductIndex.flatten i ∈
          (ProductParamsTransport.typedParamsOfProduct p).active :=
      ProductParamsTransport.flatten_mem_typed_active_of_mem_product_active
        (p := p) (i := i) hi
    have hnat :
        (ProductIndex.flatten i).val ∈
          (officialRestrictedParams p).active := by
      unfold officialRestrictedParams
      exact List.mem_map_of_mem hw
    have htop := hofficial (ProductIndex.flatten i).val hnat
    rw [officialRestrictedState_getD_flatten] at htop
    exact htop

end ProductOfficialRestrictedBridgeStateTransport
end VFH2
