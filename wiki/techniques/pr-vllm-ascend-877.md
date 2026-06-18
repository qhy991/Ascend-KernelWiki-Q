---
id: technique-pr-vllm-ascend-877
title: "PR Insight: vllm-project/vllm-ascend #877"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - quantization
  - online-serving
  - inference
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/877"
---

# PR Insight: vllm-project/vllm-ascend #877

**Title:** enable online serving quantization

## Overview
This PR enables Ascend quantization method for online serving by adding "ascend" to the quantization methods list. Users can now enable quantization using the command `vllm serve --quantization ascend` for online inference workloads.

## Technical Significance
Quantization reduces model size and improves inference throughput. Enabling Ascend-specific quantization for online serving allows users to leverage these benefits in production deployments, making quantized models more practical for real-world applications on Ascend hardware.

## Related
- `technique-quantization`
- `technique-inference`
- `kernel-online-serving`