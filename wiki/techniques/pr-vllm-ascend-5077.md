---
id: technique-pr-vllm-ascend-5077
title: "PR Insight: vllm-project/vllm-ascend #5077"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - operator-fusion
  - quantization
  - layernorm
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5077"
---

# PR Insight: vllm-project/vllm-ascend #5077

**Title:** [Graph][Fusion]Add new pattern for AddRmsnormQuant with SP.

## Overview
This PR extends the AddRmsnormQuant operator fusion patterns for Sequence Parallelism (SP) enabled scenarios. It adds two new patterns that insert `maybe_all_gather_and_maybe_unpad` between `addrmsnorm` and `quantize` operations. Additionally, it introduces a new API `torch.ops.vllm.quantize` that passes both `input_scale` and `input_scale_reciprocal` to handle different `div_mode` requirements between `npu_add_rms_norm_quant` and `npu_quantize` operators.

## Technical Significance
This optimization improves quantization efficiency for SP workloads by avoiding redundant reciprocal calculations at runtime and properly handling tensor sequence parallelism distribution. The fusion patterns reduce kernel launch overhead and memory bandwidth consumption on Ascend NPUs.

## Related
- technique-operator-fusion
- technique-quantization
- technique-layernorm