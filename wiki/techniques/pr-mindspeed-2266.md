---
id: technique-pr-mindspeed-2266
title: "PR Insight: Ascend/MindSpeed #2266"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - npu-permute
  - fusion
  - operator
  - documentation
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2266"
---

# PR Insight: Ascend/MindSpeed #2266

**Title:** 添加npu_permute融合算子特性兼容说明

## Overview
This PR adds compatibility documentation for the npu_permute fused operator. Permute operations are common in tensor manipulations, and fused operators combine multiple operations for efficiency.

## Technical Significance
Fused operators reduce memory traffic and improve performance by combining multiple operations into a single kernel. NPU-specific fused operators like npu_permute leverage Ascend hardware capabilities. Compatibility documentation helps users understand when and how to use this operator.

## Related
- `technique-operator-fusion`
- `kernel-permute`
- `pattern-fused-operators`
- `pattern-hardware-acceleration`