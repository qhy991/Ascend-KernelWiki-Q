---
id: technique-pr-vllm-ascend-2038
title: "PR Insight: vllm-project/vllm-ascend #2038"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - moe
  - quantization
  - prefill
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2038"
---

# PR Insight: vllm-project/vllm-ascend #2038

**Title:** [0.9.1][Prefill Perf] add D2H & initRoutingQuantV2

## Overview
This PR optimizes MoE prefill performance by integrating D2H (Device-to-Host) operations and the `initRoutingQuantV2` method. It removes the deprecated `fused_experts_with_all2all_v2` method and consolidates prefill optimization points into the alltoall method for better performance in W8A8 dynamic quantization scenarios.

## Technical Significance
The integration of `initRoutingQuantV2` improves routing computation efficiency during prefill phase for quantized MoE models. This optimization reduces communication overhead and leverages specialized Ascend NPU operators for improved throughput in quantized inference workloads.

## Related
- `technique-moe`
- `technique-quantization`
- `technique-hccl-optimization`
- `kernel-moe-w8a8`