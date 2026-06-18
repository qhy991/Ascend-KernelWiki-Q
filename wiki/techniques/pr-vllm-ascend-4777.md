---
id: technique-pr-vllm-ascend-4777
title: "PR Insight: vllm-project/vllm-ascend #4777"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - quantization
  - eplb
  - expert-load-balance
  - w8a8
  - shape-mismatch
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/4777"
---

# PR Insight: vllm-project/vllm-ascend #4777

**Title:** BugFix: Resolve shape mismatch in eplb update and calculation issues in quant_apply_mlp

## Overview
This PR fixes two issues in the MoE module: (1) shape mismatch in EPLB expert map updates when redundant experts are enabled, where expert_map_per_layer and log2phy_map_per_layer had inconsistent physical vs logical expert dimensions, and (2) calculation precision issue in quant_apply_mlp where torch_npu.npu_dequant_swiglu_quant expected group lists in Count format but received Cumsum format.

## Technical Significance
Fixes critical bugs affecting MoE expert load balancing (EPLB) and quantized MLP inference. The shape consistency fix ensures correct expert routing when using redundant experts. The precision fix corrects format mismatch in dequantization operators, ensuring accurate W8A8 quantized computation on NPU.

## Related
- `kernel-moe-mlp`
- `technique-eplb`
- `technique-w8a8-quantization`
- `kernel-expert-load-balancer`