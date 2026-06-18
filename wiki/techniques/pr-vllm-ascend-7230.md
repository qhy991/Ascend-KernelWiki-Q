---
id: technique-pr-vllm-ascend-7230
title: "PR Insight: vllm-project/vllm-ascend #7230"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - speculative-decoding
  - draft-model
  - eagle
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/7230"
---

# PR Insight: vllm-project/vllm-ascend #7230

**Title:** [SpecDecode] Fix Draft model proposer

## Overview
This PR fixes the Unified draft parallel feature in speculative decoding by: removing incorrect assertions on layer number, getting block size through draft_attn_groups instead of attn_metadata_builder after 0.17.0, and ensuring attn_update_stack_num_spec_norm is not done when unified draft parallel is enabled.

## Technical Significance
This bugfix matters for Ascend speculative decoding correctness with Eagle and similar draft models. The issues would cause incorrect metadata handling when target models have multiple attention layers. The fixes ensure proper block size retrieval and prevent normalization operations that should be skipped in unified draft parallel mode, maintaining correctness across the target/draft model interface.

## Related
- technique-speculative-decoding