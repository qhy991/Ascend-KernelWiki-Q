---
id: technique-pr-vllm-ascend-4885
title: "PR Insight: vllm-project/vllm-ascend #4885"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - moe-mlp
  - quantization
  - dequant
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/4885"
---

# PR Insight: vllm-project/vllm-ascend #4885

**Title:** [Bugfix] bugfix for moe_mlp in vllm-ascend/v0.11.0-dev

## Overview
This PR fixes a bug in the moe_mlp module for v0.11.0-dev by correcting the arguments passed to torch_npu.npu_dequant_swiglu_quant. The fix properly converts group_list from cumulative sum format to count format for the group_index parameter.

## Technical Significance
Backports the fix from PR #4822 to the v0.11.0-dev branch, ensuring consistent quantization behavior across branches. Corrects operator input format mismatch for quantized MoE MLP dequantization.

## Related
- `kernel-moe-mlp`
- `technique-dequantization`
- `technique-swiglu`
- `kernel-fused-moe`