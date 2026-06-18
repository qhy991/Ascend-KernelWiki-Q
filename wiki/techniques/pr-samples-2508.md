---
id: technique-pr-samples-2508
title: "PR Insight: Ascend/samples #2508"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - ascendc
  - matmul
  - quantization
  - cann-mobile
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2508"
---

# PR Insight: Ascend/samples #2508

**Title:** QuantMatMulCustom软件包替换正式Cann Mobile版本包

## Overview
This PR replaces the QuantMatMulCustom operator's software package with the official CANN Mobile version. CANN Mobile is a lightweight runtime for edge devices with Ascend NPUs.

## Technical Significance
Using official CANN Mobile packages ensures compatibility with edge deployment scenarios and follows best practices for mobile/edge development. This update makes the sample production-ready for mobile applications.

## Related
- `kernel-matmul-ascendc`, `technique-quantization`