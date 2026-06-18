---
id: technique-pr-samples-1901
title: "PR Insight: Ascend/samples #1901"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - add
  - elementwise
  - ascendc
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1901"
---

# PR Insight: Ascend/samples #1901

**Title:** 修改Add样例

## Overview
This PR modifies the Add operator sample, which demonstrates how to implement and use the element-wise Add operation on Ascend hardware. The changes likely improve the sample's correctness, clarity, or compatibility with current CANN versions, providing a better reference for implementing custom operators.

## Technical Significance
The Add operator is a fundamental building block in neural networks, and understanding how to implement it correctly in AscendC is essential for kernel development. This sample demonstrates basic AscendC programming patterns, memory management, and operator fusion strategies that apply to more complex element-wise operations on Ascend910/910B.

## Related
- `kernel-elementwise`
- `technique-operator-fusion`