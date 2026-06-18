---
id: technique-pr-vllm-ascend-4216
title: "PR Insight: vllm-project/vllm-ascend #4216"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - eplb
  - moe
  - custom-ops
  - dynamic-eplb
  - quantization
  - vllm
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/4216"
---

# PR Insight: vllm-project/vllm-ascend #4216

**Title:** [EPLB][Ops] Integerate grouped_matmul_swiglu_quant_weight_nz_tensor_list operator into dynamic EPLB

## Overview
This PR integrates the `grouped_matmul_swiglu_quant_weight_nz_tensor_list` operator into dynamic EPLB to support list-type parameters. The PR also modifies the logic of loading models in dynamic-eplb scenarios. The operator is based on PR #3804 and provides performance improvements for quantized models like DeepSeek-V3.1 w8a8mix.

## Technical Significance
Integrating custom operators into dynamic EPLB enables better performance for quantized MoE models. The grouped_matmul operator with SwiGLU and quantization support provides hardware-optimized computation for expert MLP layers. Dynamic EPLB with custom operators provides flexible, high-performance expert load balancing.

## Related
- `technique-eplb`, `technique-moe`, `pattern-custom-ops`, `technique-quantization`, `technique-dynamic-eplb`