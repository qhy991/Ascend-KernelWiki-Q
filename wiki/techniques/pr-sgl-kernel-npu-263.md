---
id: technique-pr-sgl-kernel-npu-263
title: "PR Insight: sgl-project/sgl-kernel-npu #263"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - shmem
  - decode
  - buffer
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/263"
---

# PR Insight: sgl-project/sgl-kernel-npu #263

**Title:** Add Shmem Implementations for MoE Decode Operators with Buffer

## Overview
Implements v2 shared memory versions of MoE decode operators with buffer support, replacing previous shmem kernel implementations. The comprehensive rewrite includes new dispatch and combine operators with optimized tiling and buffer management.

## Technical Significance
The v2 shmem implementation with buffer support provides significant improvements over the original design, offering better memory management and improved performance for decode-phase MoE operations. The buffer-based approach reduces overhead and improves scalability for long-running inference scenarios requiring efficient shared memory utilization.

## Related
- `wiki-kernel-moe`
- `wiki-technique-shared-memory`
- `wiki-technique-buffer-management`
- `wiki-technique-decode-optimization`