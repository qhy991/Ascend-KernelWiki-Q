---
id: technique-pr-vllm-ascend-4356
title: "PR Insight: vllm-project/vllm-ascend #4356"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - quantization
  - vllm
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/4356"
---

# PR Insight: vllm-project/vllm-ascend #4356

**Title:** [refactor]support gatingtopk operator generalization

**Author:** 1092626063 | **Merged:** 2025-12-04

## Overview
Adds new functionality for experts_selector, test_fused_moe operations. The feature enhances model capabilities and performance.

## Technical Significance
This change improves the robustness and performance of core inference operations. Better handling of edge cases and more efficient operator implementations contribute to overall system stability and throughput.

## Related
- Related to MoE, attention, and quantization optimization techniques
