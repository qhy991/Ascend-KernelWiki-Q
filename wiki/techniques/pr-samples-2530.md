---
id: technique-pr-samples-2530
title: "PR Insight: Ascend/samples #2530"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - ascendc
  - matmul
  - workspace
  - api
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2530"
---

# PR Insight: Ascend/samples #2530

**Title:** 修改Matmul样例，将localMemSize通过host接口获取并传入kernel

## Overview
This PR modifies the matmul samples to retrieve localMemSize through the host interface and pass it to the kernel. This approach queries available memory rather than hardcoding workspace sizes.

## Technical Significance
Dynamic workspace sizing based on actual available memory improves portability across different Ascend hardware and CANN versions. It prevents hard-coded size assumptions that could cause out-of-memory errors.

## Related
- `kernel-matmul-ascendc`, `pattern-api-usage`, `hw-unified-buffer`