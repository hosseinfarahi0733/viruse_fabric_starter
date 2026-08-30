# C133 Semantic Contract / قرارداد معنایی C133

## فارسی

این milestone سه نماد زمانی را به‌عنوان سه **دورهٔ علّی مرتب‌شده** تعریف می‌کند،
نه سه بُعد فیزیکی زمان:

| نماد | معنا |
|---|---|
| `Past` | حالت بالادست/پایه که پیش از مداخلات downstream تعیین شده است |
| `Present` | حالت میانی که قانون `presentLaw` آن را از `Past` می‌سازد |
| `Future` | حالت پایین‌دست که `futureLaw` آن را از `Past` و `Present` می‌سازد |
| `doPresent` | جایگزینی جراحی حالت میانی و محاسبهٔ دوبارهٔ آینده |
| `doFuture` | جایگزینی جراحی حالت نهایی بدون بازنویسی گذشته یا حال تولیدشده |
| `EvidenceRefines` | هر state پذیرفته‌شده با evidence قوی‌تر، با evidence ضعیف‌تر نیز پذیرفته می‌شود |
| `CandidatePast` | گذشته‌هایی که با observation ثابت و evidence فعلی سازگارند |

قضیهٔ no-retrocausality در این milestone دقیقاً می‌گوید intervention پایین‌دست
فیلد `past` را تغییر نمی‌دهد. این یک قانون دربارهٔ مدل تعریف‌شده است، نه اثبات
تجربی دربارهٔ طبیعت.

قضیهٔ observer recontextualization می‌گوید evidence قوی‌تر می‌تواند مجموعهٔ
`CandidatePast` را strict کوچک کند، در حالی که actual past ثابت و پذیرفته‌شده
باقی می‌ماند. بنابراین «گذشته بازتفسیر می‌شود» معنای epistemic دارد، نه
retrocausal.

## English

C133 treats the three temporal symbols as three **ordered causal epochs**, not
three physical time dimensions.

- `presentLaw : Past → Present` is the middle structural equation.
- `futureLaw : Past → Present → Future` is the downstream equation.
- `doPresent` replaces the middle value and recomputes the downstream value.
- `doFuture` replaces only the terminal value.
- downstream interventions preserve the supplied upstream past by theorem.
- evidence refinement is set inclusion on accepted complete states.
- observer recontextualization is strict shrinkage of compatible pasts while
  the realized past stays fixed.

The semantics are deterministic and generic. Concrete finite Boolean fixtures
provide executable witnesses. Probability, identification, measurement error,
and biological interpretation remain future layers.
