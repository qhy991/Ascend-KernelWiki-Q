---
id: technique-pr-vllm-ascend-6705
title: "PR Insight: vllm-project/vllm-ascend #6705"
type: wiki-technique
architectures:
  - ascend310p
tags:
  - nz-format
  - weight-layout
  - quantization
  - 310p
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6705"
---

# PR Insight: vllm-project/vllm-ascend #6705

**Title:** [Feat.][310P]: weightNZ feature with quant or unquant.

## Overview
This PR adds NZ (N-dimensional Z-order) format support for linear layer weights on Ascend 310P, improving performance for both quantized and unquantized layers. It implements AscendUnquantizedLinearMethod310 for unquantized layers and updates w8a8_static quantization to directly transpose and apply NZ format casting.

## Technical Significance
Enables efficient weight storage and access patterns on 310P through NZ format, which improves memory bandwidth utilization and kernel performance. The implementation supports both quantized and unquantized workflows while maintaining consistency across different linear operation paths.

## Related
- `technique-nz-format`