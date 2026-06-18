---
id: technique-pr-vllm-ascend-9036
title: "PR Insight: vllm-project/vllm-ascend #9036"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - moe
  - quantization
  - routing
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/9036"
---

# PR Insight: vllm-project/vllm-ascend #9036

**Title:** [BugFix] Fix quantization accuracy bug

## Overview
This PR fixes a quantization accuracy bug by propagating the `routed_scaling_factor` parameter from quantization methods' `apply` functions to the expert selection logic. The scaling factor is necessary for maintaining accuracy in models that use scaling for routing weights (e.g., DeepSeek-V2/V3). The implementation updates expert selectors in both standard and 310P-specific paths across multiple quantization methods (W4A16, W4A8, W8A8, MXFP4, MXFP8).

## Technical Significance
Routing weight scaling is critical for quantized MoE accuracy, particularly for DeepSeek architectures where the router weights use different scales than expert weights. Without proper scaling factor propagation, quantized MoE inference would produce incorrect expert selections, leading to degraded model quality. The fix ensures that all quantization methods properly handle routing scaling, maintaining accuracy for quantized MoE models on Ascend NPUs across different quantization schemes.

## Related
- `technique-moe` (MoE expert routing)
- `pattern-quantization` (Quantization accuracy)
- `pattern-deepseek` (DeepSeek MoE architectures)