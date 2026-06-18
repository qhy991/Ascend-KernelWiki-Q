---
id: technique-pr-vllm-ascend-9334
title: "PR Insight: vllm-project/vllm-ascend #9334"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - ascend950
  - a5
  - dynamic-quantization
  - bugfix
  - layernorm
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/9334"
---

# PR Insight: vllm-project/vllm-ascend #9334

**Title:** [Ascend950][BugFix] fix npu_add_rms_norm_dynamic_quant error in A5

## Overview
This PR fixes an error in the npu_add_rms_norm_dynamic_quant operation on A5 hardware by updating the compilation pass that fuses normalization with dynamic quantization. The fix ensures proper handling of the fused operation for A5's architecture-specific requirements.

## Technical Significance
Dynamic quantization combined with normalization is a common optimization pattern that reduces memory bandwidth while maintaining accuracy. The fix prevents runtime errors and ensures that this optimization works correctly on A5 hardware, improving reliability of quantized model inference.

## Related
- `technique-operator-fusion`
- `technique-quantization`