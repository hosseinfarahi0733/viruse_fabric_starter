from __future__ import annotations

from viruse_fabric.writing.safe_abstract_toy_scientific_gap_and_evidence_upgrade_register import (
    SafeAbstractToyScientificGapAndEvidenceUpgradeRegisterBuilder,
)


def main() -> None:
    builder = SafeAbstractToyScientificGapAndEvidenceUpgradeRegisterBuilder()
    report = builder.run()
    counters = report["counters"]

    assert report["passed"] is True
    assert report["scope"] == "scientific-gap-and-evidence-upgrade-register-only"
    assert report["register_phrase"] == "scientific_gaps_registered_but_no_evidence_upgrade_completed"

    assert report["application_permission_granted"] is False
    assert report["application_execution_performed"] is False
    assert report["checklist_completion_performed"] is False
    assert report["checklist_execution_performed"] is False
    assert report["manuscript_file_modified"] is False
    assert report["manuscript_mutation"] is False
    assert report["evidence_upgrade_completed"] is False
    assert report["applied_patch_count"] == 0

    assert counters["Toy scientific gap register item count"] == 12
    assert counters["Toy scientific gap P0 count"] == 6
    assert counters["Toy scientific gap P1 count"] == 4
    assert counters["Toy scientific gap P2 count"] == 1
    assert counters["Toy scientific gap P3 count"] == 1
    assert counters["Toy scientific evidence upgrade completed count"] == 0

    assert counters["Toy scientific gap register source assembly section count"] == 9
    assert counters["Toy scientific gap register source audit pass count"] == 11
    assert counters["Toy scientific gap register source audit failure count"] == 0

    gap_text = " ".join(
        item["gap_family"] + " " + item["current_gap"] + " " + item["boundary_note"]
        for item in report["gap_items"]
    )

    for phrase in [
        "Citation integration",
        "Synthetic toy evaluation design",
        "Toy evaluation metrics",
        "Coherence and narrative",
        "Contribution sharpening",
        "Related work positioning",
        "Limitations balance",
        "Proof pathway",
        "External validation",
        "Submission readiness",
        "Reproducibility package",
        "Manuscript mutation gate",
    ]:
        assert phrase in gap_text, f"Missing gap family phrase: {phrase}"

    must_be_zero = [
        "Toy manuscript patch application checklist completion count",
        "Toy manuscript patch application checklist execution count",
        "Toy manuscript patch application permission count",
        "Toy manuscript patch application applied patch count",
        "Toy manuscript patch application manuscript file modified count",
        "Toy manuscript patch application manuscript mutation count",
        "Real biological dataset import count",
        "Real pathogen simulation count",
        "Real receptor parameter count",
        "Operational host targeting count",
        "Wet-lab protocol count",
        "Actionable biosafety-risk instruction count",
        "Real-world infectivity optimization count",
        "Immune evasion optimization count",
        "Real host range prediction count",
        "Proof assistant verification count",
        "External validation count",
        "Independent experiment count",
        "Manuscript submission ready count",
        "Readiness approval count",
        "New citation added count",
    ]

    for name in must_be_zero:
        assert counters[name] == 0, f"Expected zero counter for {name}, got {counters[name]}"

    print("V8_216_SAFE_ABSTRACT_TOY_SCIENTIFIC_GAP_AND_EVIDENCE_UPGRADE_REGISTER_OK")
    print("TOY_SCIENTIFIC_GAP_AND_EVIDENCE_UPGRADE_REGISTER_DIRECT_CHECK_OK")
    print(f"Gap item count: {counters['Toy scientific gap register item count']}")
    print(f"P0 count: {counters['Toy scientific gap P0 count']}")
    print(f"P1 count: {counters['Toy scientific gap P1 count']}")
    print(f"P2 count: {counters['Toy scientific gap P2 count']}")
    print(f"P3 count: {counters['Toy scientific gap P3 count']}")
    print(f"Evidence upgrade completed count: {counters['Toy scientific evidence upgrade completed count']}")
    print(f"Source assembly section count: {counters['Toy scientific gap register source assembly section count']}")
    print(f"Source audit pass count: {counters['Toy scientific gap register source audit pass count']}")
    print(f"Source audit failure count: {counters['Toy scientific gap register source audit failure count']}")
    print(f"Checklist completion count: {counters['Toy manuscript patch application checklist completion count']}")
    print(f"Checklist execution count: {counters['Toy manuscript patch application checklist execution count']}")
    print(f"Application permission count: {counters['Toy manuscript patch application permission count']}")
    print(f"Applied patch count: {counters['Toy manuscript patch application applied patch count']}")
    print(f"Manuscript mutation count: {counters['Toy manuscript patch application manuscript mutation count']}")
    print(f"Manuscript submission ready count: {counters['Manuscript submission ready count']}")
    print(f"Readiness approval count: {counters['Readiness approval count']}")
    print(f"External validation count: {counters['External validation count']}")
    print(f"Independent experiment count: {counters['Independent experiment count']}")
    print(f"Proof assistant verification count: {counters['Proof assistant verification count']}")
    print(f"New citation added count: {counters['New citation added count']}")
    print(f"Passed: {report['passed']}")


if __name__ == "__main__":
    main()
