#!/usr/bin/env python3
"""
Enrich existing PR pages with additional metadata from GitHub/Gitee.

This script scans existing source-pr pages and updates them with:
- techniques (extracted from PR body keywords)
- hardware_features (extracted from PR body keywords)
- kernel_types (extracted from PR body keywords)
- languages (extracted from PR body keywords)

Usage:
    python3 scripts/enrich_pr_pages.py [--repo-filter org/name] [--dry-run]
"""

import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = ROOT / "data" / "tags.yaml"
SOURCES_DIR = ROOT / "sources" / "prs"

# Keyword mapping for enrichment
KEYWORD_MAPPINGS = {
    "kernel_types": {
        "matmul": ["matmul", "matrix multiplication", "gemm", "gemm-like"],
        "gemm": ["gemm", "general matrix multiply"],
        "attention": ["attention", "self-attention", "cross-attention"],
        "flash-attention": ["flash attention", "flashattention"],
        "moe": ["moe", "mixture of experts", "mixture-of-experts"],
        "grouped-gemm": ["grouped gemm", "grouped-gemm", "group gemm"],
        "softmax": ["softmax", "soft-max"],
        "layernorm": ["layer norm", "layernorm", "layer-norm"],
        "rmsnorm": ["rms norm", "rmsnorm", "rms-norm"],
        "elementwise": ["element-wise", "elementwise", "element wise"],
        "reduce": ["reduction", "reduce", "sum reduction"],
        "conv": ["convolution", "conv", "conv2d"],
        "embedding": ["embedding", "embed"],
        "activation": ["activation", "relu", "gelu", "sigmoid", "tanh"],
    },
    "hardware_features": {
        "cube-unit": ["cube", "cube unit", "matrix unit"],
        "vector-unit": ["vector", "vector unit", "simd"],
        "scalar-unit": ["scalar", "scalar unit"],
        "mte": ["mte", "memory transfer", "data movement"],
        "unified-buffer": ["unified buffer", "ub", "on-chip memory"],
        "l1-buffer": ["l1", "l1 buffer", "l1-cache"],
        "l0-buffer": ["l0", "l0 buffer", "register file"],
        "global-memory": ["global memory", "hbm", "ddr", "gm"],
        "nz-format": ["nz", "fractal_nz", "fractal nz", "nz format"],
        "nd-format": ["nd", "row major", "nd format"],
        "hccs": ["hccs", "interconnect", "npu link"],
    },
    "techniques": {
        "pipeline-scheduling": ["pipeline", "overlap", "schedule"],
        "double-buffering": ["double buffer", "ping-pong", "double buffering"],
        "nz-tiling": ["nz tiling", "tiling", "tile"],
        "cube-vector-overlap": ["cube vector", "overlap", "pipeline"],
        "bank-conflict-avoidance": ["bank conflict", "bank", "alignment"],
        "data-reuse": ["reuse", "data reuse", "cache"],
        "hccl-optimization": ["hccl", "communication", "collective"],
        "format-conversion": ["format conversion", "nd to nz", "nz to nd"],
    },
    "languages": {
        "ascendc": ["ascendc", "ascend c"],
        "tbe-dsl": ["tbe", "tbe-dsl", "tbe dsl"],
        "tbe-tik": ["tik", "tik-c", "tbe-tik"],
        "python": ["python", ".py"],
        "cpp": ["cpp", "c++", ".cpp", ".cc"],
    }
}


def load_tracked_repos():
    """Load tracked repositories from data/tags.yaml."""
    if not DATA_FILE.exists():
        return []

    with open(DATA_FILE) as f:
        data = yaml.safe_load(f)

    return data.get("tracked_repos", [])


def extract_frontmatter(content):
    """Extract YAML frontmatter from markdown content."""
    match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not match:
        return None, content

    frontmatter_str = match.group(1)
    body = content[match.end():]

    try:
        frontmatter = yaml.safe_load(frontmatter_str) or {}
        return frontmatter, body
    except yaml.YAMLError:
        return None, content


def generate_frontmatter(frontmatter):
    """Generate YAML frontmatter string from dict."""
    return f"---\n{yaml.dump(frontmatter, default_flow_style=False, sort_keys=False)}---"


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
        return None
    except json.JSONDecodeError:
        return None


def fetch_latest_pr_metadata(repo, pr_number):
    """Fetch latest PR metadata using GitHub CLI."""
    org = repo["org"]
    name = repo["name"]

    cmd = [
        "gh", "pr", "view",
        f"{org}/{name}",
        str(pr_number),
        "--json", "number,title,body,state,mergedAt",
        "--repo", f"{org}/{name}"
    ]

    cmd_str = " ".join(cmd)
    return run_gh_cli(cmd_str)


