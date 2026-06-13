#!/usr/bin/env python3
"""
Auto-tag PR pages with kernel_type, ext_lang, techniques, hw_features, arch.

Usage:
    python3 scripts/reclassify_pr_pages.py [--dry-run] [--verbose]
"""

import argparse, re, sys, yaml
from pathlib import Path
from collections import Counter

ROOT = Path(__file__).resolve().parent.parent
SOURCES_DIR = ROOT / "sources" / "prs"

# Kernel type classification (same as ROCm)
KERNEL_TYPE_RULES = {
    "gemm": r"gemm|matmul|matrix.?multiply",
    "attention": r"attention|attn|flash.?attention|fa[0-9]|fa\.",
    "moe": r"moe|mixture.?of.?experts|expert.?dispatch|routing",
    "conv": r"conv|convolution",
    "reduction": r"reduc|sum|prod|norm",
    "softmax": r"soft|max",
    "layernorm": r"layer.?ln|ln_|layernorm",
    "rmsnorm": r"rms|norm",
    "embedding": r"embed|lookup|vocab",
}

# Extension language mapping (Ascend-specific)
EXT_LANG = {
    ".cpp": "ascendc",
    ".hpp": "ascendc",
    ".h": "ascendc",
    ".py": "python",
    ".sh": "bash",
}

# Technique patterns (Ascend-specific)
TECHNIQUE_RULES = {
    "pipeline-scheduling": r"pipeline|schedul|stage",
    "double-buffering": r"double.buffer|prefetch",
    "nz-tiling": r"nz.?tiling|fractal.?nz",
    "cube-vector-overlap": r"cube.?vector|overlap",
    "bank-conflict-avoidance": r"bank.?conflict|ub.?pad",
    "data-reuse": r"data.?reuse|ub.?reuse",
    "hccl-optimization": r"hccl|collective",
    "format-conversion": r"format.?convert|nd.?to.?nz",
}

# Hardware feature patterns (Ascend-specific)
HW_RULES = {
    "cube-unit": r"cube|matrix.?unit",
    "vector-unit": r"vector|simd",
    "unified-buffer": r"unified.?buffer|\bub\b",
    "nz-format": r"fractal.?nz|nz.?format",
    "hccs": r"hccs",
}

# Architecture patterns (Ascend-specific)
ARCH_RULES = {
    "ascend910b": r"910b|910-b",
    "ascend910": r"910a|910[^b]",
    "ascend310p": r"310p",
}

DEFAULT_ARCH_TRIPLE = ["ascend910", "ascend910b"]

def extract_frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", text, re.DOTALL)
    if not m:
        return {}, text
    try:
        return (yaml.safe_load(m.group(1)) or {}), m.group(2)
    except yaml.YAMLError:
        return {}, text

def infer_tags(text, rules, max_matches=3):
    tags = []
    for tag, pat in rules.items():
        if re.search(pat, text, re.IGNORECASE):
            tags.append(tag)
            if len(tags) >= max_matches:
                break
    return tags

def classify_page(path, dry_run, verbose, stats):
    text = path.read_text(encoding="utf-8")
    fm, body = extract_frontmatter(text)
    if fm.get("type") != "source-pr":
        return False
    stats["total"] += 1

    full_text = f"{fm.get('title', '')} {body}".lower()
    sources = fm.get("sources", {})
    source_list = sources.get("list", []) if isinstance(sources, dict) else sources
    source_text = " ".join(str(s).lower() for s in source_list)

    changed = False
    updates = {}

    # Infer kernel_type
    if not fm.get("kernel_type"):
        ktypes = infer_tags(full_text, KERNEL_TYPE_RULES)
        if ktypes:
            fm["kernel_type"] = ktypes[0]
            updates["kernel_type"] = ktypes[0]
            changed = True
            stats["kernel_type"] += 1

    # Infer ext_lang
    if not fm.get("ext_lang"):
        langs = []
        for ext, lang in EXT_LANG.items():
            if ext in source_text or any(ext in str(s).lower() for s in source_list):
                if lang not in langs:
                    langs.append(lang)
        if langs:
            fm["ext_lang"] = langs
            updates["ext_lang"] = langs
            changed = True
            stats["ext_lang"] += 1

    # Infer techniques
    if not fm.get("techniques"):
        techs = infer_tags(full_text, TECHNIQUE_RULES, max_matches=5)
        if techs:
            fm["techniques"] = techs
            updates["techniques"] = techs
            changed = True
            stats["techniques"] += 1

    # Infer hw_features
    if not fm.get("hw_features"):
        hw = infer_tags(full_text, HW_RULES)
        if hw:
            fm["hw_features"] = hw
            updates["hw_features"] = hw
            changed = True
            stats["hw_features"] += 1

    # Infer arch (default if none match)
    if not fm.get("arch"):
        archs = []
        for arch, pat in ARCH_RULES.items():
            if re.search(pat, full_text, re.IGNORECASE):
                archs.append(arch)
        if not archs:
            archs = DEFAULT_ARCH_TRIPLE
        fm["arch"] = archs
        updates["arch"] = archs
        changed = True
        stats["arch"] += 1

    if changed and not dry_run:
        new_text = "---\n" + yaml.safe_dump(fm, sort_keys=False).strip() + "\n---\n\n" + body.lstrip("\n")
        path.write_text(new_text, encoding="utf-8")

    if verbose and changed:
        print(f"{path.relative_to(ROOT)}")
        for k, v in updates.items():
            print(f"  {k}: {v}")

    if changed:
        stats["updated"] += 1
    return changed

def main():
    ap = argparse.ArgumentParser(description="Auto-classify PR pages")
    ap.add_argument("--dry-run", action="store_true", help="don't write changes")
    ap.add_argument("--verbose", "-v", action="store_true", help="show updated fields")
    args = ap.parse_args()

    stats = Counter()
    if not SOURCES_DIR.exists():
        print("No sources/prs/ directory found")
        return 0

    for path in sorted(SOURCES_DIR.rglob("PR-*.md")):
        classify_page(path, args.dry_run, args.verbose, stats)

    print(f"Processed {stats['total']} PR pages{' (dry-run)' if args.dry_run else ''}")
    print(f"Updated: {stats['updated']}")
    for k in ("kernel_type", "ext_lang", "techniques", "hw_features", "arch"):
        if stats[k]:
            print(f"  {k:18} {stats[k]}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
