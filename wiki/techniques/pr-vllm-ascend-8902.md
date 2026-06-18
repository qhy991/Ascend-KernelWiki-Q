---
id: technique-pr-vllm-ascend-8902
title: "PR Insight: vllm-project/vllm-ascend #8902"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - ascendc
  - moe
  - operator-fusion
  - performance
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/8902"
---

# PR Insight: vllm-project/vllm-ascend #8902

**Title:** [Feature] update dataWithScale and combine in dispatch_ffn_kernel

## Overview
This PR updates the `dispatch_ffn_combine` fusion kernel in `csrc/dispatch_ffn_combine/` to fix known performance degradation issues. The changes improve the `dataWithScale` and combine operations in the MoE dispatch/combine pipeline, including updated kernel implementations in `op_kernel/dispatch_ffn_combine_kernel.hpp` and related MoE dynamic quantization kernels. Single kernel testing confirms performance improvements.

## Technical Significance
The `dispatch_ffn_combine` fusion operator is critical for MoE inference performance on Ascend NPUs, combining dispatch, expert FFN computation, and combine into a single kernel. The performance degradation fix directly impacts MoE throughput by optimizing memory access patterns and instruction scheduling. The updates to dynamic quantization kernels ensure that the benefits extend to quantized MoE deployments, maintaining high throughput while reducing memory footprint.

## Related
- `technique-moe` (MoE dispatch/combine)
- `technique-operator-fusion` (Fused operator optimization)
- `pattern-quantization` (Dynamic quantization integration)