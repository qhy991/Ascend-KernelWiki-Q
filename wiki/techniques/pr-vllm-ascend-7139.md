---
id: technique-pr-vllm-ascend-7139
title: "PR Insight: vllm-project/vllm-ascend #7139"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mtp
  - rotary-quant
  - glm5
  - quantization
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/7139"
---

# PR Insight: vllm-project/vllm-ascend #7139

**Title:** [MTP][Bugfix] Fix GLM5-W8A8 precision issues caused by rotary quant MTP weights

## Overview
Fixes precision issues in GLM5-W8A8 models with MTP when rotary quantization is enabled. The issue occurs when final hidden states pass to MTP and need an extra rotary operation. The fix adds proper handling for rotary quantized MTP weights.

## Technical Significance
Ensures correct acceptance rates for GLM5-W8A8 models with MTP by fixing rotary quantization handling. The fix aligns Ascend NPU acceptance rates with GPU performance, maintaining parity across platforms.

## Related
- `technique-mtp`, `technique-rotary-quant`, `technique-glm5`, `technique-quantization-w8a8`