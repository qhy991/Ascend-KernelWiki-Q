---
id: technique-pr-vllm-ascend-2112
title: "PR Insight: vllm-project/vllm-ascend #2112"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - moe
  - softmax
  - ascendc
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2112"
---

# PR Insight: vllm-project/vllm-ascend #2112

**Title:** [main] adapt usage of npu_moe_gating_top_k_softmax and remove envs.SELECT_GATING_TOPK_SOTFMAX_EXPERTS

## Overview
This PR adapts the usage of the Ascend-specific `npu_moe_gating_top_k_softmax` operator for MoE expert selection and removes the environment variable `SELECT_GATING_TOPK_SOTFMAX_EXPERTS`. The change backports improvements from the v0.9.1-dev branch to main.

## Technical Significance
Using the optimized AscendC operator for MoE gating improves expert selection efficiency and reduces dependency on environment variables. This provides more deterministic behavior and better integration with the Ascend NPU stack for MoE inference workloads.

## Related
- `kernel-moe-gating`
- `technique-moe`
- `technique-ascendc`
- `kernel-fused-moe`