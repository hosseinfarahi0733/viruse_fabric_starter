# Viruse Fabric Public Demo Package v2.3

## What this demo is

This report is a public entry point for Viruse Fabric. It summarizes the current milestones, generated artifacts, safety boundary, and recommended inspection order.

Viruse Fabric's current core claim is:

> Causality is not a chain; it is a geometry of constraints.

> علیت زنجیره نیست؛ هندسه‌ی قیود است.

## Recommended inspection order

1. Read `outputs/theory_manifest_v2_0.md`.
2. Read `outputs/scenario_stress_report_v2_2.md`.
3. Open `outputs/fabric_diagram_v2_1.png`.
4. Read `outputs/visual_explanation_report_v2_1.md`.
5. Inspect `outputs/theory_chapter_fa_v1_8.md` or `outputs/theory_chapter_v1_7.md`.
6. Check `notes/theory_log.md` for version history.

## Milestones

| Version | Title | Experiment | Main output | Summary |
|---|---|---|---|---|
| v1.7.0 | English Theory Chapter Exporter | `python -m viruse_fabric.experiments.exp_17_theory_chapter_exporter` | `outputs/theory_chapter_v1_7.md` | Exports an English manuscript-facing theory chapter from simulation results. |
| v1.8.0 | Persian Theory Chapter Exporter | `python -m viruse_fabric.experiments.exp_18_persian_theory_chapter_exporter` | `outputs/theory_chapter_fa_v1_8.md` | Exports a Persian theory chapter with safe conceptual boundaries. |
| v1.9.0 | Bilingual Quality Audit | `python -m viruse_fabric.experiments.exp_19_bilingual_quality_audit` | `outputs/bilingual_quality_report_v1_9.md` | Adds a bilingual glossary and an automated quality gate for manuscript outputs. |
| v2.0.0 | Theory Manifest | `python -m viruse_fabric.experiments.exp_20_theory_manifest` | `outputs/theory_manifest_v2_0.md` | States the theory claims, limits, evidence, safety boundary, and open weak points. |
| v2.1.0 | Visual Explanation Layer | `python -m viruse_fabric.experiments.exp_21_visual_explanation` | `outputs/visual_explanation_report_v2_1.md` | Renders a diagram and report connecting paths, attractors, targeting, and observer misreading. |
| v2.2.0 | Scenario Stress Tests | `python -m viruse_fabric.experiments.exp_22_scenario_stress_tests` | `outputs/scenario_stress_report_v2_2.md` | Checks whether the model rejects broken scenarios without flattening valid ones. |
| v2.3.0 | Public Demo Package | `python -m viruse_fabric.experiments.exp_23_public_demo_package` | `outputs/public_demo_report_v2_3.md` | Provides a public-facing entry point for milestones, outputs, safety boundary, and current limits. |

## Artifacts

| Artifact | Type | Path | Size bytes | Purpose |
|---|---|---|---:|---|
| English theory chapter | markdown | `outputs/theory_chapter_v1_7.md` | 9658 | English manuscript-facing theory output. |
| Persian theory chapter | markdown | `outputs/theory_chapter_fa_v1_8.md` | 14434 | Persian manuscript-facing theory output. |
| Bilingual quality report | markdown | `outputs/bilingual_quality_report_v1_9.md` | 2122 | Quality gate report for Persian chapter and glossary. |
| Theory manifest | markdown | `outputs/theory_manifest_v2_0.md` | 8839 | Boundary document for claims, evidence, limits, and weaknesses. |
| Visual explanation diagram | image | `outputs/fabric_diagram_v2_1.png` | 166769 | Diagram of route structure, attractor roles, and disrupted paths. |
| Visual explanation report | markdown | `outputs/visual_explanation_report_v2_1.md` | 2061 | Report explaining the visual layer. |
| Scenario stress report | markdown | `outputs/scenario_stress_report_v2_2.md` | 2104 | Internal stress-test report. |
| Theory log | markdown | `notes/theory_log.md` | 31017 | Versioned theoretical development log. |

## Missing required artifacts

No missing required artifacts.

## Safety boundary

This project is conceptual and non-operational. It does not provide real pathogens, real hosts, doses, receptors, laboratory protocols, executable biological procedures, or deployable interventions.

## What this project does not yet prove

- It does not provide external empirical validation yet.
- It does not prove that the current formulas are final.
- It does not predict real biological outcomes.
- It does not convert abstract biological language into executable biological procedure.
- It does not claim that apparent targeting is real intention.

## Demo commands

```bash
python -m viruse_fabric.experiments.exp_20_theory_manifest
python -m viruse_fabric.experiments.exp_21_visual_explanation
python -m viruse_fabric.experiments.exp_22_scenario_stress_tests
```

## Interpretation

The project is currently strongest as a conceptual-computational theory-building system. Its next weakness is public readability: a new reader still needs guidance. This demo package is the first entry point that reduces that friction.
