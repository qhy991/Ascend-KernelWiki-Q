---
id: technique-pr-samples-2216
title: "PR Insight: Ascend/samples #2216"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - abs
  - gather
  - mask
  - memory-alignment
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2216"
---

# PR Insight: Ascend/samples #2216

**Title:** 添加非对齐样例AbsGatherMask

## Overview
This PR adds an unaligned use case for the AbsGatherMask operator, demonstrating how to combine absolute value, gather indexing, and masking operations with non-aligned memory access.

## Technical Significance
Shows advanced patterns for combining elementwise operations (abs) with gather operations and masking, which are common in attention mechanisms and conditional operations. Unaligned handling is crucial for real-world tensor shapes.

## Related
- `kernel-elementwise`
- `technique-bank-conflict-avoidance`