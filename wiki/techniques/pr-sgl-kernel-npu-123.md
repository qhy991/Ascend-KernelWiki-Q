---
id: technique-pr-sgl-kernel-npu-123
title: "PR Insight: sgl-project/sgl-kernel-npu #123"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - matmul
  - dynamic-shape
  - quantization
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/123"
---

# PR Insight: sgl-project/sgl-kernel-npu #123

**Title:** Support different token hidden sizes and gmm hidden sizes [FusedDeepMoe Operator]

## Overview
This PR expands FusedDeepMoe to support flexible dimensions: token lengths [512, 7168] instead of only 7168, and GMM hidden sizes [1024, 6144] instead of only 4096. It updates tiling and kernel code to handle these dynamic shapes.

## Technical Significance
Flexible dimension support enables FusedDeepMoe to serve a wider range of model architectures without kernel modifications. Proper tiling for variable shapes ensures efficient memory access and Cube utilization across different model configurations, improving operator reusability.

## Related
- `technique-moe`, `kernel-matmul-ascendc`, `technique-quantization`