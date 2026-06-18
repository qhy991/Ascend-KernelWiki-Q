---
id: technique-pr-vllm-ascend-6182
title: "PR Insight: vllm-project/vllm-ascend #6182"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - acl-graph
  - tensor-accumulation
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6182"
---

# PR Insight: vllm-project/vllm-ascend #6182

**Title:** BugFix:  Fix moe_load accumulation error in ACL graph mode

## Overview
This PR fixes a numerical error in MoE load accumulation under ACL graph mode. The issue occurred because using `+=` for NPU tensors in graph mode produces incorrect values without raising errors. The fix replaces `+=` with the in-place `add_()` method to ensure accurate calculations.

## Technical Significance
ACL graph mode traces and compiles operations differently than eager mode. The `+=` operator may not be correctly traced or executed in graph mode, leading to silent numerical errors. Using the explicit `add_()` method ensures proper graph compilation and correct accumulation semantics for MoE expert load balancing calculations, preventing incorrect routing decisions.

## Related
- `technique-moe`, `technique-acl-graph`, `technique-tensor-operations`