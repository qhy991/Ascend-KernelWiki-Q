---
id: technique-pr-vllm-ascend-4495
title: "PR Insight: vllm-project/vllm-ascend #4495"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - nz-format
  - vllm
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/4495"
---

# PR Insight: vllm-project/vllm-ascend #4495

**Title:** For nz unset in bf16&fp16

**Author:** henryxuxu0716 | **Merged:** 2025-11-28

## Overview
Modifies linear, common_fused_moe for improved functionality. The changes affect core inference operations and model compatibility.

## Technical Significance
NZ format is a key Ascend-specific memory layout that optimizes data access patterns for matrix operations. Proper handling of NZ format in both FP16 and BF16 is essential for achieving peak performance.

## Related
- `technique-nz-tiling`
