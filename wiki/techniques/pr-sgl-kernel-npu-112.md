---
id: technique-pr-sgl-kernel-npu-112
title: "PR Insight: sgl-project/sgl-kernel-npu #112"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - quantization
  - moe
  - int8
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/112"
---

# PR Insight: sgl-project/sgl-kernel-npu #112

**Title:** feat:add env var to switch quant

## Overview
This PR adds an environment variable `DEEP_NORMAL_MODE_USE_INT8_QUANT` to control whether normal mode uses BF16 or INT8 quantization. The default remains BF16, with INT8 enabled via the environment variable.

## Technical Significance
Environment-based quantization switching enables runtime flexibility for performance tuning and A/B testing without code changes. This allows operators to dynamically trade off between accuracy (BF16) and throughput/memory (INT8) based on deployment requirements.

## Related
- `technique-quantization`, `technique-moe`