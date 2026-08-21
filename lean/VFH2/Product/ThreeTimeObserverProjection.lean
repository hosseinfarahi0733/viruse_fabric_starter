import VFH2.Product.ThreeTimeGlobalFabric

/-!
# C113: Observer Projection and Information Loss

An observer is represented explicitly as a map out of the global three-time
fabric.  The full named projection is lossless, while the observer that retains
only the present slice is proved non-injective by a concrete bounded witness.

Boundary: this proves information loss for the observer map defined here. It
does not claim that every physical observer has exactly this projection.
-/

namespace VFH2
namespace ThreeTime

/-- A typed observer of the global fabric. -/
structure ObserverProjection (n d : Nat) (Narrative : Type) where
  observe : GlobalFabricState n d → Narrative

/-- The observer that compresses the fabric to a single present slice. -/
def presentObserverProjection (n d : Nat) :
    ObserverProjection n d (SpatialSlice n d) where
  observe := presentSlice

/-- The full three-component projection is information preserving. -/
theorem projectNamedSlices_injective
    {n d : Nat} :
    Function.Injective
      (@projectNamedSlices n d) := by
  intro x y h
  have hpast : pastSlice x = pastSlice y :=
    congrArg NamedSlices.past h
  have hpresent : presentSlice x = presentSlice y :=
    congrArg NamedSlices.present h
  have hfuture : futureSlice x = futureSlice y :=
    congrArg NamedSlices.future h
  exact ext_namedSlices hpast hpresent hfuture

/-- Constant zero spatial slice. -/
def zeroSlice (n d : Nat) : SpatialSlice n d :=
  fun _ => Typed.BoundedCoord.zero n

/-- Constant top spatial slice. -/
def topSlice (n d : Nat) : SpatialSlice n d :=
  fun _ => Typed.BoundedCoord.top n

/-- The all-zero three-time witness fabric. -/
def allZeroFabric : GlobalFabricState 1 1 :=
  assemble (zeroSlice 1 1) (zeroSlice 1 1) (zeroSlice 1 1)

/-- A witness fabric with a changed past but the same present and future. -/
def pastTopFabric : GlobalFabricState 1 1 :=
  assemble (topSlice 1 1) (zeroSlice 1 1) (zeroSlice 1 1)

/-- The two witness fabrics have exactly the same present narrative. -/
theorem presentObserver_witnesses_agree :
    (presentObserverProjection 1 1).observe allZeroFabric =
      (presentObserverProjection 1 1).observe pastTopFabric := by
  simp [presentObserverProjection, allZeroFabric, pastTopFabric]

/-- The two witness fabrics are globally different. -/
theorem presentObserver_witnesses_differ :
    allZeroFabric ≠ pastTopFabric := by
  intro h
  let s0 : SpaceIndex 1 := ⟨0, by decide⟩
  have hcoord := congrFun h (TimeLayer.t1, s0)
  have hval := congrArg Typed.BoundedCoord.val hcoord
  change (0 : Nat) = 1 at hval
  omega

/-- A one-slice observer cannot recover the entire three-time fabric. -/
theorem presentObserverProjection_not_injective :
    ¬ Function.Injective (presentObserverProjection 1 1).observe := by
  intro hinjective
  exact presentObserver_witnesses_differ
    (hinjective presentObserver_witnesses_agree)

/-- Explicit existence of two global fabrics with one perceived narrative. -/
theorem exists_distinct_fabrics_same_present_narrative :
    ∃ x y : GlobalFabricState 1 1,
      x ≠ y ∧
        (presentObserverProjection 1 1).observe x =
          (presentObserverProjection 1 1).observe y := by
  exact ⟨
    allZeroFabric,
    pastTopFabric,
    presentObserver_witnesses_differ,
    presentObserver_witnesses_agree
  ⟩

end ThreeTime
end VFH2
