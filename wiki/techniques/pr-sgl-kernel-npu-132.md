---
id: technique-pr-sgl-kernel-npu-132
title: "PR Insight: sgl-project/sgl-kernel-npu #132"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - topk
  - quantization
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/132"
---

# PR Insight: sgl-project/sgl-kernel-npu #132

**Title:** support topk=-1

## Overview
This PR adds support for topk=-1 in MoE routing, which enables routing to all experts instead of a fixed subset. It updates dispatch/combine kernels and grouped matmul implementations.

## Technical Significance
Topk=-1 routing allows all experts to process tokens, useful for specialized models or debugging. This requires special handling in dispatch/combine as token counts per expert become deterministic rather than sparse, affecting communication patterns and memory allocation.

## Related
- `technique-moe`, `technique-hccl-optimization`, `technique-quantization`