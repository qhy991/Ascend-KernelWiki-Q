---
id: technique-pr-sgl-kernel-npu-517
title: "PR Insight: sgl-project/sgl-kernel-npu #517"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - attention
  - mte
  - kernel-scheduling
  - inference
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/517"
---

# PR Insight: sgl-project/sgl-kernel-npu #517

**Title:** feat: pto mega-gdn support dynamic num heads

## Overview
This PR adds dynamic head count support to the PTO (Per-Token Optimization) mega-chunk GDN (Gated Deep Network) attention kernel. The implementation makes key-value head counts fully dynamic and supports multiple value head configurations (16, 24, 32, 48, 64) in a single binary. The changes also simplify CMake and launch logic, making PTO the default backend unless explicitly overridden.

## Technical Significance
Dynamic head count support significantly improves the flexibility and performance of the GDN attention kernel. Benchmarking shows 50%-300% speedup over the Triton backend, with greater gains at smaller context lengths. End-to-end testing demonstrates 37% throughput improvement on GSM8k with maintained accuracy. This enhancement enables more efficient attention computation across various model configurations and reduces deployment complexity.

## Related
- `kernel-attention`
- `kernel-gdn`
- `technique-mte-optimization`
- `pattern-dynamic-shape`