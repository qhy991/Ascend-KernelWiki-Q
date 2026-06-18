---
id: technique-pr-samples-2656
title: "PR Insight: Ascend/samples #2656"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - ascendc
  - add-custom
  - tiling-sink
  - optimization
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2656"
---

# PR Insight: Ascend/samples #2656

**Title:** 【tiling下沉样例】【AR20250522891845】AddCustomTilingSink样例

## Overview
This PR adds an AddCustomTilingSink sample demonstrating "tiling sink" optimization. Tiling sink moves tiling logic from the host to the kernel or NPU side, reducing host-NPU communication overhead.

## Technical Significance
Tiling sink is an advanced optimization that reduces launch overhead and enables more dynamic, data-dependent tiling strategies. The sample provides a reference for implementing this pattern.

## Related
- `pattern-tiling`, `technique-double-buffering`