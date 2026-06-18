---
id: technique-pr-vllm-ascend-3985
title: "PR Insight: vllm-project/vllm-ascend #3985"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - aclgraph
  - performance
  - stream-scheduling
  - vllm
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3985"
---

# PR Insight: vllm-project/vllm-ascend #3985

**Title:** [Perf] Move attention update stream out of loop to optimize performance

## Overview
This PR optimizes performance by moving the `torch.npu.stream(update_stream)` context manager from inside the per-layer for-loop to wrapping the entire loop in `update_*attn_params` functions. Previously, the stream was initiated redundantly for every layer, adding unnecessary overhead. This change reduces 90μs per decode model by ensuring the update stream is initiated only once per function call.

## Technical Significance
Stream management overhead accumulates across layers in deep transformer models. Moving the stream context outside the loop eliminates redundant stream switches, reducing overhead per layer. This optimization is particularly impactful for models with many layers, where the cumulative overhead becomes significant. Proper stream scheduling is essential for maximizing Ascend NPU utilization.

## Related
- `technique-aclgraph`, `technique-stream-scheduling`, `pattern-performance-optimization`, `technique-attention`