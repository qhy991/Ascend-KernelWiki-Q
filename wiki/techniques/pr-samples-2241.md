---
id: technique-pr-samples-2241
title: "PR Insight: Ascend/samples #2241"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - atlas-a2
  - hardware-adaptation
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2241"
---

# PR Insight: Ascend/samples #2241

**Title:** 【1】部分算子增加对Atlas A2训练系列产品适配-infinity

## Overview
This PR adds Atlas A2 training series product support to a subset of operators. This involves adapting implementations for the new hardware generation's architecture and capabilities.

## Technical Significance
Demonstrates the systematic approach to hardware migration across multiple operators. Atlas A2 support requires understanding differences in compute units, memory hierarchy, and instruction sets compared to previous generations.

## Related
- `wiki-hardware-atlas-a2`
- `technique-pipeline-scheduling`