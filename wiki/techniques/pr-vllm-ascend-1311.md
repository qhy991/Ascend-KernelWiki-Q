---
id: technique-pr-vllm-ascend-1311
title: "PR Insight: vllm-project/vllm-ascend #1311"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - mla
  - deepseek
  - memory
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/1311"
---

# PR Insight: vllm-project/vllm-ascend #1311

**Title:** [0.9.1][Bugfix] fix oom issue in mla and enable mla_pa for deepseek mla decode

## Overview
This PR fixes OOM issues in Multi-Head Latent Attention (MLA) and enables paged attention (mla_pa) for DeepSeek MLA decode, improving memory efficiency and correctness.

## Technical Significance
Resolves memory allocation bugs in MLA that caused out-of-memory errors during inference. The fix enables paged attention for MLA decode phase in DeepSeek models, allowing better memory utilization for long sequences. This is critical for production deployments running DeepSeek V2 models on resource-constrained Ascend NPUs.

## Related
- `kernel-attention`
- `technique-mla`
- `kernel-deepseek`