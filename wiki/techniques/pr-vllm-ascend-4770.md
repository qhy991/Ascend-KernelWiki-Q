---
id: technique-pr-vllm-ascend-4770
title: "PR Insight: vllm-project/vllm-ascend #4770"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - qwen3-next
  - mtp
  - chunked-prefill
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/4770"
---

# PR Insight: vllm-project/vllm-ascend #4770

**Title:** [BugFix][main] Adapted Qwen3-Next-MTP to chunked prefill

## Overview
This PR adapts Qwen3-Next-MTP to chunked prefill by adjusting padding logic (from upstream PR #25743). The fix ensures correctness for batched chunked prefill scenarios, passing the distributed TP4 SIMILARITY test for Qwen3_NEXT_MTP.

## Technical Significance
Fixes compatibility issues between Qwen3-Next-MTP and chunked prefill mode, specifically handling padding adjustments needed for batched inference. Ensures MTP speculative decoding works correctly with chunked prefill across multiple TP ranks.

## Related
- `kernel-qwen3-next`
- `technique-mtp`
- `technique-chunked-prefill`
- `kernel-casual-conv1d`