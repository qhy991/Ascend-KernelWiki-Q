---
id: technique-pr-vllm-ascend-5808
title: "PR Insight: vllm-project/vllm-ascend #5808"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - cube-unit
  - event-sync
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5808"
---

# PR Insight: vllm-project/vllm-ascend #5808

**Title:** [main][BugFix]Fix DispatchGmmCombineDecode acc bug when big batch

## Overview
This PR fixes an accuracy bug in the DispatchGmmCombineDecode AscendC kernel when one expert processes more than 384 tokens (48 * 8). The issue was caused by premature event flag setting before all Unified Buffer tensors were freed, leading to race conditions during memory transfers from global memory.

## Technical Significance
The fix addresses a critical synchronization issue in the grouped matmul kernel. Multiple LocalTensor objects (ubInputRightHalf, ubInputTmp, ubQuantF32, ubQuantS32, ubQuantF16) share the same memory space as ubAbs. The AscendC::SetFlag<AscendC::HardEvent::V_MTE2>(0) event was being set too early, before all these tensors were freed. This caused the copy from global memory to ubInputRightHalf to start prematurely, corrupting data and causing accuracy failures. The fix delays flag setting until the correct time, ensuring proper memory synchronization.

## Related
- `technique-event-sync`, `technique-unified-buffer`, `technique-moe-dispatch`, `hw-cube-unit`