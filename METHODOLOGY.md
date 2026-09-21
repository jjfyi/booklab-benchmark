# Methodology and limits

[Overview](README.md)

## The task

Booklab Benchmark currently tests chapter analysis. Every chapter is a separate task with the same analysis instructions within its suite. Models do not accumulate context from previous chapters. The initial screen used four chapters of *Ender's Game*; the complete-book tests used all 27 chapters of *A Talent for War* and all 34 chapters of *Killing Floor*.

A configuration identifies the model and effort setting. Repeated runs let us inspect variation instead of relying on one answer. All 30 configurations in the final screen and all 18 in each full-book field have multiple runs.

Effort labels describe the setting requested within each provider's interface. They do not represent equivalent amounts of computation across providers, and higher effort does not guarantee a better result. The Opus 5 `standard` configuration is the benchmark's name for its low-effort setting. Codex configurations label that setting `low`. Gemini's effort is selected through its model variant. Kimi has no per-run effort control in this workflow, and Haiku 4.5 has no supported effort setting, so their configuration names have no effort suffix.

For long chapters, Kimi received its input through a local file instead of the inline delivery used by Claude and Codex. That changes the execution environment as well as the model. The comparisons describe the tested workflows; they do not isolate model behavior from every delivery detail.

## Quality

The quality scores are AI evaluations. Chapter reference keys were developed from the source text through independent candidate keys, with disagreements reconciled against the chapter before adoption. Each key defines what an analysis should capture and explain.

Opus 5 and Sol 5.6, both at medium effort, independently score anonymized analyses against the adopted keys without being told which model produced them. The two evaluations are averaged within each run, then run scores are averaged for each configuration. These are judgments against the benchmark's reference keys, rather than human ratings or an objective measure of every possible reading of a novel. The public release reports the combined results.

- **Recap (0–100):** fitness for remembering what happened.
- **Craft (0–100):** fitness for studying how the chapter works.
- **Overall (0–100):** equal-weight mean of recap and craft.

Component values and the overall value retain source precision in the data; displayed tables round to two decimal places. Tiny rounding discrepancies can occur because the source aggregates were stored separately.

Run range means the highest minus lowest overall run score, not a confidence interval. Unequal repeat counts affect the opportunity to observe a wider range.

## Subscription use

Quota is the share of the subscription's allowance consumed by the job, not a dollar charge and not elapsed time. A 25% reading means roughly one quarter of a fresh allowance. Segmented runs can sum to more than 100% when they span resets.

The five-hour charts compare plans costing roughly $20 per month under the tested conditions. Codex values use the reinstated-window period, rather than mixing earlier and later allowance regimes. Codex's reinstated five-hour limit applied to Plus, not Pro; the $20/$200 Codex comparison therefore uses weekly readings only.

A chart's quality point averages its scored repeats; its quota point can come from fewer eligible meter captures. It is not necessarily the cost of the average-quality execution. Clean measurements and estimates are distinguished in the data.

Fable has no direct $20 capture in these charts. Its measured $200 consumption is multiplied by 949/29, the pooled ratio from 12 matched Claude book/configuration comparisons. That factor is a task-specific empirical estimate, not a universal plan conversion. It is never applied to weekly usage.

## Weekly readings and dates

The measurements span July through September 2026. Weekly readings are net changes on rolling meters: old use can expire while new work is running. A 0% change does not mean zero consumption. One-point denominators on the $200 plans make ratios coarse.

The Claude runs benefited from a temporary weekly allowance increase. The [tier analysis](analysis/subscription-tiers.md#the-claude-weekly-promotion) distinguishes those measured readings from a conditional adjustment after the promotion. Historical results are not silently rewritten when a plan changes.

## Timing

Where supplied, the duration column is the recorded execution-duration aggregate from the reviewed evidence. It excludes any claim to total calendar wait across resets and resumptions. Timing varies with the environment and the provider's reporting convention; use it for coarse comparisons, not a precise prediction of your completion time. This public snapshot does not reconstruct missing timing fields.

One Killing Floor Sol-low run (`20260826T124227-0700-ea4ea2`) crossed a Codex command-line software update during execution. Its timing remains included in the published mean, but it is not a clean comparison of speed under one software version. It should not be used to establish the fastest Sol effort setting.

## What these results do not establish

These are a small set of texts, small and unequal repeat samples, and a particular chapter-analysis workflow. They do not measure whole-book conversational memory, every kind of knowledge work, or guaranteed books per allowance.

Compare scores within a suite and dated evidence cohort. Different texts, reference keys, and evaluation conditions mean absolute scores across suites are not directly interchangeable. Averaging 27 or 34 chapters can smooth variation more than averaging four; tighter book-level ranges do not prove that individual chapters became more reliable.

The repository publishes derived numeric results and documentation. It does not include copyrighted book text or claim to be a complete, independently runnable reproduction package.
