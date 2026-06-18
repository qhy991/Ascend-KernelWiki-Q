---
id: technique-pr-sgl-kernel-npu-430
title: "PR Insight: sgl-project/sgl-kernel-npu #430"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - lora
  - cube-unit
  - revert
  - mamba
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/430"
---

# PR Insight: sgl-project/sgl-kernel-npu #430

**Title:** Revert "LoRA: Implementing kernels using CUBE computation unit"

## Overview
This PR reverts the LoRA CUBE unit implementation from PR #384, restoring the previous VECTOR unit-based implementations. The rollback removes all CUBE-specific code for sgemmc_expand, sgemmc_shrink kernels and associated tiling infrastructure.

## Technical Significance
Reverting the CUBE unit implementation suggests issues with the original approach, possibly related to correctness, performance, or compatibility. The return to VECTOR units maintains stability while preserving the functionality needed for LoRA operations in Mamba-style attention models.

## Related
- `kernel-lora`, `kernel-sgemm`, `hw-vector-unit`, `technique-revert`