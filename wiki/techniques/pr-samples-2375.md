---
id: technique-pr-samples-2375
title: "PR Insight: Ascend/samples #2375"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - ascendc
  - matmul
  - samples
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2375"
---

# PR Insight: Ascend/samples #2375

**Title:** add matmul_ABshare_custom

## Overview
This PR adds a new matmul sample called matmul_ABshare_custom, demonstrating a matrix multiplication kernel where input matrices A and B share memory buffers. This optimization reduces memory footprint and potentially improves cache utilization for certain workloads.

## Technical Significance
Memory sharing between input matrices is a valuable technique for memory-bound workloads on Ascend hardware. It demonstrates advanced buffer management in AscendC and can be applied to transformer inference where weight sharing patterns exist.

## Related
- `kernel-matmul-ascendc`, `technique-data-reuse`