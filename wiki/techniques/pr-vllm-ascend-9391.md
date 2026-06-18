---
id: technique-pr-vllm-ascend-9391
title: "PR Insight: vllm-project/vllm-ascend #9391"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - ascend950
  - mxfp4
  - flatquant
  - row-parallelism
  - quantization
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/9391"
---

# PR Insight: vllm-project/vllm-ascend #9391

**Title:** [Ascend950] [Feature] Enable MXFP4 flatquant and support for row parallelism

## Overview
This PR enables MXFP4 flatquantization and adds support for row parallelism on Ascend 950. The implementation updates multiple quantization methods including W4A4, W8A8, and base methods, along with device compatibility layers and method adapters.

## Technical Significance
MXFP4 flatquant provides ultra-low precision quantization with flattened weight layouts, maximizing memory efficiency. Row parallelism support enables distributed model parallelism, allowing larger models to be served across multiple devices. Together, these features significantly expand the scalability of quantized model serving.

## Related
- `technique-quantization`
- `technique-hccl-optimization`