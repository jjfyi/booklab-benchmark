# Killing Floor: full results

[Suite overview](README.md) · [Methodology](../../METHODOLOGY.md) · [Numeric data](data/results-2026-09-16.json)

Snapshot: 2026-09-16. All 18 configurations are shown, sorted by mean overall quality. Overall is the equal-weight mean of recap and craft. “Range” is the highest minus lowest overall run score. Repeats are included to show the evidence behind the means, not as the headline measure of coverage.

| Configuration | Repeats | Overall | Recap | Craft | Run range | Recorded minutes |
|---|---|---|---|---|---|---|
| gpt-6-astra-medium | 2 | 90.51 | 92.97 | 88.05 | 0.04 | 73.82 |
| gpt-5.6-sol-high | 3 | 89.17 | 91.53 | 86.82 | 0.56 | 59.94 |
| gpt-5.6-sol-medium | 3 | 88.98 | 91.51 | 86.45 | 0.57 | 52.90 |
| gpt-5.6-sol-low | 3 | 88.77 | 90.85 | 86.68 | 0.37 | 57.18 |
| claude-opus-5-medium | 2 | 87.63 | 89.90 | 85.35 | 0.68 | 47.69 |
| claude-fable-5-medium | 2 | 87.16 | 90.82 | 83.49 | 0.31 | 40.39 |
| gpt-5.5-medium | 3 | 86.26 | 90.04 | 82.49 | 0.39 | 38.74 |
| kimi-k3 | 2 | 86.02 | 89.95 | 82.10 | 0.78 | 62.65 |
| gpt-5.4-high | 3 | 84.59 | 90.46 | 78.72 | 0.39 | 45.28 |
| gpt-5.4-medium | 3 | 83.98 | 89.61 | 78.35 | 0.14 | 33.46 |
| gpt-5.6-terra-high | 3 | 83.65 | 89.93 | 77.37 | 0.79 | 31.38 |
| gpt-5.6-terra-medium | 3 | 83.64 | 89.68 | 77.60 | 0.72 | 32.59 |
| claude-opus-4-8-medium | 2 | 83.11 | 89.32 | 76.89 | 0.36 | 32.63 |
| claude-sonnet-4-6-medium | 2 | 80.90 | 86.18 | 75.63 | 0.30 | 49.73 |
| claude-sonnet-5-high | 2 | 80.86 | 87.61 | 74.12 | 0.29 | 38.43 |
| gpt-5.6-luna-high | 3 | 80.43 | 88.34 | 72.51 | 1.20 | 40.85 |
| claude-sonnet-5-medium | 2 | 79.87 | 87.13 | 72.62 | 0.39 | 27.47 |
| claude-haiku-4-5 | 2 | 77.84 | 84.38 | 71.30 | 0.18 | 56.91 |

Recorded minutes are the mean of the source execution-duration aggregates, not reset-inclusive calendar wait. [Five-hour quota values](quality-vs-five-hour.md) and [weekly/tier readings](subscription-tiers.md) are separate because their eligible measurements need not cover every scored repeat.

## Individual scored runs

Run identifiers begin with their recorded start date. Scores below are the combined evaluation results, not separate evaluator scores.

Recorded minutes show each run's analysis duration, excluding reset waits, rounded from the numeric snapshot. Sol-low run `20260826T124227-0700-ea4ea2` crossed a command-line software update; its timing is included but is not a clean comparison under one software version. See the [timing qualification](../../METHODOLOGY.md#timing).

