---
id: technique-pr-catlass-99
title: "PR Insight: Ascend/catlass #99"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - catlass
  - matmul
  - device-layer
  - moe
confidence: inferred
sources:
  - "https://gitee.com/ascend/catlass/pulls/99"
---

# PR Insight: Ascend/catlass #99

**Title:** Add device-layer feature to master in 06_optimized_matmul, 07_grouped_matmul_slice_m_per_token_dequant_moe, 08_grouped_matmul

## Overview
This PR adds device-layer feature support to the master branch for multiple matmul variants including optimized matmul, grouped matmul for MoE token routing, and general grouped matmul implementations.

## Technical Significance
Device-layer abstraction enables better code reuse across different matmul variants and simplifies integration with host-side launchers. For MoE workloads, grouped matmul with per-token dequantization is essential for efficient expert routing on Ascend hardware.

## Related
- `kernel-matmul-ascendc`
- `kernel-moe-ascendc`
- `technique-operator-fusion`