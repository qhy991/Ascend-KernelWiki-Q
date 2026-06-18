---
id: technique-pr-vllm-ascend-5394
title: "PR Insight: vllm-project/vllm-ascend #5394"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - lora
  - custom-operators
  - rank-scaling
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5394"
---

# PR Insight: vllm-project/vllm-ascend #5394

**Title:** [BufFix]Fix the error when using Ascend custom operators with rank=128

## Overview
This PR fixes an error where custom Ascend operators `sgmv_expand` and `sgmv_shrink` fail when rank >= 128. The operators were only designed for rank values of 8, 16, 32, and 64, causing out-of-range errors for higher rank values.

## Technical Significance
LoRA (Low-Rank Adaptation) with high rank values requires proper operator support. This fix ensures LoRA works correctly with rank=128 and higher by falling back to alternative implementations when custom operators are not available.

## Related
- technique-lora
- technique-custom-operators
- technique-rank-scaling