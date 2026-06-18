---
id: technique-pr-vllm-ascend-4194
title: "PR Insight: vllm-project/vllm-ascend #4194"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - custom-ops
  - prefill
  - ascendc
  - vllm
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/4194"
---

# PR Insight: vllm-project/vllm-ascend #4194

**Title:** [Kernel] add custom moe ops for prefill

## Overview
This PR adds custom AscendC operators for MoE prefill operations: MoeCombineNormal, MoeDispatchNormal, NotifyDispatch, and DispatchLayout. The operators implement combine and dispatch logic for MoE operations, exchange topk_idx information across ranks for memory calculation, and provide PyTorch interfaces (get_dispatch_layout, dispatch_prefill, combine_prefill) for MoE communication during prefill.

## Technical Significance
Custom MoE operators for prefill enable hardware-specific optimizations that cannot be achieved with standard PyTorch operations. The operators handle complex communication patterns for expert dispatch and combine across distributed ranks. Proper prefill optimization is critical for TTFT in MoE models, which is a key performance metric.

## Related
- `technique-moe`, `technique-ascendc`, `pattern-custom-ops`, `technique-prefill-optimization`, `technique-distributed-inference`