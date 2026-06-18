---
id: technique-pr-vllm-ascend-7877
title: "PR Insight: vllm-project/vllm-ascend #7877"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - quantization
  - moe
  - w4a4
  - mxfp4
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/7877"
---

# PR Insight: vllm-project/vllm-ascend #7877

**Title:** [Ascend950][quant][Feature] Add W4A4 MXFP4 quantization support for Ascend950

## Overview
This PR adds support for W4A4 MXFP4 (Microscaling FP4) quantization on Ascend devices, implementing `AscendW4A4MXFP4DynamicLinearMethod` and `AscendW4A4MXFP4DynamicFusedMoEMethod`. The changes include parameterizing the `npu_grouped_matmul_swiglu_quant` operation for different quantization types, and integrating MXFP4 into the MoE runtime, stage parameters, and token dispatching logic.

## Technical Significance
MXFP4 is a micro-precision floating point format that enables 4-bit weight and activation quantization while maintaining better accuracy than traditional INT4. This support is particularly valuable for Ascend950 hardware and enables running larger models with reduced memory footprint. The integration extends to both linear layers and MoE FFN operations, covering key compute-heavy components of transformer models.

## Related
- `kernel-matmul`
- `kernel-moe`
- `technique-quantization`
- `quantization-w4a4-mxfp4`