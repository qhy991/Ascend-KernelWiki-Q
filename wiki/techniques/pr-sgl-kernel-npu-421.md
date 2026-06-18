---
id: technique-pr-sgl-kernel-npu-421
title: "PR Insight: sgl-project/sgl-kernel-npu #421"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - deepep
  - notify-dispatch
  - memory-management
  - bugfix
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/421"
---

# PR Insight: sgl-project/sgl-kernel-npu #421

**Title:** [deepep] fix notify use ub exceeds the limit

## Overview
This PR fixes a "MPU address access is invalid" error in the notify_dispatch kernel caused by Unified Buffer (UB) usage exceeding hardware limits. The solution reduces batchRounds when the number of experts per NPU is large (e.g., 128 experts with round=32 parameter configuration in Qwen3.5-35B model).

## Technical Significance
Preventing UB overflow is critical for DeepEP operation with large expert counts, as excessive buffer usage can cause kernel crashes. The dynamic batchRounds adjustment ensures proper memory management while maintaining performance for high-expert-count MoE models running on A3 hardware.

## Related
- `kernel-notify-dispatch`, `kernel-deepep-normal`, `technique-memory-management`, `hw-unified-buffer`