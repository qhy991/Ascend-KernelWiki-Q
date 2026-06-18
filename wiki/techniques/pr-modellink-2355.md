---
id: technique-pr-modellink-2355
title: "PR Insight: Ascend/ModelLink #2355"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - recompute
  - normalization
  - memory-optimization
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2355"
---

# PR Insight: Ascend/ModelLink #2355

**Title:** feat:支持recompute norm特性

## Overview
This PR adds support for recomputing normalization layers during training backward pass. Instead of storing intermediate layer normalization outputs for gradient computation, they are recomputed on-the-fly during backpropagation.

## Technical Significance
Activation recomputation (also known as gradient checkpointing) is a critical memory optimization technique for training large language models on limited NPU memory. By recomputeing normalization layers (LayerNorm/RMSNorm) instead of storing their outputs, this feature trades additional compute for reduced memory footprint. This enables training of larger models or larger batch sizes on Ascend hardware, particularly beneficial for DeepSeekV3 and Qwen models with deep transformer stacks.

## Related
- `technique-gradient-checkpointing`
- `technique-memory-optimization`
- `technique-double-buffering`