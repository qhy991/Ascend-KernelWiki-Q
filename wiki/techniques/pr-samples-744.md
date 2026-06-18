---
id: technique-pr-samples-744
title: "PR Insight: Ascend/samples #744"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - dvpp
  - memory-allocation
  - bugfix
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/744"
---

# PR Insight: Ascend/samples #744

**Title:** fix bug (使用dvpp必须使用acldvppMalloc分配输入输出内存)

## Overview
This PR fixes a bug where DVPP (Digital Vision Pre-Processing) operations were not using the proper memory allocation function. The fix ensures that acldvppMalloc is used for allocating input and output memory when using DVPP operations.

## Technical Significance
Proper memory allocation for DVPP operations is critical for correct functionality and performance on Ascend hardware. DVPP requires specialized memory allocation that works with the hardware acceleration units, and using the wrong allocation function can cause crashes or undefined behavior.

## Related
- N/A (DVPP memory management)