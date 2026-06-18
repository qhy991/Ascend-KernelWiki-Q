---
id: technique-pr-vllm-ascend-3743
title: "PR Insight: vllm-project/vllm-ascend #3743"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mla
  - memory-leak
  - weak-references
  - decode-graph
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3743"
---

# PR Insight: vllm-project/vllm-ascend #3743

**Title:** [Fix] Prevent memory leak in MLA decode graph

## Overview
This PR fixes a memory leak in MLA (Multi-Head Latent Attention) decode graph parameters. The cache was holding strong references to tensors, preventing garbage collection and causing increased memory usage. The fix wraps cached tensors in weak references, allowing deallocation when no longer in use. Changes were made to `vllm_ascend/attention/attention_v1.py`, `vllm_ascend attention/mla_v1.py`, `vllm_ascend/compilation/acl_graph.py`, and `vllm_ascend/utils.py`.

## Technical Significance
Memory leaks in graph mode can cause OOM failures over time, especially in long-running inference services. Using weak references for cached parameters allows proper memory management while maintaining graph reuse benefits. This fix is critical for production stability of MLA-based models in graph execution mode.

## Related
- `technique-mla`
- `technique-memory-management`
- `technique-decode-graph`