---
id: technique-pr-vllm-ascend-9403
title: "PR Insight: vllm-project/vllm-ascend #9403"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - w4a8
  - dispatch-ffn-combine
  - swiglu
  - moe
  - quantization
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/9403"
---

# PR Insight: vllm-project/vllm-ascend #9403

**Title:** [Feature] w4a8 dispatch_ffn_combine: support x_active_mask and fix bias as TensorList

## Overview
This PR adds support for x_active_mask and fixes bias handling as TensorList in the W4A8 dispatch_ffn_combine operator. The implementation updates the operator definition, tiling logic, kernel implementation, torch adapters, and adds multi-card E2E tests.

## Technical Significance
x_active_mask enables efficient handling of sparse activation patterns, reducing computation for inactive experts. Fixing bias handling as TensorList ensures proper parameter passing for complex MoE configurations. Together, these improvements enhance the flexibility and efficiency of quantized MoE inference.

## Related
- `kernel-moe`
- `technique-quantization`