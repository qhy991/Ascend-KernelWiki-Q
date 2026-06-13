#!/usr/bin/env python3
"""
Repair common issues in source-pr pages (fix dates, normalize fields).

Usage:
    python3 scripts/repair_pr_pages.py [--dry-run]
"""

import argparse, re, yaml
from pathlib import Path
from collections import Counter

ROOT = Path(__file__).resolve().parent.parent
SOURCES_DIR = ROOT / "sources" / "prs"

def extract_frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", text, re.DOTALL)
    if not m:
        return {}, text
    try:
        return (yaml.safe_load(m.group(1)) or {}), m.group(2)
    except yaml.YAMLError:
        return {}, text

def repair_page(path, dry_run, stats):
    text = path.read_text(encoding="utf-8")
    fm, body = extract_frontmatter(text)
    if fm.get("type") != "source-pr":
        return False
    changed = False

    # Ensure status is lowercase
    status = fm.get("status", "")
    if status and status != status.lower():
        fm["status"] = status.lower()
        changed = True
        stats["fixed_status"] += 1

    # Ensure date is string format
    date = fm.get("date")
    if date and not isinstance(date, str):
        fm["date"] = str(date)
        changed = True
        stats["fixed_date"] += 1

    # Ensure captured_at exists
    if "captured_at" not in fm:
        fm["captured_at"] = "2026-06-13"
        changed = True
        stats["added_captured_at"] += 1

    if changed and not dry_run:
        new_text = "---\n" + yaml.safe_dump(fm, sort_keys=False).strip() + "\n---\n\n" + body.lstrip("\n")
        path.write_text(new_text, encoding="utf-8")
    if changed:
        stats["pages_changed"] += 1
    return changed

def main():
    ap = argparse.ArgumentParser(description="Repair PR page issues")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    stats = Counter()
    total = 0
    if not SOURCES_DIR.exists():
        print("No sources/prs/ directory found")
        return 0

    for path in sorted(SOURCES_DIR.rglob("PR-*.md")):
        total += 1
        repair_page(path, args.dry_run, stats)

    print(f"Scanned {total} PR pages{' (dry-run)' if args.dry_run else ''}")
    for k in ("pages_changed", "fixed_status", "fixed_date", "added_captured_at"):
        print(f"  {k:26} {stats[k]}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
