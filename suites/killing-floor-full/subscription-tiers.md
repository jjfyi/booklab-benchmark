# Killing Floor: subscription tiers

[Suite overview](README.md) · [Combined analysis and caveats](../../analysis/subscription-tiers.md)

## Claude five-hour allowance

Matched configuration, same book, separate executions on the $20 and $200 plans. Ratio = $20 percentage / $200 percentage.

| Configuration | $20 measured | $200 measured | Ratio |
|---|---|---|---|
| claude-sonnet-5-medium | 51% | 2% | 25.50× |
| claude-sonnet-5-high | 69% | 2% | 34.50× |
| claude-sonnet-4-6-medium | 84% | 3% | 28.00× |
| claude-opus-5-medium | 118% | 4% | 29.50× |
| claude-opus-4-8-medium | 107% | 2% | 53.50× |
| claude-haiku-4-5 | 61% | 3% | 20.33× |

The combined 12-pair evidence across both books gives a pooled 32.72× factor. That is the estimate used for Fable, not a universal plan multiplier. Codex has no corresponding five-hour tier table: Pro did not have the reinstated Plus limit during this measurement period.

## Weekly allowance

| Provider | Configuration | $20 measured | $200 measured | Arithmetic ratio |
|---|---|---|---|---|
| Kimi | kimi-k3 | 39–52% | Not measured | No pair |
| Codex | gpt-6-astra-medium | 20% | 1% | 20.00× |
| Codex | gpt-5.6-terra-medium | 3% | 0% | Unresolved |
| Codex | gpt-5.4-high | 4–5% | Not measured | No pair |
| Codex | gpt-5.6-terra-high | 2–4% | Not measured | No pair |
| Codex | gpt-5.6-luna-high | 0% | 0% | Unresolved |
| Codex | gpt-5.6-sol-medium | 4–6% | Not measured | No pair |
| Codex | gpt-5.5-medium | 5% | 0% | Unresolved |
| Codex | gpt-5.4-medium | 4% | 1% | 4.00× |
| Codex | gpt-5.6-sol-low | 3–4% | 1% | 3.00–4.00× |
| Codex | gpt-5.6-sol-high | 5–7% | 0% | Unresolved |
| Claude | claude-opus-4-8-medium | 8% | 1% | 8.00× |
| Claude | claude-sonnet-4-6-medium | 6% | 1% | 6.00× |
| Claude | claude-fable-5-medium | Not measured | 2% | No pair |
| Claude | claude-opus-5-medium | 9% | 0% | Unresolved |
| Claude | claude-haiku-4-5 | 5% | 1% | 5.00× |
| Claude | claude-sonnet-5-medium | 4% | 0% | Unresolved |
| Claude | claude-sonnet-5-high | 5% | 1% | 5.00× |

Ranges show retained measurements across repeats. Zero means an unchanged meter, not zero work. Weekly expiry can offset new consumption. Every nonzero $200 denominator here is only one percentage point; unresolved ratios must not be replaced with a guessed multiplier.

Claude figures were measured during the temporary weekly boost. [Policy context and conditional adjustment](../../analysis/subscription-tiers.md#the-claude-weekly-promotion). These are general weekly readings, not Fable's separate model-specific pool. Compare vendors within the same price tier and book; the measurements do not establish a universal vendor capacity ratio.
