---
id: technique-pr-vllm-ascend-5130
title: "PR Insight: vllm-project/vllm-ascend #5130"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - pangu
  - moe
  - cleanup
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5130"
---

# PR Insight: vllm-project/vllm-ascend #5130

**Title:** [2/N][Pangu][MoE] Remove Pangu Related Code

## Overview
This PR continues the cleanup of deprecated Pangu model support by removing Pangu-related code from documentation, tests, attention implementations, platform configurations, and quantization utilities across the vLLM-Ascend codebase.

## Technical Significance
Removing unsupported Pangu model code reduces maintenance burden and eliminates potential bugs from dead code paths. This cleanup allows the codebase to focus on current and future optimizations for Ascend NPUs, improving code clarity and reducing technical debt.

## Related
- technique-moe
- technique-attention