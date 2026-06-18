---
id: technique-pr-samples-2512
title: "PR Insight: Ascend/samples #2512"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - printf
  - dumptensor
  - debugging
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2512"
---

# PR Insight: Ascend/samples #2512

**Title:** 新增printf和DumpTensor样例

## Overview
This PR adds new samples demonstrating printf and DumpTensor functionality. The examples show how to use printf for kernel debugging and DumpTensor for inspecting tensor values during execution.

## Technical Significance
Debugging tools like printf and DumpTensor are essential for kernel development. These samples provide developers with practical examples for inspecting kernel state, tensor values, and diagnosing issues in their implementations.

## Related
- `kernel-matmul-ascendc`
- `hw-unified-buffer`
- `technique-data-reuse`