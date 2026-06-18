---
id: technique-pr-sgl-kernel-npu-63
title: "PR Insight: sgl-project/sgl-kernel-npu #63"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - deepep
  - combine
  - memory-management
  - isolation
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/63"
---

# PR Insight: sgl-project/sgl-kernel-npu #63

**Title:** combine use dedicated memory

## Overview
This PR configures the combine operation to use dedicated memory to ensure no memory intersection with dispatch operations. Updates deep_ep.cpp buffer allocation and combine kernel tiling to use isolated memory regions.

## Technical Significance
Prevents memory corruption issues that could occur when dispatch and combine operations access overlapping memory regions. Dedicated memory allocation ensures clean separation between stages, critical for correct MoE inference where dispatch writes expert outputs and combine reads them.

## Related
- technique-memory-management
- technique-moe-combine
- technique-memory-isolation