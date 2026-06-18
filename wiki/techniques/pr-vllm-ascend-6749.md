---
id: technique-pr-vllm-ascend-6749
title: "PR Insight: vllm-project/vllm-ascend #6749"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - fusion
  - split-qkv-rmsnorm-rope
  - rope
  - guard-rails
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6749"
---

# PR Insight: vllm-project/vllm-ascend #6749

**Title:** [v0.13.0][Fusion]add checks to skip fusion where split_rmsnorm_rope is not supported

## Overview
This PR adds guard checks to restrict split_qkv_rmsnorm_rope fusion to only cases where head_size == 128 && rotary_dim == head_size. This prevents incorrect fusion applications after PR #6602 unified rope implementations.

## Technical Significance
Prevents operator fusion errors by ensuring split_qkv_rmsnorm_rope is only applied to supported configurations. The guard checks maintain correctness while allowing future generalization of the fusion operation.

## Related
- `technique-operator-fusion`