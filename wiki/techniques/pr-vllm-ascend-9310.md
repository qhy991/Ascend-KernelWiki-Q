---
id: technique-pr-vllm-ascend-9310
title: "PR Insight: vllm-project/vllm-ascend #9310"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - performance
  - gdn
  - chunk-ops
  - qwen
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/9310"
---

# PR Insight: vllm-project/vllm-ascend #9310

**Title:** [Performance] Reuse prebuilt chunk host metadata for Ascend chunk ops and earse synconize for qwen3.5 model

## Overview
This PR optimizes performance by reusing prebuilt chunk host metadata for Ascend chunk operations and removing unnecessary synchronization for the Qwen 3.5 model. The changes affect GDN operations, attention builders, chunk operators, speculative decoding, and worker model runners.

## Technical Significance
Reusing prebuilt metadata eliminates redundant host-side computations, reducing CPU overhead and improving overall inference throughput. Removing unnecessary synchronization for specific models further reduces latency. These optimizations are particularly impactful for chunked attention and GDN operations which are frequently called during inference.

## Related
- `technique-pipeline-scheduling`
- `kernel-attention`
- `technique-operator-fusion`