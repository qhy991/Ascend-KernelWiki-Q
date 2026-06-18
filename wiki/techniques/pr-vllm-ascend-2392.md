---
id: technique-pr-vllm-ascend-2392
title: "PR Insight: vllm-project/vllm-ascend #2392"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - quantization
  - w4a8
  - deepseek
  - weight-format
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2392"
---

# PR Insight: vllm-project/vllm-ascend #2392

**Title:** [main][quantization] Adapt to the new format of ds w4a8 weight

## Overview
This PR adapts to a new DeepSeek w4a8 weight format that uses two int4 packs to save weights (reducing size) instead of the previous mindie-format that used int8 to represent int4. The new format also generates the required bias directly in the apply method via Modelslim. Changes are in `vllm_ascend/quantization/w4a8_dynamic.py` and related files.

## Technical Significance
This update enables more efficient memory usage by supporting the new packed w4a8 format, where two int4 values are packed into int8, reducing weight size and eliminating the need for extra conversion steps. The system maintains backward compatibility with the previous mindie format while supporting the new more efficient format.

## Related
- `technique-quantization-w4a8`, `technique-weight-packing`, `technique-modelslim-integration`, `technique-backward-compatibility`