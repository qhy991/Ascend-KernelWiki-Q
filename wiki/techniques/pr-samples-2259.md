---
id: technique-pr-samples-2259
title: "PR Insight: Ascend/samples #2259"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - unpad
  - pad
  - memory-alignment
  - ascendc
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2259"
---

# PR Insight: Ascend/samples #2259

**Title:** 添加了AbsUnPad非对齐用例，使用UnPad进行搬出

## Overview
This PR adds an unaligned use case for the AbsUnPad operator, demonstrating how to use UnPad for data movement out of memory. This is important for handling non-contiguous memory layouts.

## Technical Significance
Shows techniques for handling unaligned memory access patterns in AscendC. UnPad operations are essential for converting between aligned internal formats and user-facing data layouts, especially for operators like absolute value that may have boundary conditions.

## Related
- `technique-format-conversion`
- `wiki-hardware-unified-buffer`