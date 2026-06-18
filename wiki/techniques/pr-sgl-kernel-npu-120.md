---
id: technique-pr-sgl-kernel-npu-120
title: "PR Insight: sgl-project/sgl-kernel-npu #120"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - testing
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/120"
---

# PR Insight: sgl-project/sgl-kernel-npu #120

**Title:** feat:add moe fused operator test draft

## Overview
This PR adds basic functional test code for the fused MoE operator, establishing the testing infrastructure for validating correctness and performance of MoE kernels.

## Technical Significance
Comprehensive testing is critical for MoE operators due to their complexity involving routing, distributed computation, and communication. The test infrastructure ensures reliability as features evolve and catches regressions in expert routing, quantization, and fusion logic.

## Related
- `technique-moe`, `technique-operator-fusion`