# What changes between $20 and $200 subscriptions?

[Booklab Benchmark](../README.md) · [ATFW tables](../suites/atfw-full/subscription-tiers.md) · [Killing Floor tables](../suites/killing-floor-full/subscription-tiers.md) · [Numeric data](../data/subscription-tiers-2026-09-16.json)

Subscription price alone doesn't tell me how much of this work a plan will support. I measured both tiers where possible, keeping five-hour and weekly allowances separate.

## Claude: five-hour to five-hour

The table compares the same configuration on the same book across separate $20 and $200 executions.

| Configuration | ATFW: $20 / $200 | Ratio | KF: $20 / $200 | Ratio |
|---|---|---|---|---|
| claude-sonnet-5-medium | 42% / 1% | 42.00× | 51% / 2% | 25.50× |
| claude-sonnet-5-high | 69% / 2% | 34.50× | 69% / 2% | 34.50× |
| claude-sonnet-4-6-medium | 105% / 2% | 52.50× | 84% / 3% | 28.00× |
| claude-opus-5-medium | 111% / 3% | 37.00× | 118% / 4% | 29.50× |
| claude-opus-4-8-medium | 83% / 3% | 27.67× | 107% / 2% | 53.50× |
| claude-haiku-4-5 | 49% / 2% | 24.50× | 61% / 3% | 20.33× |

Across these 12 comparisons, the median ratio is 32×. Dividing the sum of the $20 readings by the sum of the corresponding $200 readings gives **949/29 = 32.72×**. Opus 5 alone gives 229/7 = 32.71×.

That agreement makes roughly 33× a useful empirical estimate for these full-book workloads. The individual ratios range from about 20× to 54×. Excluding Haiku, the smallest observed ratio was 25.5×. Applying that lower multiplier to Fable’s measured $200 five-hour consumption of 9% and 10% would put it at about **230% for *A Talent for War* and 255% for *Killing Floor*** on the $20 plan. Even at that end of the observed comparisons, either book would consume more than two full allowances.

The calculations use the pooled factor of 949/29, which I describe as roughly 33×, with 25.5× as a conservative comparison rather than a guaranteed lower bound. The $200 readings in those 12 comparisons are only 1–4 percentage points, and these are separate executions on different dates, not a controlled measurement of the plans’ underlying capacity.

## Why Fable is estimated at roughly 300% and 330%

Fable's clean $200 readings were 9% for *A Talent for War* and 10% for *Killing Floor*. Applying the pooled factor gives 294.52% and 327.24% in $20-equivalent terms. The charts use those values; rounded prose describes them as roughly 300% and 330%.

This is an extrapolation from other Claude configurations, not measured Fable use on a $20 plan. The factor applies only to this five-hour estimate, never to weekly readings.

## Weekly comparisons

Claude can be compared five-hour to five-hour and weekly to weekly. Codex's reinstated five-hour windows applied to Plus, not Pro, so its tier comparison is weekly only. Weekly also gives a common window for comparing the vendors at the same monthly subscription price.

Each table cell below shows $20 / $200, followed by the arithmetic ratio when it is resolvable.

### Claude

| Configuration | ATFW | Killing Floor |
|---|---|---|
| Opus 5 medium | 8% / 1%; 8× | 9% / 0%; Unresolved |
| Opus 4.8 medium | 5% / 0%; Unresolved | 8% / 1%; 8× |
| Sonnet 5 medium | 3% / 1%; 3× | 4% / 0%; Unresolved |
| Sonnet 5 high | 4% / 0%; Unresolved | 5% / 1%; 5× |
| Sonnet 4.6 medium | 7% / 0%; Unresolved | 6% / 1%; 6× |
| Haiku 4.5 | 3% / 0%; Unresolved | 5% / 1%; 5× |
| Fable 5 medium | n/a / 1%; No pair | n/a / 2%; No pair |

### Codex

| Configuration | ATFW | Killing Floor |
|---|---|---|
| Astra medium | 15% / 1%; 15× | 20% / 1%; 20× |
| Sol low | 4% / 0%; Unresolved | 3–4% / 1%; 3–4× |
| Sol medium | 4–5% / n/a; No pair | 4–6% / n/a; No pair |
| Sol high | 3% / 0%; Unresolved | 5–7% / 0%; Unresolved |
| GPT-5.5 medium | 3–4% / 0%; Unresolved | 5% / 0%; Unresolved |
| GPT-5.4 medium | 2–4% / 0%; Unresolved | 4% / 1%; 4× |
| GPT-5.4 high | 3–5% / n/a; No pair | 4–5% / n/a; No pair |
| Terra medium | 3% / 0%; Unresolved | 3% / 0%; Unresolved |
| Terra high | 2–3% / n/a; No pair | 2–4% / n/a; No pair |
| Luna high | 0% / 0%; Unresolved | 0% / 0%; Unresolved |

The weekly figures do not support one stable multiplier for either provider. Every calculable $200 denominator is only one percentage point. Half of the Claude matched pairs have unchanged $200 meters; many Codex readings do too. Zero movement cannot support a ratio and does not establish free work.

Ranges show the lowest and highest retained readings, not confidence intervals. Weekly limits roll forward, so older usage can expire during a run. Shared-activity readings and a reversed-direction Terra medium weekly reading were excluded. The latter exclusion does not invalidate that run's separate five-hour measurement.

### Kimi

| Configuration | ATFW: $20 / $200 | Killing Floor: $20 / $200 |
|---|---|---|
| Kimi K3 | 35–47% / Not measured | 39–52% / Not measured |

The two complete Kimi runs used 35% and 47% of the $20 weekly allowance on *A Talent for War*, and 39% and 52% on *Killing Floor*. There are no measured $200 weekly readings, so no tier ratio is calculated. These observed ranges describe the weekly constraint in addition to the five-hour reset waits; they are not guaranteed books-per-week counts.

## The Claude weekly promotion

The measured Claude weekly readings came from the temporary 50% increase. [Pondero reports](https://pondero.ai/news/2026-09-14-claude-code-limits/) that this ended September 13 and was replaced September 14 with a permanent 25% increase over the pre-May baseline. The linked primary announcement was inaccessible during verification, so this policy account remains attributed to Pondero.

The tables preserve the actual promotion-era readings. If allowance size were the only change, the same work would now consume **1.50 / 1.25 = 1.20×** as much of the weekly allowance. That is 20% more of the meter, not a new measurement. It does not alter five-hour results.

Claude values here are for the general weekly allowance, not Fable's separate model-specific weekly pool.

## What the cross-vendor comparison adds

On $20 plans, Sol medium used 4–5% weekly for *A Talent for War* and 4–6% for *Killing Floor*. Opus 5 used 8% and 9% under the Claude promotion. The conditional allowance-only adjustment would make those Opus readings approximately 9.6% and 10.8%.

Sonnet 5 medium used 3% and 4%, so Codex does not have a blanket quota advantage over every Claude configuration. Quality remains part of the comparison.

At $200, the one-point or unchanged meters provide too little resolution to rank sustained capacity confidently. These results are a comparison point across vendors, not proof of a universal $200-plan winner.

Five-hour use describes the shorter-term constraint where that window exists. Weekly use describes the longer horizon. Neither can be converted into the other.
