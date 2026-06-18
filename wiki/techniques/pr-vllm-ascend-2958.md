---
id: technique-pr-vllm-ascend-2958
title: "PR Insight: vllm-project/vllm-ascend #2958"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - operator-generalization
  - torchair
  - quantization
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2958"
---

# PR Insight: vllm-project/vllm-ascend #2958

**Title:** [refactor]support gatingtopk operator generalization

## Overview
This PR generalizes the npu_moe_gating_top_k operator to support all group_count sizes, not just the previous hardcoded 256. It also consolidates functionality by including torch_npu.npu_moe_gating_top_k_softmax within npu_moe_gating_top_k, improving GLM4.5-w8a8 TPS by 6%.

## Technical Significance
The operator generalization removes a hardcoded constraint, enabling flexible MoE routing configurations across different model architectures. By merging the softmax functionality into the gating operator, it reduces operator count and improves performance, particularly beneficial for quantized models like GLM4.5.

## Related
- `kernel-moe-ascendc`, `technique-operator-fusion`, `kernel-quantization-ascendc`