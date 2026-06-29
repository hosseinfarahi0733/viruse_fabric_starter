from __future__ import annotations

from viruse_fabric.writing.safe_abstract_toy_manuscript_patch_application_decision_ledger_audit import (
    SafeAbstractToyManuscriptPatchApplicationDecisionLedgerAuditBuilder,
)


def main() -> None:
    builder = SafeAbstractToyManuscriptPatchApplicationDecisionLedgerAuditBuilder()
    report = builder.run()
    counters = report["counters"]

    assert report["passed"] is True
    assert report["scope"] == "audit-only"
    assert report["application_permission_granted"] is False
    assert report["application_execution_performed"] is False
    assert report["checklist_completion_performed"] is False
    assert report["checklist_execution_performed"] is False
    assert report["manuscript_file_modified"] is False
    assert report["manuscript_mutation"] is False
    assert report["applied_patch_count"] == 0

    assert counters["Toy manuscript patch application decision ledger audit item count"] == 9
    assert counters["Toy manuscript patch application decision ledger audit pass count"] == 9
    assert counters["Toy manuscript patch application decision ledger audit failure count"] == 0

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

    print("V8_205_SAFE_ABSTRACT_TOY_MANUSCRIPT_PATCH_APPLICATION_DECISION_LEDGER_AUDIT_OK")
    print("TOY_MANUSCRIPT_PATCH_APPLICATION_DECISION_LEDGER_AUDIT_DIRECT_CHECK_OK")
    print(f"Audit items: {counters['Toy manuscript patch application decision ledger audit item count']}")
    print(f"Audit pass count: {counters['Toy manuscript patch application decision ledger audit pass count']}")
    print(f"Audit failure count: {counters['Toy manuscript patch application decision ledger audit failure count']}")
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
