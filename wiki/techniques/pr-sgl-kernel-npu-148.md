---
id: technique-pr-sgl-kernel-npu-148
title: "PR Insight: sgl-project/sgl-kernel-npu #148"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - attention
  - kv-cache
  - elementwise
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/148"
---

# PR Insight: sgl-project/sgl-kernel-npu #148

**Title:** add op transfer_kv_dim_exchange

## Overview
This PR adds a new operator `transfer_kv_dim_exchange` for handling KV dimension exchange operations, including host code, kernel implementation, and Python bindings with test cases.

## Technical Significance
KV dimension exchange is important for attention mechanisms where key/value tensors need reformatting between different layouts (e.g., head-major vs batch-major). The operator enables efficient in-place or streaming transformations without host-side copies, reducing memory bandwidth overhead.

## Related
- `kernel-attention-ascendc`, `technique-kv-cache`