---
id: technique-pr-samples-2807
title: "PR Insight: Ascend/samples #2807"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - double-buffering
  - bugfix
  - ascendc
  - samples
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2807"
---

# PR Insight: Ascend/samples #2807

**Title:** 1115 fix double buffer

## Overview
This PR fixes a bug in the double buffering implementation. Double buffering is a performance optimization technique that overlaps computation with data transfer by using multiple buffers.

## Technical Significance
Double buffering is critical for hiding memory latency and maximizing utilization of the Cube and Vector units. A bug in double buffering can lead to incorrect results or performance degradation. This fix ensures samples correctly demonstrate this important optimization technique.

## Related
- technique-double-buffering
- technique-pipeline-scheduling