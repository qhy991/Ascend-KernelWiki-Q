---
id: technique-pr-vllm-ascend-2633
title: "PR Insight: vllm-project/vllm-ascend #2633"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - quantization
  - performance
  - custom-op
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2633"
---

# PR Insight: vllm-project/vllm-ascend #2633

**Title:** [Perf]Enable npu_moe_gating_top_k_softmax on quantized scenarios

## Overview
This PR enables the `npu_moe_gating_top_k_softmax` custom operator for quantized MoE scenarios (such as W8A8). The operator works identically for both quantized and non-quantized scenarios and provides performance improvements.

## Technical Significance
The performance optimization reduces TPOT (Time Per Output Token) by 3-4ms for quantized MoE inference. By enabling the NPU custom operator for expert gating and top-k softmax operations, the PR leverages hardware-accelerated operations that were previously only used in non-quantized scenarios, improving overall inference throughput.

## Related
- `technique-moe`
- `technique-quantization`
- `technique-custom-op`