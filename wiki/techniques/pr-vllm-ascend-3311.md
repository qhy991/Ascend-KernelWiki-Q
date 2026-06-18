---
id: technique-pr-vllm-ascend-3311
title: "PR Insight: vllm-project/vllm-ascend #3311"
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
  - "https://github.com/vllm-project/vllm-ascend/pull/3311"
---

# PR Insight: vllm-project/vllm-ascend #3311

**Title:** [Feat][quantization] Support new version w4a8 dynamic quantization for Linear layers

## Overview
The existing implementation for the w4a8-dynamic linear method only supports the old quantization format from msmodelslim. When attempting to load models quantized with the new version, vLLM encounters errors due to mismatched tensor shapes and unprocessed quantization parameters.

## Technical Significance
Supports new version W4A8 dynamic quantization format for Linear layers, enabling compatibility with models quantized using updated msmodelslim format.

## Related
- `technique-quantization`
