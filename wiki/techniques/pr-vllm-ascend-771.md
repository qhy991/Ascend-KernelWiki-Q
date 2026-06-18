---
id: technique-pr-vllm-ascend-771
title: "PR Insight: vllm-project/vllm-ascend #771"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - aclgraph
  - inference
  - vllm
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/771"
---

# PR Insight: vllm-project/vllm-ascend #771

**Title:** Add Func: aclgraph_batch_size auto-adjust to different model

## Overview
This PR implements dynamic adjustment of `aclgraph_batch_size` based on model characteristics (hidden layer count) and parallel configuration. Previously, fixed batch sizes caused "insufficient resources" errors on different models. The new system adapts batch sizes - 33 for Qwen2.5-7B, 11 for Qwen2.5-72B.

## Technical Significance
Dynamic batch size adjustment prevents resource allocation errors and optimizes memory usage across different model sizes. This is crucial for aclgraph mode performance and stability when running various models on Ascend hardware with different parallel configurations.

## Related
- `technique-aclgraph`
- `technique-inference`