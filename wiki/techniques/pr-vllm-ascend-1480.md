---
id: technique-pr-vllm-ascend-1480
title: "PR Insight: vllm-project/vllm-ascend #1480"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - quantization
  - w4a8
  - graph-mode
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/1480"
---

# PR Insight: vllm-project/vllm-ascend #1480

**Title:** [0.9.1]Refactoring w4a8 and w8a8 and supporting w4a8 graph mode

## Overview
This PR refactors W4A8 and W8A8 quantization implementations and adds W4A8 graph mode support for TorchAir optimization.

## Technical Significance
Improves code maintainability by consolidating quantization logic and enables graph-mode acceleration for W4A8 quantization. The refactoring allows TorchAir to optimize W4A8 operations through graph compilation, improving inference throughput for quantized models.

## Related
- `technique-w4a8-quantization`
- `technique-w8a8-quantization`
- `technique-torchair`