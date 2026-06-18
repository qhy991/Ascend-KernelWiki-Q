---
id: technique-pr-samples-3
title: "PR Insight: Ascend/samples #3"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - ascendc
  - samples
  - elementwise
  - broadcast
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/3"
---

# PR Insight: Ascend/samples #3

**Title:** update broadcast

## Overview
This PR updates the broadcast operation implementation in AscendC samples. Broadcast is a fundamental elementwise operation that expands tensor dimensions for arithmetic operations between tensors of different shapes.

## Technical Significance
Broadcast operations require careful handling of memory access patterns and shape broadcasting logic. The sample likely demonstrates how to implement efficient broadcast operations on the Vector unit, handling various tensor shape combinations while minimizing redundant computation and memory transfers.

## Related
- `technique-elementwise`
- `technique-vector-unit`
- `technique-unified-buffer`