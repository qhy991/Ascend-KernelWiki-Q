---
id: technique-pr-vllm-ascend-2805
title: "PR Insight: vllm-project/vllm-ascend #2805"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - code-cleanup
  - fused-ops
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2805"
---

# PR Insight: vllm-project/vllm-ascend #2805

**Title:** Remove unused code in fused_moe.py

## Overview
This PR removes unused code from the fused_moe.py implementation, cleaning up the MoE operator implementation by eliminating dead code paths and redundant functions.

## Technical Significance
Code maintenance cleanup that improves code quality and readability. Removing unused code reduces maintenance burden and potential confusion, making the MoE implementation easier to understand and maintain. This is particularly important for complex fused operators where unused code might suggest incorrect or outdated implementation patterns.

## Related
- `kernel-moe-ascendc`, `technique-operator-fusion`