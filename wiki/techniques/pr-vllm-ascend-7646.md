---
id: technique-pr-vllm-ascend-7646
title: "PR Insight: vllm-project/vllm-ascend #7646"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - triton
  - qwen3.5
  - kernel-optimization
  - flash-attention
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/7646"
---

# PR Insight: vllm-project/vllm-ascend #7646

**Title:** [v0.18.0][Triton][Qwen3.5] delete expr for kernels args

## Overview
This PR removes expression-based kernel arguments for Qwen3.5 models, affecting flash attention operators (chunk_o, l2norm, wy_fast) and layernorm_gated. The simplification improves kernel compilation and execution stability.

## Technical Significance
Eliminates complex expression handling in Triton kernel arguments for Qwen3.5 flash attention, reducing compilation complexity and potential runtime errors. This improves reliability for attention-heavy workloads.

## Related
- `kernel-flash-attention`, `kernel-layernorm`, `technique-triton-optimization`, `pattern-qwen-architecture`