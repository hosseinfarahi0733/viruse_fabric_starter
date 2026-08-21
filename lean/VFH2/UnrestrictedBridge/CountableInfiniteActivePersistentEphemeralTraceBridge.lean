import VFH2.UnrestrictedBridge.CountableInfiniteActiveGlobalLedgerStrictComparison

/-!
# Countable Infinite-Active Persistent/Ephemeral Trace Bridge

This module gives one explicit operational bridge from finite token traces to
the countable infinite-active residual-ledger model.  A persistent observer
remembers tokens across windows; an ephemeral observer resets its memory at
every window boundary.  Their repeat counts are represented as convergent
ledger effects, and the normalized rational gap is positive exactly when a
token returns in a later window.

The bridge is a mathematical semantics for these explicitly defined finite
trace statistics, encoded in a finite active prefix of a countable state.  It
is not a byte-for-byte translation of a Python algorithm, does not identify
the statistics with an external Memory/Null metric, and is not unrestricted
TTP-VF-H2-004, a full-theory result, or an empirical, physical, or biological
validation claim.
-/

namespace VFH2
namespace UnrestrictedBridge

private def c125_repeatFlagPairsWithin
    {Token : Type}
    [DecidableEq Token]
    (prior current : List Token) : List Token -> List (Bool × Bool)
  | [] => []
  | token :: rest =>
      (decide (token ∈ prior ∨ token ∈ current),
        decide (token ∈ current)) ::
        c125_repeatFlagPairsWithin prior (token :: current) rest

private def c125_repeatFlagPairsFromSeen
    {Token : Type}
    [DecidableEq Token]
    (prior : List Token) : List (List Token) -> List (Bool × Bool)
  | [] => []
  | window :: rest =>
      c125_repeatFlagPairsWithin prior [] window ++
        c125_repeatFlagPairsFromSeen (window ++ prior) rest

private def c125_hasCrossStepReturnFromSeen
    {Token : Type}
    (prior : List Token) : List (List Token) -> Prop
  | [] => False
  | window :: rest =>
      (∃ token, token ∈ prior ∧ token ∈ window) ∨
        c125_hasCrossStepReturnFromSeen (window ++ prior) rest

/-- A token appearing in one window appears again in a later window. -/
def hasCrossStepReturn
    {Token : Type}
    (trace : List (List Token)) : Prop :=
  c125_hasCrossStepReturnFromSeen [] trace

private def c125_persistentRepeatFlags
    {Token : Type}
    [DecidableEq Token]
    (trace : List (List Token)) : List Bool :=
  (c125_repeatFlagPairsFromSeen [] trace).map Prod.fst

private def c125_ephemeralRepeatFlags
    {Token : Type}
    [DecidableEq Token]
    (trace : List (List Token)) : List Bool :=
  (c125_repeatFlagPairsFromSeen [] trace).map Prod.snd

/-- The number of repeats seen by persistent memory across the whole trace. -/
def persistentRepeatCount
    {Token : Type}
    [DecidableEq Token]
    (trace : List (List Token)) : Nat :=
  (c125_persistentRepeatFlags trace).count true

/-- The number of repeats seen when memory resets at each window boundary. -/
def ephemeralRepeatCount
    {Token : Type}
    [DecidableEq Token]
    (trace : List (List Token)) : Nat :=
  (c125_ephemeralRepeatFlags trace).count true

/-- Unit-top ledger parameters active exactly on serialized trace positions. -/
def repeatTraceParamsU
    {Token : Type}
    (trace : List (List Token)) : InfiniteActiveParamsU where
  top := 1
  active := fun i => decide (i < trace.flatten.length)

/--
State with deficit one exactly at persistent-repeat positions in the active
serialized prefix; its inactive tail is zero.
-/
def persistentRepeatStateU
    {Token : Type}
    [DecidableEq Token]
    (trace : List (List Token)) : StateU :=
  fun i =>
    if i < (c125_persistentRepeatFlags trace).length then
      if (c125_persistentRepeatFlags trace).getD i false then 0 else 1
    else 0

/--
State with deficit one exactly at within-window repeat positions in the active
serialized prefix; its inactive tail is zero.
-/
def ephemeralRepeatStateU
    {Token : Type}
    [DecidableEq Token]
    (trace : List (List Token)) : StateU :=
  fun i =>
    if i < (c125_ephemeralRepeatFlags trace).length then
      if (c125_ephemeralRepeatFlags trace).getD i false then 0 else 1
    else 0

