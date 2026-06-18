---
id: technique-pr-vllm-ascend-4212
title: "PR Insight: vllm-project/vllm-ascend #4212"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - sp
  - chunked
  - bugfix
  - vllm
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/4212"
---

# PR Insight: vllm-project/vllm-ascend #4212

**Title:** [Bugfix]Fix moe error when sp chunked the hidden_states

## Overview
This PR fixes a MoE error that occurred when SP (Sequence Parallel) chunked the hidden_states. The fix modifies the platform configuration to prevent incorrect behavior when combining SP chunking with MoE operations.

## Technical Significance
SP chunking combined with MoE operations can cause data layout issues that lead to incorrect results. The fix ensures proper interaction between SP and MoE, enabling users to benefit from both optimizations simultaneously without correctness issues.

## Related
- `technique-moe`, `technique-sequence-parallel`, `pattern-feature-compatibility`, `technique-chunked-computation`