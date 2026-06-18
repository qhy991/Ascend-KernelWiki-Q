---
id: technique-pr-modellink-2320
title: "PR Insight: Ascend/ModelLink #2320"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - weight-conversion
  - tp2d
  - memory-optimization
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2320"
---

# PR Insight: Ascend/ModelLink #2320

**Title:** 按需加载&转换模型参数基本版本+TP2D模型参数转换

## Overview
This PR implements on-demand model parameter loading and conversion, plus TP2D (2D Tensor Parallelism) weight conversion. The feature enables efficient parameter management for large models with optional loading of only required components.

## Technical Significance
On-demand loading reduces memory footprint by loading only the parameters needed for current training or inference phases. Combined with TP2D weight conversion, this enables training very large models on memory-constrained Ascend systems. TP2D conversion properly reshapes weights for 2D tensor parallelism distribution, ensuring correct computation across row and column parallel dimensions. This is critical for scaling models beyond single-device memory limits.

## Related
- `technique-tensor-parallelism`
- `technique-2d-tp`
- `technique-weight-conversion`
- `technique-memory-optimization`