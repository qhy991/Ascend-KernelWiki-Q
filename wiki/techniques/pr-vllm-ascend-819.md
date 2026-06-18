---
id: technique-pr-vllm-ascend-819
title: "PR Insight: vllm-project/vllm-ascend #819"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - quantization
  - all2all
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/819"
---

# PR Insight: vllm-project/vllm-ascend #819

**Title:** [BugFix]add all2all when dp_size > 1 && downgrade npu_dequant_swiglu_quant

## Overview
This PR introduces native `all_to_all` communication operator to fix allgather bugs when data parallel size exceeds 1. It also disables the `npu_dequant_swiglu_quant` operator in quantized cases due to excessive memory usage of int32 hidden states tensors, falling back to separate swiglu and quantize operations.

## Technical Significance
The all_to_all operator is essential for correct MoE communication patterns when using data parallelism. Disabling memory-intensive operators prevents out-of-memory errors while maintaining quantization benefits. Together, these changes ensure MoE models work correctly across different parallel configurations.

## Related
- `kernel-moe`
- `technique-all2all`
- `technique-quantization`