---
id: technique-pr-samples-2222
title: "PR Insight: Ascend/samples #2222"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - reduce
  - whole-reduce
  - non-aligned
  - ascendc
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2222"
---

# PR Insight: Ascend/samples #2222

**Title:** 添加非对齐样例WholeReduceSum

## Overview
This PR adds a WholeReduceSum sample for non-aligned memory scenarios, demonstrating how to perform reduction operations when data is not aligned to optimal memory boundaries.

## Technical Significance
Addresses the common challenge of handling non-aligned data in real-world workloads, showing how to maintain performance and correctness even when data doesn't match hardware alignment requirements.

## Related
- `technique-cube-vector-overlap`
- `technique-data-reuse`