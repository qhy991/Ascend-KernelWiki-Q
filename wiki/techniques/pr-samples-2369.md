---
id: technique-pr-samples-2369
title: "PR Insight: Ascend/samples #2369"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - data-reorganization
  - s2-operator
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2369"
---

# PR Insight: Ascend/samples #2369

**Title:** 【S2算子提交】DeepToSpace算子

## Overview
This PR submits the DeepToSpace operator as an S2 (level 2) operator sample, providing a reference implementation for the depth-to-space operation that reorganizes tensor data from depth to spatial dimensions.

## Technical Significance
Demonstrates complex data reorganization patterns on Ascend hardware, showing how to efficiently transpose and reshape tensors for computer vision applications requiring depth-to-space transformations.

## Related
- `technique-format-conversion`