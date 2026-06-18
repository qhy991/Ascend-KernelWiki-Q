---
id: technique-pr-samples-2286
title: "PR Insight: Ascend/samples #2286"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - dynamic-input
  - tensor
  - ascendc
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2286"
---

# PR Insight: Ascend/samples #2286

**Title:** 新增动态输入Tensor数量自定义工程样例

## Overview
This PR adds a custom project sample demonstrating how to handle dynamic numbers of input tensors. This is important for operators that need to process varying numbers of inputs at runtime.

## Technical Significance
Shows techniques for handling dynamic tensor counts in AscendC operators, which is essential for flexible operator design. Demonstrates memory management and execution flow patterns for variadic inputs.

## Related
- `technique-double-buffering`
- `wiki-language-ascendc`