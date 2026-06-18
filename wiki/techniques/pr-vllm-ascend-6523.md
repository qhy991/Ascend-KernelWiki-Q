---
id: technique-pr-vllm-ascend-6523
title: "PR Insight: vllm-project/vllm-ascend #6523"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - rotary-embedding
  - rope
  - refactor
  - cleanup
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6523"
---

# PR Insight: vllm-project/vllm-ascend #6523

**Title:** [Ops][Refactor] Remove custom rotary_embedding operator

## Overview
This PR removes the custom rotary_embedding operator implementation including C++ kernel code, PyTorch bindings, and associated tests. The codebase now relies on the native torch_npu._npu_rotary_embedding implementation instead of the custom platform-specific kernel.

## Technical Significance
Simplifies the codebase by removing duplicate rotary embedding implementations and relying on the optimized standard NPU library implementation. This reduces maintenance burden and potential for inconsistencies while leveraging better-optimized native implementations.

## Related
- `kernel-attention`