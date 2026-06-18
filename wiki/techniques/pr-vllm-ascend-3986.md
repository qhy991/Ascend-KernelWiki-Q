---
id: technique-pr-vllm-ascend-3986
title: "PR Insight: vllm-project/vllm-ascend #3986"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - attention
  - paged-attention
  - bugfix
  - vllm
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3986"
---

# PR Insight: vllm-project/vllm-ascend #3986

**Title:** [main][bugfix] Fix a rare bug triggered by _npu_paged_attention in FULL_DECODE_ONLY mode

## Overview
This PR fixes a bug where the workspace of `_npu_paged_attention` during graph capture was smaller than required during execution. For FULL_DECODE_ONLY mode, workspace calculation assumed larger seq_lens inputs require larger workspace, but rare cases exist where smaller seq_lens need larger workspace. The fix adds `get_workspace` directly into `update_attn_params` to calculate workspace correctly for each execution.

## Technical Significance
Paged attention workspace calculation is critical for memory safety and performance. The assumption-based calculation could lead to insufficient workspace in edge cases, causing crashes or incorrect results. Calculating workspace per-execution ensures correctness, though it may introduce ~1% performance degradation for small token counts. This trade-off is acceptable for correctness.

## Related
- `technique-attention`, `technique-paged-attention`, `technique-aclgraph`, `pattern-memory-safety`