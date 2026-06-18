#!/usr/bin/env python3
"""Generate source-code evidence pages from data/source-code.yaml."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_CATALOG = ROOT / "data" / "source-code.yaml"
DEFAULT_OUTPUT_DIR = ROOT / "sources" / "code"


@dataclass
class WriteStats:
    written: int = 0
    skipped_existing: int = 0


def load_catalog(path: Path = DEFAULT_CATALOG) -> list[dict]:
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    return data.get("source_code", [])


def render_page(entry: dict) -> str:
    frontmatter = {
        "id": entry["id"],
        "title": entry["title"],
        "type": "source-code",
        "repo": entry["repo"],
        "path": entry["path"],
        "url": entry["url"],
        "source_category": entry.get("source_category", "upstream-code"),
        "architectures": entry["architectures"],
        "tags": entry["tags"],
        "date": str(entry["date"]),
        "captured_at": str(entry.get("captured_at", entry["date"])),
        "confidence": entry.get("confidence", "source-reported"),
    }
    for field in ("hardware_features", "techniques", "kernel_types", "languages", "aliases"):
        if entry.get(field):
            frontmatter[field] = entry[field]

    body = f"""# {entry["title"]}

{entry["summary"].strip()}

## Code Location

- Repository: `{entry["repo"]}`
- Path: `{entry["path"]}`
- URL: {entry["url"]}
"""
    return "---\n" + yaml.safe_dump(frontmatter, sort_keys=False).strip() + "\n---\n\n" + body


def write_pages(entries: list[dict], output_dir: Path = DEFAULT_OUTPUT_DIR, force: bool = False) -> WriteStats:
    output_dir.mkdir(parents=True, exist_ok=True)
    stats = WriteStats()
    for entry in entries:
        repo_key = entry.get("repo_key") or entry["repo"].replace("/", "-").lower()
        repo_dir = output_dir / repo_key
        repo_dir.mkdir(parents=True, exist_ok=True)
        path = repo_dir / f"{entry['slug']}.md"
        if path.exists() and not force:
            stats.skipped_existing += 1
            continue
        path.write_text(render_page(entry), encoding="utf-8")
        stats.written += 1
    return stats


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--catalog", type=Path, default=DEFAULT_CATALOG)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    entries = load_catalog(args.catalog)
    stats = write_pages(entries, output_dir=args.output_dir, force=args.force)
    print(f"Source-code catalog entries: {len(entries)}")
    print(f"Written: {stats.written}")
    print(f"Skipped existing: {stats.skipped_existing}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
