---
id: technique-pr-vllm-ascend-4325
title: "PR Insight: vllm-project/vllm-ascend #4325"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mtp
  - vllm
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/4325"
---

# PR Insight: vllm-project/vllm-ascend #4325

**Title:** [Fix] Remove unnecessary NPU synchronization in MTP proposer

**Author:** yiz-liu | **Merged:** 2025-11-24

## Overview
Fixes a bug in  operations. The issue affects model accuracy and stability. Changes are focused on core operator implementations.

## Technical Significance
This change improves the robustness and performance of core inference operations. Better handling of edge cases and more efficient operator implementations contribute to overall system stability and throughput.

## Related
- Related to MoE, attention, and quantization optimization techniques
