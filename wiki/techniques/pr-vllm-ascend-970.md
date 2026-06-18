---
id: technique-pr-vllm-ascend-970
title: "PR Insight: vllm-project/vllm-ascend #970"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - sampler
  - topk
  - topp
  - performance
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/970"
---

# PR Insight: vllm-project/vllm-ascend #970

**Title:** optimize the funtion of computing topk and topp in sampler.

## Overview
This PR optimizes the topk and topp computation logic in sampler and deepseekv2 models. It adds the `VLLM_ENABLE_TOPK_OPTIMZE` configuration option to enable the optimization.

## Technical Significance
Efficient sampling is critical for inference throughput. Optimizing topk and topp computations reduces token generation latency, directly improving time-per-output-token (TPOT) metrics for generation workloads on Ascend hardware.

## Related
- `kernel-sampler`
- `technique-topk`
- `kernel-inference`