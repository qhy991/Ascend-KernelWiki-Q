---
id: technique-pr-vllm-ascend-3485
title: "PR Insight: vllm-project/vllm-ascend #3485"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - quantization
  - moe
  - hccl-optimization
  - prefill
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3485"
---

# PR Insight: vllm-project/vllm-ascend #3485

**Title:** [feat][torchair] support super kernel feat for quantized dsr1

## Overview
Port #1916 and #2157 to master branch to fuse operators in deepseek moe layers, which can reduce scheduling overhead on devices. Note that this feature is valid only when `tp_size = 1`  and `multistream_overlap_shared_expert` is enabled with torchair graph mode.

## Technical Significance
Supports super kernel feature for quantized DSR1 in TorchAir for optimized operator fusion.

## Related
- `technique-quantization`
- `technique-moe-routing`
