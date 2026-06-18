---
id: technique-pr-sgl-kernel-npu-173
title: "PR Insight: sgl-project/sgl-kernel-npu #173"
type: wiki-technique
architectures:
  - ascend910b
tags:
  - moe
  - dispatch
  - combine
  - batchsize
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/173"
---

# PR Insight: sgl-project/sgl-kernel-npu #173

**Title:** dispatch and combine batchsize support 4096 for A2

## Overview
Enables A2 dispatch and combine operators to support batch sizes up to 4096 by updating the tiling check batch size limits. The operators already supported this batch size, but the tiling validation was restricting it.

## Technical Significance
This change removes artificial batch size limitations in the tiling validation, allowing A2 operators to utilize their full capability for large batch processing. Supporting batch sizes up to 4096 is important for high-throughput inference scenarios where large batches are needed to maximize hardware utilization and improve overall throughput.

## Related
- `wiki-kernel-moe`
- `wiki-technique-tiling`
- `wiki-hardware-a2`
- `wiki-technique-batch-optimization`