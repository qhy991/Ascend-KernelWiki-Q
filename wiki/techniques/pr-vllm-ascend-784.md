---
id: technique-pr-vllm-ascend-784
title: "PR Insight: vllm-project/vllm-ascend #784"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - quantization
  - moe
  - memory-optimization
  - npu-memory
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/784"
---

# PR Insight: vllm-project/vllm-ascend #784

**Title:** [Perf] Optimize fused_experts quantization code to save npu memory

## Overview
This PR optimizes NPU memory usage in W8A8 quantized fused_experts by reusing the `hidden_states` variable name across operator outputs instead of creating new variables. This approach ends the lifecycle of previous tensors more efficiently, eliminating the need for explicit `del` statements throughout the code.

## Technical Significance
Memory optimization is crucial for quantized MoE models, which process many intermediate tensors. By reusing variable names and letting Python's garbage collection free memory immediately, this approach reduces NPU memory footprint without code clutter from manual deletion statements.

## Related
- `technique-quantization`
- `kernel-moe`
- `technique-memory-optimization`