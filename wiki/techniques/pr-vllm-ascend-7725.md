---
id: technique-pr-vllm-ascend-7725
title: "PR Insight: vllm-project/vllm-ascend #7725"
type: wiki-technique
architectures:
  - ascend310p
tags:
  - w8a8
  - quantization
  - dynamic-linear
  - modelslim
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/7725"
---

# PR Insight: vllm-project/vllm-ascend #7725

**Title:** [Feature][310P]: 310P support W8A8 dynamic linear method

## Overview
This PR adds W8A8 dynamic linear quantization method support for Ascend 310P. It implements dynamic weight-8-bit activation-8-bit quantization using ModelSlim configuration for efficient inference.

## Technical Significance
Enables memory-efficient inference on Ascend 310P using W8A8 dynamic quantization, reducing memory footprint while maintaining model accuracy through dynamic quantization of linear layers.

## Related
- `technique-quantization`, `pattern-w8a8-quantization`, `technique-dynamic-quantization`, `kernel-quantized-linear`