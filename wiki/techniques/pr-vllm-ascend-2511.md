---
id: technique-pr-vllm-ascend-2511
title: "PR Insight: vllm-project/vllm-ascend #2511"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - qwen3-moe
  - aclgraph
  - sizes-capture
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2511"
---

# PR Insight: vllm-project/vllm-ascend #2511

**Title:** [Bugfix]Support Qwen3-MOE on aclgraph mode in sizes capture and add new ut

## Overview
This PR solves problems of sizes capture and stream errors when using ACL Graph on Qwen3-30B MoE models. The implementation modifies `vllm_ascend/utils.py` and adds comprehensive unit tests to ensure proper ACL Graph compatibility.

## Technical Significance
This bugfix ensures Qwen3-MoE models work correctly with ACL Graph mode by addressing sizes capture issues and stream errors. The added unit tests provide confidence in the fix and prevent regressions in future ACL Graph integration work.

## Related
- `kernel-fused-moe-ascendc`, `kernel-qwen3-moe`, `technique-aclgraph-integration`, `technique-sizes-capture`