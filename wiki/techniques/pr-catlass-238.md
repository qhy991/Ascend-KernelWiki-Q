---
id: technique-pr-catlass-238
title: "PR Insight: Ascend/catlass #238"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - catlass
  - matmul
  - quantization
  - w8a16
confidence: inferred
sources:
  - "https://gitee.com/ascend/catlass/pulls/238"
---

# PR Insight: Ascend/catlass #238

**Title:** 新增30_w8a16_matmul

## Overview
This PR adds example 30 demonstrating W8A16 (8-bit weights, 16-bit activations) quantized matrix multiplication. It shows how to implement efficient mixed-precision matmul on Ascend hardware.

## Technical Significance
W8A16 quantization is a popular inference optimization that reduces memory bandwidth while maintaining accuracy. This example provides a reference implementation for quantized matmul, which is essential for deploying large models with reduced memory footprint.

## Related
- `kernel-matmul-ascendc`
- `technique-quantization`
- `technique-format-conversion`