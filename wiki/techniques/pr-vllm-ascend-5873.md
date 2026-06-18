---
id: technique-pr-vllm-ascend-5873
title: "PR Insight: vllm-project/vllm-ascend #5873"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - cube-unit
  - event-sync
  - bugfix
  - cherry-pick
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5873"
---

# PR Insight: vllm-project/vllm-ascend #5873

**Title:** [v0.13.0][cherry-pick][BugFix] Fix DispatchGmmCombineDecode acc bug when big batch

## Overview
This is a cherry-pick of PR #5808 for the v0.13.0 release branch. It fixes the same accuracy bug in DispatchGmmCombineDecode when one expert processes more than 384 tokens. The issue was caused by premature event flag setting before all Unified Buffer tensors were freed.

## Technical Significance
This fix ensures the v0.13.0 branch maintains correctness for large-batch MoE inference. The race condition in the grouped matmul kernel could corrupt data when experts handled many tokens. By delaying the AscendC::SetFlag<AscendC::HardEvent::V_MTE2>(0) event until all shared UB tensors (ubInputRightHalf, ubInputTmp, ubQuantF32, ubQuantS32, ubQuantF16) are freed, the fix ensures proper memory synchronization.

## Related
- `technique-pr-vllm-ascend-5808`, `technique-event-sync`, `technique-moe-dispatch`