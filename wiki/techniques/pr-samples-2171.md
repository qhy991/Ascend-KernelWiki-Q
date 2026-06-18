---
id: technique-pr-samples-2171
title: "PR Insight: Ascend/samples #2171"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - memory-allocation
  - huge-pages
  - ascendc
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2171"
---

# PR Insight: Ascend/samples #2171

**Title:** sample算子样例device申请内存优先使用大页内存

## Overview
This PR updates operator samples to prioritize huge page memory allocation for device memory, improving memory access efficiency.

## Technical Significance
Huge page allocation reduces TLB misses and improves memory bandwidth utilization, which is particularly beneficial for operator kernels with large memory footprints. This pattern should be applied in performance-critical operator implementations.

## Related
- `wiki-hardware-unified-buffer`
- `technique-data-reuse`