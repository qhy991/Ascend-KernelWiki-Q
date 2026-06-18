"""Regression tests for Ascend-KernelWiki-Q query behavior."""

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import query  # noqa: E402


def test_short_type_alias_kernel_matches_wiki_kernel_pages():
    pages = query.collect_pages()

    results = query.filter_pages(pages, type="kernel")

    assert results
    assert all(page["type"] == "wiki-kernel" for page in results)


def test_short_type_alias_pr_matches_source_pr_pages():
    pages = query.collect_pages()

    results = query.filter_pages(pages, type="pr")

    assert results
    assert all(page["type"] == "source-pr" for page in results)


def test_has_recipe_filter_matches_operator_recipe_pages():
    pages = [
        {"type": "wiki-kernel", "operator_recipe": {"operator": "matmul"}, "tags": [], "architectures": []},
        {"type": "wiki-kernel", "tags": [], "architectures": []},
    ]

    results = query.filter_pages(pages, has_recipe=True)

    assert results == [pages[0]]


def test_query_supports_common_operator_filter():
    result = subprocess.run(
        [sys.executable, "scripts/query.py", "--type", "kernel", "--operator", "matmul", "--limit", "3"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )

    assert result.returncode == 0, result.stderr
    assert "kernel-matmul-ascendc" in result.stdout


def test_get_page_supports_common_frontmatter_body_aliases():
    frontmatter = subprocess.run(
        [sys.executable, "scripts/get_page.py", "kernel-matmul-ascendc", "--frontmatter-only"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    assert frontmatter.returncode == 0, frontmatter.stderr
    assert "id: kernel-matmul-ascendc" in frontmatter.stdout

    body = subprocess.run(
        [sys.executable, "scripts/get_page.py", "kernel-matmul-ascendc", "--body-only"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    assert body.returncode == 0, body.stderr
    assert "id: kernel-matmul-ascendc" not in body.stdout
    assert "Matmul" in body.stdout


def test_generate_indices_writes_common_manifest_files():
    result = subprocess.run(
        [sys.executable, "scripts/generate-indices.py"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )

    assert result.returncode == 0, result.stderr
    index = ROOT / "queries" / "INDEX.md"
    manifest = ROOT / "queries" / "pages.json"
    assert index.exists()
    assert manifest.exists()

    records = json.loads(manifest.read_text(encoding="utf-8"))
    assert any(record["id"] == "kernel-matmul-ascendc" for record in records)
