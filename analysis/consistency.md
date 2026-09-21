# Did the stronger models remain consistent?

[Booklab Benchmark](../README.md) · [Ender's Game](../suites/enders-4ch/README.md) · [ATFW](../suites/atfw-full/README.md) · [Killing Floor](../suites/killing-floor-full/README.md)

The leading models repeatedly delivered high-quality analysis. Astra's overall repeat-run ranges were 0.18 points on *A Talent for War* and 0.04 on *Killing Floor*. Sol's effort settings stayed below 0.86 and 0.58 points; Opus 5's ranges were 0.10 and 0.68.

Lower-tier configurations could also be tightly grouped. Haiku's full-book ranges were 0.08 and 0.18. Consistency alone does not imply high quality.

## Did narrowing the field change the comparison?

Yes, the full-book tests incidentally left out some variable configurations, including Gemini Pro and Kimi K2.7. But they retained others that had varied substantially in the screen, including Sonnet 4.6, Haiku, and Sonnet 5 high. The retained field was not simply the most consistent set.

Comparing exactly the same 18 configurations avoids attributing every change to the smaller field.

| Median repeat-run range | Ender's Game | ATFW | Killing Floor |
|---|---|---|---|
| Same 18 configurations | 1.48 | 0.78 | 0.39 |
| Same nine flagship-and-above configurations | 1.07 | 0.49 | 0.39 |
| Same nine below-flagship configurations | 1.68 | 0.99 | 0.39 |

The flagship group includes Astra, all three Sol settings, Opus 5, Opus 4.8, Fable 5, GPT-5.5, and Kimi K3. Older flagships remain in that group. No configuration is excluded because of its measured consistency.

The full-book leaders remained consistent. On ATFW the below-flagship median range was about twice the flagship group's; KF did not show that group-level gap.

## Matched configuration table

| Configuration | Ender repeats | Ender range | ATFW repeats | ATFW range | KF repeats | KF range |
|---|---|---|---|---|---|---|
| claude-fable-5-medium | 2 | 0.08 | 2 | 0.49 | 2 | 0.31 |
| claude-haiku-4-5 | 3 | 3.38 | 2 | 0.08 | 2 | 0.18 |
| claude-opus-4-8-medium | 4 | 2.23 | 2 | 1.46 | 2 | 0.36 |
| claude-opus-5-medium | 3 | 0.87 | 2 | 0.10 | 2 | 0.68 |
| claude-sonnet-4-6-medium | 3 | 3.64 | 2 | 0.12 | 2 | 0.30 |
| claude-sonnet-5-high | 3 | 3.09 | 2 | 0.13 | 2 | 0.29 |
| claude-sonnet-5-medium | 3 | 2.22 | 2 | 2.96 | 2 | 0.39 |
| gpt-5.4-high | 3 | 1.68 | 3 | 1.48 | 3 | 0.39 |
| gpt-5.4-medium | 2 | 0.41 | 3 | 1.02 | 3 | 0.14 |
| gpt-5.5-medium | 2 | 1.31 | 3 | 0.33 | 3 | 0.39 |
| gpt-5.6-luna-high | 2 | 0.27 | 3 | 1.47 | 3 | 1.20 |
| gpt-5.6-sol-high | 2 | 0.61 | 3 | 0.85 | 3 | 0.56 |
| gpt-5.6-sol-low | 2 | 1.55 | 4 | 0.78 | 3 | 0.37 |
| gpt-5.6-sol-medium | 3 | 1.07 | 3 | 0.83 | 3 | 0.57 |
| gpt-5.6-terra-high | 2 | 1.63 | 3 | 0.99 | 3 | 0.79 |
| gpt-5.6-terra-medium | 2 | 1.41 | 3 | 0.77 | 3 | 0.72 |
| gpt-6-astra-medium | 2 | 0.35 | 2 | 0.18 | 2 | 0.04 |
| kimi-k3 | 2 | 1.81 | 2 | 0.38 | 2 | 0.78 |

## Interpretation limits

The final 30-configuration screen had median range 1.31. The retained 18 had median 1.48; the excluded 12 had median 1.12. Some wide-ranging models were removed, but the retained set was not collectively tighter in the screen.

These are small, unequal repeat samples on different texts and evaluation conditions. Averaging 27 or 34 chapter scores can smooth more variation than averaging four. Smaller book-average ranges do not prove that individual chapters became more reliable. The range is descriptive, not a statistical significance test.
