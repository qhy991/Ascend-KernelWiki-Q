---
id: technique-pr-mindspeed-2160
title: "PR Insight: Ascend/MindSpeed #2160"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - pipeline-parallel
  - feature
  - training
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2160"
---

# PR Insight: Ascend/MindSpeed #2160

**Title:** feat: unaligned pipeline

## Overview
This PR adds unaligned pipeline support to MindSpeed. Unaligned pipeline enables pipeline parallel training with uneven tensor shapes across stages, improving flexibility for models with varying layer dimensions.

## Technical Significance
Unaligned pipeline is a critical feature for efficient pipeline parallel training on Ascend NPUs, particularly for models with varying hidden dimensions or layer architectures. The feature eliminates the need for padding or reshaping tensors to align pipeline stages, reducing memory overhead and improving compute efficiency. This optimization is particularly important for models with adaptive layer sizes, sparse architectures, or heterogeneous layer configurations. The implementation likely includes efficient HCCL communication for irregular tensor shapes.

## Related
- `technique-pipeline-scheduling`
- `technique-hccl-optimization`