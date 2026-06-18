---
id: technique-pr-vllm-ascend-5284
title: "PR Insight: vllm-project/vllm-ascend #5284"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - moe
  - ep
  - memory-optimization
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5284"
---

# PR Insight: vllm-project/vllm-ascend #5284

**Title:** [bugfix] remove the EP buffer allocation introduced by fused-op dispatch_ffn_c…

## Overview
This PR removes the Expert Parallel (EP) HCCL buffer allocation that was previously introduced by the fused-op `dispatch_ffn_combine`, since the operator has switched to using the MC2 HCCL buffer instead.

## Technical Significance
Removing unused EP buffer allocation reduces memory overhead. The switch to MC2 buffer provides a more efficient communication pattern for MoE expert parallelism on Ascend NPUs, eliminating redundant memory allocation and simplifying the buffer management logic.

## Related
- technique-moe
- technique-expert-parallelism
- technique-memory-optimization