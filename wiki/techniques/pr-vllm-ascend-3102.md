---
id: technique-pr-vllm-ascend-3102
title: "PR Insight: vllm-project/vllm-ascend #3102"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - pagedattention
  - full-decode-only
  - workspace
  - deadlock-prevention
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3102"
---

# PR Insight: vllm-project/vllm-ascend #3102

**Title:** add pagedattention to support FULL_DECODE_ONLY.

## Overview
This PR adds FULL_DECODE_ONLY mode support to PagedAttention by pre-calculating workspace memory size to avoid deadlocks during resource cleanup. The implementation requires torch_npu version 0920 or newer.

## Technical Significance
FULL_DECODE_ONLY mode optimizes for decode-only workloads, which is common in production inference. Pre-calculating workspace memory prevents deadlocks during resource cleanup, improving reliability. The feature requires specific torch_npu versions, indicating integration with Ascend's latest runtime improvements.

## Related
- `kernel-pagedattention-ascendc`, `technique-kv-cache-paging`, `pattern-full-decode-only`