---
id: technique-pr-vllm-ascend-3171
title: "PR Insight: vllm-project/vllm-ascend #3171"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - aclgraph
  - bge-m3
  - embedding
  - model-support
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3171"
---

# PR Insight: vllm-project/vllm-ascend #3171

**Title:** [Feat] Supports Aclgraph for bge-m3

## Overview
This PR adds ACL graph support for BGE-M3 embedding models. The optimization enables graph-based execution for embedding operations, improving performance for large-scale embedding inference workloads.

## Technical Significance
BGE-M3 is a popular embedding model used for semantic search and retrieval. ACL graph support reduces Python overhead and improves performance for embedding computations, which is critical for production embedding services that handle high query volumes.

## Related
- `technique-aclgraph`, `kernel-bge-m3-ascendc`, `kernel-embedding-ascendc`