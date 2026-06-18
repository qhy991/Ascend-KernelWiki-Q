---
id: technique-pr-vllm-ascend-9720
title: "PR Insight: vllm-project/vllm-ascend #9720"
type: wiki-technique
architectures:
  - ascend310p
tags:
  - operator
  - conv1d
  - triton
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/9720"
---

# PR Insight: vllm-project/vllm-ascend #9720

**Title:** [BugFix][310P] Fix the precision of the causal_conv1d_v310 operator on 310P

## Overview
This PR fixes precision issues in the 310P `causal_conv1d_v310` custom operator caused by incorrect state initialization, ring buffer handling, and missing Ascend pipeline synchronization. It corrects `hasInit` defaults, initializes unused ring slots, restores V-pipe barriers, fixes state writeback indexing, and improves cross-engine sync.

## Technical Significance
Addresses read-before-write races on vector pipeline by adding `PipeBarrier<PIPE_V>()` between Cast and MulAddDst. Fixes state writeback to use `RetreatRingSlot()` for walking back from the last ring slot. Replaces generic barriers with HardEvent-based synchronization in `WriteBackStateSpec`, preventing garbage values from uninitialized memory from affecting convolution.

## Related
- `kernel-conv1d`, `technique-pipeline-scheduling`, `technique-event-sync`