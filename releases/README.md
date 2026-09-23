# Dated releases

Each directory records one immutable published view of Booklab Benchmark. A release manifest names the evidence cohort and public destinations; `checksums.sha256` locks the files that readers saw.

The repository's main branch may gain later models and new dated data files. Historical releases are never regenerated or repriced. To verify one, check out its Git tag and run:

```text
python tools/verify_release.py <release-id>
```

## Releases

- `booklab-results-2026-09-23` — initial published baseline; September 6 Ender's Game evidence and September 16 full-book evidence.
