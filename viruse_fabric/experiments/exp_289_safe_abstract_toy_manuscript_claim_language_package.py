from __future__ import annotations

from viruse_fabric.writing.safe_abstract_toy_manuscript_claim_language_package import (
    SafeAbstractToyManuscriptClaimLanguagePackageBuilder,
)


def main() -> None:
    builder = SafeAbstractToyManuscriptClaimLanguagePackageBuilder()
    report = builder.run()
    counters = report["counters"]

    assert report["passed"] is True
    assert report["scope"] == "claim-language-package-only"
    assert report["package_phrase"] == "safe_claim_language_packaged_but_no_readiness_or_real_bio_claims"

    assert counters["Toy manuscript claim language package safe language item count"] == 8
    assert counters["Toy manuscript claim language package blocked language item count"] == 9
    assert counters["Toy manuscript claim language package source allowed claim count"] == 4
    assert counters["Toy manuscript claim language package source deferred claim count"] == 3
    assert counters["Toy manuscript claim language package source prohibited claim count"] == 2

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

    print("V8_209_SAFE_ABSTRACT_TOY_MANUSCRIPT_CLAIM_LANGUAGE_PACKAGE_OK")
    print("TOY_MANUSCRIPT_CLAIM_LANGUAGE_PACKAGE_DIRECT_CHECK_OK")
    print(f"Safe language item count: {counters['Toy manuscript claim language package safe language item count']}")
    print(f"Blocked language item count: {counters['Toy manuscript claim language package blocked language item count']}")
    print(f"Source allowed claim count: {counters['Toy manuscript claim language package source allowed claim count']}")
    print(f"Source deferred claim count: {counters['Toy manuscript claim language package source deferred claim count']}")
    print(f"Source prohibited claim count: {counters['Toy manuscript claim language package source prohibited claim count']}")
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