/-- Positive denominator used to normalize both repeat counts. -/
def repeatTraceDenominator
    {Token : Type}
    (trace : List (List Token)) : Nat :=
  max 1 trace.flatten.length

/-- Persistent repeat count divided by the positive trace denominator. -/
def persistentNormalizedRepeatScore
    {Token : Type}
    [DecidableEq Token]
    (trace : List (List Token)) : Rat :=
  (persistentRepeatCount trace : Rat) / (repeatTraceDenominator trace : Rat)

/-- Ephemeral repeat count divided by the positive trace denominator. -/
def ephemeralNormalizedRepeatScore
    {Token : Type}
    [DecidableEq Token]
    (trace : List (List Token)) : Rat :=
  (ephemeralRepeatCount trace : Rat) / (repeatTraceDenominator trace : Rat)

/-- Rational normalized persistent-minus-ephemeral residual-ledger size. -/
def persistentEphemeralNormalizedLedgerEffectSize
    {Token : Type}
    [DecidableEq Token]
    (trace : List (List Token)) : Rat :=
  persistentNormalizedRepeatScore trace -
    ephemeralNormalizedRepeatScore trace

@[simp] private theorem c125_repeatFlagPairsWithin_length
    {Token : Type}
    [DecidableEq Token]
    (prior current rest : List Token) :
    (c125_repeatFlagPairsWithin prior current rest).length = rest.length := by
  induction rest generalizing current with
  | nil => rfl
  | cons token rest ih =>
      simp [c125_repeatFlagPairsWithin, ih]

@[simp] private theorem c125_repeatFlagPairsFromSeen_length
    {Token : Type}
    [DecidableEq Token]
    (prior : List Token)
    (trace : List (List Token)) :
    (c125_repeatFlagPairsFromSeen prior trace).length =
      trace.flatten.length := by
  induction trace generalizing prior with
  | nil => rfl
  | cons window rest ih =>
      simp [c125_repeatFlagPairsFromSeen, ih]

private theorem c125_map_range_getD_eq_self
    {α : Type}
    (values : List α)
    (fallback : α) :
    (List.range values.length).map (fun i => values.getD i fallback) =
      values := by
  apply List.ext_getElem
  · simp
  · intro i hLeft hRight
    simp only [List.length_map, List.length_range] at hLeft
    simp [List.getD, hLeft]

private theorem c125_boolIndicator_sum_eq_count_true
    (flags : List Bool) :
    (flags.map fun flag => if flag then 1 else 0).sum =
      flags.count true := by
  induction flags with
  | nil => rfl
  | cons flag flags ih =>
      cases flag <;> simp [ih, Nat.add_comm]

private theorem c125_flagState_effectPrefix_eq_count
    (flags : List Bool) :
    (List.range flags.length |>.map fun i =>
      1 - (if flags.getD i false then 0 else 1)).sum =
      flags.count true := by
  have hEnumerate := c125_map_range_getD_eq_self flags false
  calc
    (List.range flags.length |>.map fun i =>
        1 - (if flags.getD i false then 0 else 1)).sum =
        (List.range flags.length |>.map fun i =>
          if flags.getD i false then 1 else 0).sum := by
            apply congrArg List.sum
            apply List.map_congr_left
            intro i hi
            cases flags.getD i false <;> rfl
    _ = (flags.map fun flag => if flag then 1 else 0).sum := by
      calc
        (List.range flags.length |>.map fun i =>
            if flags.getD i false then 1 else 0).sum =
            ((List.range flags.length |>.map fun i =>
              flags.getD i false).map fun flag =>
                if flag then 1 else 0).sum := by
                  apply congrArg List.sum
                  rw [List.map_map]
                  apply List.map_congr_left
                  intro i hi
                  simp only [Function.comp_apply]
        _ = (flags.map fun flag => if flag then 1 else 0).sum := by
          rw [hEnumerate]
    _ = flags.count true := c125_boolIndicator_sum_eq_count_true flags

private theorem c125_persistent_stateSpace
    {Token : Type}
    [DecidableEq Token]
    (trace : List (List Token)) :
    inInfiniteActiveStateSpaceU
      (repeatTraceParamsU trace)
      (persistentRepeatStateU trace) := by
  unfold inInfiniteActiveStateSpaceU
  intro i
  change persistentRepeatStateU trace i ≤ 1
  unfold persistentRepeatStateU
  split
  · split <;> omega
  · omega

