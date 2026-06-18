---
id: technique-pr-samples-1093
title: "PR Insight: Ascend/samples #1093"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - memory-allocation
  - aclrt
  - optimization
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1093"
---

# PR Insight: Ascend/samples #1093

**Title:** rtMalloc第三个参数ACL_MEM_MALLOC_NORMAL_ONLY改为ACL_MEM_MALLOC_HUGE_FIRST

## Overview
This PR changes the third parameter of rtMalloc from ACL_MEM_MALLOC_NORMAL_ONLY to ACL_MEM_MALLOC_HUGE_FIRST. This modification alters the memory allocation strategy to prefer huge pages first.

## Technical Significance
ACL_MEM_MALLOC_HUGE_FIRST prioritizes huge page allocation, which can improve performance for large memory allocations by reducing TLB misses and improving memory bandwidth. This change is particularly beneficial for inference workloads with large model weights or batch processing, where performance gains from huge pages are significant.

## Related
- Memory allocation strategies
- Huge page optimization
- ACL runtime API
- Memory performance tuning