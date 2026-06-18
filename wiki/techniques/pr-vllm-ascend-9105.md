---
id: technique-pr-vllm-ascend-9105
title: "PR Insight: vllm-project/vllm-ascend #9105"
type: wiki-technique
architectures:
  - ascend310p
tags:
  - moe
  - routing
  - performance
  - nz-format
  - w8a8
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/9105"
---

# PR Insight: vllm-project/vllm-ascend #9105

**Title:** [Performance][310p] optimize moe routing path

## Overview
This PR optimizes the Mixture of Experts (MoE) routing path for Ascend 310P by integrating specialized NPU operators (`npu_moe_gating_top_k_softmax` and `npu_moe_init_routing_v2`), implementing NZ format conversion for expert weights during loading, and explicitly disabling Expert Parallelism (EP) on 310P due to current lack of support.

## Technical Significance
The optimization leverages NPU-specific operators for efficient expert selection and token dispatching, while NZ format conversion for expert weights (w13 and w2) enhances inference efficiency. The PR adds defensive checks for hidden state alignment and disables EP to prevent silent failures on unsupported hardware, ensuring robust MoE inference on Ascend 310P.

## Related
- `kernel-moe-ascendc`, `technique-nz-format`, `kernel-quantization-ascendc`, `technique-moe-routing`