private theorem c125_ephemeral_stateSpace
    {Token : Type}
    [DecidableEq Token]
    (trace : List (List Token)) :
    inInfiniteActiveStateSpaceU
      (repeatTraceParamsU trace)
      (ephemeralRepeatStateU trace) := by
  unfold inInfiniteActiveStateSpaceU
  intro i
  change ephemeralRepeatStateU trace i ≤ 1
  unfold ephemeralRepeatStateU
  split
  · split <;> omega
  · omega

private theorem c125_flagState_fullPrefix_eq_count
    (flags : List Bool) :
    (List.range flags.length |>.map fun i =>
      if decide (i < flags.length) then
        1 -
          (if i < flags.length then
            if flags.getD i false then 0 else 1
          else 0)
      else 0).sum = flags.count true := by
  calc
    (List.range flags.length |>.map fun i =>
        if decide (i < flags.length) then
          1 -
            (if i < flags.length then
              if flags.getD i false then 0 else 1
            else 0)
        else 0).sum =
        (List.range flags.length |>.map fun i =>
          1 - (if flags.getD i false then 0 else 1)).sum := by
            apply congrArg List.sum
            apply List.map_congr_left
            intro i hi
            have hlt : i < flags.length := List.mem_range.mp hi
            simp [hlt]
    _ = flags.count true := c125_flagState_effectPrefix_eq_count flags

private theorem c125_persistent_hasEffect
    {Token : Type}
    [DecidableEq Token]
    (trace : List (List Token)) :
    HasInfiniteActiveGlobalLedgerEffectU
      (repeatTraceParamsU trace)
      (persistentRepeatStateU trace)
      (persistentRepeatCount trace) := by
  apply
    (hasInfiniteActiveGlobalLedgerEffectU_iff_exists_eventuallyFixedActive_and_eq_prefix
      (repeatTraceParamsU trace)
      (persistentRepeatStateU trace)
      (c125_persistent_stateSpace trace)
      (persistentRepeatCount trace)).2
  refine ⟨trace.flatten.length, ?_, ?_⟩
  · intro i hi hiActive
    have hlt : i < trace.flatten.length := by
      exact of_decide_eq_true hiActive
    omega
  · unfold persistentRepeatCount infiniteActiveLedgerEffectPrefixU
    let flags := c125_persistentRepeatFlags trace
    have hLength : flags.length = trace.flatten.length := by
      simp [flags, c125_persistentRepeatFlags]
    simp only [repeatTraceParamsU, persistentRepeatStateU]
    rw [← hLength]
    change flags.count true =
      (List.range flags.length |>.map fun i =>
        if decide (i < flags.length) then
          1 -
            (if i < flags.length then
              if flags.getD i false then 0 else 1
            else 0)
        else 0).sum
    exact (c125_flagState_fullPrefix_eq_count flags).symm

private theorem c125_ephemeral_hasEffect
    {Token : Type}
    [DecidableEq Token]
    (trace : List (List Token)) :
    HasInfiniteActiveGlobalLedgerEffectU
      (repeatTraceParamsU trace)
      (ephemeralRepeatStateU trace)
      (ephemeralRepeatCount trace) := by
  apply
    (hasInfiniteActiveGlobalLedgerEffectU_iff_exists_eventuallyFixedActive_and_eq_prefix
      (repeatTraceParamsU trace)
      (ephemeralRepeatStateU trace)
      (c125_ephemeral_stateSpace trace)
      (ephemeralRepeatCount trace)).2
  refine ⟨trace.flatten.length, ?_, ?_⟩
  · intro i hi hiActive
    have hlt : i < trace.flatten.length := by
      exact of_decide_eq_true hiActive
    omega
  · unfold ephemeralRepeatCount infiniteActiveLedgerEffectPrefixU
    let flags := c125_ephemeralRepeatFlags trace
    have hLength : flags.length = trace.flatten.length := by
      simp [flags, c125_ephemeralRepeatFlags]
    simp only [repeatTraceParamsU, ephemeralRepeatStateU]
    rw [← hLength]
    change flags.count true =
      (List.range flags.length |>.map fun i =>
        if decide (i < flags.length) then
          1 -
            (if i < flags.length then
              if flags.getD i false then 0 else 1
            else 0)
        else 0).sum
    exact (c125_flagState_fullPrefix_eq_count flags).symm

