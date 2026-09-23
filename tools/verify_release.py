#!/usr/bin/env python3
"""Create once or verify a Booklab public-release checksum manifest."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent


def digest(path: Path) -> str:
    value = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            value.update(chunk)
    return value.hexdigest()


def protected_files() -> list[Path]:
    """Return published artifacts, excluding Git and the release-control machinery itself."""
    files = []
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        rel = path.relative_to(ROOT)
        if rel.parts[0] in {".git", "releases", "tools"}:
            continue
        files.append(path)
    return sorted(files, key=lambda item: item.relative_to(ROOT).as_posix())


def checksum_path(release_id: str) -> Path:
    release_dir = ROOT / "releases" / release_id
    manifest = release_dir / "manifest.json"
    if not manifest.is_file():
        raise SystemExit(f"missing release manifest: {manifest}")
    data = json.loads(manifest.read_text(encoding="utf-8"))
    if data.get("release_id") != release_id or data.get("status") != "published":
        raise SystemExit("release manifest must match the requested id and have status=published")
    return release_dir / "checksums.sha256"


def write_checksums(release_id: str) -> None:
    output = checksum_path(release_id)
    if output.exists():
        raise SystemExit(f"refusing to overwrite frozen checksums: {output}")
    files = [output.parent / "manifest.json", *protected_files()]
    lines = [f"{digest(path)}  {path.relative_to(ROOT).as_posix()}" for path in files]
    output.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    print(f"froze {len(lines)} files for {release_id}")


def verify(release_id: str) -> None:
    source = checksum_path(release_id)
    if not source.is_file():
        raise SystemExit(f"missing checksums: {source}")
    failures = []
    checked = 0
    for line in source.read_text(encoding="utf-8").splitlines():
        expected, rel = line.split("  ", 1)
        path = ROOT / rel
        if not path.is_file():
            failures.append(f"missing: {rel}")
        elif digest(path) != expected:
            failures.append(f"changed: {rel}")
        checked += 1
    if failures:
        raise SystemExit("release verification failed:\n" + "\n".join(failures))
    print(f"verified {checked} frozen files for {release_id}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("release_id")
    parser.add_argument("--write", action="store_true", help="create checksums once; refuses overwrite")
    args = parser.parse_args()
    if args.write:
        write_checksums(args.release_id)
    else:
        verify(args.release_id)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
