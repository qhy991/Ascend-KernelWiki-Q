---
id: technique-pr-vllm-ascend-8787
title: "PR Insight: vllm-project/vllm-ascend #8787"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - attention
  - mla
  - pcp
  - prefill
  - optimization
  - context-parallel
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/8787"
---

# PR Insight: vllm-project/vllm-ascend #8787

**Title:** [Performance][MLA][PCP] Optimize MLA PCP prefill attention

## Overview
This PR optimizes MLA (Multi-head Latent Attention) PCP (Prefill Cache Picking) prefill path through several improvements: (1) avoids projecting unnecessary tail KV tokens using `kv_tail_proj_idx` metadata, (2) refactors PCP head/tail attention paths to use a shared `_attention_with_optional_kv_select` helper, (3) uses packed attention path with `sparse_mode=3` and `actual_seq_lengths_kv` to reduce redundant attention calls. Testing on A2 with 8192-token input and TP8+PCP2 shows TTFT improvement from 620ms to 580ms.

## Technical Significance
MLA compresses KV cache representations to reduce memory bandwidth and improve performance. The PCP optimization eliminates redundant computation by only projecting KV tokens visible to the tail attention path, avoiding wasted computation on tokens that won't be accessed. The shared helper function and packed attention approach reduces code duplication and operator launch overhead. These optimizations are particularly impactful for long-context inference where prefill dominates runtime.

## Related
- `kernel-attention-ascendc`
- `technique-cube-vector-overlap`
- `technique-kv-cache-paging`
- `technique-data-reuse`