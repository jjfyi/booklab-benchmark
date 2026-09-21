# A Talent for War

[Booklab Benchmark](../../README.md) · [Methodology](../../METHODOLOGY.md)

First complete-book test: **27 chapters**, **18 configurations**, with multiple runs per configuration. Book by Jack McDevitt. Evidence snapshot: 2026-09-16.

Each chapter was analyzed independently across the entire book. The model did not build up memory of the novel.

## Quality versus five-hour allowance

![A Talent for War: quality and five-hour use for all 18 configurations.](charts/quality-vs-five-hour.png)

Higher is better quality; farther right is less allowance used. The utilization scale is segmented. Horizontal ranges show observed use; Fable is estimated. [Chart values and interpretation](quality-vs-five-hour.md).

## Quality standings

![A Talent for War: all configuration means, with recap and craft alongside overall bars.](charts/quality.svg)

Bars start at zero. Overall is the equal-weight mean of recap and craft. The five highest overall means are below; use the component scores when one kind of analysis matters more to you.

| Configuration | Overall | Recap | Craft |
|---|---|---|---|
| gpt-6-astra-medium | 88.53 | 92.52 | 84.55 |
| gpt-5.6-sol-low | 86.50 | 90.88 | 82.11 |
| gpt-5.6-sol-high | 86.49 | 91.33 | 81.66 |
| gpt-5.6-sol-medium | 86.45 | 91.05 | 81.85 |
| claude-opus-5-medium | 85.52 | 90.40 | 80.64 |

[All configurations and every included run](results.md) · [Numeric snapshot](data/results-2026-09-16.json)

## Further analysis

- [Quality versus five-hour use](quality-vs-five-hour.md): complete plot data and what the tradeoff means.
- [Subscription tiers](subscription-tiers.md): this book's $20/$200 readings and ratios.
- [Cross-book consistency](../../analysis/consistency.md): the same 18 configurations across the screen and both books.
