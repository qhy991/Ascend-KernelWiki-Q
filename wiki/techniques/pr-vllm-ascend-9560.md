---
id: technique-pr-vllm-ascend-9560
title: "PR Insight: vllm-project/vllm-ascend #9560"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - glm4.7-flash
  - mla
  - attention
  - context-parallel
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/9560"
---

# PR Insight: vllm-project/vllm-ascend #9560

**Title:** [Feature][Attention] Support Model GLM4.7-Flash

## Overview
This PR adds support for the GLM4.7-Flash model by implementing MLA (Multi-head Latent Attention) with context parallelism. The implementation includes MLA v1 attention code, context parallel precision tests, and general MLA tests.

## Technical Significance
GLM4.7-Flash is a state-of-the-art model that requires efficient attention implementation. MLA with context parallelism provides both memory efficiency and scalability, enabling efficient deployment of GLM4.7-Flash on distributed Ascend clusters.

## Related
- `kernel-attention`
- `kernel-mla`
- `technique-hccl-optimization`