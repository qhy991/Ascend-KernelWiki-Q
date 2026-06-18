---
id: technique-pr-vllm-ascend-6116
title: "PR Insight: vllm-project/vllm-ascend #6116"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - kv-cache
  - refactoring
  - block-table
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6116"
---

# PR Insight: vllm-project/vllm-ascend #6116

**Title:** [Refactor] use the count of kv_cache_group to create multi_block_table

## Overview
This PR refactors the `MultiBlockTable` creation logic in `vllm_ascend/worker/block_table.py`. Previously, block tables were created based on different `block_sizes` and `kernel_block_sizes`, but this changes to create block tables based on `kv_cache_groups` count, ensuring a specific `block_table` corresponds to each `kv_cache_group`.

## Technical Significance
This refactoring aligns block table management with the KV cache group structure, making the system more predictable and maintainable. It ensures that each KV cache group has its dedicated block table, which is important for handling different page sizes and page-size-adapted KV cache specifications in hybrid spec scenarios.

## Related
- `technique-kv-cache-paging`, `technique-multi-block-pool`