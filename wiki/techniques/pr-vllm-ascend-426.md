---
id: technique-pr-vllm-ascend-426
title: "PR Insight: vllm-project/vllm-ascend #426"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - aclgraph
  - npugraph
  - compile
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/426"
---

# PR Insight: vllm-project/vllm-ascend #426

**Title:** support aclgraph

## Overview
This PR adds support for Ascend's ACL Graph (NPUGraph) feature in the v1 engine. Implementation includes registering unified_ascend_attention_with_output for graph splitting, NPUGraph kernel launch acceleration, and comprehensive testing. Users can disable via enforce_eager=True.

## Technical Significance
Graph capture reduces kernel launch overhead by capturing and reusing computation graphs. This is a major performance optimization on Ascend, similar to CUDA graphs. The PR enables graph mode by default for compatible torch_npu and CANN versions.

## Related
- technique-aclgraph
- technique-npugraph