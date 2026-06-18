---
id: technique-pr-samples-2212
title: "PR Insight: Ascend/samples #2212"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - memory-allocation
  - huge-pages
  - acl
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2212"
---

# PR Insight: Ascend/samples #2212

**Title:** 优先申请大页内存，使用ACL_MEM_MALLOC_HUGE_FIRST 替换ACL_MEM_MALLOC_NORMAL_ONLY

## Overview
This PR updates memory allocation in sample code to prioritize huge page memory by using ACL_MEM_MALLOC_HUGE_FIRST instead of ACL_MEM_MALLOC_NORMAL_ONLY.

## Technical Significance
Huge page memory allocation can improve performance by reducing TLB misses and improving memory access efficiency. This is particularly important for large model workloads with significant memory footprints.

## Related
- `wiki-hardware-unified-buffer`
- `technique-data-reuse`