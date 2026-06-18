---
id: technique-pr-vllm-ascend-2469
title: "PR Insight: vllm-project/vllm-ascend #2469"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - mc2
  - allgather
  - communication-optimization
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2469"
---

# PR Insight: vllm-project/vllm-ascend #2469

**Title:** [2/N][Feat] Add MC2 communication method for MoE layers

## Overview
This PR adds an MC2 communication method for MoE layers as an alternative to all-gather for small token counts. The implementation creates a new `AscendFusedMoE` layer that handles token splitting, local computation, and aggregation via all-gather, with logic to dynamically select between MC2 and existing all-gather methods based on input token count.

## Technical Significance
This optimization provides an alternative communication strategy that may be more efficient for certain token count ranges. The dynamic selection logic allows the system to choose the best communication method based on runtime conditions, optimizing performance across different workloads.

## Related
- `kernel-fused-moe-ascendc`, `technique-moe-communication`, `technique-hccl-optimization`, `kernel-token-dispatcher`