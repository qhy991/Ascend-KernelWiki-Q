"""Regression tests for source-code evidence pages."""

import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import generate_source_code_pages as gen  # noqa: E402
import query  # noqa: E402
import validate  # noqa: E402


def test_render_source_code_page_validates(tmp_path):
    page = tmp_path / "catlass-basic-matmul.md"
    page.write_text(gen.render_page({
        "id": "code-catlass-basic-matmul",
        "title": "CATLASS Basic Matmul Example",
        "slug": "catlass-basic-matmul",
        "repo": "Ascend/catlass",
        "path": "examples/00_basic_matmul",
        "url": "https://gitee.com/ascend/catlass/tree/master/examples/00_basic_matmul",
        "date": "2026-06-18",
        "architectures": ["ascend910b"],
        "tags": ["catlass", "matmul", "cpp", "ascendc"],
        "kernel_types": ["matmul", "gemm"],
        "languages": ["cpp", "ascendc"],
        "hardware_features": ["cube-unit", "l1-buffer", "l0-buffer"],
        "techniques": ["nz-tiling", "pipeline-scheduling"],
        "confidence": "source-reported",
        "summary": "CUTLASS-style GEMM example for Ascend.",
    }), encoding="utf-8")

    schemas = validate.load_schemas()
    tags = validate.load_tags()
    errors, warnings = validate.validate_page(page, schemas, tags, {})

    assert errors == []
    assert warnings == []


def test_short_type_alias_code_matches_source_code_pages():
    pages = [
        {"type": "source-code", "tags": [], "architectures": []},
        {"type": "source-doc", "tags": [], "architectures": []},
    ]

    results = query.filter_pages(pages, type="code")

    assert results == [pages[0]]


def test_write_source_code_pages_does_not_overwrite_existing_file(tmp_path):
    output_dir = tmp_path / "sources" / "code" / "catlass"
    output_dir.mkdir(parents=True)
    existing = output_dir / "basic-matmul.md"
    existing.write_text("keep me", encoding="utf-8")

    stats = gen.write_pages([
        {
            "id": "code-catlass-basic-matmul",
            "title": "CATLASS Basic Matmul Example",
            "slug": "basic-matmul",
            "repo": "Ascend/catlass",
            "repo_key": "catlass",
            "path": "examples/00_basic_matmul",
            "url": "https://gitee.com/ascend/catlass/tree/master/examples/00_basic_matmul",
            "date": "2026-06-18",
            "architectures": ["ascend910b"],
            "tags": ["catlass", "matmul"],
            "summary": "CUTLASS-style GEMM example for Ascend.",
        }
    ], output_dir=tmp_path / "sources" / "code", force=False)

    assert stats.written == 0
    assert stats.skipped_existing == 1
    assert existing.read_text(encoding="utf-8") == "keep me"
