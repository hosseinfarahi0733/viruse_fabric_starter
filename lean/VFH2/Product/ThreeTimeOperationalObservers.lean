import VFH2.Product.ThreeTimeLocalGlobalGluing
import VFH2.Product.ThreeTimeObserverProjection

/-!
# C120: Operational Observer Families

This module turns observation into an indexed operational family.  Equality of
all outcomes defines observational equivalence.  The three named time
observations jointly separate global fabrics, while the present-only family is
proved incomplete by the concrete C113 witness.
-/

namespace VFH2
namespace ThreeTime

/-- An indexed collection of operational measurements. -/
structure ObserverFamily
    (index State Outcome : Type) where
  observe : index -> State -> Outcome

/-- Two states are indistinguishable to every observer in the family. -/
def ObservationallyEquivalent
    {index State Outcome : Type}
    (observers : ObserverFamily index State Outcome)
    (x y : State) : Prop :=
  forall i, observers.observe i x = observers.observe i y

/-- The family is complete when its joint outcomes separate states. -/
def JointlySeparating
    {index State Outcome : Type}
    (observers : ObserverFamily index State Outcome) : Prop :=
  forall {x y},
    ObservationallyEquivalent observers x y -> x = y

/-- Collect all operational outcomes into one joint observation. -/
def jointObservation
    {index State Outcome : Type}
    (observers : ObserverFamily index State Outcome) :
    State -> (index -> Outcome) :=
  fun state i => observers.observe i state

/-- Operational completeness is exactly injectivity of the joint observation. -/
theorem jointlySeparating_iff_jointObservation_injective
    {index State Outcome : Type}
    (observers : ObserverFamily index State Outcome) :
    JointlySeparating observers <->
      Function.Injective (jointObservation observers) := by
  constructor
  · intro hseparating x y hjoint
    apply hseparating
    intro i
    exact congrFun hjoint i
  · intro hinjective x y hequivalent
    apply hinjective
    funext i
    exact hequivalent i

/-- Observe one complete spatial slice at each time-layer index. -/
def namedTimeObserverFamily (n d : Nat) :
    ObserverFamily
      TimeLayer
      (GlobalFabricState n d)
      (SpatialSlice n d) where
  observe := fun time state => slice state time

/-- The complete three-time observer family separates all global fabrics. -/
theorem namedTimeObserverFamily_jointlySeparating
    (n d : Nat) :
    JointlySeparating (namedTimeObserverFamily n d) := by
  intro x y hequivalent
  apply ext_namedSlices
  · exact hequivalent TimeLayer.t1
  · exact hequivalent TimeLayer.t2
  · exact hequivalent TimeLayer.t3

/-- A family containing only the present-slice observation. -/
def presentOnlyObserverFamily :
    ObserverFamily
      Unit
      (GlobalFabricState 1 1)
      (SpatialSlice 1 1) where
  observe := fun _ state => presentSlice state

/-- The present-only operational family does not separate global fabrics. -/
theorem presentOnlyObserverFamily_not_jointlySeparating :
    ¬ JointlySeparating presentOnlyObserverFamily := by
  intro hseparating
  apply presentObserver_witnesses_differ
  apply hseparating
  intro i
  cases i
  exact presentObserver_witnesses_agree

/-- A concrete blind pair exists for the present-only operational family. -/
theorem presentOnlyObserverFamily_blindPair :
    exists x y : GlobalFabricState 1 1,
      x ≠ y /\
        ObservationallyEquivalent presentOnlyObserverFamily x y := by
  exact ⟨
    allZeroFabric,
    pastTopFabric,
    presentObserver_witnesses_differ,
    fun _ => presentObserver_witnesses_agree
  ⟩

end ThreeTime
end VFH2
