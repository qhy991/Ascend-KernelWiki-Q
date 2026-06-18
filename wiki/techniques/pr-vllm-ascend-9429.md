---
id: technique-pr-vllm-ascend-9429
title: "PR Insight: vllm-project/vllm-ascend #9429"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - dispatch-ffn-combine
  - swiglu-limit
  - moe
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/9429"
---

# PR Insight: vllm-project/vllm-ascend #9429

**Title:** [Feature] support ffncombine swiglulimit

## Overview
This PR adds support for SwiGLU activation limits in the dispatch_ffn_combine operator. The implementation updates the operator definition, tiling logic, kernel implementation, torch adapters, and MoE communication methods.

## Technical Significance
SwiGLU activation limits prevent numerical instability and ensure proper gradient flow during training. Adding support for this feature in the ffn combine operator enables correct behavior for models that require activation clamping, improving numerical stability.

## Related
- `kernel-moe`
- `hw-cube-unit`