private theorem c125_pair_second_true_implies_first_true_within
    {Token : Type}
    [DecidableEq Token]
    (prior current rest : List Token) :
    ∀ pair ∈ c125_repeatFlagPairsWithin prior current rest,
      pair.2 = true -> pair.1 = true := by
  induction rest generalizing current with
  | nil => simp [c125_repeatFlagPairsWithin]
  | cons token rest ih =>
      intro pair hPair hSecond
      simp only [c125_repeatFlagPairsWithin, List.mem_cons] at hPair
      rcases hPair with rfl | hTail
      · have hCurrent : token ∈ current := of_decide_eq_true hSecond
        simp [hCurrent]
      · exact ih (token :: current) pair hTail hSecond

private theorem c125_pair_second_true_implies_first_true
    {Token : Type}
    [DecidableEq Token]
    (prior : List Token)
    (trace : List (List Token)) :
    ∀ pair ∈ c125_repeatFlagPairsFromSeen prior trace,
      pair.2 = true -> pair.1 = true := by
  induction trace generalizing prior with
  | nil => simp [c125_repeatFlagPairsFromSeen]
  | cons window rest ih =>
      intro pair hPair hSecond
      simp only [c125_repeatFlagPairsFromSeen, List.mem_append] at hPair
      rcases hPair with hWindow | hRest
      · exact
          c125_pair_second_true_implies_first_true_within
            prior [] window pair hWindow hSecond
      · exact ih (window ++ prior) pair hRest hSecond

private theorem c125_pairStates_le
    (pairs : List (Bool × Bool))
    (hPairs : ∀ pair ∈ pairs, pair.2 = true -> pair.1 = true)
    (i : Nat) :
    (if (pairs.map Prod.fst).getD i false then 0 else 1) ≤
      (if (pairs.map Prod.snd).getD i false then 0 else 1) := by
  induction pairs generalizing i with
  | nil => simp
  | cons pair pairs ih =>
      cases i with
      | zero =>
          cases hFirst : pair.1 <;> cases hSecond : pair.2 <;> simp_all
      | succ i =>
          simp only [List.map_cons, List.getD_cons_succ]
          apply ih
          intro tailPair hTail hSecond
          exact hPairs tailPair (by simp [hTail]) hSecond

private theorem c125_persistent_le_ephemeral
    {Token : Type}
    [DecidableEq Token]
    (trace : List (List Token))
    (i : Nat) :
    persistentRepeatStateU trace i ≤ ephemeralRepeatStateU trace i := by
  let pairs := c125_repeatFlagPairsFromSeen [] trace
  change
    (if i < (pairs.map Prod.fst).length then
      if (pairs.map Prod.fst).getD i false then 0 else 1
    else 0) ≤
      (if i < (pairs.map Prod.snd).length then
        if (pairs.map Prod.snd).getD i false then 0 else 1
      else 0)
  simp only [List.length_map]
  by_cases hRange : i < pairs.length
  · simp only [hRange, if_true]
    exact
      c125_pairStates_le
        pairs
        (c125_pair_second_true_implies_first_true [] trace)
        i
  · simp [hRange]

