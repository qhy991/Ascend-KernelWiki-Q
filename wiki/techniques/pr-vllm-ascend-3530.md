---
id: technique-pr-vllm-ascend-3530
title: "PR Insight: vllm-project/vllm-ascend #3530"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - attention
  - hccl-optimization
  - speculative-decoding
  - decode
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3530"
---

# PR Insight: vllm-project/vllm-ascend #3530

**Title:** remove redundant params in mla_preprocess kernel

## Overview
This pull request removes the redundant parameters `gamma1` and `beta1` (also named `gamma0`/`beta0` in some places) from the `mla_preprocess` kernel and its calling hierarchy. The changes are consistent across C++ kernel code, bindings, and Python call sites. The parameters were unused in the lower-level functions, so their removal is a good cleanup.

## Technical Significance
Removes redundant parameters in mla_preprocess kernel to simplify implementation and improve performance.

## Related
- `hw-cube-unit`
- `technique-speculative-decoding`
