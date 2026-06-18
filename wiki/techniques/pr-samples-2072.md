---
id: technique-pr-samples-2072
title: "PR Insight: Ascend/samples #2072"
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
  - "https://gitee.com/ascend/samples/pulls/2072"
---

# PR Insight: Ascend/samples #2072

**Title:** 修改Add自定义算子用例shape信息与修复load_library样例

## Overview
This PR fixes shape information in Add custom operator test cases and repairs the load_library sample implementation. The changes correct metadata used in custom operator loading and execution.

## Technical Significance
Correct shape metadata is essential for AscendC operators to properly tile data for the Cube/Vector units and allocate Unified Buffer space. The load_library fix ensures dynamic loading of custom operators works correctly, which is critical for inference frameworks that need to register custom kernels at runtime.

## Related
- `technique-ascendc`
- `technique-tiling-strategy`