private theorem c125_exists_strict_pair_within_iff
    {Token : Type}
    [DecidableEq Token]
    (prior current rest : List Token) :
    (∃ pair ∈ c125_repeatFlagPairsWithin prior current rest,
        pair.1 = true ∧ pair.2 = false) ↔
      ∃ token, token ∈ prior ∧ token ∈ rest ∧ token ∉ current := by
  induction rest generalizing current with
  | nil => simp [c125_repeatFlagPairsWithin]
  | cons token rest ih =>
      constructor
      · rintro ⟨pair, hPair, hFirst, hSecond⟩
        simp only [c125_repeatFlagPairsWithin, List.mem_cons] at hPair
        rcases hPair with rfl | hTail
        · have hPriorOrCurrent : token ∈ prior ∨ token ∈ current :=
            of_decide_eq_true hFirst
          have hNotCurrent : token ∉ current := by
            exact of_decide_eq_false hSecond
          rcases hPriorOrCurrent with hPrior | hCurrent
          · exact ⟨token, hPrior, by simp, hNotCurrent⟩
          · exact False.elim (hNotCurrent hCurrent)
        · rcases
              (ih (current := token :: current)).1
                ⟨pair, hTail, hFirst, hSecond⟩ with
            ⟨witness, hPrior, hRest, hNotCons⟩
          have hNotCurrent : witness ∉ current := by
            intro hCurrent
            exact hNotCons (by simp [hCurrent])
          exact ⟨witness, hPrior, by simp [hRest], hNotCurrent⟩
      · rintro ⟨witness, hPrior, hHeadOrRest, hNotCurrent⟩
        simp only [List.mem_cons] at hHeadOrRest
        rcases hHeadOrRest with rfl | hRest
        · refine
            ⟨(decide (witness ∈ prior ∨ witness ∈ current),
                decide (witness ∈ current)), ?_, ?_, ?_⟩
          · simp [c125_repeatFlagPairsWithin]
          · exact decide_eq_true (Or.inl hPrior)
          · exact decide_eq_false hNotCurrent
        · by_cases hEq : witness = token
          · subst witness
            refine
              ⟨(decide (token ∈ prior ∨ token ∈ current),
                  decide (token ∈ current)), ?_, ?_, ?_⟩
            · simp [c125_repeatFlagPairsWithin]
            · exact decide_eq_true (Or.inl hPrior)
            · exact decide_eq_false hNotCurrent
          · have hNotCons : witness ∉ token :: current := by
              simp [hEq, hNotCurrent]
            rcases
                (ih (current := token :: current)).2
                  ⟨witness, hPrior, hRest, hNotCons⟩ with
              ⟨pair, hPair, hFirst, hSecond⟩
            exact
              ⟨pair, by simp [c125_repeatFlagPairsWithin, hPair],
                hFirst, hSecond⟩

private theorem c125_exists_strict_pair_iff_crossStepFromSeen
    {Token : Type}
    [DecidableEq Token]
    (prior : List Token)
    (trace : List (List Token)) :
    (∃ pair ∈ c125_repeatFlagPairsFromSeen prior trace,
        pair.1 = true ∧ pair.2 = false) ↔
      c125_hasCrossStepReturnFromSeen prior trace := by
  induction trace generalizing prior with
  | nil => simp [c125_repeatFlagPairsFromSeen,
      c125_hasCrossStepReturnFromSeen]
  | cons window rest ih =>
      constructor
      · rintro ⟨pair, hPair, hFirst, hSecond⟩
        simp only [c125_repeatFlagPairsFromSeen, List.mem_append] at hPair
        simp only [c125_hasCrossStepReturnFromSeen]
        rcases hPair with hWindow | hRest
        · left
          rcases
              (c125_exists_strict_pair_within_iff prior [] window).1
                ⟨pair, hWindow, hFirst, hSecond⟩ with
            ⟨token, hPrior, hInWindow, hNotNil⟩
          exact ⟨token, hPrior, hInWindow⟩
        · right
          exact
            (ih (prior := window ++ prior)).1
              ⟨pair, hRest, hFirst, hSecond⟩
      · intro hCross
        simp only [c125_hasCrossStepReturnFromSeen] at hCross
        rcases hCross with hWindow | hRest
        · rcases hWindow with ⟨token, hPrior, hInWindow⟩
          rcases
              (c125_exists_strict_pair_within_iff prior [] window).2
                ⟨token, hPrior, hInWindow, by simp⟩ with
            ⟨pair, hPair, hFirst, hSecond⟩
          exact
            ⟨pair,
              by simp [c125_repeatFlagPairsFromSeen, hPair],
              hFirst, hSecond⟩
        · rcases (ih (prior := window ++ prior)).2 hRest with
            ⟨pair, hPair, hFirst, hSecond⟩
          exact
            ⟨pair,
              by simp [c125_repeatFlagPairsFromSeen, hPair],
              hFirst, hSecond⟩

private theorem c125_pairState_strict_iff
    (pair : Bool × Bool) :
    (if pair.1 then 0 else 1) < (if pair.2 then 0 else 1) ↔
      pair.1 = true ∧ pair.2 = false := by
  cases pair with
  | mk first second =>
      cases first <;> cases second <;> simp

