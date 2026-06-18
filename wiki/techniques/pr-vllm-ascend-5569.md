---
id: technique-pr-vllm-ascend-5569
title: "PR Insight: vllm-project/vllm-ascend #5569"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - operator-fusion
  - layernorm
  - quantization
  - npugraph
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5569"
---

# PR Insight: vllm-project/vllm-ascend #5569

**Title:** [Graph][Fusion] Add AddRMSNormSPPattern and AddRMSNormSPPatternWithBias

## Overview
This PR extends the npugraph_ex_passes module by adding two new fusion patterns: AddRMSNormSPPattern for standard scenarios and AddRMSNormSPPatternWithBias for scenarios with bias terms. Building on PR #5011, this enhancement provides significant throughput improvements for W8A8 quantized models like Qwen3-235B-A22B-W8A8 and Qwen3-32B.

## Technical Significance
The AddRMSNorm fusion patterns enable better operator fusion on Ascend NPU by combining addition, RMS normalization, and quantization operations into single fused kernels. Both standard and bias-inclusive variants provide comprehensive coverage of different model architectures, significantly improving inference throughput for quantized models while maintaining accuracy.

## Related
- `technique-operator-fusion` (AddRMSNorm fusion pattern)
- `kernel-layernorm` (RMS normalization)
- `kernel-quantization` (W8A8 quantization)
- `technique-npugraph` (NPU graph compilation)