---
id: technique-pr-vllm-ascend-2219
title: "PR Insight: vllm-project/vllm-ascend #2219"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - qwen3-moe
  - quantization
  - w8a8
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2219"
---

# PR Insight: vllm-project/vllm-ascend #2219

**Title:** [main][Bugfix] Fix unable to load qwen3_moe quantized weights

## Overview
This PR fixes an issue where Qwen3-MoE quantized weights could not be loaded, which was introduced by PR #1994. The fix modifies `vllm_ascend/models/qwen3_moe.py` to properly handle quantized weight loading and adds e2e test cases for Qwen3-MoE W8A8 quantized models.

## Technical Significance
This bugfix resolves compatibility issues between Qwen3-MoE models and quantization weight loading, ensuring that quantized Qwen3-MoE models can be successfully loaded and used for inference. The fix addresses the specific issue introduced by the weight handling changes in PR #1994 and maintains proper quantization support.

## Related
- `kernel-fused-moe-ascendc`, `technique-quantization-w8a8`, `technique-weight-loading`, `kernel-qwen3-moe`