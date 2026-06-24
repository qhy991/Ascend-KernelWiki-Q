---
id: technique-spec-decode-mtp-buffers
title: "Isolating Attention Metadata Buffers for MTP Speculative Decoding"
type: wiki-technique
confidence: verified
architectures:
  - ascend910b
kernel_types:
  - attention
tags:
  - speculative-decoding
  - mtp
  - sfa
  - dsa-cp
sources:
  - pr-vllm-ascend-10825
---

# Isolating Attention Metadata Buffers for MTP Speculative Decoding

## Overview
In Multi-Token Prediction (MTP) speculative decoding, the model rapidly generates multiple draft tokens in a single forward pass. This creates extreme pressure on the attention-metadata builder, especially for complex sparse formats like DeepSeek's Sparse Flash Attention (SFA).

## The Issue
If the metadata builder recycles a single memory buffer for `actual_seq_lengths_query` across all draft steps, steps will overwrite each other. When `num_speculative_tokens > 1`, the indexer only sees the metadata of the final draft token, plummeting the acceptance rate.

## The Optimization
The builder must be split into a non-draft path (`build`) and a draft path (`build_for_drafting(draft_step)`). The draft path allocates one tensor *per step* (sized `max_num_reqs * (num_speculative_tokens + 1) + 1`), guaranteeing absolute metadata isolation. Furthermore, rotary embedding (RoPE) caches must be bypassed (`use_cache=False`) during drafting to enforce step-specific recomputation.
