---
id: technique-pr-sgl-kernel-npu-252
title: "PR Insight: sgl-project/sgl-kernel-npu #252"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - notify
  - shmem
  - adaptation
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/252"
---

# PR Insight: sgl-project/sgl-kernel-npu #252

**Title:** notify dispatch and combine operator adapted to shmem

## Overview
Adapts notify dispatch and combine operators to use shared memory (shmem) infrastructure. The adaptation includes updates to tiling implementations and operator interfaces for shmem compatibility.

## Technical Significance
The shmem adaptation for notify and combine operators enables efficient inter-process communication for MoE operations. By leveraging shared memory, these operators reduce data transfer overhead and improve overall distributed MoE performance. The adaptation maintains compatibility with existing interfaces while adding shmem optimization paths.

## Related
- `wiki-kernel-moe`
- `wiki-technique-shared-memory`
- `wiki-technique-ipc`
- `wiki-technique-adaptation`