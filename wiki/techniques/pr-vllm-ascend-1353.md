---
id: technique-pr-vllm-ascend-1353
title: "PR Insight: vllm-project/vllm-ascend #1353"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - mla
  - multistream
  - performance
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/1353"
---

# PR Insight: vllm-project/vllm-ascend #1353

**Title:** [Perf] Improve MLA multistream performance

## Overview
This PR optimizes MLA (Multi-Head Latent Attention) multistream performance through improved scheduling and memory access patterns.

## Technical Significance
Enhances MLA throughput in multistream mode by optimizing attention computation and memory management. The improvements span MLA V1, DeepSeek V2 model integration, and utility functions, resulting in better utilization of Ascend's vector unit and unified buffer for concurrent request processing.

## Related
- `technique-mla`
- `technique-multistream`
- `kernel-attention`