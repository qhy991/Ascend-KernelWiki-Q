---
id: technique-pr-mindspeed-2213
title: "PR Insight: Ascend/MindSpeed #2213"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - memory
  - optimizer
  - refactor
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2213"
---

# PR Insight: Ascend/MindSpeed #2213

**Title:** refactor reuse_params and smart_swap

## Overview
This PR refactors parameter reuse and smart swap features in MindSpeed. These features optimize memory usage by reusing parameter buffers and intelligently swapping tensors between unified buffer and global memory during training.

## Technical Significance
Parameter reuse and smart swap are critical memory optimization techniques for training large models on Ascend NPUs with limited unified buffer capacity. The refactoring improves the implementation of these features, enabling more efficient memory management and reducing memory fragmentation. Smart swapping reduces memory pressure by offloading infrequently accessed tensors to global memory while keeping hot tensors in unified buffer for fast access. This optimization enables training of larger models and larger batch sizes on Ascend hardware.

## Related
- `technique-nz-tiling`
- `technique-data-reuse`