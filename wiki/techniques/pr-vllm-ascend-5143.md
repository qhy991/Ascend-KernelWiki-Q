---
id: technique-pr-vllm-ascend-5143
title: "PR Insight: vllm-project/vllm-ascend #5143"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - quantization
  - w4a4
  - laos
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5143"
---

# PR Insight: vllm-project/vllm-ascend #5143

**Title:** [Feature] Add support of new W4A4_LAOS_DYNAMIC quantization method

## Overview
This PR introduces W4A4_LAOS_DYNAMIC quantization support, a new 4-bit weight and 4-bit activation quantization method using the LAOS (Learned Asymmetric Output Scaling) dynamic quantization approach for better model compression and inference efficiency on Ascend devices.

## Technical Significance
W4A4_LAOS_DYNAMIC provides extreme model compression with minimal quality degradation, enabling larger models to run in limited memory on Ascend NPUs. The dynamic LAOS scaling adapts to activation statistics at runtime, maintaining accuracy while reducing memory bandwidth and improving throughput.

## Related
- technique-quantization
- technique-accuracy-validation