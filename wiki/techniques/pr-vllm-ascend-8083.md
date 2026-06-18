---
id: technique-pr-vllm-ascend-8083
title: "PR Insight: vllm-project/vllm-ascend #8083"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - triton
  - sampling
  - temperature
  - topk
  - softmax
  - performance
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/8083"
---

# PR Insight: vllm-project/vllm-ascend #8083

**Title:** [Performance][model_runner_v2]:optimize for triton op _temperature_kernel and _topk_log_softmax_kernel

## Overview
This PR adds NPU-optimized Triton implementations of `_temperature_kernel` and `_topk_log_softmax_kernel` operations to the vllm-ascend model_runner_v2 module. The previous GPU-optimized implementations performed poorly on Ascend NPU. The new implementations are added to `vllm_ascend/worker/v2/sample/logprob.py` and `vllm_ascend/worker/v2/sample/gumbel.py`, with proper patching in `patch_triton.py`.

## Technical Significance
This optimization addresses the performance gap between GPU and NPU implementations of critical sampling operations. The temperature scaling and top-k log-softmax operations are fundamental to sampling-based generation, and NPU-specific optimizations are essential for achieving competitive inference performance on Ascend hardware. The PR includes comprehensive unit tests for validation.

## Related
- `technique-triton-optimization`
- `technique-sampling-optimization`