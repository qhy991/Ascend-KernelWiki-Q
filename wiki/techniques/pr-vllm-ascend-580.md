---
id: technique-pr-vllm-ascend-580
title: "PR Insight: vllm-project/vllm-ascend #580"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - quantization
  - w8a8
  - moe
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/580"
---

# PR Insight: vllm-project/vllm-ascend #580

**Title:** [quantization] Support w8a8 quantization

## Overview
This PR adds comprehensive W8A8 quantization support including static (W8A8) and dynamic (W8A8_DYNAMIC) for linear and MoE layers. Implementation includes VLLMAscendQuantizer, RMSNorm quantization patches, and new quantization method classes.

## Technical Significance
Production-ready W8A8 quantization on Ascend. The quantizer auto-detects quantized models via config fields and falls back to MindIE Turbo when available. Supports Qwen2.5 and DeepSeek models, verified through comprehensive testing.

## Related
- technique-quantization
- technique-w8a8
- technique-moe