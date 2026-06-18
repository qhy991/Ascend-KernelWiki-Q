---
id: technique-pr-vllm-ascend-6258
title: "PR Insight: vllm-project/vllm-ascend #6258"
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
  - "https://github.com/vllm-project/vllm-ascend/pull/6258"
---

# PR Insight: vllm-project/vllm-ascend #6258

**Title:** [v0.13.0][cherry-pick][BugFix] Fix moe_load accumulation error in ACL graph mode

## Overview
This PR cherry-picks the MoE load accumulation fix for ACL graph mode into the v0.13.0 branch. The issue where `+=` for NPU tensors in graph mode produces incorrect values is fixed by replacing it with the in-place `add_()` method.

## Technical Significance
This is the v0.13.0 backport of PR #6182. Using explicit `add_()` instead of `+=` ensures correct graph compilation and accumulation semantics for MoE expert load balancing. The backport ensures v0.13.0 users receive this critical numerical accuracy fix for MoE workloads in ACL graph mode.

## Related
- `technique-moe`, `technique-acl-graph`, `technique-tensor-operations`