"""Regression tests for generating source-doc pages from a catalog."""

import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import generate_source_docs as gen  # noqa: E402


def test_render_source_doc_page_contains_required_frontmatter():
    entry = {
        "id": "doc-test-ascendc-pipe",
        "title": "Ascend C Pipe API",
        "slug": "test-ascendc-pipe",
        "url": "https://www.hiascend.com/document/detail/en/example",
        "date": "2026-06-18",
        "architectures": ["ascend910b"],
        "tags": ["ascendc", "api", "cann"],
        "hardware_features": ["mte", "unified-buffer"],
        "techniques": ["pipeline-scheduling"],
        "confidence": "source-reported",
        "summary": "Official Ascend C Pipe API reference for queue-based kernel pipelines.",
    }

    text = gen.render_page(entry)
    fm_text = text.split("---", 2)[1]
    fm = yaml.safe_load(fm_text)

    assert fm["id"] == "doc-test-ascendc-pipe"
    assert fm["type"] == "source-doc"
    assert fm["architectures"] == ["ascend910b"]
    assert fm["hardware_features"] == ["mte", "unified-buffer"]
    assert "Official Ascend C Pipe API reference" in text


def test_write_pages_does_not_overwrite_existing_file(tmp_path):
    output_dir = tmp_path / "sources" / "docs"
    output_dir.mkdir(parents=True)
    existing = output_dir / "test-ascendc-pipe.md"
    existing.write_text("keep me", encoding="utf-8")

    stats = gen.write_pages([
        {
            "id": "doc-test-ascendc-pipe",
            "title": "Ascend C Pipe API",
            "slug": "test-ascendc-pipe",
            "url": "https://www.hiascend.com/document/detail/en/example",
            "date": "2026-06-18",
            "architectures": ["ascend910b"],
            "tags": ["ascendc", "api", "cann"],
            "summary": "Official reference.",
        }
    ], output_dir=output_dir, force=False)

    assert stats.written == 0
    assert stats.skipped_existing == 1
    assert existing.read_text(encoding="utf-8") == "keep me"
