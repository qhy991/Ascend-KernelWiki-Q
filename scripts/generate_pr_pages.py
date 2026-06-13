#!/usr/bin/env python3
"""
Generate source-pr pages from tracked repositories.

This script fetches recent merged PRs from tracked repositories (defined in
data/tags.yaml tracked_repos) and generates markdown files with source-pr frontmatter.

Usage:
    python3 scripts/generate_pr_pages.py [--days 30] [--limit 20] [--repo-filter org/name] [--dry-run]
"""

import argparse
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timedelta
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = ROOT / "data" / "tags.yaml"
SOURCES_DIR = ROOT / "sources" / "prs"

# Default configuration
DEFAULT_LOOKBACK_DAYS = 30
DEFAULT_PR_LIMIT = 20
DEFAULT_SEARCH_LIMIT = 50  # Internal search limit, we filter further


def load_tracked_repos():
    """Load tracked repositories from data/tags.yaml."""
    if not DATA_FILE.exists():
        print(f"Error: {DATA_FILE} not found", file=sys.stderr)
        sys.exit(1)

    with open(DATA_FILE) as f:
        data = yaml.safe_load(f)

    return data.get("tracked_repos", [])


def run_gh_cli(cmd):
    """Run GitHub CLI command and return parsed JSON output."""
    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            check=True,
            shell=True
        )
        return json.loads(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"GitHub CLI error: {e.stderr}", file=sys.stderr)
        return []
    except json.JSONDecodeError as e:
        print(f"Failed to parse GitHub CLI output: {e}", file=sys.stderr)
        return []


def fetch_merged_prs(repo, days=30, limit=50):
    """
    Fetch merged PRs from a repository using GitHub CLI.

    Args:
        repo: dict with 'org' and 'name' keys
        days: lookback period in days
        limit: maximum number of PRs to fetch

    Returns:
        List of PR dictionaries
    """
    org = repo["org"]
    name = repo["name"]
    since_date = (datetime.now() - timedelta(days=days)).strftime("%Y-%m-%d")

    # GitHub CLI search query for merged PRs
    query = f"repo:{org}/{name} is:pr is:merged merged:>={since_date}"
    cmd = [
        "gh", "search", "prs",
        "--query", query,
        "--json", "number,title,author,url,mergedAt,body,state",
        "--limit", str(limit),
        "--search", "issues"  # Use issues search for better PR filtering
    ]

    # Construct command string
    cmd_str = " ".join(cmd)

    prs = run_gh_cli(cmd_str)

    # Filter to ensure we only get merged PRs
    merged_prs = [pr for pr in prs if pr.get("state") == "MERGED"]

    return merged_prs[:limit]


def slugify(text):
    """Convert text to URL-friendly slug."""
    # Convert to lowercase and replace spaces with hyphens
    slug = text.lower().strip()
    # Remove special characters except hyphens and alphanumeric
    slug = re.sub(r'[^\w\s-]', '', slug)
    # Replace spaces and multiple hyphens with single hyphen
    slug = re.sub(r'[-\s]+', '-', slug)
    return slug


