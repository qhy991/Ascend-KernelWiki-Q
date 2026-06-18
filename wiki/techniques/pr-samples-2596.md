---
id: technique-pr-samples-2596
title: "PR Insight: Ascend/samples #2596"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - ascendc
  - flash-attention
  - samples
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2596"
---

# PR Insight: Ascend/samples #2596

**Title:** commit FlashAttentionScore

## Overview
This PR adds FlashAttentionScore samples to the repository. FlashAttention is an optimized attention mechanism that reduces memory usage and improves performance by being IO-aware.

## Technical Significance
FlashAttention is critical for efficient transformer inference and training. Samples provide reference implementations for this complex algorithm, which involves sophisticated tiling and data reuse strategies.

## Related
- `kernel-flash-attention`, `technique-double-buffering`, `technique-data-reuse`