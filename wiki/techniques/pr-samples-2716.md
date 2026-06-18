---
id: technique-pr-samples-2716
title: "PR Insight: Ascend/samples #2716"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - memory-hierarchy
  - l2-cache
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2716"
---

# PR Insight: Ascend/samples #2716

**Title:** add l2 bypass case

## Overview
This PR adds a sample demonstrating L2 cache bypass on Ascend. L2 bypass allows data to flow directly to L1 or global memory, bypassing the L2 cache in specific scenarios.

## Technical Significance
L2 bypass is an advanced memory optimization technique. It can improve performance for certain access patterns by reducing L2 cache pollution and latency, though it requires careful use to avoid degrading overall performance.

## Related
- `technique-data-reuse`, `memory-hierarchy-optimization`, `cache-bypass-patterns`