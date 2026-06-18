---
id: technique-pr-vllm-ascend-3532
title: "PR Insight: vllm-project/vllm-ascend #3532"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - unified-buffer
  - quantization
  - moe
  - hccl-optimization
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3532"
---

# PR Insight: vllm-project/vllm-ascend #3532

**Title:** add `dispatch_gmm_combine` kernel

## Overview
This PR introduces the Ascend implementation of the `dispatch_ffn_combine` kernel and wires it into the vLLM-Ascend runtime, together with follow‑up fixes to ensure the kernel builds and runs correctly in CI.

## Technical Significance
Adds dispatch_gmm_combine kernel for optimized MoE token routing and expert computation.

## Related
- `technique-quantization`
- `technique-moe-routing`
