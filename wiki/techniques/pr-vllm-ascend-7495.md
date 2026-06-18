---
id: technique-pr-vllm-ascend-7495
title: "PR Insight: vllm-project/vllm-ascend #7495"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - causal-conv1d
  - qwen3-next
  - qwen3.5
  - ascendc-operator
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/7495"
---

# PR Insight: vllm-project/vllm-ascend #7495

**Title:** [Ops][Misc] Refactor and optimize CausalConv1d for Ascend

## Overview
This PR optimizes CausalConv1d for Qwen3-Next and Qwen3.5 prefill by re-implementing it using torch.ops._C_ascend.npu_causal_conv1d_custom instead of torch.ops._C_ascend.causal_conv1d_fn. The new implementation is an AscendC operator with better performance.

## Technical Significance
This optimization matters for prefill performance of Qwen3.5/Next on Ascend. The original causal_conv1d_fn had significant performance bottlenecks. The new npu_causal_conv1d_custom AscendC operator leverages NPU hardware more efficiently, reducing prefill latency. Accuracy tests show maintained correctness (GSM8k: 96.21%).

## Related
- technique-state-space-models
- technique-ascendc-optimization