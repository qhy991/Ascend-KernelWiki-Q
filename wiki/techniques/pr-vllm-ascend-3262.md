---
id: technique-pr-vllm-ascend-3262
title: "PR Insight: vllm-project/vllm-ascend #3262"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - hccl-optimization
  - kv-cache
  - vllm
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3262"
---

# PR Insight: vllm-project/vllm-ascend #3262

**Title:** [bugfix] Fix bugs in _dumm_run and re-initialize kv-cache.

## Overview
Currently we run an extra profile_run with `num_tokens == self.mc2_tokens_capacity`. However, when setting `max_num_batched_tokens < self.mc2_tokens_capacity`, this will trigger an assertion error that requires num_tokens in `_dummy_run` to be smaller than `max_num_batched_tokens`. This PR skips this extra `profile_run` if `self.max_num_tokens <= self.mc2_tokens_capacity` so as to avoid this bug.

## Technical Significance
Fixes bugs in dummy run operations and KV cache re-initialization to prevent runtime errors during model inference.

## Related
- `technique-kv-cache-paging`
