---
id: technique-pr-vllm-ascend-4518
title: "PR Insight: vllm-project/vllm-ascend #4518"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - inference
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/4518"
---

# PR Insight: vllm-project/vllm-ascend #4518

**Title:** [Fix] Fix FIA `query` and `query_start_loc` shape mismatch error

**Author:** momo609 | **Merged:** 2025-12-03

## Overview
Fixes a bug in  operations. The issue affects model accuracy and stability. Changes are focused on core operator implementations.

## Technical Significance
This change improves the robustness and performance of core inference operations. Better handling of edge cases and more efficient operator implementations contribute to overall system stability and throughput.

## Related
- Related to MoE, attention, and quantization optimization techniques
