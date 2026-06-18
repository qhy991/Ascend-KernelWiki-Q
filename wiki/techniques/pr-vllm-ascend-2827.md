---
id: technique-pr-vllm-ascend-2827
title: "PR Insight: vllm-project/vllm-ascend #2827"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - qwen
  - aclgraph
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2827"
---

# PR Insight: vllm-project/vllm-ascend #2827

**Title:** [Bugfix] Fix aclgraph sizes capture error in Qwen3 Moe model case

## Overview
This PR fixes an error in aclgraph size capture specific to Qwen3 MoE models, addressing issues in the utility functions that handle shape and size capture during graph compilation.

## Technical Significance
Critical bug fix for aclgraph mode when running Qwen3 MoE models. Proper size capture is essential for graph compilation to succeed; otherwise, operators cannot be compiled correctly. This fix ensures that aclgraph can handle the dynamic shapes and configurations specific to MoE models like Qwen3.

## Related
- `kernel-moe-ascendc`, `technique-aclgraph-optimization`