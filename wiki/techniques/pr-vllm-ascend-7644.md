---
id: technique-pr-vllm-ascend-7644
title: "PR Insight: vllm-project/vllm-ascend #7644"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - qwen3.5-moe
  - flash-comm
  - v0.18.0
  - cherry-pick
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/7644"
---

# PR Insight: vllm-project/vllm-ascend #7644

**Title:** [v0.18.0] Qwen3.5 MoE supports flashcomm v1

## Overview
This PR cherry-picks flash comm V1 support for Qwen3.5 MoE to v0.18.0. Since multimodal MoE models like Qwen3.5 do embedding in model_runner, the first AllGather operation should be skipped when flash comm is enabled to avoid unnecessary communication.

## Technical Significance
This cherry-pick matters for v0.18.0 Qwen3.5 MoE performance. Flash comm optimizes tensor-parallel communication, but the embedding layer's first AllGather was redundant. Skipping this first AllGather reduces communication overhead. The cherry-pick ensures v0.18.0 users benefit from this optimization for Qwen3.5 MoE models.

## Related
- technique-flash-comm
- technique-moe
- technique-tensor-parallelism