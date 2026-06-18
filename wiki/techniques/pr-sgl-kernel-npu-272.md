---
id: technique-pr-sgl-kernel-npu-272
title: "PR Insight: sgl-project/sgl-kernel-npu #272"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - a3
  - shmem
  - normal-mode
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/272"
---

# PR Insight: sgl-project/sgl-kernel-npu #272

**Title:** a3 normal dispatch&combine with shmem

## Overview
Implements A3 normal dispatch and combine operators with shared memory (shmem) support. The implementation includes comprehensive tiling and kernel-side operations, enabled by setting DEEPEP_SHMEM_ENABLE=1 environment variable.

## Technical Significance
Shmem support for A3 normal mode operators provides efficient inter-process communication for distributed MoE inference. The implementation enables better resource utilization and reduced communication overhead for A3 architecture deployments, maintaining compatibility with normal mode while adding shmem optimization paths.

## Related
- `wiki-kernel-moe`
- `wiki-technique-shared-memory`
- `wiki-hardware-a3`
- `wiki-technique-distributed`