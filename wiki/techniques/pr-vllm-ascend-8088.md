---
id: technique-pr-vllm-ascend-8088
title: "PR Insight: vllm-project/vllm-ascend #8088"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - attention
  - bugfix
  - short-prompt
  - prefill
  - decode
  - state-management
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/8088"
---

# PR Insight: vllm-project/vllm-ascend #8088

**Title:** [0.18.0][BugFix] Fix attention state of short prompt for correct forwarding

## Overview
This PR fixes attention state handling for short prompts during the prefill phase. When batched requests contain short prompts (prefill tokens <= num_spec_tokens + 1), they were incorrectly treated as decode requests, causing a mismatch between their PrefillNoCache attention state and the actual execution path. The fix ensures correct attention state transitions for mixed short and long prompt batches.

## Technical Significance
The fix addresses a critical correctness issue in attention computation for short prompts. Short prompts require special handling to avoid incorrect execution path selection that can lead to inference errors. This is particularly important for workloads with variable-length prompts and speculative decoding scenarios where prefill/decode boundaries need precise state management.

## Related
- `technique-attention-optimization`
- `technique-state-management`