---
id: technique-pr-samples-1974
title: "PR Insight: Ascend/samples #1974"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - matmul
  - api-update
  - ascendc
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1974"
---

# PR Insight: Ascend/samples #1974

**Title:** 修改MatMul调用API

## Overview
This PR updates the MatMul sample to use the latest AscendC API for kernel invocation, ensuring compatibility with current CANN SDK versions and showcasing best practices.

## Technical Significance
Improves code maintainability and future compatibility by using current API patterns. The update may also include performance improvements or bug fixes from newer API versions.

## Related
- `kernel-matmul-ascendc`
- `technique-instruction-queue`