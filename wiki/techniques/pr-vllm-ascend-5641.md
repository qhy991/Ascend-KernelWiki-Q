---
id: technique-pr-vllm-ascend-5641
title: "PR Insight: vllm-project/vllm-ascend #5641"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mla
  - fia
  - context-parallel
  - attention
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5641"
---

# PR Insight: vllm-project/vllm-ascend #5641

**Title:** [Feat] Integrate FIA operator in mla_cp._forward_decode

## Overview
This PR replaces the `npu_multi_head_latent_attention` operator with the FIA (Flash Incremental Attention) operator in the MLA context parallel decode forward pass. The integration includes adjustments to mla_attn_dpc_pcp in acl_graph.py for proper graph compilation support.

## Technical Significance
Integrating FIA into MLA context parallel inference provides better performance optimization by leveraging Flash Incremental Attention's efficient memory access patterns. The replacement improves decode performance for long-context models using MLA while maintaining compatibility with context parallelism.

## Related
- `kernel-attention` (FIA attention kernels)
- `technique-mla` (Multi-Head Latent Attention)
- `technique-context-parallel` (Context parallelism)