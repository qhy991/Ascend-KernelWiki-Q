---
id: technique-pr-sgl-kernel-npu-329
title: "PR Insight: sgl-project/sgl-kernel-npu #329"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - deepep
  - environment-variables
  - hccl-optimization
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/329"
---

# PR Insight: sgl-project/sgl-kernel-npu #329

**Title:** The environment variable DEEPEP_HCCL_BUFFSIZE is added

## Overview
This PR introduces the DEEPEP_HCCL_BUFFSIZE environment variable to control HCCL buffer size in DeepEP operators. The implementation provides fallback logic that prioritizes DEEPEP_HCCL_BUFFSIZE, then falls back to HCCL_BUFFSIZE, and finally uses a default value of 200MB when neither is set.

## Technical Significance
Adding a dedicated DeepEP-specific HCCL buffer size environment variable allows fine-grained control over memory allocation without conflicting with other HCCL operations. This enables users to optimize memory usage for DeepEP MoE workloads independently from other HCCL-based operations in the inference pipeline.

## Related
- `technique-hccl-optimization`, `technique-memory-management`, `hw-unified-buffer`