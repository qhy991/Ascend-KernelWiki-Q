---
id: technique-pr-vllm-ascend-6479
title: "PR Insight: vllm-project/vllm-ascend #6479"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - memory-management
  - context-parallel
  - attention
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6479"
---

# PR Insight: vllm-project/vllm-ascend #6479

**Title:** [0.13.0][Bugfix] fix npu memory is not released in cp

## Overview
This PR fixes a memory leak in the Qwen context parallel chunk scenario where NPU memory is not released. The issue occurs because variables created in the main stream are directly used in the communication stream, preventing proper memory deallocation.

## Technical Significance
Fixes a memory leak in multi-stream attention backend execution. The problem is solved by using clone mode to ensure proper NPU memory management across different CUDA/NPU streams, preventing memory pressure and OOM issues in long-running inference scenarios with context parallelism.

## Related
- `technique-context-parallel`
- `kernel-attention`