def generate_pr_page(pr, repo, output_dir, dry_run=False):
    """
    Generate a markdown page for a single PR.

    Args:
        pr: PR dictionary from GitHub CLI
        repo: repository dict with 'org' and 'name'
        output_dir: base directory for output
        dry_run: if True, print content instead of writing

    Returns:
        Tuple of (filepath, generated_content)
    """
    org = repo["org"]
    name = repo["name"]
    repo_slug = f"{org.lower()}-{name.lower()}"

    pr_number = pr["number"]
    pr_title = pr["title"]
    author = pr.get("author", {}).get("login", "unknown")
    merged_at = pr.get("mergedAt", "")
    url = pr["url"]
    body = pr.get("body", "")

    # Create unique ID
    pr_id = f"pr-{repo_slug}-{pr_number}"

    # Parse merged_at date
    try:
        merged_date = datetime.fromisoformat(merged_at.replace("Z", "+00:00")).strftime("%Y-%m-%d")
    except (ValueError, AttributeError):
        merged_date = datetime.now().strftime("%Y-%m-%d")

    # Generate directory structure
    target_dir = output_dir / repo_slug
    if not dry_run:
        target_dir.mkdir(parents=True, exist_ok=True)

    # Generate filename
    filename = f"PR-{pr_number}.md"
    filepath = target_dir / filename

    # Truncate body for preview (first 500 chars)
    body_preview = body[:500] if body else "No description provided."

    # Get current date
    today = datetime.now().strftime("%Y-%m-%d")

    # Add truncation note if body was truncated
    truncation_note = ""
    if len(body) > 500:
        truncation_note = f"...\\n\\n*[Full description truncated ({len(body)} chars)]*"

    # Generate frontmatter
    frontmatter = f"""---
id: {pr_id}
title: "{pr_title}"
type: source-pr
repo: {org}/{name}
pr: {pr_number}
author: {author}
date: '{merged_date}'
url: {url}
source_category: upstream-code
architectures: [ascend910, ascend910b]
tags: [auto-generated]
captured_at: '{today}'
status: merged
inclusion_reason: "Auto-captured from tracked repository"
---

## {pr_title}

**PR**: [{org}/{name}#{pr_number}]({url})
**Author**: @{author}
**Merged**: {merged_date}

### Description

{body_preview}

{truncation_note}
"""

    if dry_run:
        print(f"\n[DRY RUN] Would create: {filepath}")
        print(f"--- {frontmatter} ---")
    else:
        with open(filepath, "w") as f:
            f.write(frontmatter)

    return (str(filepath), frontmatter)


def main():
    parser = argparse.ArgumentParser(
        description="Generate source-pr pages from tracked repositories"
    )
    parser.add_argument(
        "--days",
        type=int,
        default=DEFAULT_LOOKBACK_DAYS,
        help=f"Lookback period in days (default: {DEFAULT_LOOKBACK_DAYS})"
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=DEFAULT_PR_LIMIT,
        help=f"Maximum PRs per repository (default: {DEFAULT_PR_LIMIT})"
    )
    parser.add_argument(
        "--repo-filter",
        type=str,
        help="Filter to specific repo (e.g., 'Ascend/pytorch')"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview without writing files"
    )

    args = parser.parse_args()

    # Load tracked repositories
    repos = load_tracked_repos()

    if not repos:
        print("No tracked repositories found in data/tags.yaml")
        return

    # Apply repo filter if specified
    if args.repo_filter:
        repos = [r for r in repos if f"{r['org']}/{r['name']}" == args.repo_filter]
        if not repos:
            print(f"Repository '{args.repo_filter}' not found in tracked_repos")
            return

    print(f"Fetching PRs from {len(repos)} repositories (last {args.days} days)")
    print(f"Limit: {args.limit} PRs per repository")

    if args.dry_run:
        print("[DRY RUN MODE] - No files will be written")

    # Check if GitHub CLI is available
    try:
        subprocess.run(
            ["gh", "--version"],
            capture_output=True,
            check=True,
            shell=False
        )
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("Error: GitHub CLI (gh) not found or not working", file=sys.stderr)
        print("Install from: https://cli.github.com/")
        sys.exit(1)

    # Process each repository
    total_prs = 0
    for repo in repos:
        org = repo["org"]
        name = repo["name"]
        print(f"\nProcessing: {org}/{name}")

        # Fetch merged PRs
        prs = fetch_merged_prs(repo, days=args.days, limit=DEFAULT_SEARCH_LIMIT)
        prs = prs[:args.limit]  # Apply user limit

        if not prs:
            print(f"  No merged PRs found")
            continue

        print(f"  Found {len(prs)} merged PRs")

        # Generate pages for each PR
        for pr in prs:
            filepath, content = generate_pr_page(
                pr, repo, SOURCES_DIR, dry_run=args.dry_run
            )
            total_prs += 1

    print(f"\n{'='*60}")
    print(f"Total PRs processed: {total_prs}")

    if not args.dry_run:
        print(f"Pages written to: {SOURCES_DIR}")
    else:
        print("[DRY RUN] No files written")


if __name__ == "__main__":
    main()
