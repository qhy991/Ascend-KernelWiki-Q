---
id: technique-pr-samples-2469
title: "PR Insight: Ascend/samples #2469"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - ascendc
  - matmul
  - quantization
  - samples
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2469"
---

# PR Insight: Ascend/samples #2469

**Title:** 添加Matmul常量化用例

## Overview
This PR adds matmul constant quantization use cases, extending the constant quantization samples from PR #2407. These additional samples likely cover more quantization formats or edge cases in constant weight handling.

## Technical Significance
Comprehensive constant quantization coverage is important because different model quantization schemes (per-tensor, per-channel, symmetric, asymmetric) require different handling. More samples provide better reference implementations.

## Related
- `kernel-matmul-ascendc`, `technique-quantization`, `technique-format-conversion`