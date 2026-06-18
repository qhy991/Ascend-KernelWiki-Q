---
id: technique-pr-vllm-ascend-2841
title: "PR Insight: vllm-project/vllm-ascend #2841"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - quantization
  - allgather
  - dynamic
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2841"
---

# PR Insight: vllm-project/vllm-ascend #2841

**Title:** [Feat]support dynamic quantization in allgather

## Overview
This PR adds support for dynamic quantization in the allgather operation used by MoE token dispatching, enabling more efficient communication for quantized MoE models.

## Technical Significance
Enables dynamic quantization for MoE allgather operations, reducing communication bandwidth and improving performance for quantized MoE models. This is particularly important for large MoE models where communication between experts can be a bottleneck. Dynamic quantization at allgather time allows for adaptive precision based on the data being communicated.

## Related
- `kernel-moe-ascendc`, `technique-quantization`, `technique-hccl-optimization`