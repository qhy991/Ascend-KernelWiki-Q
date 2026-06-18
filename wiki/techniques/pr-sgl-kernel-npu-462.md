---
id: technique-pr-sgl-kernel-npu-462
title: "PR Insight: sgl-project/sgl-kernel-npu #462"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - gated-delta-rule
  - mega-kernel
  - qwen3.5
  - performance-optimization
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/462"
---

# PR Insight: sgl-project/sgl-kernel-npu #462

**Title:** feat: pto-isa gdn mega kernel

## Overview
This PR integrates the pto-isa mega-kernel for chunk_gated_delta_rule_fwd, combining 6 kernels (cumsum, chunk_h, chunk_o, dot_kkt, tri_inverse, wy_fast) into a single kernel launch. The mega-kernel supports initial_state and output_final_state modes, achieving 2-15% speedup across Qwen 3.5/3.6 models with TP=1.

## Technical Significance
The mega-kernel approach significantly reduces kernel launch overhead by fusing multiple gated delta rule operations into a single execution. This optimization provides consistent performance improvements across various input lengths (32-32k) and demonstrates particular benefits in realistic serving benchmarks, making it highly valuable for Qwen 3.5/3.6 inference.

## Related
- `kernel-gated-delta-rule`, `kernel-chunk-gdn`, `technique-mega-kernel`, `technique-operator-fusion`