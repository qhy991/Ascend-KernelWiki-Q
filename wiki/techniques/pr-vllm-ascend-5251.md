---
id: technique-pr-vllm-ascend-5251
title: "PR Insight: vllm-project/vllm-ascend #5251"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - moe
  - aclnn
  - custom-operator
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5251"
---

# PR Insight: vllm-project/vllm-ascend #5251

**Title:** [OP] add custom op aclnnMoeInitRoutingCustom

## Overview
This PR introduces a new custom operator `aclnnMoeInitRoutingCustom` for Mixture-of-Experts routing initialization. The operator includes comprehensive kernel implementations for quantized and unquantized scenarios, with optimized tiling and multi-core support for Ascend NPUs.

## Technical Significance
Custom MoE routing operators provide specialized functionality not available in standard ACLNN APIs. The implementation includes optimized kernels for dynamic/static quantization, expert token counting, gathering, and sorting, enabling high-performance MoE inference on Ascend hardware. This can be replaced by `aclnnMoeInitRoutingV3` once CANN 8.5 becomes available.

## Related
- technique-moe
- technique-quantization
- technique-custom-operators