---
id: technique-pr-vllm-ascend-7628
title: "PR Insight: vllm-project/vllm-ascend #7628"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - deepseek-v3.2
  - c8-quantization
  - quantization-layer-reversion
  - precision
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/7628"
---

# PR Insight: vllm-project/vllm-ascend #7628

**Title:** [Bugfix]Fix deepseek 3.2 C8 precision by revert quantization layers

## Overview
This PR fixes DeepSeek V3.2 C8 precision by reverting quantization layers from INT8 back to FLOAT. The reversion addresses accuracy issues that occurred when certain layers were quantized, indicating that these layers require full precision for correct computation.

## Technical Significance
This fix matters for DeepSeek V3.2 C8 quantization accuracy. While C8 quantization reduces memory usage, some layers are sensitive to quantization errors. By selectively reverting these layers to FLOAT precision, it maintains accuracy while still benefiting from memory reduction in other layers. This demonstrates the importance of layer-wise quantization sensitivity analysis.

## Related
- technique-quantization
- technique-c8-quantization