from __future__ import annotations

from viruse_fabric.writing.safe_abstract_toy_manuscript_assembly_preview_package import (
    SafeAbstractToyManuscriptAssemblyPreviewPackageBuilder,
)


def main() -> None:
    builder = SafeAbstractToyManuscriptAssemblyPreviewPackageBuilder()
    report = builder.run()
    counters = report["counters"]

    assert report["passed"] is True
    assert report["scope"] == "manuscript-assembly-preview-package-only"
    assert report["package_phrase"] == "safe_manuscript_assembly_preview_packaged_but_no_manuscript_file_modified"

    assert report["application_permission_granted"] is False
    assert report["application_execution_performed"] is False
    assert report["checklist_completion_performed"] is False
    assert report["checklist_execution_performed"] is False
    assert report["manuscript_file_modified"] is False
    assert report["manuscript_mutation"] is False
    assert report["applied_patch_count"] == 0

    assert counters["Toy manuscript assembly preview section count"] == 9
    assert counters["Toy manuscript assembly preview source draft item count"] == 9
    assert counters["Toy manuscript assembly preview source audit item count"] == 11
    assert counters["Toy manuscript assembly preview source audit pass count"] == 11
    assert counters["Toy manuscript assembly preview source audit failure count"] == 0

    for phrase in [
        "internally audited, safety-bounded, safe abstract toy-only governance pipeline",
        "does not import real biological datasets",
        "does not model real pathogens",
        "zero applied patches",
        "does not establish external validation",
        "Future work may only introduce stronger claims",
    ]:
        assert phrase in report["assembled_text"], f"Missing required phrase: {phrase}"

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

    print("V8_215_SAFE_ABSTRACT_TOY_MANUSCRIPT_ASSEMBLY_PREVIEW_PACKAGE_OK")
    print("TOY_MANUSCRIPT_ASSEMBLY_PREVIEW_PACKAGE_DIRECT_CHECK_OK")
    print(f"Assembly preview section count: {counters['Toy manuscript assembly preview section count']}")
    print(f"Source draft item count: {counters['Toy manuscript assembly preview source draft item count']}")
    print(f"Source audit item count: {counters['Toy manuscript assembly preview source audit item count']}")
    print(f"Source audit pass count: {counters['Toy manuscript assembly preview source audit pass count']}")
    print(f"Source audit failure count: {counters['Toy manuscript assembly preview source audit failure count']}")
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
