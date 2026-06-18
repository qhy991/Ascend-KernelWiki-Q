---
id: technique-pr-sgl-kernel-npu-302
title: "PR Insight: sgl-project/sgl-kernel-npu #302"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - batchsize
  - int8
  - testing
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/302"
---

# PR Insight: sgl-project/sgl-kernel-npu #302

**Title:** fix little batchsize and int8 quant on ci

## Overview
Fixes issues with small batch sizes and INT8 quantization in CI testing. Adds test cases for edge scenarios including num-tokens=1/2 and configurations where dispatch_use_fp8 is set to false.

## Technical Significance
Edge case testing for small batches and quantization configurations is critical for ensuring production reliability. These fixes prevent CI failures and runtime errors that occur in extreme but realistic deployment scenarios, improving overall system robustness.

## Related
- `wiki-kernel-moe`
- `wiki-technique-int8-quantization`
- `wiki-technique-edge-cases`
- `wiki-technique-testing`