# C20 Impact Report: Score Boundedness Source Audit

## Summary

C20 audits whether the current VF-H2 codebase already contains a natural source
for deriving score boundedness for a non-constant product score.

This is an audit milestone, not a new Lean theorem milestone.

## Current formal position

C19 generalized the constructed fixed-state route from constant scores to any
score satisfying two assumptions:

```lean
productScoreInactiveInsensitive p productScore
productScoreBoundedBy p productScore thresholdLo thresholdHi
```

This removed the constant-score restriction but retained boundedness as an
explicit assumption.

## Audit finding

The current codebase contains:

- the constant score construction `constantProductScore p c`;
- inactive-insensitivity for the constant score;
- a general inactive-insensitive score preservation route;
- multiple threshold/window/bridge lemmas involving `thresholdLo`, `thresholdHi`,
  `baseEffect`, and updated-score targets;
- the C19 theorem for constructed fixed states and arbitrary bounded
  inactive-insensitive scores.

However, the audit does not identify a non-trivial constructed score class whose
boundedness is already derived globally as:

```lean
productScoreBoundedBy p productScore thresholdLo thresholdHi
```

The existing threshold/window lemmas mostly discharge target-window obligations
or update-point obligations. They do not yet provide a reusable global boundedness
source for arbitrary states.

## Scientific interpretation

C20 should therefore be recorded as a source-gap audit.

It would be premature to add a theorem claiming a naturally bounded non-constant
score unless a concrete score construction and a derived global boundedness lemma
are first introduced.

## Assumption status

C20 does not reduce a Lean assumption.

It clarifies that the next real assumption-reduction target is the boundedness
assumption introduced in C19:

```lean
productScoreBoundedBy p productScore thresholdLo thresholdHi
```

## Recommended C21 target

C21 should introduce a conservative non-constant score construction or a bounded
score certificate structure.

A safe target is one of the following:

1. A constructed non-constant score with derived inactive-insensitivity and
   derived global boundedness.
2. A bounded score certificate record that packages a score with its
   inactive-insensitivity and boundedness proofs.
3. A bridge from existing local target-window lemmas to a clearly stated global
   boundedness condition, if such a bridge is mathematically justified.

The preferred path is option 2 if no natural non-constant score is available yet,
because it improves proof architecture without pretending that boundedness has
been derived from nowhere.
