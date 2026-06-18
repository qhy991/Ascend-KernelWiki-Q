---
id: technique-pr-vllm-ascend-429
title: "PR Insight: vllm-project/vllm-ascend #429"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - deepseek
  - mtp
  - graph-mode
  - mla
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/429"
---

# PR Insight: vllm-project/vllm-ascend #429

**Title:** port deepseekv2 and mtp to main branch

## Overview
This PR ports DeepSeek v2 and MTP (Multi-Token Prediction) features from v0.7.3 to the main branch, including graph mode support. The implementation spans attention, MLA, MoE, rotary embedding, and distributed components, with major additions including mla_v1.py (561 lines).

## Technical Significance
Major feature merge bringing DeepSeek optimizations to the main codebase. Includes MTP speculative decoding, MLA attention, graph mode execution, and distributed training support. The PR unifies v0.7.3 improvements into the main development branch.

## Related
- technique-deepseek
- technique-mtp
- technique-mla
- technique-aclgraph