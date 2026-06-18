---
id: technique-pr-samples-1461
title: "PR Insight: Ascend/samples #1461"
type: wiki-technique
architectures:
  - ascend910b
tags:
  - samples
  - ascendc
  - custom-operator
  - l1-buffer
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1461"
---

# PR Insight: Ascend/samples #1461

**Title:** 自定义算子适配910B. 注意，910B的L1 size比较小，而验证case的weight太大，在910B上无法生成om，这里将测试用例改小一点

## Overview
This PR adapts a custom operator sample for Ascend 910B hardware. The PR addresses an issue where the L1 buffer size on 910B is smaller than on other variants, causing OM model generation failures due to large weight sizes in the verification test case. The fix reduces the test case size to fit within 910B memory constraints.

## Technical Significance
This highlights the importance of hardware-specific memory constraints when developing AscendC operators, particularly for L1 buffer management. Understanding the smaller L1 size on 910B is critical for custom operator portability across Ascend architectures.

## Related
- hw-l1-buffer
- technique-memory-optimization
- technique-custom-operator