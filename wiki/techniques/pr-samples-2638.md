---
id: technique-pr-samples-2638
title: "PR Insight: Ascend/samples #2638"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - npu
  - default-value
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2638"
---

# PR Insight: Ascend/samples #2638

**Title:** 删除默认值npu

## Overview
This PR removes default NPU values from configuration or parameters. The change likely makes NPU device selection explicit rather than implicit, improving clarity in sample code.

## Technical Significance
Explicit device selection helps developers understand how to specify target NPU devices properly. Clear device selection is important for multi-device scenarios and ensures samples demonstrate correct usage patterns.

## Related
- `hw-cube-unit`
- `hw-vector-unit`