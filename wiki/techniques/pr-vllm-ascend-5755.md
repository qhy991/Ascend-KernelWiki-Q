---
id: technique-pr-vllm-ascend-5755
title: "PR Insight: vllm-project/vllm-ascend #5755"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - dispatch-gmm-combine
  - moe
  - quantization
  - w8a8
  - dtype
  - cast
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5755"
---

# PR Insight: vllm-project/vllm-ascend #5755

**Title:** [Feature] Adapt DispathGmmCombineDecode opertor to align with weight scale dtype of small operators. [RFC: issue 5476]

## Overview
This PR adapts the `DispatchGmmCombineDecode` operator to support flexible weight scale data types, changing from requiring float32 scales to allowing float32/float16 when input is float16, and float32/bfloat16 when input is float32/bfloat16. The implementation modifies the operator's C++ host and kernel code, particularly the epilogue handling for per-token dequantization, to handle different scale dtypes. The changes also allow w1 and w2 scales to use different dtypes, providing greater flexibility in quantized MoE inference.

## Technical Significance
This optimization reduces memory copy operations for scale tensors by half while introducing minimal computational overhead. The key technique is allowing scales to use the same dtype as the input data, which reduces memory bandwidth requirements for scale loading. Although the operator internally casts non-fp32 scales to fp32 for computation, the reduced memory copying provides performance benefits. Benchmarks on Qwen3-235B show minimal performance impact (96.28us vs 96.06us for bs18, 108.83us vs 107.90us for bs32), confirming the effectiveness of the dtype alignment optimization.

## Related
- `technique-quantization`, `technique-w8a8`, `technique-moe`, `technique-dtype-alignment`, `technique-memory-bandwidth`