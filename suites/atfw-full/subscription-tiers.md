# A Talent for War: subscription tiers

[Suite overview](README.md) · [Combined analysis and caveats](../../analysis/subscription-tiers.md)

## Claude five-hour allowance

Matched configuration, same book, separate executions on the $20 and $200 plans. Ratio = $20 percentage / $200 percentage.

| Configuration | $20 measured | $200 measured | Ratio |
|---|---|---|---|
| claude-sonnet-5-medium | 42% | 1% | 42.00× |
| claude-sonnet-5-high | 69% | 2% | 34.50× |
| claude-sonnet-4-6-medium | 105% | 2% | 52.50× |
| claude-opus-5-medium | 111% | 3% | 37.00× |
| claude-opus-4-8-medium | 83% | 3% | 27.67× |
| claude-haiku-4-5 | 49% | 2% | 24.50× |

The combined 12-pair evidence across both books gives a pooled 32.72× factor. That is the estimate used for Fable, not a universal plan multiplier. Codex has no corresponding five-hour tier table: Pro did not have the reinstated Plus limit during this measurement period.

## Weekly allowance

| Provider | Configuration | $20 measured | $200 measured | Arithmetic ratio |
|---|---|---|---|---|
| Kimi | kimi-k3 | 35–47% | Not measured | No pair |
| Codex | gpt-6-astra-medium | 15% | 1% | 15.00× |
| Codex | gpt-5.6-terra-medium | 3% | 0% | Unresolved |
| Codex | gpt-5.4-high | 3–5% | Not measured | No pair |
| Codex | gpt-5.6-terra-high | 2–3% | Not measured | No pair |
| Codex | gpt-5.6-luna-high | 0% | 0% | Unresolved |
| Codex | gpt-5.6-sol-medium | 4–5% | Not measured | No pair |
| Codex | gpt-5.5-medium | 3–4% | 0% | Unresolved |
| Codex | gpt-5.4-medium | 2–4% | 0% | Unresolved |
| Codex | gpt-5.6-sol-low | 4% | 0% | Unresolved |
| Codex | gpt-5.6-sol-high | 3% | 0% | Unresolved |
| Claude | claude-opus-4-8-medium | 5% | 0% | Unresolved |
| Claude | claude-sonnet-4-6-medium | 7% | 0% | Unresolved |
| Claude | claude-fable-5-medium | Not measured | 1% | No pair |
| Claude | claude-opus-5-medium | 8% | 1% | 8.00× |
| Claude | claude-haiku-4-5 | 3% | 0% | Unresolved |
| Claude | claude-sonnet-5-medium | 3% | 1% | 3.00× |
| Claude | claude-sonnet-5-high | 4% | 0% | Unresolved |

Ranges show retained measurements across repeats. Zero means an unchanged meter, not zero work. Weekly expiry can offset new consumption. Every nonzero $200 denominator here is only one percentage point; unresolved ratios must not be replaced with a guessed multiplier.

Claude figures were measured during the temporary weekly boost. [Policy context and conditional adjustment](../../analysis/subscription-tiers.md#the-claude-weekly-promotion). These are general weekly readings, not Fable's separate model-specific pool. Compare vendors within the same price tier and book; the measurements do not establish a universal vendor capacity ratio.
