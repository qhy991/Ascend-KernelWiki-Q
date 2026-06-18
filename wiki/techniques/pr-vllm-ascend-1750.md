---
id: technique-pr-vllm-ascend-1750
title: "PR Insight: vllm-project/vllm-ascend #1750"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mla
  - multistream
  - prefetch
  - performance
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/1750"
---

# PR Insight: vllm-project/vllm-ascend #1750

**Title:** [0.9.1][Perf] Port MLA multistream optimazition and prefetch to v0.9.1

## Overview
This PR ports MLA (Multi-Head Latent Attention) multistream optimization and prefetch features from main branch to v0.9.1-dev. The changes affect `vllm_ascend/attention/mla_v1.py`, `vllm_ascend/models/deepseek_v2.py`, and `vllm_ascend/utils.py`.

## Technical Significance
Performance optimization for DeepSeek models with MLA attention. Multistream execution and data prefetching hide memory latency and improve utilization of the Ascend compute units during attention computation, particularly beneficial for large-batch inference scenarios.

## Related
- `kernel-mla-ascendc`
- `technique-multistream`
- `technique-prefetch`
- `technique-attention-optimization`