---
id: technique-pr-sgl-kernel-npu-397
title: "PR Insight: sgl-project/sgl-kernel-npu #397"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - dispatch-ffn-combine
  - fuse-mode
  - performance-optimization
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/397"
---

# PR Insight: sgl-project/sgl-kernel-npu #397

**Title:** deepep support different fuse_mode for dispatch_ffn_combine

## Overview
This PR adds support for different fusion modes (fuse_mode) in DeepEP's dispatch_ffn_combine operator, allowing runtime selection between fused_deep_moe and alternative execution strategies. Performance comparison shows baseline throughput of 2985.94 tokens/s versus 2438.48 tokens/s with fused_deep_moe for bs=4096 in prefill stage.

## Technical Significance
Supporting multiple fuse modes enables dynamic optimization based on model characteristics and hardware configurations, allowing operators to choose between fused and non-fused execution paths for optimal performance. This flexibility helps balance memory usage, kernel complexity, and computational efficiency across different MoE configurations.

## Related
- `kernel-dispatch-ffn-combine`, `kernel-fused-deep-moe`, `technique-execution-mode-selection`