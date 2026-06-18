---
id: technique-pr-vllm-ascend-3433
title: "PR Insight: vllm-project/vllm-ascend #3433"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - hccl-optimization
  - kv-cache
  - vllm
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3433"
---

# PR Insight: vllm-project/vllm-ascend #3433

**Title:** [Feat] add native kvcache offload

## Overview
This pr is for https://github.com/vllm-project/vllm-ascend/issues/3241 , which is in-house solution for offloading KV cache data from the GPU memory to other medium (in particular, CPU memory)。Previous solutions required reliance on third-party components, which had issues with compatibility between different versions.

## Technical Significance
Implements native KV cache offloading to CPU memory for handling larger models within limited NPU memory capacity.

## Related
- `technique-kv-cache-paging`
- `technique-hccl-optimization`
