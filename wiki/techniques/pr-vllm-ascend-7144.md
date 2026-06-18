---
id: technique-pr-vllm-ascend-7144
title: "PR Insight: vllm-project/vllm-ascend #7144"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - fia
  - full-graph
  - cudagraph
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/7144"
---

# PR Insight: vllm-project/vllm-ascend #7144

**Title:** fixed fia pad logic in graph mode.

## Overview
Fixes FIA operator errors in full graph mode caused by deleting `relax_for_mixed_batch_cudagraphs` function (related to vLLM PR #34043). The deletion caused `num_reqs` to no longer equal the actual number of requests, and since FIA requires `query_start_loc[-1]` to equal total computed tokens, this caused errors. The fix sets `num_reqs_paded = num_reqs` in full graph mode.

## Technical Significance
Resolves FIA operator compatibility issues in full graph mode by ensuring correct request count handling. The fix maintains FIA requirements while adapting to upstream vLLM changes in CUDA graph management.

## Related
- `technique-fia`, `technique-full-graph`, `technique-cudagraph`, `technique-batch-handling`