private theorem c125_exists_index_pairState_strict_iff
    (pairs : List (Bool × Bool)) :
    (∃ i, i < pairs.length ∧
        (if (pairs.map Prod.fst).getD i false then 0 else 1) <
          (if (pairs.map Prod.snd).getD i false then 0 else 1)) ↔
      ∃ pair ∈ pairs, pair.1 = true ∧ pair.2 = false := by
  induction pairs with
  | nil => simp
  | cons pair pairs ih =>
      constructor
      · rintro ⟨i, hi, hStrict⟩
        cases i with
        | zero =>
            refine ⟨pair, by simp, ?_⟩
            exact c125_pairState_strict_iff pair |>.1 (by simpa using hStrict)
        | succ i =>
            have hiTail : i < pairs.length := by simp at hi; omega
            have hTailStrict :
                (if (pairs.map Prod.fst).getD i false then 0 else 1) <
                  (if (pairs.map Prod.snd).getD i false then 0 else 1) := by
              simpa using hStrict
            rcases ih.mp ⟨i, hiTail, hTailStrict⟩ with
              ⟨witness, hMem, hFlags⟩
            exact ⟨witness, by simp [hMem], hFlags⟩
      · rintro ⟨witness, hMem, hFlags⟩
        simp only [List.mem_cons] at hMem
        rcases hMem with rfl | hTail
        · refine ⟨0, by simp, ?_⟩
          have hStrict := (c125_pairState_strict_iff witness).2 hFlags
          simpa using hStrict
        · rcases ih.mpr ⟨witness, hTail, hFlags⟩ with
            ⟨i, hi, hStrict⟩
          refine ⟨i + 1, by simp; omega, ?_⟩
          simpa using hStrict

private theorem c125_exists_active_state_lt_iff_crossStep
    {Token : Type}
    [DecidableEq Token]
    (trace : List (List Token)) :
    (∃ i,
        (repeatTraceParamsU trace).active i = true ∧
          persistentRepeatStateU trace i < ephemeralRepeatStateU trace i) ↔
      hasCrossStepReturn trace := by
  let pairs := c125_repeatFlagPairsFromSeen [] trace
  have hLength : pairs.length = trace.flatten.length := by
    simp [pairs]
  calc
    (∃ i,
        (repeatTraceParamsU trace).active i = true ∧
          persistentRepeatStateU trace i < ephemeralRepeatStateU trace i) ↔
        ∃ i, i < pairs.length ∧
          (if (pairs.map Prod.fst).getD i false then 0 else 1) <
            (if (pairs.map Prod.snd).getD i false then 0 else 1) := by
              simp only [repeatTraceParamsU,
                persistentRepeatStateU, ephemeralRepeatStateU,
                c125_persistentRepeatFlags, c125_ephemeralRepeatFlags]
              rw [hLength]
              constructor
              · rintro ⟨i, hi, hStrict⟩
                have hi' : i < trace.flatten.length :=
                  of_decide_eq_true hi
                have hiSum : i < (trace.map List.length).sum := by
                  simpa using hi'
                refine ⟨i, hi', ?_⟩
                simpa [pairs, hiSum] using hStrict
              · rintro ⟨i, hi, hStrict⟩
                have hiSum : i < (trace.map List.length).sum := by
                  simpa using hi
                refine ⟨i, decide_eq_true hi, ?_⟩
                simpa [pairs, hiSum] using hStrict
    _ ↔ ∃ pair ∈ pairs, pair.1 = true ∧ pair.2 = false :=
      c125_exists_index_pairState_strict_iff pairs
    _ ↔ c125_hasCrossStepReturnFromSeen [] trace := by
      exact c125_exists_strict_pair_iff_crossStepFromSeen [] trace
    _ ↔ hasCrossStepReturn trace := Iff.rfl

private theorem c125_repeatCount_lt_iff_crossStep
    {Token : Type}
    [DecidableEq Token]
    (trace : List (List Token))
    (hEphemeralSpace :
      inInfiniteActiveStateSpaceU
        (repeatTraceParamsU trace)
        (ephemeralRepeatStateU trace))
    (hPersistentEffect :
      HasInfiniteActiveGlobalLedgerEffectU
        (repeatTraceParamsU trace)
        (persistentRepeatStateU trace)
        (persistentRepeatCount trace))
    (hEphemeralEffect :
      HasInfiniteActiveGlobalLedgerEffectU
        (repeatTraceParamsU trace)
        (ephemeralRepeatStateU trace)
        (ephemeralRepeatCount trace)) :
    ephemeralRepeatCount trace < persistentRepeatCount trace ↔
      hasCrossStepReturn trace := by
  rw [hasInfiniteActiveGlobalLedgerEffectU_lt_iff_exists_active_lt_of_active_pointwise_le
    (repeatTraceParamsU trace)
    (persistentRepeatStateU trace)
    (ephemeralRepeatStateU trace)
    hEphemeralSpace
    (persistentRepeatCount trace)
    (ephemeralRepeatCount trace)
    hPersistentEffect
    hEphemeralEffect
    (fun i _ => c125_persistent_le_ephemeral trace i)]
  exact c125_exists_active_state_lt_iff_crossStep trace

