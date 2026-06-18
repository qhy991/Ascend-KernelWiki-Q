---
id: technique-pr-vllm-ascend-4810
title: "PR Insight: vllm-project/vllm-ascend #4810"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - prefill
  - dispatch
  - combine
  - ascendc
  - aclnn
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/4810"
---

# PR Insight: vllm-project/vllm-ascend #4810

**Title:** [Kernel] Add moe normal ops

## Overview
This PR adds four AscendC operators for MoE prefill operations: MoeCombineNormal (combine logic), MoeDispatchNormal (dispatch logic), NotifyDispatch (exchanges topk_idx info between ranks), and DispatchLayout (calculates device memory layout info for dispatch). It also provides PyTorch interfaces: get_dispatch_layout, dispatch_prefill, and combine_prefill.

## Technical Significance
Provides high-performance AscendC implementations for MoE dispatch/combine operations during the prefill stage. The operators enable distributed MoE communication across NPUs with optimized memory layout calculation and token routing.

## Related
- `kernel-moe-combine-normal`
- `kernel-moe-dispatch-normal`
- `kernel-notify-dispatch`
- `kernel-dispatch-layout`
- `technique-moe-communication`