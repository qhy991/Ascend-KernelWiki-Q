---
id: technique-pr-vllm-ascend-740
title: "PR Insight: vllm-project/vllm-ascend #740"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - llama4
  - mllama4
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/740"
---

# PR Insight: vllm-project/vllm-ascend #740

**Title:** [Attention][Kernel]moe support for llama4 and mllama4

## Overview
This PR adds MoE support for Llama-4 and MLLaMA-4 models on Ascend. Changes include fused_moe and common_fused_moe optimizations, plus attention backend updates.

## Technical Significance
Llama-4 and MLLaMA-4 are Meta's latest models, incorporating MoE for efficiency. This PR brings Ascend support to these state-of-the-art models, enabling deployment of Meta's newest architectures.

## Related
- kernel-moe
- technique-llama4