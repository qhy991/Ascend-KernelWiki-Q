---
id: technique-pr-vllm-ascend-6301
title: "PR Insight: vllm-project/vllm-ascend #6301"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - triton
  - bugfix
  - rotary-embedding
  - stability
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6301"
---

# PR Insight: vllm-project/vllm-ascend #6301

**Title:** [Bugfix] Improve Triton stability on Ascend for large grids

## Overview
This PR improves Triton kernel stability on Ascend hardware when processing large grids by setting `TRITON_ALL_BLOCKS_PARALLEL=1` when the grid size exceeds 65535. The change was made in `vllm_ascend/ops/rotary_embedding.py`.

## Technical Significance
Large grid sizes can cause Triton kernel failures on Ascend hardware. This environment variable fix ensures proper parallelization of block execution for grids exceeding the 16-bit limit, preventing crashes and improving stability for models with large sequence lengths.

## Related
- `technique-triton`
- `technique-rotary-embedding`
- `technique-kernel-stability`