---
id: technique-pr-vllm-ascend-2183
title: "PR Insight: vllm-project/vllm-ascend #2183"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - qwen3-moe
  - aclgraph
  - bugfix
  - sparse-moe
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2183"
---

# PR Insight: vllm-project/vllm-ascend #2183

**Title:** [BugFix] Fix the bug that qwen3 moe doesn't work with aclgraph

## Overview
This PR fixes Qwen3 MoE compatibility with ACL Graph by moving `AscendSparseMoeBlock` to the qwen3 model (since it's only used by Qwen3) and disabling it when ACL Graph is enabled. Changes include modifications to `vllm_ascend/models/qwen3_moe.py` and `vllm_ascend/ops/fused_moe.py` and adding comprehensive tests.

## Technical Significance
This bugfix resolves the incompatibility between Qwen3's sparse MoE implementation and ACL Graph mode. By conditionally disabling the AscendSparseMoeBlock when ACL Graph is enabled, the system can fall back to compatible implementations. This ensures Qwen3 MoE models work correctly in both ACL Graph and non-ACL Graph modes.

## Related
- `kernel-fused-moe-ascendc`, `kernel-sparse-moe-qwen3`, `technique-aclgraph-integration`, `technique-moe-implementation`