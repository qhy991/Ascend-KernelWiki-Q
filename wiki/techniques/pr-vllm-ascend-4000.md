---
id: technique-pr-vllm-ascend-4000
title: "PR Insight: vllm-project/vllm-ascend #4000"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mla
  - attention
  - pcp
  - dcp
  - vllm
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/4000"
---

# PR Insight: vllm-project/vllm-ascend #4000

**Title:** [Feat] update op for mla

## Overview
This PR updates the MLA (Multi-Head Latent Attention) v1 module to use `torch_npu.npu_attention_update` operator when both PCP (Prefill Context Parallel) and DCP (Decode Context Parallel) are enabled. The changes modify the attention update logic to use the Ascend-specific operator for better performance in context parallel scenarios.

## Technical Significance
The `npu_attention_update` operator is optimized for Ascend hardware and provides better performance when context parallelism is enabled. Using this operator for MLA when PCP and DCP are both active leverages hardware-specific optimizations for attention parameter updates, improving throughput in distributed inference scenarios with context parallelism.

## Related
- `technique-attention`, `technique-mla`, `technique-context-parallel`, `technique-operator-optimization`