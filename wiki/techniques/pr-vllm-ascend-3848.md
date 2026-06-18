---
id: technique-pr-vllm-ascend-3848
title: "PR Insight: vllm-project/vllm-ascend #3848"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - attention
  - stream-management
  - performance
  - aclgraph
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3848"
---

# PR Insight: vllm-project/vllm-ascend #3848

**Title:** [Perf] Move attention update stream out of loop to optimize performance

## Overview
This PR optimizes performance by moving the `torch.npu.stream(update_stream)` context manager from inside the per-layer loop to wrap the entire parameter update function. Previously, redundant stream initiations for every layer added unnecessary overhead. The refactoring in `vllm_ascend/compilation/acl_graph.py` (90 additions, 88 deletions) reduces 90us per decode model.

## Technical Significance
Stream context switches have non-zero overhead. By moving the stream context manager outside the loop, the update stream is initiated only once per function call instead of per layer, reducing cumulative overhead across many layers. This optimization is particularly valuable for deep models with many attention layers.

## Related
- `technique-attention`
- `technique-stream-management`
- `technique-performance-optimization`