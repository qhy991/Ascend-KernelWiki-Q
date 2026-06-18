---
id: technique-pr-vllm-ascend-7109
title: "PR Insight: vllm-project/vllm-ascend #7109"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - triton
  - qwen
  - ssm
  - compatibility
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/7109"
---

# PR Insight: vllm-project/vllm-ascend #7109

**Title:** Add patch_qwen3_5 for triton ops fused_recurrent_gated_delta_rule

## Overview
Adds a patch for Qwen3.5 to retain the Triton implementation of `fused_recurrent_gated_delta_rule` operation. The patch is needed because the current `torch_npu.npu_recurrent_gated_delta_rule` operator does not support `ssm_state` inputs in float32 format.

## Technical Significance
Maintains compatibility with Qwen3.5 SSM requirements by using Triton kernels for float32 SSM state inputs while the NPU operator is enhanced. The patch ensures correct SSM computation for models requiring float32 precision in state management.

## Related
- `technique-triton`, `technique-ssm`, `technique-qwen`, `technique-operator-compatibility`