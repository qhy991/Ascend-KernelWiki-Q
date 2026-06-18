---
id: technique-pr-vllm-ascend-4765
title: "PR Insight: vllm-project/vllm-ascend #4765"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - attention
  - pa
  - fia
  - performance
  - batch-size
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/4765"
---

# PR Insight: vllm-project/vllm-ascend #4765

**Title:** [Attention] Temporarily add back pa for small batch sizes.

## Overview
This PR temporarily re-enables PA (prefill-attention) in scenarios with small batch sizes due to performance considerations. The change is intended to be temporary, with plans to remove PA once FIA (FlashInference-Attention) performs better than PA in all scenarios.

## Technical Significance
Address performance regression in small-batch scenarios by reverting to PA attention implementation. This highlights that FIA, while optimized for large batches, may not yet match PA's efficiency for smaller batch sizes on Ascend hardware.

## Related
- `kernel-attention-pa`
- `kernel-attention-fia`
- `technique-attention-optimization`
- `kernel-attention`