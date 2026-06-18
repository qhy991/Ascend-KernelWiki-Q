---
id: technique-pr-samples-1059
title: "PR Insight: Ascend/samples #1059"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - jpege
  - memory-management
  - synchronization
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1059"
---

# PR Insight: Ascend/samples #1059

**Title:** 增加jpege同步处理流程中的free input操作

## Overview
This PR adds memory cleanup (free input operations) to the synchronous processing workflow of the JPEG encoder (JPEGE). The modification ensures that input memory is properly deallocated after encoding completes in synchronous mode.

## Technical Significance
Proper memory deallocation in synchronous workflows prevents memory leaks, especially in batch processing or long-running services. Adding free input operations to the JPEGE sync path ensures that memory allocated for input images is released promptly after encoding, improving resource management stability.

## Related
- JPEG encoder (JPEGE) implementation
- Synchronous processing workflows
- Memory cleanup patterns
- Resource lifecycle management