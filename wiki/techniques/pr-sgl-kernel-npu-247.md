---
id: technique-pr-sgl-kernel-npu-247
title: "PR Insight: sgl-project/sgl-kernel-npu #247"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - deepep
  - shmem
  - initialization
  - memory
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/247"
---

# PR Insight: sgl-project/sgl-kernel-npu #247

**Title:** Added shmem initialization in the DeepEP adaptation layer.

## Overview
Adds shared memory (shmem) initialization functionality to the DeepEP adaptation layer, including build system updates and shmem header implementation.

## Technical Significance
Shared memory initialization is critical for efficient inter-process communication in distributed DeepEP deployments. The shmem infrastructure enables optimized data sharing between processes, reducing memory copy overhead and improving overall communication efficiency for MoE operations across distributed processes.

## Related
- `wiki-kernel-moe`
- `wiki-technique-shared-memory`
- `wiki-technique-ipc`
- `wiki-technique-memory-optimization`