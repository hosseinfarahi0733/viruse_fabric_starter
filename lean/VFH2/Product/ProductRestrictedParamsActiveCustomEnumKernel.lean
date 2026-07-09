import VFH2.Product.ProductRestrictedParamsActiveNoncoverageCertificate
import VFH2.Product.ProductFlattenEquiv
import VFH2.Product.ProductFlattenFullInjective

namespace VFH2
namespace ProductRestrictedParamsActiveCustomEnumKernel

/-- Transparent local enumeration of `Fin n`, avoiding opaque `List.ofFn` internals. -/
def finEnum : (n : Nat) → List (Fin n)
  | 0 => []
  | n + 1 => (⟨0, Nat.succ_pos n⟩ : Fin (n + 1)) :: List.map Fin.succ (finEnum n)

theorem finEnum_length (n : Nat) : (finEnum n).length = n := by
  induction n with
  | zero =>
      rfl
  | succ n ih =>
      simp [finEnum, ih]

theorem nodup_map_of_injective_local
    {α β : Type} {f : α → β}
    (hf : Function.Injective f)
    {xs : List α} :
    xs.Nodup → (List.map f xs).Nodup := by
  induction xs with
  | nil =>
      intro _hnd
      simp
  | cons a xs ih =>
      intro hnd
      have hparts := (List.nodup_cons.mp hnd)
      change (f a :: List.map f xs).Nodup
      apply List.nodup_cons.mpr
      constructor
      · intro hmem
        rw [List.mem_map] at hmem
        rcases hmem with ⟨a', ha_mem, hfa'⟩
        have ha'eq : a' = a := hf hfa'
        have ha_in_xs : a ∈ xs := by
          simpa [ha'eq] using ha_mem
        exact hparts.left ha_in_xs
      · exact ih hparts.right

theorem finEnum_nodup (n : Nat) : (finEnum n).Nodup := by
  induction n with
  | zero =>
      simp [finEnum]
  | succ n ih =>
      change ((⟨0, Nat.succ_pos n⟩ : Fin (n + 1)) :: List.map Fin.succ (finEnum n)).Nodup
      apply List.nodup_cons.mpr
      constructor
      · intro hmem
        rw [List.mem_map] at hmem
        rcases hmem with ⟨b, _hbmem, hb⟩
        exact Fin.succ_ne_zero b hb
      · exact nodup_map_of_injective_local (fun a b h => (Fin.succ_inj.mp h)) ih

theorem finEnum_complete (n : Nat) (i : Fin n) : i ∈ finEnum n := by
  cases n with
  | zero =>
      exact False.elim ((Nat.not_lt_zero i.val) i.isLt)
  | succ n =>
      cases i with
      | mk k hklt =>
          cases k with
          | zero =>
              simp [finEnum]
          | succ k =>
              have hk : k < n := Nat.lt_of_succ_lt_succ hklt
              have hmem : (⟨k, hk⟩ : Fin n) ∈ finEnum n := finEnum_complete n ⟨k, hk⟩
              have hmapped : (⟨k + 1, hklt⟩ : Fin (n + 1)) ∈ List.map Fin.succ (finEnum n) := by
                rw [List.mem_map]
                refine ⟨(⟨k, hk⟩ : Fin n), hmem, ?_⟩
                apply Fin.ext
                rfl
              simp [finEnum, hmapped]

def productWidthEnum (d : Nat) : List (Typed.WidthIndex d) :=
  finEnum (Typed.typedWidth d)

def productIndexEnum (d : Nat) : List (ProductIndex d) :=
  List.map ProductIndex.unflatten (productWidthEnum d)

theorem productWidthEnum_length_typedWidth (d : Nat) :
    (productWidthEnum d).length = Typed.typedWidth d := by
  simp [productWidthEnum, finEnum_length]

theorem productWidthEnum_complete (d : Nat) (w : Typed.WidthIndex d) :
    w ∈ productWidthEnum d := by
  exact finEnum_complete (Typed.typedWidth d) w

theorem productWidthEnum_nodup (d : Nat) :
    (productWidthEnum d).Nodup := by
  exact finEnum_nodup (Typed.typedWidth d)

theorem ProductIndex_unflatten_injective {d : Nat} :
    Function.Injective (ProductIndex.unflatten : Typed.WidthIndex d → ProductIndex d) := by
  intro a b h
  have hflat := congrArg ProductIndex.flatten h
  simpa [ProductIndex.flatten_unflatten] using hflat

theorem productIndexEnum_length_typedWidth (d : Nat) :
    (productIndexEnum d).length = Typed.typedWidth d := by
  simp [productIndexEnum, productWidthEnum_length_typedWidth]

theorem productIndexEnum_nodup (d : Nat) :
    (productIndexEnum d).Nodup := by
  unfold productIndexEnum
  exact nodup_map_of_injective_local ProductIndex_unflatten_injective (productWidthEnum_nodup d)

theorem productIndexEnum_complete (d : Nat) (i : ProductIndex d) :
    i ∈ productIndexEnum d := by
  unfold productIndexEnum
  have hw : i.flatten ∈ productWidthEnum d := productWidthEnum_complete d i.flatten
  have hmapped : ProductIndex.unflatten i.flatten ∈ List.map ProductIndex.unflatten (productWidthEnum d) :=
    List.mem_map_of_mem hw
  simpa [ProductIndex.unflatten_flatten i] using hmapped

theorem typedWidth_le_active_length_of_productIndexEnum_sublist
    (p : ProductRestrictedParams)
    (hsub : (productIndexEnum p.d).Sublist p.active) :
    Typed.typedWidth p.d ≤ p.active.length := by
  have hlen := List.Sublist.length_le hsub
  rw [productIndexEnum_length_typedWidth] at hlen
  exact hlen

/-- A structural source: the complete product-index enumeration appears as a sublist of `p.active`,
and `p.active` is still too short to cover the whole typed width. -/
structure ActiveProductIndexEnumSublistSource (p : ProductRestrictedParams) : Type where
  enum_sublist_active : (productIndexEnum p.d).Sublist p.active
  active_length_lt_typedWidth : p.active.length < Typed.typedWidth p.d

theorem not_all_active_of_productIndexEnum_sublist_source
    (p : ProductRestrictedParams)
    (src : ActiveProductIndexEnumSublistSource p) :
    ¬ ∀ i : ProductIndex p.d, i ∈ p.active := by
  intro _hAll
  have hle : Typed.typedWidth p.d ≤ p.active.length :=
    typedWidth_le_active_length_of_productIndexEnum_sublist p src.enum_sublist_active
  exact (Nat.not_lt_of_ge hle) src.active_length_lt_typedWidth

def activeNoncoverageCertificate_of_productIndexEnum_sublist_source
    (p : ProductRestrictedParams)
    (src : ActiveProductIndexEnumSublistSource p) :
    ProductRestrictedParamsInactiveCoordScore.ActiveNoncoverageCertificate p :=
  ProductRestrictedParamsInactiveCoordScore.ActiveNoncoverageCertificate.of_not_all_active p
    (not_all_active_of_productIndexEnum_sublist_source p src)

end ProductRestrictedParamsActiveCustomEnumKernel
end VFH2
