---
id: technique-pr-vllm-ascend-6835
title: "PR Insight: vllm-project/vllm-ascend #6835"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mtp
  - spec-decode
  - prefill
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6835"
---

# PR Insight: vllm-project/vllm-ascend #6835

**Title:** [BugFix][MTP] Fix prefill misclassified as decode when prompt tokens == num_spec_tokens + 1

## Overview
Fixes a critical accuracy bug in Multi-Token Prediction (MTP) speculative decoding where prefill requests with `prompt_tokens == num_spec_tokens + 1` were incorrectly classified as decode requests. The original uniform_decode condition only checked `max_num_scheduled_tokens == uniform_decode_query_len` and `num_tokens == max_num_scheduled_tokens * num_reqs`, which was insufficient for specific prompt lengths.

## Technical Significance
Corrects MTP execution logic by improving request classification conditions, ensuring accurate distinction between prefill and decode phases. This fix is essential for maintaining correctness in speculative decoding workflows on Ascend hardware.

## Related
- `technique-spec-decode`, `technique-mtp`, `technique-prefill-decode-scheduling`