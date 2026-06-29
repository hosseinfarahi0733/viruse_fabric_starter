from __future__ import annotations

from viruse_fabric.writing.safe_abstract_toy_manuscript_patch_application_decision_ledger import (
    SafeAbstractToyManuscriptPatchApplicationDecisionLedgerBuilder,
)


def main() -> None:
    builder = SafeAbstractToyManuscriptPatchApplicationDecisionLedgerBuilder()
    report = builder.run()
    counters = report["counters"]

    assert report["passed"] is True
    assert report["scope"] == "decision-record-only"
    assert report["application_permission_granted"] is False
    assert report["application_execution_performed"] is False
    assert report["checklist_completion_performed"] is False
    assert report["checklist_execution_performed"] is False
    assert report["manuscript_file_modified"] is False
    assert report["manuscript_mutation"] is False
    assert report["applied_patch_count"] == 0

    assert counters["Safe abstract toy manuscript patch application decision ledger count"] == 1
    assert counters["New safe abstract toy manuscript patch application decision ledger count"] == 1
    assert counters["Toy manuscript patch application decision ledger JSON export count"] == 1
    assert counters["Toy manuscript patch application decision ledger item count"] == 9
    assert counters["Toy manuscript patch application decision ledger accepted decision count"] == 9
    assert counters["Toy manuscript patch application decision ledger rejected decision count"] == 0
    assert counters["Toy manuscript patch application decision ledger execution count"] == 1
    assert counters["Toy manuscript patch application checklist completion count"] == 0
    assert counters["Toy manuscript patch application checklist execution count"] == 0
    assert counters["Toy manuscript patch application permission count"] == 0
    assert counters["Toy manuscript patch application applied patch count"] == 0
    assert counters["Toy manuscript patch application manuscript file modified count"] == 0
    assert counters["Toy manuscript patch application manuscript mutation count"] == 0
    assert counters["Toy manuscript patch application decision ledger non-readiness disclaimer count"] == 1
    assert counters["Toy manuscript patch application decision ledger boundary note count"] == 9
    assert counters["Toy manuscript patch application decision ledger direct execution count"] == 1

    assert counters["Real biological dataset import count"] == 0
    assert counters["Real pathogen simulation count"] == 0
    assert counters["Real receptor parameter count"] == 0
    assert counters["Operational host targeting count"] == 0
    assert counters["Wet-lab protocol count"] == 0
    assert counters["Actionable biosafety-risk instruction count"] == 0
    assert counters["Real-world infectivity optimization count"] == 0
    assert counters["Immune evasion optimization count"] == 0
    assert counters["Real host range prediction count"] == 0
    assert counters["Proof assistant verification count"] == 0
    assert counters["External validation count"] == 0
    assert counters["Independent experiment count"] == 0
    assert counters["Manuscript submission ready count"] == 0
    assert counters["Readiness approval count"] == 0
    assert counters["New citation added count"] == 0

    print("V8_204_SAFE_ABSTRACT_TOY_MANUSCRIPT_PATCH_APPLICATION_DECISION_LEDGER_OK")
    print("TOY_MANUSCRIPT_PATCH_APPLICATION_DECISION_LEDGER_DIRECT_CHECK_OK")
    print(f"Decision ledger items: {counters['Toy manuscript patch application decision ledger item count']}")
    print(f"Accepted decisions: {counters['Toy manuscript patch application decision ledger accepted decision count']}")
    print(f"Rejected decisions: {counters['Toy manuscript patch application decision ledger rejected decision count']}")
    print(f"Checklist completion count: {counters['Toy manuscript patch application checklist completion count']}")
    print(f"Checklist execution count: {counters['Toy manuscript patch application checklist execution count']}")
    print(f"Application permission count: {counters['Toy manuscript patch application permission count']}")
    print(f"Applied patch count: {counters['Toy manuscript patch application applied patch count']}")
    print(f"Manuscript file modified count: {counters['Toy manuscript patch application manuscript file modified count']}")
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
