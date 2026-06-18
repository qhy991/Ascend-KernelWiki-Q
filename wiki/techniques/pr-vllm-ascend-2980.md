---
id: technique-pr-vllm-ascend-2980
title: "PR Insight: vllm-project/vllm-ascend #2980"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - shared-expert
  - custom-op
  - deepseek
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2980"
---

# PR Insight: vllm-project/vllm-ascend #2980

**Title:** [CustomOp] Register AscendSharedFusedMoE custom op

## Overview
This PR registers the AscendSharedFusedMoE custom operator, enabling support for MoE models with shared experts like DeepSeek-V2-Lite. It removes the patch-based approach and directly registers the custom operator for better integration.

## Technical Significance
Registering AscendSharedFusedMoE as a custom operator improves integration with the vLLM operator registry, enabling better optimization and compatibility with graph execution modes. This is essential for models like DeepSeek-V2-Lite that use shared experts in their MoE architecture.

## Related
- `kernel-moe-ascendc`, `kernel-shared-expert-ascendc`, `technique-custom-op-registration`