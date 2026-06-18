---
id: technique-pr-vllm-ascend-7010
title: "PR Insight: vllm-project/vllm-ascend #7010"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - gmm
  - custom-operator
  - small-batch
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/7010"
---

# PR Insight: vllm-project/vllm-ascend #7010

**Title:** [MOE] commit GMM custom operator

## Overview
Implements a GMM (Grouped Matrix Multiplication) custom operator optimized for small batch scenarios in MoE models. The operator is submitted for subsequent integration into the MoE processing pipeline.

## Technical Significance
Provides optimized MoE routing computation through custom GMM operator that improves performance in small batch scenarios. The custom operator leverages Ascend hardware capabilities for efficient grouped matrix multiplication operations.

## Related
- `technique-moe`, `technique-gmm`, `technique-custom-operator`, `technique-small-batch-optimization`