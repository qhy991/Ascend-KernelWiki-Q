---
id: technique-pr-vllm-ascend-442
title: "PR Insight: vllm-project/vllm-ascend #442"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - attention
  - performance
  - mask
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/442"
---

# PR Insight: vllm-project/vllm-ascend #442

**Title:** [ModelRunner][V1] Optimize V1 attention mask

## Overview
This PR optimizes V1 attention mask construction by pre-constructing mask matrices instead of dynamically building them during inference. The implementation adds environment variable configuration for balancing mask matrix size between memory and performance.

## Technical Significance
Attention mask construction is per-request overhead that can degrade throughput. Pre-constructing masks trades memory for computation, especially beneficial for long-context scenarios. The environment variable allows tuning based on available NPU memory.

## Related
- kernel-attention
- technique-performance-optimization