---
id: technique-pr-vllm-ascend-5088
title: "PR Insight: vllm-project/vllm-ascend #5088"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - moe
  - cleanup
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5088"
---

# PR Insight: vllm-project/vllm-ascend #5088

**Title:** [1/N][Pangu][MoE] Remove PanguProMoEV1 related code

## Overview
This PR removes deprecated PanguProMoEV1 (Mixture of Experts V1) related code from vLLM-Ascend since this architecture is no longer supported. The cleanup includes removal from tests, token dispatcher, and MoE communication method implementations.

## Technical Significance
Removing unsupported MoE variants reduces code complexity and maintenance burden. This cleanup allows the codebase to focus on current and future MoE optimizations for Ascend NPUs, improving code clarity and reducing potential bugs from dead code paths.

## Related
- technique-moe
- technique-hccl-optimization