#!/usr/bin/env python3
"""Generate source-doc pages from data/source-docs.yaml."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_CATALOG = ROOT / "data" / "source-docs.yaml"
DEFAULT_OUTPUT_DIR = ROOT / "sources" / "docs"


@dataclass
class WriteStats:
    written: int = 0
    skipped_existing: int = 0


def load_catalog(path: Path = DEFAULT_CATALOG) -> list[dict]:
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    return data.get("source_docs", [])


def render_page(entry: dict) -> str:
    frontmatter = {
        "id": entry["id"],
        "title": entry["title"],
        "type": "source-doc",
        "architectures": entry["architectures"],
        "tags": entry["tags"],
        "date": str(entry["date"]),
        "url": entry["url"],
    }
    for field in ("hardware_features", "techniques", "confidence", "aliases"):
        if entry.get(field):
            frontmatter[field] = entry[field]

    body = f"""# {entry["title"]}

{entry["summary"].strip()}

## Source

- {entry["url"]}
"""
    return "---\n" + yaml.safe_dump(frontmatter, sort_keys=False).strip() + "\n---\n\n" + body


def write_pages(entries: list[dict], output_dir: Path = DEFAULT_OUTPUT_DIR, force: bool = False) -> WriteStats:
    output_dir.mkdir(parents=True, exist_ok=True)
    stats = WriteStats()
    for entry in entries:
        path = output_dir / f"{entry['slug']}.md"
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
    print(f"Source-doc catalog entries: {len(entries)}")
    print(f"Written: {stats.written}")
    print(f"Skipped existing: {stats.skipped_existing}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
