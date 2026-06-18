---
id: technique-pr-vllm-ascend-5391
title: "PR Insight: vllm-project/vllm-ascend #5391"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - mamba
  - causal-conv1d
  - revert
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5391"
---

# PR Insight: vllm-project/vllm-ascend #5391

**Title:** rollback causal_conv1d_fn to torch ops & update qwen3Next doc

## Overview
This PR rolls back the `causal_conv1d_fn` operations from Triton to PyTorch implementations to fix hanging issues, and updates the Qwen3-Next documentation accordingly.

## Technical Significance
Hanging issues in causal_conv1d can cause inference deadlocks. Rolling back to PyTorch operations ensures stability while allowing time to debug and fix the Triton implementation. The documentation update keeps users informed about the current implementation status.

## Related
- technique-mamba
- technique-causal-conv1d
- technique-stability