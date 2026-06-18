---
id: technique-pr-sgl-kernel-npu-250
title: "PR Insight: sgl-project/sgl-kernel-npu #250"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - low-latency
  - shmem
  - distributed
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/250"
---

# PR Insight: sgl-project/sgl-kernel-npu #250

**Title:** add shmem implementation for low_latency moe

## Overview
Implements shared memory (shmem) versions of low_latency MoE distribute operators, including comprehensive dispatch and combine implementations with tiling support. Adds DEEPEP_SHMEM_ENABLE environment variable for shmem activation control.

## Technical Significance
Shared memory implementations significantly reduce inter-process communication overhead for low-latency MoE operations. The shmem-based operators avoid expensive data copies between processes, enabling faster distributed MoE inference. The comprehensive implementation includes both host-side tiling and kernel-side operations for optimal performance.

## Related
- `wiki-kernel-moe`
- `wiki-technique-shared-memory`
- `wiki-technique-low-latency`
- `wiki-technique-distributed`