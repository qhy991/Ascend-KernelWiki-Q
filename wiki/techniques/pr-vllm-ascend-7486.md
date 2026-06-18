---
id: technique-pr-vllm-ascend-7486
title: "PR Insight: vllm-project/vllm-ascend #7486"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - qwen3.5-moe
  - flash-comm
  - embedding
  - allgather
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/7486"
---

# PR Insight: vllm-project/vllm-ascend #7486

**Title:** Qwen3.5 MoE supports flash comm

## Overview
This PR enables Flash Comm V1 for Qwen3.5 MoE models. Since multimodal MoE models like Qwen3.5 do embedding in model_runner, the first AllGather operation should be skipped when flash comm is enabled to avoid unnecessary communication.

## Technical Significance
This optimization matters for Qwen3.5 MoE inference efficiency on Ascend. Flash comm optimizes tensor-parallel communication, but the embedding layer's first AllGather was redundant because embedding happens locally. Skipping this first AllGather reduces communication overhead and improves overall throughput for MoE models.

## Related
- technique-flash-comm
- technique-moe
- technique-tensor-parallelism