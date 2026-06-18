---
id: technique-pr-samples-2540
title: "PR Insight: Ascend/samples #2540"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - abspad
  - tposition
  - queue-position
  - memory-management
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2540"
---

# PR Insight: Ascend/samples #2540

**Title:** AbsPad case remove unused workspace; using TPosition instead of QuePosition

## Overview
This PR modifies the AbsPad sample by removing unused workspace allocation and replacing QuePosition with TPosition. The changes optimize memory usage and update to use newer position-related APIs.

## Technical Significance
Removing unused workspace reduces memory overhead and improves kernel efficiency. TPosition provides more accurate tensor position tracking compared to QuePosition, leading to better memory management and performance.

## Related
- `technique-data-reuse`
- `hw-unified-buffer`
- `technique-double-buffering`