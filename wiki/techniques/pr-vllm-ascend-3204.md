---
id: technique-pr-vllm-ascend-3204
title: "PR Insight: vllm-project/vllm-ascend #3204"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - aclgraph
  - qwen3
  - dp
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3204"
---

# PR Insight: vllm-project/vllm-ascend #3204

**Title:** [BugFix] Fix ACLgraph bug in Qwen3_32b_int8 case

## Overview
This PR fixes ACL graph size capture failures for Qwen3-32b-int8 models when ACL graph, DP1, and TP4 are enabled. It adds exception handling for capture failures, provides solutions, and documents the issue in the FAQ.

## Technical Significance
ACL graph size capture is critical for memory allocation and graph compilation. The fix ensures that graph capture works correctly in quantized distributed scenarios. Adding exception handling and documentation helps users troubleshoot and resolve similar issues in production deployments.

## Related
- `technique-aclgraph`, `kernel-qwen3-ascendc`, `kernel-quantization-ascendc`