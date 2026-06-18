---
id: technique-pr-vllm-ascend-2373
title: "PR Insight: vllm-project/vllm-ascend #2373"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - qwen-moe
  - arange
  - performance
  - optimization
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2373"
---

# PR Insight: vllm-project/vllm-ascend #2373

**Title:** [Qwen-moe] Remove the minor operation arange

## Overview
This PR removes the minor `arange` operation to reduce execution time and improve performance in Qwen-MoE models. The changes affect `vllm_ascend/ops/fused_moe.py`, `vllm_ascend/ops/layers/experts_selector.py`, and quantization files, reducing unnecessary computation.

## Technical Significance
This optimization eliminates a small but unnecessary operation that was adding overhead to MoE expert selection. By removing the `arange` operation and integrating the arange operator where needed, the system reduces computation time and improves overall MoE inference performance.

## Related
- `kernel-fused-moe-ascendc`, `technique-operator-elimination`, `technique-performance-optimization`, `kernel-qwen-moe`