from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from viruse_fabric.biology.apparent_targeting import ApparentTargetingAnalyzer
from viruse_fabric.biology.viral_scenarios import ViralPatternScenario
from viruse_fabric.geometry.attractor_classifier import AttractorTypeClassifier


Severity = Literal["info", "low", "medium", "high"]
AuditStatus = Literal["pass", "warning", "fail"]


@dataclass
class AuditFinding:
    scenario_name: str
    category: str
    severity: Severity
    message: str
    evidence: str
    recommendation: str


@dataclass
class ScenarioAuditResult:
    scenario_name: str
    status: AuditStatus
    score: float
    path: list[str]
    constructive_nodes: list[str]
    tension_wells: list[str]
    strained_gateways: list[str]
    findings: list[AuditFinding]

    @property
    def finding_count(self) -> int:
        return len(self.findings)


@dataclass
class ScenarioAuditReport:
    results: list[ScenarioAuditResult]
    global_findings: list[AuditFinding]

    @property
    def status(self) -> AuditStatus:
        severities = [
            finding.severity
            for result in self.results
            for finding in result.findings
        ] + [finding.severity for finding in self.global_findings]

        if "high" in severities:
            return "fail"
        if "medium" in severities or "low" in severities:
            return "warning"
        return "pass"

    @property
    def passed(self) -> bool:
        return self.status == "pass"

    @property
    def total_findings(self) -> int:
        return sum(result.finding_count for result in self.results) + len(self.global_findings)

    @property
    def interpretation(self) -> str:
        if self.status == "pass":
            return "scenario layer is safe and internally consistent"
        if self.status == "warning":
            return "scenario layer is usable but needs minor theoretical or wording corrections"
        return "scenario layer should not be used until safety or consistency failures are corrected"


