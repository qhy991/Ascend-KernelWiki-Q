---
id: technique-pr-samples-2246
title: "PR Insight: Ascend/samples #2246"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - pad
  - memory-alignment
  - ascendc
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2246"
---

# PR Insight: Ascend/samples #2246

**Title:** 添加Abs非对齐样例，使用Pad进行非对齐搬运

## Overview
This PR adds an unaligned use case for the Abs operator, demonstrating how to use Pad for non-aligned data movement. This pattern is common when dealing with boundary conditions or irregular tensor shapes.

## Technical Significance
Demonstrates padding techniques for handling unaligned memory access in AscendC operators. Padding is crucial for maintaining alignment requirements of hardware units while processing arbitrary input shapes.

## Related
- `technique-format-conversion`
- `wiki-hardware-unified-buffer`