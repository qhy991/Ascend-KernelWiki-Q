---
id: technique-pr-sgl-kernel-npu-400
title: "PR Insight: sgl-project/sgl-kernel-npu #400"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - dispatch-ffn-combine
  - testing
  - validation
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/400"
---

# PR Insight: sgl-project/sgl-kernel-npu #400

**Title:** add fused_deep_moe test for dispatch_ffn_combine

## Overview
This PR adds precision and performance tests for the dispatch_ffn_combine kernel in the fused_deep_moe configuration. The tests validate numerical correctness and measure performance improvements, showing fused execution time of ~1019μs versus baseline ~1397μs across 16 ranks with num_tokens=256, hidden=7168, num_experts=256, topk=8.

## Technical Significance
Comprehensive testing of dispatch_ffn_combine ensures both numerical accuracy and performance validation for the fused MoE execution path. The benchmark results demonstrate ~27% speedup from the fused implementation, providing evidence for the performance benefits of the mega-kernel approach.

## Related
- `kernel-dispatch-ffn-combine`, `kernel-fused-deep-moe`, `technique-testing`, `technique-validation`