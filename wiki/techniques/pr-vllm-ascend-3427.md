---
id: technique-pr-vllm-ascend-3427
title: "PR Insight: vllm-project/vllm-ascend #3427"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - quantization
  - hccl-optimization
  - vllm
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3427"
---

# PR Insight: vllm-project/vllm-ascend #3427

**Title:** [Feature] Add W4A4 Flat Quantization support

## Overview
This PR [feature] add w4a4 flat quantization support. It modifies core implementation files including vllm_ascend/quantization/utils.py, vllm_ascend/quantization/w4a4_flatquant_dynamic.py.

## Technical Significance
Adds W4A4 Flat Quantization support for extreme model compression with minimal accuracy loss on Ascend devices.

## Related
- `technique-quantization`
