---
id: technique-pr-vllm-ascend-8531
title: "PR Insight: vllm-project/vllm-ascend #8531"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - sampling
  - triton
  - bugfix
  - mask
  - draft-token-id
  - spec-decoding
  - memory-access
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/8531"
---

# PR Insight: vllm-project/vllm-ascend #8531

**Title:** [Bugfix][0.18.0] fix kernels in sample when mask is not static or draft_token_id is invalid

## Overview
This PR fixes Triton kernel issues in sampling operations. Two main problems are addressed: 1) expand_kernel, rejection_random_sample_kernel, and prepare_inputs_padded_kernel used 'tl.load(ptr + offsets -1, mask)' which caused issues when masks were not static and contiguous, fixed by using 'tl.load(ptr +tl.maximum(offsets - 1, 0), mask)' to prevent -1 reads. 2) sample_recovered_tokens_kernel and rejection_random_sample_kernel used draft_token_id as address offset, causing illegal memory access when draft_token_id was -1 in PD separation scenarios.

## Technical Significance
These fixes are critical for correct and stable sampling operations, especially in speculative decoding scenarios with PD separation. Illegal memory access can cause crashes, while incorrect mask handling can lead to wrong results. The PR demonstrates careful attention to memory access patterns and mask handling in Triton kernel implementations for sampling operations.

## Related
- `technique-sampling-optimization`
- `technique-triton-optimization`
- `technique-speculative-decoding`