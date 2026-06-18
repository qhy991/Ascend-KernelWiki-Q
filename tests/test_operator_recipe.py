"""Regression tests for structured Ascend operator recipes."""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import validate  # noqa: E402


CORE_RECIPE_PAGES = [
    "wiki/kernels/matmul-ascendc.md",
    "wiki/kernels/quant-matmul-ascendc.md",
    "wiki/kernels/paged-attention-npu.md",
    "wiki/kernels/rmsnorm-ascendc.md",
]


def test_incomplete_operator_recipe_is_validation_error(tmp_path):
    page = tmp_path / "kernel-test.md"
    page.write_text(
        """---
id: kernel-test-recipe
title: "Recipe Test"
type: wiki-kernel
architectures: [ascend910b]
tags: [matmul]
confidence: source-reported
kernel_types: [matmul]
languages: [ascendc]
sources: []
operator_recipe:
  operator: matmul
  dtype: [fp16]
---

# Recipe Test
""",
        encoding="utf-8",
    )

    errors, warnings = validate.validate_page(
        page,
        validate.load_schemas(),
        validate.load_tags(),
        {},
    )

    assert warnings == []
    assert any(error["error"] == "incomplete_operator_recipe" for error in errors)


def test_core_kernel_pages_have_valid_operator_recipes():
    schemas = validate.load_schemas()
    tags = validate.load_tags()
    all_ids = validate.collect_all_ids()

    for rel_path in CORE_RECIPE_PAGES:
        path = ROOT / rel_path
        fm, _ = validate.extract_frontmatter(path)
        errors, warnings = validate.validate_page(path, schemas, tags, all_ids)

        assert "operator_recipe" in fm, rel_path
        assert errors == [], rel_path
        assert warnings == [], rel_path