| Configuration | Run | Overall | Recap | Craft | Recorded minutes |
|---|---|---|---|---|---|
| gpt-6-astra-medium | 20260905T113913-0700-6bca83 | 90.53 | 92.97 | 88.10 | 74.11 |
| gpt-6-astra-medium | 20260905T131153-0700-d603c7 | 90.49 | 92.98 | 88.00 | 73.53 |
| gpt-5.6-sol-high | 20260824T143553-0700-31d46b | 88.85 | 91.13 | 86.57 | 61.00 |
| gpt-5.6-sol-high | 20260824T190631-0700-49ebe1 | 89.26 | 91.71 | 86.81 | 72.17 |
| gpt-5.6-sol-high | 20260826T202250-0700-17f4b6 | 89.41 | 91.75 | 87.07 | 46.64 |
| gpt-5.6-sol-medium | 20260710T120000-0700-f8c2c5 | 88.63 | 91.31 | 85.95 | 58.68 |
| gpt-5.6-sol-medium | 20260811T101407-0700-2fafa9 | 89.20 | 91.35 | 87.05 | 59.16 |
| gpt-5.6-sol-medium | 20260826T143251-0700-affc5e | 89.10 | 91.86 | 86.34 | 40.86 |
| gpt-5.6-sol-low | 20260824T133233-0700-09b46c | 88.95 | 90.94 | 86.96 | 55.57 |
| gpt-5.6-sol-low | 20260824T170156-0700-9f6395 | 88.77 | 91.05 | 86.49 | 70.52 |
| gpt-5.6-sol-low | 20260826T124227-0700-ea4ea2 | 88.58 | 90.58 | 86.58 | 45.46 |
| claude-opus-5-medium | 20260731T132955-0700-ec1042 | 87.97 | 90.12 | 85.81 | 49.35 |
| claude-opus-5-medium | 20260816T123736-0700-707b4e | 87.28 | 89.69 | 84.88 | 46.04 |
| claude-fable-5-medium | 20260729T204023-0700-a39ec1 | 87.00 | 90.72 | 83.28 | 41.41 |
| claude-fable-5-medium | 20260823T174941-0700-7c2e09 | 87.31 | 90.93 | 83.70 | 39.37 |
| gpt-5.5-medium | 20260809T092119-0700-f6cd39 | 86.12 | 89.70 | 82.54 | 40.47 |
| gpt-5.5-medium | 20260811T114657-0700-7841a2 | 86.51 | 90.54 | 82.47 | 40.11 |
| gpt-5.5-medium | 20260827T113449-0700-6cc2a8 | 86.16 | 89.87 | 82.45 | 35.66 |
| kimi-k3 | 20260729T200540-0700-6117a3 | 85.63 | 89.43 | 81.84 | 72.12 |
| kimi-k3 | 20260815T072644-0700-5abc92 | 86.42 | 90.47 | 82.36 | 53.17 |
| gpt-5.4-high | 20260720T212105-0700-f1c8ca | 84.85 | 90.74 | 78.96 | 45.82 |
| gpt-5.4-high | 20260811T214435-0700-427510 | 84.46 | 90.26 | 78.66 | 44.76 |
| gpt-5.4-high | 20260827T130312-0700-e149fa | 84.46 | 90.38 | 78.53 | 45.27 |
| gpt-5.4-medium | 20260809T082916-0700-451f64 | 83.96 | 89.77 | 78.15 | 33.43 |
| gpt-5.4-medium | 20260811T123302-0700-0deb11 | 83.92 | 89.72 | 78.12 | 33.62 |
| gpt-5.4-medium | 20260827T144400-0700-9f9bfc | 84.06 | 89.32 | 78.79 | 33.33 |
| gpt-5.6-terra-high | 20260721T131426-0700-6182f5 | 83.13 | 89.62 | 76.63 | 30.85 |
| gpt-5.6-terra-high | 20260823T214410-0700-96ba86 | 83.91 | 90.19 | 77.63 | 32.26 |
| gpt-5.6-terra-high | 20260827T155321-0700-1f7b53 | 83.92 | 89.97 | 77.86 | 31.05 |
| gpt-5.6-terra-medium | 20260729T202215-0700-4980dc | 83.64 | 89.61 | 77.66 | 30.38 |
| gpt-5.6-terra-medium | 20260811T131904-0700-365870 | 84.00 | 90.09 | 77.91 | 31.84 |
| gpt-5.6-terra-medium | 20260827T093739-0700-7dd601 | 83.28 | 89.35 | 77.22 | 35.56 |
| claude-opus-4-8-medium | 20260801T105126-0700-ad3122 | 82.93 | 89.32 | 76.53 | 32.60 |
| claude-opus-4-8-medium | 20260815T175632-0700-a98282 | 83.28 | 89.32 | 77.24 | 32.65 |
| claude-sonnet-4-6-medium | 20260808T211749-0700-654521 | 80.75 | 86.01 | 75.48 | 52.74 |
| claude-sonnet-4-6-medium | 20260816T071830-0700-5de6ed | 81.05 | 86.34 | 75.77 | 46.73 |
| claude-sonnet-5-high | 20260731T150747-0700-83d249 | 81.01 | 87.57 | 74.45 | 39.05 |
| claude-sonnet-5-high | 20260815T133329-0700-248053 | 80.72 | 87.65 | 73.78 | 37.81 |
| gpt-5.6-luna-high | 20260809T101711-0700-fe3cc9 | 79.88 | 87.98 | 71.78 | 39.05 |
| gpt-5.6-luna-high | 20260811T135320-0700-84e84f | 80.32 | 88.27 | 72.36 | 43.02 |
| gpt-5.6-luna-high | 20260827T104339-0700-b5860d | 81.08 | 88.76 | 73.40 | 40.49 |
| claude-sonnet-5-medium | 20260801T102027-0700-8b46f5 | 80.07 | 86.80 | 73.34 | 29.07 |
| claude-sonnet-5-medium | 20260815T072257-0700-eac7e8 | 79.68 | 87.47 | 71.89 | 25.87 |
| claude-haiku-4-5 | 20260809T082945-0700-6b1c09 | 77.93 | 83.94 | 71.92 | 54.89 |
| claude-haiku-4-5 | 20260815T114449-0700-de52b1 | 77.75 | 84.83 | 70.67 | 58.93 |
