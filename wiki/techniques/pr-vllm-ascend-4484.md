---
id: technique-pr-vllm-ascend-4484
title: "PR Insight: vllm-project/vllm-ascend #4484"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - inference
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/4484"
---

# PR Insight: vllm-project/vllm-ascend #4484

**Title:** fix qwen3vl mrope op

**Author:** shaopeng-666 | **Merged:** 2025-12-08

## Overview
Fixes a bug in rotary_embedding operations. The issue affects model accuracy and stability. Changes are focused on core operator implementations.

## Technical Significance
This change improves the robustness and performance of core inference operations. Better handling of edge cases and more efficient operator implementations contribute to overall system stability and throughput.

## Related
- Related to MoE, attention, and quantization optimization techniques
