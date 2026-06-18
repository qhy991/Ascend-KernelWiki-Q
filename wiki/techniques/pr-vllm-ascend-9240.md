---
id: technique-pr-vllm-ascend-9240
title: "PR Insight: vllm-project/vllm-ascend #9240"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - cudagraph
  - encoder-decoder
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/9240"
---

# PR Insight: vllm-project/vllm-ascend #9240

**Title:** [BugFix] Update cudagraph mode handling for encoder-decoder models

## Overview
This PR updates the cudagraph mode handling logic in the platform layer to properly support encoder-decoder model architectures. The change ensures that cudagraph optimization is correctly applied when working with models that have separate encoder and decoder components.

## Technical Significance
Cudagraph mode is a performance optimization that captures CUDA graphs to reduce kernel launch overhead. Proper handling for encoder-decoder models ensures this optimization can be safely applied to complex model architectures, improving inference performance while maintaining correctness.

## Related
- `technique-pipeline-scheduling`