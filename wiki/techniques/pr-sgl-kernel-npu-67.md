---
id: technique-pr-sgl-kernel-npu-67
title: "PR Insight: sgl-project/sgl-kernel-npu #67"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - deepep
  - buffer-management
  - memory-isolation
  - notify-dispatch
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/67"
---

# PR Insight: sgl-project/sgl-kernel-npu #67

**Title:** Separate the buffers used by D/C and notify_dispatch to avoid conflicts

## Overview
This PR separates buffer allocation by allocating 204MB dedicated memory for notify_dispatch, then allowing dispatch/combine operations to use memory afterward. Updates comm_args.h and normal dispatch/combine kernels to use isolated buffer regions.

## Technical Significance
Resolves memory access conflicts between notify_dispatch and dispatch/combine operations that could cause data corruption. Sequential buffer allocation ensures proper memory lifecycle management, critical for correct MoE inference where synchronization and data integrity are essential.

## Related
- technique-memory-management
- technique-buffer-isolation
- technique-lifecycle-management