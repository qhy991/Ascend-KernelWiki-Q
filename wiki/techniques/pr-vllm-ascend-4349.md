---
id: technique-pr-vllm-ascend-4349
title: "PR Insight: vllm-project/vllm-ascend #4349"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - attention
  - vllm
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/4349"
---

# PR Insight: vllm-project/vllm-ascend #4349

**Title:** [MM][Model][Perf] Remove Qwen2.5-VL modeling files and add patch for VisionAttention

**Author:** shen-shanshan | **Merged:** 2025-11-28

## Overview
Adds new functionality for  operations. The feature enhances model capabilities and performance.

## Technical Significance
Attention mechanism optimizations directly impact inference latency, as attention computation is often the bottleneck in transformer models. Improvements here reduce NPU idle time and better utilize the Cube and Vector units for matrix multiplications and softmax operations.

## Related
- `kernel-flash-attention-ascendc`
