# Published data

[Overview](../README.md)

The dated JSON files in each suite's data folder are the public numeric source for this snapshot. Markdown tables and quality charts are views of those records. Keep full numeric precision in JSON; round only for display.

| Field | Meaning |
|---|---|
| config | Model/effort identifier used in the evidence |
| n | Number of scored repeated executions |
| overall / recap / craft | Mean quality scores, 0–100 |
| spread | Maximum minus minimum overall run score |
| duration_seconds | Mean recorded execution duration, where exported; not reset-inclusive calendar wait |
| runs | Public run identifiers and combined numeric scores; no internal evaluation details |
| five_hour | Selected chart observations on roughly $20 plans |
| utilization_low / utilization_high | Single reading, or observed minimum and maximum; not statistical uncertainty |
| estimated | True for extrapolated usage, currently Fable |
| lower_bound | True where the source labels the consumption as a bound |

Missing is not zero. The [tier data](subscription-tiers-2026-09-16.json) separately record eligible weekly readings for Codex, Claude, and Kimi, and the 12 Claude five-hour matched pairs. Kimi has measured $20 weekly readings only: 35% and 47% for ATFW, and 39% and 52% for Killing Floor. An empty tier array means no eligible measurement. Ratios use $20 percentage divided by $200 percentage. A ratio is unresolved if the necessary reading is absent or the denominator is zero.

Results are exported from reviewed numeric evidence, not copied from older generated summaries. The first release intentionally omits API-equivalent dollar estimates, incomplete token totals, and unsupported cross-tier conversions. It also omits copyrighted inputs, chapter outputs, internal evaluation details, and local filesystem paths.

For ongoing updates, add a dated data snapshot, regenerate its tables/charts, and document the change. Do not replace historical measurements to reflect new plan limits. Article references should cite a tagged release or immutable commit once the repository is published.