class ScenarioSafetyConsistencyAuditor:
    """Audit scenario safety and internal consistency.

    This is not a biological risk model.
    It is a guardrail for our own abstraction layer.

    The auditor asks:
    - Did we accidentally write operational biological content?
    - Do safety notes still make clear that this is conceptual?
    - Do targeting scores match attractor roles?

    Apparently even theories need adult supervision.
    """

    def __init__(self) -> None:
        self.targeting_analyzer = ApparentTargetingAnalyzer()
        self.classifier = AttractorTypeClassifier()

        self.operational_red_flags = [
            "moi",
            "multiplicity of infection",
            "dose response",
            "viral dose",
            "viral load",
            "infectious dose",
            "plaque assay",
            "serial passage",
            "gain-of-function",
            "reverse genetics",
            "transfection",
            "infection protocol",
            "replication protocol",
            "culture condition",
            "incubation temperature",
            "biosafety level",
            "host species",
            "strain name",
            "wet-lab",
        ]

        self.required_safety_markers = [
            "safe",
            "abstract",
            "conceptual",
            "non-operational",
            "not a real",
            "not biological",
            "no actionable",
        ]

    def audit(self, scenarios: list[ViralPatternScenario]) -> ScenarioAuditReport:
        results: list[ScenarioAuditResult] = []

        targeting_by_name: dict[str, float] = {}

        for scenario in scenarios:
            targeting = self.targeting_analyzer.analyze(
                scenario.fabric,
                case_name=scenario.name,
            )
            classification = self.classifier.classify(
                scenario.fabric,
                case_name=scenario.name,
            )

            targeting_by_name[scenario.name] = targeting.score

            findings: list[AuditFinding] = []
            findings.extend(self._audit_text_safety(scenario))
            findings.extend(self._audit_node_safety(scenario))
            findings.extend(
                self._audit_role_score_consistency(
                    scenario=scenario,
                    score=targeting.score,
                    constructive_nodes=classification.constructive_nodes,
                    tension_wells=classification.tension_wells,
                    strained_gateways=classification.strained_gateways,
                    path=targeting.path,
                )
            )

            status = self._status_from_findings(findings)

            results.append(
                ScenarioAuditResult(
                    scenario_name=scenario.name,
                    status=status,
                    score=targeting.score,
                    path=targeting.path,
                    constructive_nodes=classification.constructive_nodes,
                    tension_wells=classification.tension_wells,
                    strained_gateways=classification.strained_gateways,
                    findings=findings,
                )
            )

        global_findings = self._audit_global_ordering(targeting_by_name)

        return ScenarioAuditReport(
            results=results,
            global_findings=global_findings,
        )

    def _audit_text_safety(self, scenario: ViralPatternScenario) -> list[AuditFinding]:
        findings: list[AuditFinding] = []

        combined_text = " ".join(
            [
                scenario.name,
                scenario.biological_reading,
                scenario.abstract_question,
                scenario.expected_mechanism,
                scenario.safety_note,
            ]
        ).lower()

        for term in self.operational_red_flags:
            if term in combined_text:
                findings.append(
                    AuditFinding(
                        scenario_name=scenario.name,
                        category="safety_boundary",
                        severity="high",
                        message="Operational biological wording detected.",
                        evidence=term,
                        recommendation=(
                            "Replace this with abstract, non-operational language."
                        ),
                    )
                )

        safety_text = scenario.safety_note.lower()
        if not any(marker in safety_text for marker in self.required_safety_markers):
            findings.append(
                AuditFinding(
                    scenario_name=scenario.name,
                    category="safety_boundary",
                    severity="medium",
                    message="Safety note is too weak or missing abstraction markers.",
                    evidence=scenario.safety_note,
                    recommendation=(
                        "Add wording such as safe abstraction, conceptual model, "
                        "non-operational, or no actionable biological parameters."
                    ),
                )
            )

        return findings

    def _audit_node_safety(self, scenario: ViralPatternScenario) -> list[AuditFinding]:
        findings: list[AuditFinding] = []

        for node_id, node in scenario.fabric.nodes.items():
            safe_abstraction = str(node.state.get("safe_abstraction", "")).lower()
            biological_role = str(node.state.get("biological_role", "")).lower()

            if not safe_abstraction:
                findings.append(
                    AuditFinding(
                        scenario_name=scenario.name,
                        category="node_annotation",
                        severity="medium",
                        message=f"Node {node_id} is missing safe_abstraction.",
                        evidence=node_id,
                        recommendation="Add a non-operational abstraction label.",
                    )
                )
                continue

            if not any(marker in safe_abstraction for marker in ["abstract", "proxy", "not"]):
                findings.append(
                    AuditFinding(
                        scenario_name=scenario.name,
                        category="node_annotation",
                        severity="low",
                        message=f"Node {node_id} safe abstraction could be clearer.",
                        evidence=safe_abstraction,
                        recommendation=(
                            "Use explicit language such as abstract, proxy, or not a real mechanism."
                        ),
                    )
                )

            for term in self.operational_red_flags:
                if term in biological_role or term in safe_abstraction:
                    findings.append(
                        AuditFinding(
                            scenario_name=scenario.name,
                            category="node_annotation",
                            severity="high",
                            message=f"Node {node_id} contains operational wording.",
                            evidence=term,
                            recommendation="Remove operational biological terms from node annotations.",
                        )
                    )

        return findings

    def _audit_role_score_consistency(
        self,
        *,
        scenario: ViralPatternScenario,
        score: float,
        constructive_nodes: list[str],
        tension_wells: list[str],
        strained_gateways: list[str],
        path: list[str],
    ) -> list[AuditFinding]:
        findings: list[AuditFinding] = []

        if tension_wells and score > 35:
            findings.append(
                AuditFinding(
                    scenario_name=scenario.name,
                    category="score_consistency",
                    severity="high",
                    message="Scenario has tension wells but targeting score is still high.",
                    evidence=f"score={score:.2f}, tension_wells={tension_wells}",
                    recommendation=(
                        "Increase tension well penalty or inspect geodesic routing."
                    ),
                )
            )

        if constructive_nodes and score < 50 and not tension_wells:
            findings.append(
                AuditFinding(
                    scenario_name=scenario.name,
                    category="score_consistency",
                    severity="medium",
                    message="Constructive attractors exist but apparent targeting is low.",
                    evidence=f"score={score:.2f}, constructive_nodes={constructive_nodes}",
                    recommendation=(
                        "Check whether cost efficiency or path coverage is suppressing the score."
                    ),
                )
            )

        if strained_gateways and score > 50:
            findings.append(
                AuditFinding(
                    scenario_name=scenario.name,
                    category="score_consistency",
                    severity="medium",
                    message="Strained gateways exist but targeting score is moderate/high.",
                    evidence=f"score={score:.2f}, strained_gateways={strained_gateways}",
                    recommendation=(
                        "Check strained gateway penalty and relation costs."
                    ),
                )
            )

        if scenario.name == "coherent_viral_pattern":
            if score < 75:
                findings.append(
                    AuditFinding(
                        scenario_name=scenario.name,
                        category="scenario_expectation",
                        severity="high",
                        message="Coherent viral pattern should show high apparent targeting.",
                        evidence=f"score={score:.2f}",
                        recommendation="Inspect coupling, geodesic costs, and targeting weights.",
                    )
                )
            if len(path) < 5:
                findings.append(
                    AuditFinding(
                        scenario_name=scenario.name,
                        category="scenario_expectation",
                        severity="medium",
                        message="Coherent viral pattern does not use the full route.",
                        evidence=" → ".join(path),
                        recommendation="Inspect space-time couplings and path costs.",
                    )
                )

        if scenario.name in {"spatial_context_break", "regulatory_time_disruption"}:
            if not tension_wells:
                findings.append(
                    AuditFinding(
                        scenario_name=scenario.name,
                        category="scenario_expectation",
                        severity="high",
                        message="Disrupted scenario should create at least one tension well.",
                        evidence=f"tension_wells={tension_wells}",
                        recommendation="Inspect displacement/time-shift strength or classifier thresholds.",
                    )
                )
            if score > 30:
                findings.append(
                    AuditFinding(
                        scenario_name=scenario.name,
                        category="scenario_expectation",
                        severity="high",
                        message="Disrupted scenario should have low apparent targeting.",
                        evidence=f"score={score:.2f}",
                        recommendation="Inspect tension penalties in the targeting index.",
                    )
                )

        if scenario.name == "abstract_baseline":
            if not strained_gateways:
                findings.append(
                    AuditFinding(
                        scenario_name=scenario.name,
                        category="scenario_expectation",
                        severity="medium",
                        message="Baseline is expected to contain a strained gateway.",
                        evidence=f"strained_gateways={strained_gateways}",
                        recommendation="Check geodesic and classifier thresholds.",
                    )
                )
            if score > 40:
                findings.append(
                    AuditFinding(
                        scenario_name=scenario.name,
                        category="scenario_expectation",
                        severity="medium",
                        message="Baseline targeting score is unexpectedly high.",
                        evidence=f"score={score:.2f}",
                        recommendation="Inspect targeting weights.",
                    )
                )

        return findings

    def _audit_global_ordering(self, targeting_by_name: dict[str, float]) -> list[AuditFinding]:
        findings: list[AuditFinding] = []

        coherent = targeting_by_name.get("coherent_viral_pattern")
        if coherent is None:
            findings.append(
                AuditFinding(
                    scenario_name="global",
                    category="scenario_set",
                    severity="high",
                    message="Missing coherent_viral_pattern scenario.",
                    evidence=str(sorted(targeting_by_name)),
                    recommendation="Include the coherent scenario in the scenario set.",
                )
            )
            return findings

        for name, score in targeting_by_name.items():
            if name == "coherent_viral_pattern":
                continue
            if score >= coherent:
                findings.append(
                    AuditFinding(
                        scenario_name="global",
                        category="score_ordering",
                        severity="high",
                        message="Coherent scenario is not the highest apparent targeting case.",
                        evidence=f"{name}={score:.2f}, coherent={coherent:.2f}",
                        recommendation="Inspect scenario construction or targeting weights.",
                    )
                )

        return findings

    def _status_from_findings(self, findings: list[AuditFinding]) -> AuditStatus:
        severities = [finding.severity for finding in findings]

        if "high" in severities:
            return "fail"
        if "medium" in severities or "low" in severities:
            return "warning"
        return "pass"
