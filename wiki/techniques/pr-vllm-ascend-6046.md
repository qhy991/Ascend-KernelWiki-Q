---
id: technique-pr-vllm-ascend-6046
title: "PR Insight: vllm-project/vllm-ascend #6046"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - context-parallel
  - mla
  - fia
  - feature
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6046"
---

# PR Insight: vllm-project/vllm-ascend #6046

**Title:** [0.13.0][Feat] Integrate FIA operator in mla_cp._forward_decode

## Overview
This PR integrates the FIA (Fused In-place Attention) operator in mla_cp._forward_decode for the v0.13.0 release branch. It replaces the npu_multi_head_latent_attention with the FIA operator and adjusts mla_attn_dpc_pcp in acl_graph.py.

## Technical Significance
FIA provides optimized in-place attention computation, reducing memory usage and improving performance. Integrating FIA into the MLA context parallel path enables better performance for DeepSeek models with MLA attention. The PR updates the CP attention implementation to use FIA instead of the older npu_multi_head_latent_attention operator, aligning with Ascend's latest optimization capabilities.

## Related
- `technique-mla`, `technique-fia`, `technique-context-parallel`, `technique-deepseek`