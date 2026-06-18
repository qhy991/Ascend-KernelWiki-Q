---
id: technique-pr-sgl-kernel-npu-415
title: "PR Insight: sgl-project/sgl-kernel-npu #415"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - wan2.2
  - scale-shift
  - kernel-tuning
  - performance-optimization
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/415"
---

# PR Insight: sgl-project/sgl-kernel-npu #415

**Title:** Add and update kernel for Wan

## Overview
This PR optimizes kernel launch overhead for Wan video generation models by using the number of physical cores as grid[0] and performing computations in loops within each core. The implementation uses autotune to find optimal block sizes, achieving average 4.4% E2E performance improvement with gains up to 9.7% in TP > SP scenarios.

## Technical Significance
Reducing kernel launch overhead through core-based grid organization significantly improves performance for video generation workloads where many small kernels are executed. The autotune-based block size selection eliminates manual parameter tuning while optimizing for specific hardware configurations and parallelization strategies.

## Related
- `kernel-scale-shift`, `kernel-rmsnorm-split`, `technique-kernel-tuning`, `technique-latency-optimization`