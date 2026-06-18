---
id: technique-pr-vllm-ascend-1749
title: "PR Insight: vllm-project/vllm-ascend #1749"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - quantization
  - mindie-turbo
  - refactoring
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/1749"
---

# PR Insight: vllm-project/vllm-ascend #1749

**Title:** [0.9.1]disable quantization in mindie_turbo

## Overview
This PR removes quantization functionality from mindie_turbo mode because the vLLM-Ascend interface has evolved rapidly, making the original quantization function no longer necessary. The change affects `vllm_ascend/quantization/quantizer.py`.

## Technical Significance
Code cleanup and interface evolution. The removal reflects the shifting architecture where quantization is handled differently in newer interfaces, reducing complexity and maintenance burden for obsolete code paths.

## Related
- `technique-quantization`