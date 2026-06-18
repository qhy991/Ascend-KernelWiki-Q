---
id: technique-pr-vllm-ascend-8425
title: "PR Insight: vllm-project/vllm-ascend #8425"
type: wiki-technique
architectures:
  - ascend910b
tags:
  - quantization
  - mxfp8
  - allgather
  - fc1
  - ep
  - ascend950
  - feature
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/8425"
---

# PR Insight: vllm-project/vllm-ascend #8425

**Title:** [Ascend950][Feature][quant] Add allgatherEP quantization support for Ascend950

## Overview
This PR enables allgather EP (Expert Parallel) mxfp8 quantization when FC1 is enabled for Ascend950 (A5) devices. The implementation updates MoE communication methods, token dispatching, and quantization adapters to support this configuration. The changes ensure proper quantization support in allgather EP scenarios on the latest Ascend hardware.

## Technical Significance
Allgather EP quantization is an advanced optimization that reduces communication overhead in expert parallel deployments while maintaining quantization benefits. This feature enables efficient MoE inference on Ascend950 with MXFP8 quantization, combining memory efficiency with communication optimization. The PR expands quantization capabilities for the latest Ascend hardware.

## Related
- `hw-ascend950`
- `technique-quantization`
- `technique-expert-parallel`