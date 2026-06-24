from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from textwrap import dedent

from viruse_fabric.biology.apparent_targeting import ApparentTargetingAnalyzer
from viruse_fabric.biology.scenario_auditor import ScenarioSafetyConsistencyAuditor
from viruse_fabric.biology.viral_scenarios import (
    ViralPatternScenario,
    build_viral_pattern_scenarios,
)
from viruse_fabric.geometry.attractor_classifier import AttractorTypeClassifier
from viruse_fabric.simulation.observer_misreading import ObserverMisreadingEngine


NODE_ROWS = [
    ("A", "رویداد تماس‌مانند در مرز فیزیکی", "نماینده‌ی غیرعملیاتی تماس"),
    ("B", "گذار سازگاری‌مانند یا تغییر وضعیت سلولی", "دروازه‌ی انتزاعی سازگاری، نه مدل گیرنده‌ی واقعی"),
    ("C", "بازآرایی زمینه‌ی اطلاعاتی", "جابجایی تنظیمی انتزاعی، نه پروتکل مولکولی"),
    ("D", "پایدارسازی ماندگاری‌مانند", "نماینده‌ی پایداری، نه سازوکار تکثیر"),
    ("E", "برون‌نمایی فنوتیپ‌مانند قابل مشاهده", "نماینده‌ی نقطه پایانی قابل مشاهده"),
]


SCENARIO_READINGS = {
    "abstract_baseline": (
        "سناریوی پایه‌ی انتزاعی با سازمان‌دهی ضعیف. مسیر ساختار دارد، "
        "اما از یک دروازه‌ی پرهزینه و تحت فشار عبور می‌کند.",
        "دروازه‌ی پرهزینه به‌جای هدفمندی پایدار",
    ),
    "coherent_viral_pattern": (
        "مسیر انتزاعی منسجم که در آن سازگاری، تنظیم، پایدارسازی و پیامد قابل مشاهده هم‌راستا می‌شوند.",
        "هدفمندی ظاهری بالا از راه پشتیبانی جاذب سازنده",
    ),
    "spatial_context_break": (
        "سناریوی اختلال در زمینه‌ی سازگاری. گره سازگاری‌مانند به جاذب پرتنشی تبدیل می‌شود که مسیر ژئودزیک از آن دوری می‌کند.",
        "تشکیل چاه تنش و دوری مسیر",
    ),
    "regulatory_time_disruption": (
        "سناریوی اختلال در زمان تنظیمی. گره زمینه‌ی اطلاعاتی به جاذب پرتنش تبدیل می‌شود، نه مسیر پایدار.",
        "چاه تنش تنظیمی و از دست رفتن هدفمندی ظاهری",
    ),
}


FA_INTERPRETATIONS = {
    "low apparent targeting": "هدفمندی ظاهری پایین",
    "high apparent targeting": "هدفمندی ظاهری بالا",
    "moderate apparent targeting": "هدفمندی ظاهری متوسط",
    "weak apparent targeting": "هدفمندی ظاهری ضعیف",
    "weak risk of intentionality misreading": "ریسک ضعیف قصدخوانی اشتباه",
    "high risk of intentionality misreading": "ریسک بالای قصدخوانی اشتباه",
    "low risk of intentionality misreading": "ریسک پایین قصدخوانی اشتباه",
    "moderate risk of intentionality misreading": "ریسک متوسط قصدخوانی اشتباه",
    "scenario layer is safe and internally consistent": "لایه سناریوها ایمن و از نظر درونی سازگار است",
}


@dataclass
class PersianChapterExportResult:
    output_path: Path
    title: str
    scenario_count: int
    safety_status: str
    total_findings: int
    word_count: int

    @property
    def interpretation(self) -> str:
        if self.safety_status == "pass":
            return "خروجی فصل فارسی با مرز ایمنی مفهومی ساخته شد"
        if self.safety_status == "warning":
            return "خروجی فصل فارسی ساخته شد، اما نیاز به بازبینی دارد"
        return "خروجی فصل فارسی پیش از استفاده باید اصلاح شود"


