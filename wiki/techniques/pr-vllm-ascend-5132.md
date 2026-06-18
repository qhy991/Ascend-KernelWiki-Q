---
id: technique-pr-vllm-ascend-5132
title: "PR Insight: vllm-project/vllm-ascend #5132"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - recompute
  - mm
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5132"
---

# PR Insight: vllm-project/vllm-ascend #5132

**Title:** [bugfix][mm] change get_num_encoder_tokens to get_num_encoder_embeds in recompute_schedule.py

## Overview
This PR adapts vLLM-Ascend to upstream vLLM changes by renaming `get_num_encoder_tokens()` to `get_num_encoder_embeds()` in the recompute scheduler. This function tracks encoder embedding counts for multi-modal models during activation recomputation.

## Technical Significance
Keeping the recompute scheduler synchronized with upstream vLLM API changes ensures proper handling of encoder-decoder models with activation checkpointing on Ascend NPUs. This fix maintains compatibility with multi-modal workloads that require encoder token counting.

## Related
- technique-recomputation
- technique-activation-checkpointing