---
id: technique-pr-vllm-ascend-4822
title: "PR Insight: vllm-project/vllm-ascend #4822"
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
  - "https://github.com/vllm-project/vllm-ascend/pull/4822"
---

# PR Insight: vllm-project/vllm-ascend #4822

**Title:** [Bugfix] bugfix for moe_mlp

## Overview
This PR fixes a bug in the moe_mlp module where the group_list argument passed to torch_npu.npu_dequant_swiglu_quant was in cumulative sum format instead of the required count format. The fix properly converts group_list from cumulative sum to counts for the group_index parameter.

## Technical Significance
Corrects operator input format mismatch for quantized MoE MLP dequantization. Ensures that torch_npu.npu_dequant_swiglu_quant receives group_index in count format rather than cumsum format, preventing calculation errors in quantized MoE inference.

## Related
- `kernel-moe-mlp`
- `technique-dequantization`
- `technique-swiglu`
- `kernel-fused-moe`