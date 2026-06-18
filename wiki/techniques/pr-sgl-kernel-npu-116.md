---
id: technique-pr-sgl-kernel-npu-116
title: "PR Insight: sgl-project/sgl-kernel-npu #116"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - matmul
  - quantization
  - dynamic-shape
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/116"
---

# PR Insight: sgl-project/sgl-kernel-npu #116

**Title:** EPLB for fused_deep_moe

## Overview
This PR adds Expert Per-Load Balancing (EPLB) support to the FusedDeepMoe operator, including a new recvCount output and support for dynamic inputs. It updates host code, kernel implementations, and grouped matmul kernels.

## Technical Significance
EPLB optimizes expert load balancing by tracking receive counts per expert, enabling more intelligent token distribution and reducing expert underutilization. Dynamic input support improves flexibility for varying batch sizes and sequence lengths, crucial for production inference workloads.

## Related
- `technique-moe`, `kernel-matmul-ascendc`, `technique-quantization`