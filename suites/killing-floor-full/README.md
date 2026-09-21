# Killing Floor

[Booklab Benchmark](../../README.md) · [Methodology](../../METHODOLOGY.md)

Second complete-book test: **34 chapters**, **18 configurations**, with multiple runs per configuration. Book by Lee Child. Evidence snapshot: 2026-09-16.

Each chapter was analyzed independently across the entire book. The model did not build up memory of the novel.

## Quality versus five-hour allowance

![Killing Floor: quality and five-hour use for all 18 configurations.](charts/quality-vs-five-hour.png)

Higher is better quality; farther right is less allowance used. The utilization scale is segmented. Horizontal ranges show observed use; Fable is estimated. [Chart values and interpretation](quality-vs-five-hour.md).

## Quality standings

![Killing Floor: all configuration means, with recap and craft alongside overall bars.](charts/quality.svg)

Bars start at zero. Overall is the equal-weight mean of recap and craft. The five highest overall means are below; use the component scores when one kind of analysis matters more to you.

| Configuration | Overall | Recap | Craft |
|---|---|---|---|
| gpt-6-astra-medium | 90.51 | 92.97 | 88.05 |
| gpt-5.6-sol-high | 89.17 | 91.53 | 86.82 |
| gpt-5.6-sol-medium | 88.98 | 91.51 | 86.45 |
| gpt-5.6-sol-low | 88.77 | 90.85 | 86.68 |
| claude-opus-5-medium | 87.63 | 89.90 | 85.35 |

[All configurations and every included run](results.md) · [Numeric snapshot](data/results-2026-09-16.json)

## Further analysis

- [Quality versus five-hour use](quality-vs-five-hour.md): complete plot data and what the tradeoff means.
- [Subscription tiers](subscription-tiers.md): this book's $20/$200 readings and ratios.
- [Cross-book consistency](../../analysis/consistency.md): the same 18 configurations across the screen and both books.
