---
id: technique-pr-vllm-ascend-4352
title: "PR Insight: vllm-project/vllm-ascend #4352"
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
  - "https://github.com/vllm-project/vllm-ascend/pull/4352"
---

# PR Insight: vllm-project/vllm-ascend #4352

**Title:** Revert "[cherry-pick][refactor]support gatingtopk operator generalization (#4050)"

**Author:** wangxiyuan | **Merged:** 2025-11-21

## Overview
Adds new functionality for experts_selector operations. The feature enhances model capabilities and performance.

## Technical Significance
This change improves the robustness and performance of core inference operations. Better handling of edge cases and more efficient operator implementations contribute to overall system stability and throughput.

## Related
- Related to MoE, attention, and quantization optimization techniques
