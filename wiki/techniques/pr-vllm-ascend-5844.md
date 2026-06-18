---
id: technique-pr-vllm-ascend-5844
title: "PR Insight: vllm-project/vllm-ascend #5844"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - context-parallel
  - bugfix
  - cherry-pick
  - chunked-prefill
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5844"
---

# PR Insight: vllm-project/vllm-ascend #5844

**Title:** [0.13.0][cherry-pick][bugfix](cp) replace None with zeros/inf tensor to avoid TypeError

## Overview
This is a cherry-pick of PR #5837 for the v0.13.0 release branch. It fixes the same TypeError in context parallel scenarios where some devices have no KV cache data. The `_compute_prefill_context` function now returns properly shaped zero or negative infinity tensors instead of None.

## Technical Significance
This fix ensures the v0.13.0 branch maintains robustness for chunked prefill with empty KV cache scenarios. By replacing None returns with valid tensors, the fix prevents TypeErrors in CP deployments where devices may not receive KV cache segments. The cherry-pick maintains parity with the main branch's context parallel behavior, enabling reliable multi-card inference.

## Related
- `technique-pr-vllm-ascend-5837`, `technique-context-parallel`, `technique-chunked-prefill`