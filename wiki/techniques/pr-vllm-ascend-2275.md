---
id: technique-pr-vllm-ascend-2275
title: "PR Insight: vllm-project/vllm-ascend #2275"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - quantization
  - operator-fusion
  - w8a8-dynamic
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2275"
---

# PR Insight: vllm-project/vllm-ascend #2275

**Title:** [main] Fuse GroupedMatmul, Swiglu and DynamicQuant in `W8A8_DYNAMIC` quantized MoE layers

## Overview
This PR fuses `GroupedMatmul`, `Swiglu`, and `DynamicQuant` into a single fusion operation `GroupedMatmulSwigluQuant` for W8A8_DYNAMIC quantized MoE layers. The implementation extracts common functions from `w4a8_dynamic.py` and `w8a8_dynamic.py`, adds the fusion to `vllm_ascend/ops/layers/moe_mlp.py`, and when supported, uses the `npu_grouped_matmul_swiglu_quant` operation.

## Technical Significance
This fusion delivers significant performance improvements for quantized MoE models. Benchmark results on Qwen3-235B-A22B with bs=16 show TPOP increased 21.54% and output token throughput increased 27.35% in TP8-DP1-MoEP1 configuration. The fusion reduces kernel launch overhead and improves data locality by combining three operations into one.

## Related
- `kernel-fused-moe-ascendc`, `technique-operator-fusion`, `technique-quantization-w8a8`, `kernel-grouped-matmul-ascendc`