---
id: technique-pr-vllm-ascend-9259
title: "PR Insight: vllm-project/vllm-ascend #9259"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - w4a8
  - quantization
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/9259"
---

# PR Insight: vllm-project/vllm-ascend #9259

**Title:** [BugFix]moe w4a8 ub fix and swiglu limit fix

## Overview
This PR fixes two critical issues in the MoE W4A8 (4-bit weight, 8-bit activation) quantization operator: a unified buffer (UB) out-of-bounds error and a SwiGLU activation limit issue. The fixes are implemented in the dispatch_ffn_combine_w4_a8 operator's tiling logic, kernel implementation, and post-processing utilities.

## Technical Significance
The UB fix prevents memory access violations that could cause crashes or incorrect results, while the SwiGLU limit fix ensures proper handling of activation values within the expected range. These fixes improve the stability and correctness of quantized MoE inference, which is critical for large language model deployment.

## Related
- `kernel-moe`
- `technique-quantization`
- `hw-unified-buffer`