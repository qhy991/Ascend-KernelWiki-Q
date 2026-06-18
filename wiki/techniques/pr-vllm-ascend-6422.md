---
id: technique-pr-vllm-ascend-6422
title: "PR Insight: vllm-project/vllm-ascend #6422"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - event-sync
  - bugfix
  - c++
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6422"
---

# PR Insight: vllm-project/vllm-ascend #6422

**Title:** fix: resolve sync bug in DispathFFNCombine when expert num per card is 32

## Overview
This PR addresses the same synchronization deadlock issue in `DispathFFNCombine` as PR #6416, but for a different configuration. The bug occurs on NPU cards when the number of experts per card exceeds 16, with the issue appearing prominently at 32 experts per card.

## Technical Significance
MoE inference scalability depends on proper expert dispatch synchronization. The deadlock occurs during expert parallel processing when the synchronization primitives don't handle the increased expert count correctly. This fix ensures that MoE models can scale to larger expert configurations without hitting synchronization deadlocks on Ascend NPUs.

## Related
- `kernel-moe`
- `technique-event-sync`
- `pattern-moe-dispatch`