# Manuscript Integration Plan v3.6

## Purpose

This plan defines how the v3.4 Related Work and Positioning Scaffold and the v3.5 Formal Notation Scaffold should be integrated into the v3.2 full manuscript draft. It also responds to the v3.3 manuscript quality audit warnings. The goal is not to produce a final paper in this step. The goal is to create a controlled revision map so the manuscript can be improved without turning into a stitched-together academic creature with too many elbows.

## Source Artifact Inventory

| Artifact | Path | Role | Present |
|---|---|---|---|
| Full Manuscript Draft v3.2 | `outputs/full_manuscript_draft_v3_2.md` | Base manuscript draft to be revised. | True |
| Manuscript Quality Audit v3.3 | `outputs/manuscript_quality_audit_v3_3.md` | Quality gate that identifies remaining manuscript weaknesses. | True |
| Related Work and Positioning Scaffold v3.4 | `outputs/related_work_positioning_v3_4.md` | Positioning material for related work, constraint clarification, and conceptual neighbors. | True |
| Formal Notation Scaffold v3.5 | `outputs/formal_notation_scaffold_v3_5.md` | Symbolic vocabulary for the formal model section. | True |

## Integration Map

| Target manuscript section | Source | Action | Rationale | Expected effect |
|---|---|---|---|---|
| Abstract | v3.4 and v3.5 | Add one sentence clarifying that constraints shape possible paths and one sentence stating that the notation is manuscript-facing rather than proof-level. | The abstract currently needs to signal both conceptual clarity and formal caution before readers reach the body. | Reduces risk of teleological or over-formal interpretation at the opening. |
| Introduction | v3.4 | Insert a plain-language explanation of constraint geometry after the causal-chain contrast. | Readers must understand constraint before they can understand apparent intentionality. | Makes the core thesis easier to read without weakening its originality. |
| Related Work and Positioning | v3.4 | Add a new manuscript section between Introduction and Core Thesis using the seven conceptual neighbor families. | The v3.3 audit identified missing related work as a manuscript weakness. | Addresses the related-work gap while avoiding fake citations. |
| Core Thesis | v3.4 | Add a compact statement: apparent purpose can emerge when constraint-shaped paths are read through observer projection. | The thesis needs a precise bridge between constraint geometry and apparent intentionality. | Improves conceptual continuity between thesis and model. |
| Formal Model | v3.5 | Insert the scaffold object F = (C, P, A, O), then define C, P, A, O before discussing validation. | The manuscript needs symbolic structure before presenting technical claims. | Addresses the formal-notation warning from v3.3. |
| Formal Model | v3.5 | Add K(p, C), alpha(p, A), I_app, I_false, R(I_app), and Delta_R as working notation. | The model needs explicit handles for compatibility, attractor concentration, observer projection, false intentionality, and correction. | Makes later validation claims easier to connect to model terms. |
| Validation Sequence | v3.3 and v3.5 | Add a short bridge explaining how the validation experiments map onto the formal symbols. | The validation sequence should not feel disconnected from the new notation. | Improves manuscript coherence between model and results. |
| Results | v3.3 | Convert the validation outcomes into a compact table with milestone, metric, and interpretation columns. | The quality audit recommended better readability for validation results. | Makes the evidence easier to review and reduces narrative clutter. |
| Limitations | v3.3, v3.4, and v3.5 | Preserve explicit boundaries: no external validation, no real pathogens, no real hosts, no biological protocols, no laboratory procedures, and no executable interventions. | The manuscript must keep its safety and evidence limits visible. | Keeps the project inside research-prototype boundaries. |
| Future Work | v3.4 and v3.5 | Add three future tasks: real citation work, deeper formalization, and external validation design. | The next steps should follow from current weaknesses rather than from ambition fog. | Turns audit warnings into a concrete research path. |
| Conclusion | v3.3, v3.4, and v3.5 | Restate the bounded claim: Viruse Fabric is a conceptual-computational prototype with internal validation and a first symbolic scaffold. | The conclusion should end with defensible scope, not victory music. | Prevents the final paragraph from overclaiming. |

## Warning Reduction Plan

The v3.3 audit produced three manuscript-level warnings. This plan does not pretend they disappear by being named, which would be very human and very useless. Instead, each warning gets a concrete integration response.

| Warning code | Source warning | Integration response | Status after plan |
|---|---|---|---|
| needs_related_work | The v3.3 quality audit identified missing related work. | Use v3.4 as a Related Work and Positioning section scaffold. | Addressed by planned manuscript insertion, but real citations remain pending. |
| needs_formal_notation | The v3.3 quality audit identified missing formal notation. | Use v3.5 to revise the Formal Model section with F = (C, P, A, O) and related symbols. | Addressed at scaffold level, but not yet proof-level. |
| draft_not_submission_ready | The v3.3 quality audit warned that the draft is not submission-ready. | Keep submission readiness unresolved until related work, formal notation, and quality audit are integrated into a revised draft. | Still open. The integration plan reduces risk but does not make the manuscript submission-ready. |

## Formal Model Insertion

The Formal Model section should introduce the scaffold object:

```text
F = (C, P, A, O)
```

where `C` is the constraint set, `P` is the path space, `A` is the constructive attractor set, and `O` is observer projection.

This notation should be presented as a scaffold, not as a final proof. The manuscript should explicitly say that compatibility `K(p, C)`, attractor concentration `alpha(p, A)`, apparent intentionality `I_app`, false intentionality `I_false`, and correction `R(I_app)` are working terms for technical review.

## Related Work Insertion

The Related Work and Positioning section should use the seven families from v3.4: causal-chain models, network causality, dynamical systems, constraint-based explanation, observer-dependent interpretation, teleology and apparent purpose, and model validation frameworks.

Because the scaffold does not provide real citations, the manuscript must mark this section as a positioning scaffold until real sources are selected and read. The point is to orient the manuscript, not to fake scholarship. Humanity has enough ways to do that already.

## Revision Order

The safest revision order is:

1. Preserve the v3.2 manuscript as the base.
2. Insert Related Work and Positioning after the Introduction.
3. Rewrite the Formal Model section using the v3.5 notation.
4. Add a validation mapping paragraph that connects experiments to notation.
5. Convert the Results section into a compact validation table.
6. Strengthen Limitations and Research Boundary language.
7. Update the Conclusion with the bounded v3.5 status.
8. Run a new quality audit.

## Manuscript Boundaries

- This plan does not rewrite the full manuscript yet.
- This plan does not provide real citations.
- This plan does not establish peer review.
- This plan does not establish external validation.
- This plan does not model real pathogens or real hosts.
- This plan does not support biological protocols, laboratory procedures, or executable interventions.
- This plan does not support strong public claims.
- This plan is a manuscript revision map, not a final paper.

## Next Actions

- Create an integrated manuscript draft using v3.2 as the base.
- Insert the v3.4 related-work section with citation placeholders clearly marked.
- Insert the v3.5 formal notation into the Formal Model section.
- Convert validation results into a compact table.
- Run a new manuscript quality audit after integration.
- Keep the manuscript status as cautious technical review only.

## Integration Status

After this plan, the manuscript is better prepared for an integrated revision, but it is still not submission-ready. The next milestone should generate an integrated manuscript draft and then rerun quality checks. The proper status remains: research prototype with internal validation, manuscript-facing scaffolds, and no external validation.