private theorem c125_normalized_gap_pos_iff_count_lt
    (persistent ephemeral denominator : Nat)
    (hDenominator : 0 < denominator) :
    0 < (persistent : Rat) / (denominator : Rat) -
        (ephemeral : Rat) / (denominator : Rat) ↔
      ephemeral < persistent := by
  rw [← Rat.lt_iff_sub_pos]
  simp only [Rat.div_def]
  rw [Rat.mul_lt_mul_right
    ((Rat.inv_pos).2 ((Rat.natCast_pos).2 hDenominator))]
  exact Rat.natCast_lt_natCast

/--
Both trace states are bounded and have their named convergent ledger effects;
the persistent effect and its normalized rational advantage are strict exactly
when a token returns across a window boundary.
-/
theorem persistentEphemeralTrace_globalLedgerEffect_normalizedStrictCharacterization
    {Token : Type}
    [DecidableEq Token]
    (trace : List (List Token)) :
    inInfiniteActiveStateSpaceU
        (repeatTraceParamsU trace)
        (persistentRepeatStateU trace) ∧
    inInfiniteActiveStateSpaceU
        (repeatTraceParamsU trace)
        (ephemeralRepeatStateU trace) ∧
    HasInfiniteActiveGlobalLedgerEffectU
        (repeatTraceParamsU trace)
        (persistentRepeatStateU trace)
        (persistentRepeatCount trace) ∧
    HasInfiniteActiveGlobalLedgerEffectU
        (repeatTraceParamsU trace)
        (ephemeralRepeatStateU trace)
        (ephemeralRepeatCount trace) ∧
    (ephemeralRepeatCount trace < persistentRepeatCount trace ↔
      hasCrossStepReturn trace) ∧
    (0 < persistentEphemeralNormalizedLedgerEffectSize trace ↔
      hasCrossStepReturn trace) := by
  have hPersistentSpace := c125_persistent_stateSpace trace
  have hEphemeralSpace := c125_ephemeral_stateSpace trace
  have hPersistentEffect := c125_persistent_hasEffect trace
  have hEphemeralEffect := c125_ephemeral_hasEffect trace
  have hCount :=
    c125_repeatCount_lt_iff_crossStep
      trace hEphemeralSpace hPersistentEffect hEphemeralEffect
  have hDenominator : 0 < repeatTraceDenominator trace := by
    unfold repeatTraceDenominator
    omega
  have hNormalized :
      0 < persistentEphemeralNormalizedLedgerEffectSize trace ↔
        ephemeralRepeatCount trace < persistentRepeatCount trace := by
    unfold persistentEphemeralNormalizedLedgerEffectSize
    unfold persistentNormalizedRepeatScore ephemeralNormalizedRepeatScore
    exact
      c125_normalized_gap_pos_iff_count_lt
        (persistentRepeatCount trace)
        (ephemeralRepeatCount trace)
        (repeatTraceDenominator trace)
        hDenominator
  exact
    ⟨hPersistentSpace, hEphemeralSpace, hPersistentEffect,
      hEphemeralEffect, hCount, hNormalized.trans hCount⟩

/-- Two equal singleton windows have a positive normalized persistent gap. -/
theorem repeatedSingletonTrace_has_positive_normalizedLedgerEffectSize :
    0 <
      persistentEphemeralNormalizedLedgerEffectSize
        ([[0], [0]] : List (List Nat)) := by
  apply
    (persistentEphemeralTrace_globalLedgerEffect_normalizedStrictCharacterization
      ([[0], [0]] : List (List Nat))).2.2.2.2.2.2
  simp [hasCrossStepReturn, c125_hasCrossStepReturnFromSeen]

end UnrestrictedBridge
end VFH2
