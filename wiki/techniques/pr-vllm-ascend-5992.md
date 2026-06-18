---
id: technique-pr-vllm-ascend-5992
title: "PR Insight: vllm-project/vllm-ascend #5992"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - fusion
  - performance
  - configuration
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5992"
---

# PR Insight: vllm-project/vllm-ascend #5992

**Title:** 【feat】switch for fusion ops gmmswigluquant

## Overview
This PR adds a configuration parameter to control whether the gmmswigluquant fusion operator is enabled. The operator is enabled by default (True), but can be disabled for small GPU configurations where the fusion operator can cause performance degradation.

## Technical Significance
Fusion operators like gmmswigluquant combine multiple operations (GEMM, SwiGLU, quantization) into a single kernel, reducing memory transfers and improving performance. However, with small GPU counts, the overhead of fusion can outweigh benefits. The PR adds a configurable switch to disable fusion when it's detrimental. Performance testing on GLM 4.6 (W8A8) with a single A3 node (EP16, TP16) shows the configuration allows tuning based on deployment scale.

## Related
- `technique-operator-fusion`, `technique-moe`, `technique-configuration`