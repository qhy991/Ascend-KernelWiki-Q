---
id: technique-pr-vllm-ascend-6081
title: "PR Insight: vllm-project/vllm-ascend #6081"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - eagle
  - moe
  - w8a8
  - feature
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6081"
---

# PR Insight: vllm-project/vllm-ascend #6081

**Title:** [Feature][Cherry Pick]Enable DispatchGmmCombineDecode when eagle is moe with w8a8, or not moe

## Overview
This PR enables the DispatchGmmCombineDecode operator for EAGLE speculative decoding with MoE W8A8 models or non-MoE models. It extends the operator's applicability beyond its original use cases.

## Technical Significance
DispatchGmmCombineDecode provides optimized MoE dispatch and combination. Enabling it for EAGLE with MoE W8A8 models and non-MoE scenarios expands its utility, improving performance for these configurations. The PR removes previous limitations, allowing the operator to be used more broadly across different model types and quantization schemes when paired with EAGLE speculative decoding.

## Related
- `technique-eagle`, `technique-moe`, `technique-w8a8`, `technique-dispatch-gmm`