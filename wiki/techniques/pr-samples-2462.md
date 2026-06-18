---
id: technique-pr-samples-2462
title: "PR Insight: Ascend/samples #2462"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - ascendc
  - matmul
  - quantization
  - custom-operator
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2462"
---

# PR Insight: Ascend/samples #2462

**Title:** 新增AscendC QuantMatMulCustom自定义算子及其调用样例

## Overview
This PR adds a new custom operator called QuantMatMulCustom that performs quantized matrix multiplication in AscendC, along with samples showing how to invoke it. This is a custom implementation of quantized GEMM rather than using the built-in quantized matmul operators.

## Technical Significance
Custom quantized matmul implementations allow developers to optimize for specific quantization schemes or fuse with other operations. The samples provide a reference for building custom quantized operators from scratch.

## Related
- `kernel-matmul-ascendc`, `technique-quantization`, `technique-custom-operators`