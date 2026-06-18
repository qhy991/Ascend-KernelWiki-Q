---
id: technique-pr-vllm-ascend-5460
title: "PR Insight: vllm-project/vllm-ascend #5460"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mtp
  - fullgraph
  - glm4.6
  - performance
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5460"
---

# PR Insight: vllm-project/vllm-ascend #5460

**Title:** 【Feature】GLM4.6 support mtp with fullgraph

## Overview
This PR enables MTP (Multi-Token Prediction) speculative decoding with fullgraph compilation support for the GLM4.6 model. The modification to `quant_config.py` allows GLM4.6 with w8a8 quantization to leverage fullgraph compilation for improved performance during speculative decoding.

## Technical Significance
Combining MTP speculative decoding with fullgraph compilation for GLM4.6 provides significant performance improvements by reducing kernel launch overhead and enabling better operator fusion on Ascend NPU. This feature is particularly valuable for long-context scenarios where the combination of speculative decoding and graph compilation maximizes throughput.

## Related
- `technique-speculative-decoding` (MTP algorithm)
- `technique-fullgraph` (Graph compilation optimization)
- `kernel-quantization` (w8a8 quantization support)