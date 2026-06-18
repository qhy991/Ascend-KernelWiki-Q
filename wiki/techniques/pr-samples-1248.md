---
id: technique-pr-samples-1248
title: "PR Insight: Ascend/samples #1248"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - cv
  - resize
  - padding
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1248"
---

# PR Insight: Ascend/samples #1248

**Title:** 【轻量级 PR】：开放单图多图抠图缩放边界填充的填充模式

## Overview
This PR exposes or opens up the padding mode configuration for single-image and multi-image cropping, resizing, and boundary padding operations.

## Technical Significance
Exposing padding mode configuration gives developers more control over preprocessing behavior. Different padding modes (zero, reflect, edge, etc.) have different performance characteristics on Ascend hardware. Some modes may be more efficiently implemented using vector operations, while others may require scalar processing or format conversions.

## Related
- technique-vector-unit
- technique-format-conversion
- hw-unified-buffer