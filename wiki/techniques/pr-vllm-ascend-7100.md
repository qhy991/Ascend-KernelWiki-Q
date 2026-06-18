---
id: technique-pr-vllm-ascend-7100
title: "PR Insight: vllm-project/vllm-ascend #7100"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - gmm
  - small-batch
  - performance
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/7100"
---

# PR Insight: vllm-project/vllm-ascend #7100

**Title:** GMM custom operator optimization in small batch scenarios

## Overview
Optimizes the GMM (Grouped Matrix Multiplication) custom operator for small batch scenarios, improving MoE routing performance. The optimization demonstrates measurable performance gains with reduced TPOT (Time Per Output Token) and increased token throughput.

## Technical Significance
Improves small batch MoE performance by optimizing GMM operator implementation. Benchmarks on Qwen3-30B show TPOT reduction from 7.9ms to 7.0ms and throughput increase from 125.47 to 140.63 token/s in batch 1 scenarios, demonstrating tangible performance improvements.

## Related
- `technique-gmm`, `technique-moe`, `technique-small-batch-optimization`, `technique-custom-operator`