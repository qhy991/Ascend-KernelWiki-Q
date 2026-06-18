---
id: technique-pr-vllm-ascend-1264
title: "PR Insight: vllm-project/vllm-ascend #1264"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - moe
  - refactoring
  - quantization
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/1264"
---

# PR Insight: vllm-project/vllm-ascend #1264

**Title:** [v0.9.1][refactor] Refactoring AscendFusedMoE (#1229)

## Overview
This PR refactors the fused MoE (Mixture of Experts) implementation by consolidating all fused_moe code into `vllm_ascend/ops/fused_moe.py` and integrating branch conditions into `get_fused_moe_state`. It also removes obsolete environment variables and aligns with vLLM's API by replacing `expert_tensor_parallel_size` with `enable_expert_parallel`.

## Technical Significance
Cleans up MoE operator code organization and removes technical debt. The refactoring eliminates expired environment variables (`VLLM_ENABLE_MC2`, `USING_LCCL_COM`) and consolidates MoE branching logic, making the code more maintainable. Changes span multiple model files (DeepSeek DBO/V2), quantization (w8a8 dynamic), worker components, and utility functions. This improves code clarity and reduces configuration complexity for MoE inference on Ascend.

## Related
- `kernel-moe`
- `technique-operator-fusion`
- `technique-w8a8-quantization`