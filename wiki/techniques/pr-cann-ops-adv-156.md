---
id: technique-pr-cann-ops-adv-156
title: "PR Insight: cann-ops-adv #156"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - quantization
  - matmul
  - w4a8
  - ascendc
confidence: inferred
sources:
  - "https://gitee.com/ascend/cann-ops-adv/pulls/156"
---

# PR Insight: cann-ops-adv #156 - 1、新增GMM W4A8特性

## Overview
This PR adds W4A8 (4-bit weights, 8-bit activations) quantization support for GMM (Grouped Matrix Multiplication), enabling highly memory-efficient MoE expert computation on Ascend NPUs.

## Technical Significance
W4A8 quantization significantly reduces memory bandwidth and storage for MoE expert weights while maintaining acceptable accuracy. This is critical for scaling large MoE models on Ascend NPUs, where expert weight size is a major memory bottleneck.

## Related
- `kernel-grouped-gemm`
- `kernel-quant-matmul`
- `kernel-moe`
- `technique-quantization-int8`