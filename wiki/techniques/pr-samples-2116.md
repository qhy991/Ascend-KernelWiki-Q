---
id: technique-pr-samples-2116
title: "PR Insight: Ascend/samples #2116"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - ascendc
  - samples
  - shape-inference
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2116"
---

# PR Insight: Ascend/samples #2116

**Title:** 修改Input获取Shape方式

## Overview
This PR modifies how Input tensors retrieve their shape information in AscendC sample code. The change affects shape inference mechanisms used in custom operator implementations, likely improving compatibility with newer CANN versions or fixing shape-related bugs in sample applications.

## Technical Significance
Proper shape retrieval is critical for AscendC operators to correctly allocate memory (UB/L0/L1) and execute on the Cube/Vector units. This fix addresses shape inference accuracy, which directly impacts tiling strategy correctness and memory layout decisions in kernel development.

## Related
- `technique-tiling-strategy`
- `technique-workspace-management`