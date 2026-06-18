---
id: technique-pr-vllm-ascend-4849
title: "PR Insight: vllm-project/vllm-ascend #4849"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - speculative-decoding
  - sampling
  - top-k-top-p
  - performance
  - rejection-sampler
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/4849"
---

# PR Insight: vllm-project/vllm-ascend #4849

**Title:** Fixed the performance degradation issue in post-processing in speculative decoding scenarios.

## Overview
This PR fixes performance degradation in speculative decoding when temperature > 0. The issue was that bonus_logits used a fused torch_npu.npu_top_k_top_p operator while target_logits in the rejection sampler used a less-optimized multi-operator implementation with expensive cumsum for top-p sampling. The fix applies the fused operator to target_logits sampling as well.

## Technical Significance
Reduces post-processing overhead in speculative decoding by using the optimized fused top_k_top_p operator for both bonus and target logits. This eliminates the expensive cumsum operation and improves overall speculative decoding throughput.

## Related
- `kernel-top-k-top-p`
- `kernel-rejection-sampler`
- `technique-speculative-decoding`
- `technique-sampling-optimization`