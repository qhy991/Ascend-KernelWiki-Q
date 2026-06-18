---
id: technique-pr-vllm-ascend-4235
title: "PR Insight: vllm-project/vllm-ascend #4235"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - quantization
  - w8a8
  - pd-mix
  - prefill-decode
  - vllm
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/4235"
---

# PR Insight: vllm-project/vllm-ascend #4235

**Title:** [feature] Support W8A8 PD-Mix Quantization

## Overview
This PR adds W8A8 PD-Mix quantization support, where different quantization strategies are used based on deployment scenario. In PD-separated deployments: MoE layers use dynamic quantization, while Attention modules use dynamic quantization in Prefill nodes and static quantization in Decode nodes. In PD-mixed deployments: All components fall back to dynamic quantization as distinguishing Prefill/Decode tokens is difficult.

## Technical Significance
PD-Mix quantization provides flexibility to optimize different phases with appropriate quantization strategies. Static quantization in decode provides better performance, while dynamic quantization in prefill maintains accuracy. The fallback to all dynamic in mixed scenarios ensures correctness when phase distinction is challenging.

## Related
- `technique-quantization`, `technique-w8a8`, `technique-prefill-decode`, `pattern-hybrid-quantization`, `technique-pd-disaggregation`