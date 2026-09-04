# C139 ImmPort public-metadata audit

## Result

`INSUFFICIENT_EVIDENCE` — fitting is not authorized.

This milestone audits the frozen nine-study candidate set against the empirical
gate agreed after C138. It contains public aggregate metadata only. It contains
no real participant or sample identifiers, assay matrices, HAI measurements,
fitted models, selected features, tuned parameters, or performance results.
Synthetic identifier/value sentinels occur only in fail-closed parser tests.
Replay is offline and does not contact ImmPort, GEO, or any other service.

The negative gate is substantive:

- the preferred replication cohort, `SDY1119_TIV_2011`, has an upper bound of
  34 potentially complete subjects (the ImmPort D3 assay count) and cannot reach
  the predeclared replication minimum of 50;
- the fallback, `SDY180_FLUZONE_2009_2010`, has a potentially complete-subject
  upper bound of 12 from groups 1 and 2; the additional influenza group 3 has
  D0/D1/D28 visits but no visit in the required D5-9 window;
- `SDY520_TIV_2013` and `SDY640_TIV_2014` also have
  complete-subject upper bounds below the per-cohort minimum of 25;
- even after treating every size-capable unresolved discovery candidate as if
  all remaining criteria succeeded, the optimistic discovery upper bound is
  177 with the preferred replication held out, or 211 with the fallback held
  out. Both are below 250.

The conservative whole-arm bound for SDY269 is 28 from the TIV enrollment in
the GEO GSE29617 design. For SDY1119 it is 34 from the ImmPort D3 assay count.
The smaller GEO title intersections (24 and 33 respectively) describe those
GEO series, not necessarily the entire deposited ImmPort arm, and are not used
as the gate ceilings. No individual labels or sample titles are retained in
the versioned artifacts. All nine bounds are potentially complete-subject
ceilings, not confirmed same-subject or HAI-complete counts.

SDY400 uses the conservative upper bound 31 from the deposited ImmPort design
counts, rechecked on 2026-09-04. The publication and GEO report 30 participants;
ImmPort reports 31 assay entries per epoch. The cause of this discrepancy is
unresolved. The ceiling 31 does not establish 31 distinct participants.
The same-subject complete count and exact early-window eligibility remain
unresolved. The manifest records the publication/GEO-versus-ImmPort difference.

Enrollment and assay-sample counts are never treated as complete-subject
counts. A cohort is `ELIGIBLE` only when every required criterion and the
same-subject intersection are confirmed. Missing overlap evidence is not
treated as evidence of disjointness.
An unresolved size is never replaced by zero: a numeric optimistic discovery
upper bound is reported only when all relevant upper bounds are known.

## Frozen contract

The manifest fixes these thresholds without weakening them:

- at least 25 complete subjects per cohort;
- at least five discovery cohort-seasons from at least three recruitment
  institutions;
- at least 250 complete discovery subjects;
- at least 50 complete subjects in an independent replication cohort;
- at least 80% simulated power for a 5% MSE improvement after the estimand and
  simulation contract are frozen.

The allowed windows are D0, D1–3, D7±2, and HAI D28–35. Selection is frozen to
the nearest target day D0, D1, D7, or D28 respectively; distance ties use the
earlier day, then the lexicographically first accession. The preferred
replication is SDY1119 and the only predeclared fallback is SDY180.

C139 v1 has no executable simulation-evidence contract. It therefore requires
power to remain `NOT_EVALUATED`, marks the power check false, and cannot
authorize fitting even in a synthetic manifest that clears every metadata
capacity check. A later milestone must freeze and verify the estimand and power
simulation independently.

## Evidence and provenance boundary

The manifest cites the public ImmPort search and study-design views, public GEO
series pages, and the peer-reviewed Immune Signatures resource. ImmPort's public
metadata currently exposes two release labels: study records report DR58 while
the search index identifies itself as `study_mapping_common_dr67`. C139 keeps
that conflict explicit.

Upstream response bytes are not archived in this repository, so C139 does not
claim checksum-verifiable snapshots of those external pages. `SHA256SUMS`
protects the nine versioned C139 artifacts themselves. A future source refresh
must create a new version instead of silently changing v1.
The audit identity, source inventory, retrieval date, exact source URLs, and
cohort-to-GEO mappings are pinned. Study-specific evidence cannot cite another
cohort's sources, and policy documentation cannot substitute for study data.
Committed-mode verification rejects later changes to these v1 artifacts.

The C139 implementation performed no authenticated ImmPort download. This is a
claim about the implementation and replay path only; it does not attest all
prior human, browser, or unrelated process access on the machine.
The parser rejects known identifier, measurement, credential, and encoded-blob
patterns. It is not a general deidentification algorithm and cannot establish
the truth of an evidence assertion from a citation alone; the frozen manifest
also requires independent source and content review.

Primary references:

- [ImmPort study search API](https://docs.immport.org/apidocumentation/shareddataapi/search/)
- [ImmPort study-detail API](https://docs.immport.org/apidocumentation/shareddataapi/studydetail/)
- [ImmPort download and authentication guide](https://docs.immport.org/download/)
- [ImmPort data-management and sharing guidance](https://docs.immport.org/documents/dmsp/ImmPort_Data_Management_and_Sharing_Plan_Template_v1.pdf)
- [Immune Signatures public resource](https://pmc.ncbi.nlm.nih.gov/articles/PMC9584267/)

## Reproduction

From the repository root with Python 3.12 and Lean 4.31.0:

```bash
bash scripts/verify_c139.sh
```

The verifier checks the exact milestone boundary, strict/canonical JSON,
fail-closed parser tests, synthetic non-power capacity cases, byte-stable CLI
output, all earlier Python tests, artifact checksums, the full Lean build, the
aggregate Product compile, front-door hygiene, and repository-state stability.

## Claim boundary and next action

C139 does not show that VF-H2 is empirically false, that all ImmPort data are
inadequate, or that any biological or causal effect exists or does not exist.
It shows only that this frozen candidate set cannot satisfy the predeclared
discovery and replication capacity gates.

C140 preregistration, fitting, and C141 discovery remain closed. The next
scientifically valid action is a new, separately versioned candidate-set audit
that identifies both an independent replication cohort with at least 50
complete subjects and a discovery pool with an optimistic bound of at least 250
before any outcome values are inspected. Passing that metadata-capacity audit
would still not authorize fitting until a separate, frozen power-simulation
contract passes. Thresholds must not be lowered to rescue the branch.
