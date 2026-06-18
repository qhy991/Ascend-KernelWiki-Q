---
id: technique-pr-vllm-ascend-8718
title: "PR Insight: vllm-project/vllm-ascend #8718"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - mtp
  - speculative-decoding
  - lmhead
  - tensor-parallel
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/8718"
---

# PR Insight: vllm-project/vllm-ascend #8718

**Title:** [BugFix] MTP recurrent batch size after lmhead TP logits truncation

## Overview
This PR fixes a tensor size mismatch error in MTP (Multi-Token Prediction) when used with lmhead_tensor_parallel_size. The bug occurs because the recurrent draft loop uses a batch_size that reflects padded drafter batch size, but after lmhead TP logits computation and truncation, draft_token_ids only contains the real valid sample count. The mismatch causes a RuntimeError when trying to assign a smaller tensor into a larger slice.

## Technical Significance
This fix is critical for correct MTP operation with tensor parallelism in the language model head. The semantic mismatch between padded graph batch size and effective recurrent batch size can cause runtime crashes in production. The fix ensures that the batch_size used in the recurrent draft loop matches the actual tensor dimensions after TP logits truncation, maintaining correctness of speculative decoding workflows.

## Related
- `pattern-specdecode`
- `technique-hccl-optimization`
- `hw-cube-unit`