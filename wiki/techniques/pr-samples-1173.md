---
id: technique-pr-samples-1173
title: "PR Insight: Ascend/samples #1173"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - image-processing
  - memory-alignment
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1173"
---

# PR Insight: Ascend/samples #1173

**Title:** AclLiteImage添加对齐宽高的参数

## Overview
This PR adds parameters for aligned width and height to the AclLiteImage class or utility.

## Technical Significance
Memory alignment is critical for efficient processing on Ascend hardware. Properly aligned images enable better utilization of the vector unit and avoid bank conflicts in the unified buffer. Adding alignment parameters gives developers control over memory layout optimization for their specific workloads.

## Related
- hw-bank-conflict-avoidance
- hw-vector-unit
- hw-unified-buffer