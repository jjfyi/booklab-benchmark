# Dated releases

Each directory records one immutable published view of Booklab Benchmark. A release manifest names the evidence cohort and public destinations; `checksums.sha256` locks the files that readers saw.

The repository's main branch may gain later models and new dated data files. Historical releases are never regenerated or repriced. To verify a release's original files from a maintained checkout, run:

```text
python tools/verify_release.py <release-id>
```

The verifier treats LF and CRLF as equivalent for text files, while checking images byte-for-byte. The September 23 tag's original `checksums.sha256` was made from a working copy with mixed line endings; it remains untouched. A separate `checksums-portable.sha256` records the same 33 files with normalized text line endings, so the maintained verifier can check Windows and Unix checkouts without moving the tag or changing evidence.

## Releases

- `booklab-results-2026-09-23` — initial published baseline; September 6 Ender's Game evidence and September 16 full-book evidence.
