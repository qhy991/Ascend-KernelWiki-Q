---
id: technique-pr-samples-1990
title: "PR Insight: Ascend/samples #1990"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - ascendc
  - samples
  - elementwise
  - custom-op
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1990"
---

# PR Insight: Ascend/samples #1990

**Title:** 新增Addcdiv算子样例

## Overview
This PR adds a sample implementation of the Addcdiv (Add, Multiply, and Divide) operator. The sample demonstrates how to implement this compound elementwise operation using AscendC.

## Technical Significance
Addcdiv combines multiple elementwise operations (addition, multiplication, division) into a single fused operation. This sample teaches developers how to implement compound arithmetic operations efficiently on the Vector unit, potentially reducing memory traffic and improving performance by fusing operations.

## Related
- `technique-elementwise`
- `technique-operator-fusion`
- `technique-vector-unit`