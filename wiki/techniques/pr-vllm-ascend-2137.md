---
id: technique-pr-vllm-ascend-2137
title: "PR Insight: vllm-project/vllm-ascend #2137"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mtp
  - sampling
  - greedy
  - optimization
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2137"
---

# PR Insight: vllm-project/vllm-ascend #2137

**Title:** [Perf][MTP] Optimize reject sampler in greedy situation.

## Overview
This PR optimizes the rejection sampler for MTP (speculative decoding) in greedy sampling scenarios, porting optimizations from PR #2002 to main branch. Changes include improvements to `vllm_ascend/sample/rejection_sampler.py` and updates to tests in `tests/ut/sample/test_rejection_sampler.py` and `tests/e2e/singlecard/sample/test_rejection_sampler.py`.

## Technical Significance
The optimization improves performance of MTP's rejection sampling algorithm during greedy sampling, which is a common inference pattern. By streamlining the rejection logic and reducing unnecessary computations, this optimization accelerates speculative decoding verification without changing the acceptance/rejection correctness properties. This is particularly important for MTP's multi-token prediction performance.

## Related
- `technique-speculative-decoding`, `technique-rejection-sampling`, `technique-sampling-optimization`