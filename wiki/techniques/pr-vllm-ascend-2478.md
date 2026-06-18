---
id: technique-pr-vllm-ascend-2478
title: "PR Insight: vllm-project/vllm-ascend #2478"
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
  - "https://github.com/vllm-project/vllm-ascend/pull/2478"
---

# PR Insight: vllm-project/vllm-ascend #2478

**Title:** [Bugfix] Fix the bug that qwen3 moe doesn't work with aclgraph

## Overview
This PR fixes Qwen3-MoE compatibility with ACL Graph by moving `AscendSparseMoeBlock` to the qwen3 model (since it's only used by Qwen3) and disabling it when ACL Graph is enabled. Changes include modifications to `vllm_ascend/models/qwen3_moe.py` and comprehensive tests.

## Technical Significance
This bugfix ensures Qwen3-MoE models work correctly in ACL Graph mode by conditionally disabling the incompatible sparse MoE implementation. The fix maintains backward compatibility while enabling graph mode execution for Qwen3-MoE models.

## Related
- `kernel-fused-moe-ascendc`, `kernel-sparse-moe-qwen3`, `technique-aclgraph-integration`, `technique-moe-implementation`