def extract_keywords_from_text(text, field_name):
    """Extract keywords from text based on mappings."""
    if not text:
        return []

    text_lower = text.lower()
    found_items = set()

    mapping = KEYWORD_MAPPINGS.get(field_name, {})

    for item_name, keywords in mapping.items():
        for keyword in keywords:
            if keyword.lower() in text_lower:
                found_items.add(item_name)
                break  # Found this item, move to next

    return sorted(list(found_items))


def enrich_pr_page(filepath, dry_run=False):
    """
    Enrich a single PR page with additional metadata.

    Args:
        filepath: Path to the PR markdown file
        dry_run: If True, print changes without writing

    Returns:
        Tuple of (success, changes_made)
    """
    # Read existing content
    with open(filepath) as f:
        content = f.read()

    # Extract frontmatter and body
    frontmatter, body = extract_frontmatter(content)

    if not frontmatter:
        print(f"  ⚠️  No valid frontmatter found: {filepath.name}")
        return False, []

    # Check if this is a source-pr page
    if frontmatter.get("type") != "source-pr":
        return False, []

    # Get PR information
    repo_str = frontmatter.get("repo", "")
    pr_number = frontmatter.get("pr")
    original_body = body

    if not repo_str or not pr_number:
        print(f"  ⚠️  Missing repo or pr field: {filepath.name}")
        return False, []

    # Parse repo string
    parts = repo_str.split("/")
    if len(parts) != 2:
        print(f"  ⚠️  Invalid repo format: {repo_str}")
        return False, []

    org, name = parts

    # Fetch latest PR metadata
    pr_metadata = fetch_latest_pr_metadata({"org": org, "name": name}, pr_number)

    if not pr_metadata:
        print(f"  ⚠️  Could not fetch PR metadata: {filepath.name}")
        return False, []

    # Get PR body for keyword extraction
    pr_body = pr_metadata.get("body", "")
    title = pr_metadata.get("title", "")

    # Combine title and body for keyword extraction
    combined_text = f"{title}\n{pr_body}"

    changes = []

    # Extract and enrich fields
    for field_name in ["kernel_types", "hardware_features", "techniques", "languages"]:
        existing = frontmatter.get(field_name, [])
        if not isinstance(existing, list):
            existing = []

        # Extract new keywords
        new_keywords = extract_keywords_from_text(combined_text, field_name)

        # Merge with existing (avoid duplicates)
        merged_keywords = sorted(list(set(existing + new_keywords)))

        if merged_keywords != existing:
            frontmatter[field_name] = merged_keywords
            changes.append(f"{field_name}: {existing} → {merged_keywords}")

    # Write back if changes were made
    if changes and not dry_run:
        new_frontmatter = generate_frontmatter(frontmatter)
        new_content = new_frontmatter + body

        with open(filepath, "w") as f:
            f.write(new_content)

        return True, changes
    elif changes and dry_run:
        return True, changes
    else:
        return False, []


def find_pr_pages(repo_filter=None):
    """Find all source-pr pages under sources/prs/."""
    if not SOURCES_DIR.exists():
        print(f"PR sources directory not found: {SOURCES_DIR}")
        return []

    pr_pages = []

    for md_file in SOURCES_DIR.rglob("*.md"):
        try:
            with open(md_file) as f:
                content = f.read()

            frontmatter, _ = extract_frontmatter(content)

            if frontmatter and frontmatter.get("type") == "source-pr":
                # Apply repo filter if specified
                if repo_filter:
                    repo = frontmatter.get("repo", "")
                    if repo != repo_filter:
                        continue

                pr_pages.append(md_file)

        except (IOError, yaml.YAMLError):
            continue

    return pr_pages


def main():
    parser = argparse.ArgumentParser(
        description="Enrich PR pages with additional metadata"
    )
    parser.add_argument(
        "--repo-filter",
        type=str,
        help="Filter to specific repo (e.g., 'Ascend/pytorch')"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview changes without writing files"
    )

    args = parser.parse_args()

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

    # Find all PR pages
    pr_pages = find_pr_pages(repo_filter=args.repo_filter)

    if not pr_pages:
        print("No PR pages found")
        return

    print(f"Found {len(pr_pages)} PR pages to process")

    if args.dry_run:
        print("[DRY RUN MODE] - No files will be modified")

    # Process each PR page
    total_enriched = 0
    total_changes = 0

    for filepath in pr_pages:
        print(f"\nProcessing: {filepath.relative_to(ROOT)}")

        success, changes = enrich_pr_page(filepath, dry_run=args.dry_run)

        if success:
            total_enriched += 1
            total_changes += len(changes)

            print(f"  ✓ Enriched with {len(changes)} changes:")
            for change in changes:
                print(f"    • {change}")
        else:
            if changes:  # Has changes but was dry run
                total_enriched += 1
                total_changes += len(changes)

    print(f"\n{'='*60}")
    print(f"Pages enriched: {total_enriched}/{len(pr_pages)}")
    print(f"Total changes: {total_changes}")

    if args.dry_run:
        print("[DRY RUN] No files modified")
    else:
        print("Files updated")


if __name__ == "__main__":
    main()
