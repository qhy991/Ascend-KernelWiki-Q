---
id: technique-pr-vllm-ascend-3048
title: "PR Insight: vllm-project/vllm-ascend #3048"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - attention
  - long-sequence
  - memory-optimization
  - mask-generation
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3048"
---

# PR Insight: vllm-project/vllm-ascend #3048

**Title:** [Feature] Reduce host memory usage for attention mask generation

## Overview
This PR optimizes attention mask generation to reduce host memory consumption. Previously, mask construction created multiple tensors of size (max_model_len, max_model_len), causing hundreds of GB of host memory usage and OOM crashes when max_model_len reached 128k.

## Technical Significance
The memory optimization is critical for long-sequence inference support. By reducing mask generation memory footprint, the PR enables deployment of models with long context windows (128k tokens) without exhausting host memory, which is essential for production workloads.

## Related
- `kernel-attention-ascendc`, `technique-memory-optimization`, `technique-long-sequence`