class PersianTheoryChapterExporter:
    """ساخت خروجی فارسی برای فصل نظری پروژه."""

    def __init__(self) -> None:
        self.targeting_analyzer = ApparentTargetingAnalyzer()
        self.classifier = AttractorTypeClassifier()
        self.misreading_engine = ObserverMisreadingEngine()
        self.auditor = ScenarioSafetyConsistencyAuditor()

    def export(
        self,
        *,
        output_path: str | Path = "outputs/theory_chapter_fa_v1_8.md",
        title: str = "هدفمندی ظاهری بدون قصد",
    ) -> PersianChapterExportResult:
        scenarios = build_viral_pattern_scenarios()
        audit_report = self.auditor.audit(scenarios)

        chapter = self._build_chapter(
            title=title,
            scenarios=scenarios,
            safety_status=audit_report.status,
            total_findings=audit_report.total_findings,
            safety_interpretation=audit_report.interpretation,
        )

        path = Path(output_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(chapter, encoding="utf-8")

        return PersianChapterExportResult(
            output_path=path,
            title=title,
            scenario_count=len(scenarios),
            safety_status=audit_report.status,
            total_findings=audit_report.total_findings,
            word_count=len(chapter.split()),
        )

    def _fa(self, text: str) -> str:
        return FA_INTERPRETATIONS.get(text, text)

    def _build_chapter(
        self,
        *,
        title: str,
        scenarios: list[ViralPatternScenario],
        safety_status: str,
        total_findings: int,
        safety_interpretation: str,
    ) -> str:
        parts = [
            self._front_matter(title),
            self._problem_section(),
            self._model_section(),
            self._scenario_layer_section(scenarios),
            self._results_section(scenarios),
            self._observer_section(scenarios),
            self._correction_section(),
            self._safety_section(
                safety_status=safety_status,
                total_findings=total_findings,
                safety_interpretation=safety_interpretation,
            ),
            self._closing_section(),
        ]
        return "\n\n".join(parts).strip() + "\n"

    def _front_matter(self, title: str) -> str:
        return dedent(
            f"""
            # {title}

            **پروژه:** Viruse Fabric  
            **نوع فصل:** پیش‌نویس نظری-محاسباتی  
            **گزاره مرکزی:** علیت زنجیره نیست؛ هندسه‌ی قیود است.

            > هدفمندی ظاهری، قصد نیست؛ نتیجه‌ی هم‌راستایی مسیر، جاذب‌های سازنده و فیلترهای بافت است.
            """
        ).strip()

    def _problem_section(self) -> str:
        return dedent(
            """
            ## ۱. مسئله

            برخی الگوهای زیستی در نگاه مشاهده‌گر هدفمند به نظر می‌رسند. برای نمونه، یک الگوی ویروسی ممکن است چنان دیده شود که گویی میزبان، بافت، وضعیت سلولی یا پیامد خاصی را انتخاب کرده است. اما این خوانش، معمولاً یک فشرده‌سازی روایی است: مشاهده‌گر مسیر را می‌بیند و خیلی زود از مسیر به قصد می‌پرد.

            این مدل از چنین پرشی پرهیز می‌کند.

            در این چارچوب، قصد درون الگوی ویروسی قرار داده نمی‌شود. هدفمندی ظاهری به‌عنوان اثر مشاهده‌پذیر هم‌راستایی مسیر درون یک بافت قیودی فهمیده می‌شود. مسیری ممکن است انتخاب‌شده به نظر برسد، نه چون چیزی آن را خواسته، بلکه چون پایدارتر، کم‌هزینه‌تر، هم‌راستاتر و بیشتر قابل مشاهده شده است.

            بنابراین پرسش اصلی این نیست:

            **ویروس چه قصدی دارد؟**

            پرسش دقیق‌تر این است:

            **چه نوع بافت علّی باعث می‌شود یک مسیر برای مشاهده‌گر شبیه انتخاب هدفمند دیده شود؟**
            """
        ).strip()

    def _model_section(self) -> str:
        return dedent(
            """
            ## ۲. مدل نظری

            مدل، رخدادها را به‌صورت گره‌هایی درون یک بافت علّی نمایش می‌دهد. این بافت از قیدها، تنش‌ها، کوپلینگ فضا-زمان، خمیدگی علّی، مسیرهای ژئودزیک‌مانند و projection مشاهده‌گر ساخته شده است.

            لایه‌های اصلی مدل عبارت‌اند از:

            ۱. **خمیدگی علّی:** تشخیص گره‌هایی که تنش، فشار و اتصال در آن‌ها متمرکز می‌شود.  
            ۲. **مسیر ژئودزیک علّی:** یافتن مسیرهای کم‌هزینه درون بافت.  
            ۳. **طبقه‌بندی جاذب‌ها:** جداسازی جاذب‌های مسیرساز از چاه‌های تنش.  
            ۴. **شاخص هدفمندی ظاهری:** سنجش اینکه یک مسیر چقدر هدفمند دیده می‌شود.  
            ۵. **موتور خطای مشاهده‌گر:** سنجش اینکه چه زمانی هم‌راستایی مسیر با قصد اشتباه گرفته می‌شود.  
            ۶. **گزارش اصلاح قصدخوانی:** تبدیل داستان اشتباه مشاهده‌گر به خوانش مبتنی بر قید و مسیر.

            این مدل عمداً انتزاعی باقی می‌ماند. در آن از پاتوژن واقعی، میزبان واقعی، دوز، گیرنده واقعی، پروتکل آزمایشگاهی یا مداخله عملیاتی استفاده نمی‌شود.
            """
        ).strip()

    def _scenario_layer_section(self, scenarios: list[ViralPatternScenario]) -> str:
        lines = [
            "## ۳. لایه سناریوهای انتزاعی زیستی",
            "",
            "گره‌های انتزاعی مدل به زبان زیستیِ امن و غیرعملیاتی ترجمه شده‌اند:",
            "",
            "| گره | نقش زیستی-خوانا | انتزاع امن |",
            "|---|---|---|",
        ]

        for node_id, role, safe in NODE_ROWS:
            lines.append(f"| {node_id} | {role} | {safe} |")

        lines.extend(
            [
                "",
                "سناریوهای بررسی‌شده:",
                "",
                "| سناریو | خوانش زیستی-انتزاعی | سازوکار مورد انتظار |",
                "|---|---|---|",
            ]
        )

        for scenario in scenarios:
            reading, mechanism = SCENARIO_READINGS[scenario.name]
            lines.append(f"| {scenario.name} | {reading} | {mechanism} |")

        return "\n".join(lines)

    def _results_section(self, scenarios: list[ViralPatternScenario]) -> str:
        lines = [
            "## ۴. نتایج: هدفمندی ظاهری و نقش جاذب‌ها",
            "",
            "| سناریو | مسیر | امتیاز هدفمندی | جاذب سازنده | چاه تنش | دروازه پرهزینه | تفسیر |",
            "|---|---|---:|---|---|---|---|",
        ]

        for scenario in scenarios:
            targeting = self.targeting_analyzer.analyze(
                scenario.fabric,
                case_name=scenario.name,
            )
            classification = self.classifier.classify(
                scenario.fabric,
                case_name=scenario.name,
            )

            lines.append(
                "| "
                f"{scenario.name} | "
                f"{' → '.join(targeting.path)} | "
                f"{targeting.score:.2f} | "
                f"{', '.join(classification.constructive_nodes) or 'ندارد'} | "
                f"{', '.join(classification.tension_wells) or 'ندارد'} | "
                f"{', '.join(classification.strained_gateways) or 'ندارد'} | "
                f"{self._fa(targeting.interpretation)} |"
            )

        lines.append("")
        lines.append(
            "سناریوی coherent_viral_pattern بالاترین هدفمندی ظاهری را نشان می‌دهد، زیرا مسیر کامل، کم‌هزینه و به‌وسیله‌ی جاذب سازنده پشتیبانی می‌شود. "
            "در مقابل، سناریوهای مختل‌شده هدفمندی ظاهری پایینی دارند، چون گره‌های غالب در آن‌ها به چاه تنش تبدیل می‌شوند، نه به سازمان‌دهنده‌ی مسیر."
        )

        return "\n".join(lines)

    def _observer_section(self, scenarios: list[ViralPatternScenario]) -> str:
        lines = [
            "## ۵. خطای مشاهده‌گر",
            "",
            "| سناریو | امتیاز هدفمندی | امتیاز قصدخوانی مشاهده‌گر | ریسک اصلی |",
            "|---|---:|---:|---|",
        ]

        for scenario in scenarios:
            misreading = self.misreading_engine.analyze(
                scenario.fabric,
                case_name=scenario.name,
            )

            lines.append(
                "| "
                f"{scenario.name} | "
                f"{misreading.apparent_targeting_score:.2f} | "
                f"{misreading.misreading_score:.2f} | "
                f"{self._fa(misreading.interpretation)} |"
            )

        lines.append("")
        lines.append(
            "خطای مشاهده‌گر زمانی رخ می‌دهد که مسیر هم‌راستا، پیامد قابل مشاهده و جاذب غالب، در ذهن مشاهده‌گر به داستانی از قصد فشرده می‌شوند. "
            "این قصد، ویژگی خود مسیر نیست؛ خوانش مشاهده‌گر از مسیر است."
        )

        return "\n".join(lines)

    def _correction_section(self) -> str:
        return dedent(
            """
            ## ۶. اصلاح خوانش قصد

            ### abstract_baseline

            **داستان اشتباه مشاهده‌گر:** در سناریوی abstract_baseline، مشاهده‌گر ممکن است مسیر اجباری از D را به‌صورت پیشروی جهت‌دار بخواند.

            **خوانش اصلاح‌شده:** مسیر A → D → E ساختار دارد، اما پرهزینه است. دروازه‌ی تحت فشار D نشان‌دهنده‌ی فشار قیود است، نه جهت‌گیری قصدی.

            **اصل اصلاحی:** عبور اجباری و پرهزینه را با جهت‌گیری قصدی اشتباه نگیر.

            **پاراگراف پیشنهادی فصل:** در سناریوی abstract_baseline، مسیر قابل مشاهده A → D → E است. امتیاز هدفمندی ظاهری 8.70 و امتیاز قصدخوانی اشتباه مشاهده‌گر 40.44 است. خطای تفسیری اصلی، اشتباه گرفتن پیشروی اجباری با جهت‌گیری قصدی است. مسیر A → D → E ساختار دارد، اما پرهزینه است. دروازه‌ی تحت فشار D نشان‌دهنده‌ی فشار قیود است، نه جهت‌گیری قصدی.

            ### coherent_viral_pattern

            **داستان اشتباه مشاهده‌گر:** در سناریوی coherent_viral_pattern، مشاهده‌گر ممکن است مسیر A → B → C → D → E را ببیند و نتیجه بگیرد که الگو عمداً نقطه پایانی را انتخاب کرده است.

            **خوانش اصلاح‌شده:** مسیر A → B → C → D → E هدفمند دیده می‌شود، چون جاذب سازنده‌ی D مسیر را پایدار می‌کند. این هم‌راستایی مسیر است، نه قصد.

            **اصل اصلاحی:** رفتار هدفمند-نما را به‌عنوان هم‌راستایی تولیدشده توسط جاذب‌های سازنده بخوان.

            **پاراگراف پیشنهادی فصل:** در سناریوی coherent_viral_pattern، مسیر قابل مشاهده A → B → C → D → E است. امتیاز هدفمندی ظاهری 88.53 و امتیاز قصدخوانی اشتباه مشاهده‌گر 91.21 است. خطای تفسیری اصلی، فشرده‌سازی هم‌راستایی مسیر به انتخاب قصدی است. مسیر A → B → C → D → E هدفمند دیده می‌شود، چون جاذب سازنده‌ی D مسیر را پایدار می‌کند. این هم‌راستایی مسیر است، نه قصد.

            ### spatial_context_break

            **داستان اشتباه مشاهده‌گر:** در سناریوی spatial_context_break، مشاهده‌گر ممکن است چاه تنش B را علت پنهان یا هدف پنهان بداند.

            **خوانش اصلاح‌شده:** مسیر A → D → E نشان‌دهنده‌ی قصد نیست. این مسیر از چاه تنش B دوری می‌کند. جاذب غالب، تمرکز بحران است، نه هدف انتخاب‌شده.

            **اصل اصلاحی:** نقطه‌ی بحرانیِ پرجاذبه را با هدف انتخاب‌شده اشتباه نگیر.

            **پاراگراف پیشنهادی فصل:** در سناریوی spatial_context_break، مسیر قابل مشاهده A → D → E است. امتیاز هدفمندی ظاهری 0.00 و امتیاز قصدخوانی اشتباه مشاهده‌گر 13.95 است. خطای تفسیری اصلی، اشتباه گرفتن تمرکز بحران با قصد علّی است. مسیر A → D → E نشان‌دهنده‌ی قصد نیست. این مسیر از چاه تنش B دوری می‌کند. جاذب غالب، تمرکز بحران است، نه هدف انتخاب‌شده.

            ### regulatory_time_disruption

            **داستان اشتباه مشاهده‌گر:** در سناریوی regulatory_time_disruption، مشاهده‌گر ممکن است چاه تنش C را علت پنهان یا هدف پنهان بداند.

            **خوانش اصلاح‌شده:** مسیر A → D → E نشان‌دهنده‌ی قصد نیست. این مسیر از چاه تنش C دوری می‌کند. جاذب غالب، تمرکز بحران است، نه هدف انتخاب‌شده.

            **اصل اصلاحی:** نقطه‌ی بحرانیِ پرجاذبه را با هدف انتخاب‌شده اشتباه نگیر.

            **پاراگراف پیشنهادی فصل:** در سناریوی regulatory_time_disruption، مسیر قابل مشاهده A → D → E است. امتیاز هدفمندی ظاهری 0.00 و امتیاز قصدخوانی اشتباه مشاهده‌گر 13.95 است. خطای تفسیری اصلی، اشتباه گرفتن تمرکز بحران با قصد علّی است. مسیر A → D → E نشان‌دهنده‌ی قصد نیست. این مسیر از چاه تنش C دوری می‌کند. جاذب غالب، تمرکز بحران است، نه هدف انتخاب‌شده.
            """
        ).strip()

    def _safety_section(
        self,
        *,
        safety_status: str,
        total_findings: int,
        safety_interpretation: str,
    ) -> str:
        status_fa = {
            "pass": "قبول",
            "warning": "هشدار",
            "fail": "رد",
        }.get(safety_status, safety_status)

        return dedent(
            f"""
            ## ۷. مرز ایمنی و انتزاع

            پیش از تولید این فصل، لایه سناریوها با auditor ایمنی و سازگاری بررسی شد.

            - وضعیت ممیزی: **{status_fa}**
            - تعداد یافته‌ها: **{total_findings}**
            - تفسیر: **{self._fa(safety_interpretation)}**

            این فصل غیرعملیاتی است. در آن از پاتوژن واقعی، میزبان واقعی، دوز، گیرنده، پروتکل آزمایشگاهی، دستور اجرایی یا مداخله قابل اجرا صحبت نمی‌شود.

            هدف این لایه توضیحی است: ترجمه نقش‌های انتزاعی علّی به زبانی زیستی-خوانا، بدون تبدیل مدل به یک سامانه زیستی عملیاتی.
            """
        ).strip()

    def _closing_section(self) -> str:
        return dedent(
            """
            ## ۸. جمع‌بندی فصل

            هدفمندی ظاهری نیازمند قصد نیست. یک مسیر می‌تواند هدفمند دیده شود، اگر بافت قیود آن را هم‌راستا، کم‌هزینه، پایدار و قابل مشاهده کند. مشاهده‌گر سپس این مسیر را به داستان انتخاب یا هدف تبدیل می‌کند.

            خوانش اصلاح‌شده چنین است:

            **قصد، ویژگی مسیر نیست؛ قصد، خوانش فشرده و اشتباه مشاهده‌گر از مسیرهای هم‌راستا و پرجاذبه است.**

            در نتیجه، پرسش اصلی نظریه این نیست که «چه چیزی قصد کرده است؟» بلکه این است که «کدام قیود باعث شده‌اند یک مسیر، قصدآلود دیده شود؟»
            """
        ).strip()
